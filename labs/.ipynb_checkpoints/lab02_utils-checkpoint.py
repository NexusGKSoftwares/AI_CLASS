"""
CSC 315 Lab 2: helper code for uninformed search.

You do NOT need to edit this file. It provides:
  - InstrumentedProblem: wraps any problem and counts nodes expanded and generated.
  - run_search: runs a search algorithm and returns a row of statistics.
  - 8-puzzle helpers: GOAL_8, scramble, show_puzzle, TEST_PUZZLES.
  - Maze helpers: make_maze, show_maze.
"""
import random
import time

# ---------------------------------------------------------------------------
# Instrumentation
# ---------------------------------------------------------------------------

class InstrumentedProblem:
    """Wraps a problem and counts calls.

    expanded  = number of times actions() is called (one per node expanded)
    generated = number of child states created by result()
    max_frontier = largest frontier size reported through track(frontier)
    Every other attribute is passed through to the wrapped problem.
    """

    def __init__(self, problem):
        self.problem = problem
        self.expanded = 0
        self.generated = 0
        self.max_frontier = 0

    def actions(self, state):
        self.expanded += 1
        return self.problem.actions(state)

    def result(self, state, action):
        self.generated += 1
        return self.problem.result(state, action)

    def track(self, frontier):
        self.max_frontier = max(self.max_frontier, len(frontier))

    def __getattr__(self, name):
        return getattr(self.problem, name)


def run_search(algorithm, problem, name=None):
    """Run algorithm(problem) on an instrumented copy and return a dict of results."""
    p = InstrumentedProblem(problem)
    start = time.perf_counter()
    node = algorithm(p)
    elapsed = time.perf_counter() - start
    solved = node is not None and getattr(node, "state", None) not in ("failure", "cutoff")
    return {
        "algorithm": name or algorithm.__name__,
        "solved": solved,
        "path_cost": node.path_cost if solved else None,
        "steps": node.depth if solved else None,
        "expanded": p.expanded,
        "generated": p.generated,
        "max_frontier": p.max_frontier,
        "seconds": round(elapsed, 4),
        "node": node if solved else None,
    }


def print_table(rows, columns=("algorithm", "solved", "steps", "path_cost", "expanded", "generated", "max_frontier", "seconds")):
    """Print a list of dicts as an aligned text table."""
    widths = {c: max(len(c), *(len(str(r.get(c))) for r in rows)) for c in columns}
    print("  ".join(c.ljust(widths[c]) for c in columns))
    print("  ".join("-" * widths[c] for c in columns))
    for r in rows:
        print("  ".join(str(r.get(c)).ljust(widths[c]) for c in columns))

# ---------------------------------------------------------------------------
# 8-puzzle
# ---------------------------------------------------------------------------
# A state is a tuple of 9 numbers read row by row; 0 is the blank.

GOAL_8 = (1, 2, 3,
          4, 5, 6,
          7, 8, 0)

# Puzzles with known optimal solution lengths (number of moves).
TEST_PUZZLES = {
    2:  (1, 2, 3, 4, 5, 6, 0, 7, 8),
    4:  (1, 3, 0, 4, 2, 5, 7, 8, 6),
    8:  (1, 3, 5, 4, 0, 6, 7, 2, 8),
    12: (0, 1, 3, 4, 7, 2, 8, 6, 5),
    16: (4, 2, 5, 6, 1, 3, 7, 8, 0),
    20: (0, 4, 3, 1, 5, 6, 8, 7, 2),
    24: (0, 5, 7, 3, 2, 8, 1, 6, 4),
}

# One of the hardest 8-puzzle states: it needs 31 moves, the maximum.
HARDEST_8 = (6, 4, 7, 8, 5, 0, 3, 2, 1)

_MOVES = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}


def _blank_moves(state):
    i = state.index(0)
    row, col = divmod(i, 3)
    moves = []
    if row > 0: moves.append("Up")
    if row < 2: moves.append("Down")
    if col > 0: moves.append("Left")
    if col < 2: moves.append("Right")
    return moves


def scramble(n_moves, seed=None, start=GOAL_8):
    """Return a solvable state made by moving the blank n_moves times at random."""
    rng = random.Random(seed)
    state = list(start)
    for _ in range(n_moves):
        i = state.index(0)
        j = i + _MOVES[rng.choice(_blank_moves(state))]
        state[i], state[j] = state[j], state[i]
    return tuple(state)


def show_puzzle(state, title=None, ax=None):
    """Draw an 8-puzzle state with matplotlib."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(figsize=(2.2, 2.2))
    for i, tile in enumerate(state):
        r, c = divmod(i, 3)
        color = "white" if tile == 0 else "#cfe2f3"
        ax.add_patch(plt.Rectangle((c, 2 - r), 1, 1, facecolor=color, edgecolor="#1f4e79", lw=2))
        if tile:
            ax.text(c + 0.5, 2.5 - r, str(tile), ha="center", va="center", fontsize=18, weight="bold", color="#1f4e79")
    ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_aspect("equal"); ax.axis("off")
    if title:
        ax.set_title(title)
    return ax

# ---------------------------------------------------------------------------
# Mazes
# ---------------------------------------------------------------------------

class Maze:
    """A grid maze.

    grid[r][c] is "#" for a wall, "." for open floor, or "~" for mud.
    Moving onto floor costs 1; moving onto mud costs MUD_COST.
    start and goal are (row, col) pairs.
    """
    MUD_COST = 5

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_open(self, cell):
        r, c = cell
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != "#"

    def cost(self, cell):
        r, c = cell
        return self.MUD_COST if self.grid[r][c] == "~" else 1

    def __str__(self):
        out = []
        for r, row in enumerate(self.grid):
            line = ""
            for c, ch in enumerate(row):
                line += "S" if (r, c) == self.start else "G" if (r, c) == self.goal else ch
            out.append(line)
        return "\n".join(out)


def make_maze(n, loops=0.15, mud=0.15, seed=None):
    """Make an n x n cell maze (drawn on a (2n+1) x (2n+1) grid).

    The maze is first carved as a perfect maze (one path between any two cells)
    with randomised depth-first search. Then a fraction `loops` of the remaining
    inner walls is removed, which creates cycles and alternative routes. Finally
    a fraction `mud` of the open squares is turned into mud.
    Start is the top-left cell and goal is the bottom-right cell.
    """
    rng = random.Random(seed)
    size = 2 * n + 1
    g = [["#"] * size for _ in range(size)]
    stack = [(0, 0)]
    seen = {(0, 0)}
    g[1][1] = "."
    while stack:
        r, c = stack[-1]
        nbrs = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in seen]
        if not nbrs:
            stack.pop()
            continue
        nr, nc = rng.choice(nbrs)
        g[2 * r + 1 + (nr - r)][2 * c + 1 + (nc - c)] = "."
        g[2 * nr + 1][2 * nc + 1] = "."
        seen.add((nr, nc))
        stack.append((nr, nc))
    inner = [(r, c) for r in range(1, size - 1) for c in range(1, size - 1)
             if g[r][c] == "#" and (r % 2) != (c % 2)]
    for r, c in rng.sample(inner, int(loops * len(inner))):
        g[r][c] = "."
    start, goal = (1, 1), (size - 2, size - 2)
    floor = [(r, c) for r in range(size) for c in range(size) if g[r][c] == "." and (r, c) not in (start, goal)]
    for r, c in rng.sample(floor, int(mud * len(floor))):
        g[r][c] = "~"
    return Maze(["".join(row) for row in g], start, goal)


def show_maze(maze, path=None, explored=None, title=None, ax=None):
    """Draw a maze. path is a list of (row, col) cells; explored is a set of cells."""
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap
    codes = {"#": 0, ".": 1, "~": 2}
    img = np.array([[codes[ch] for ch in row] for row in maze.grid])
    if explored:
        for (r, c) in explored:
            if img[r, c] == 1:
                img[r, c] = 3
            elif img[r, c] == 2:
                img[r, c] = 4
    cmap = ListedColormap(["#263238", "#ffffff", "#c8a97e", "#bbdefb", "#9fa8da"])
    if ax is None:
        size = min(8, 2 + maze.rows / 8)
        _, ax = plt.subplots(figsize=(size, size))
    ax.imshow(img, cmap=cmap, vmin=0, vmax=4, interpolation="nearest")
    if path:
        ys, xs = zip(*path)
        ax.plot(xs, ys, color="#d32f2f", lw=2)
    ax.plot(maze.start[1], maze.start[0], "o", color="#2e7d32", ms=8)
    ax.plot(maze.goal[1], maze.goal[0], "*", color="#f9a825", ms=14, mec="black")
    ax.set_xticks([]); ax.set_yticks([])
    if title:
        ax.set_title(title)
    return ax

# ---------------------------------------------------------------------------
# Road map used in the Module 2 lecture notes: ten Kenyan towns.
# Distances are approximate road distances in km, rounded for teaching.
# Only some roads are included, so routes are simplified.
# ---------------------------------------------------------------------------

ROAD_MAP = {
    ("Kisumu", "Kakamega"): 52,
    ("Kisumu", "Nakuru"): 185,
    ("Kisumu", "Kericho"): 82,
    ("Kakamega", "Eldoret"): 115,
    ("Eldoret", "Nakuru"): 156,
    ("Nakuru", "Nyeri"): 165,
    ("Nakuru", "Naivasha"): 80,
    ("Kericho", "Narok"): 185,
    ("Narok", "Naivasha"): 120,
    ("Narok", "Nairobi"): 142,
    ("Naivasha", "Nairobi"): 93,
    ("Nyeri", "Thika"): 115,
    ("Nairobi", "Thika"): 45,
}

# Drawing positions, roughly following the towns' real layout (west on the left, north at the top).
TOWN_XY = {
    "Kisumu": (0, 3), "Kakamega": (0.5, 5.0), "Eldoret": (2.2, 5.6), "Nakuru": (3.0, 3.4),
    "Kericho": (1.3, 1.9), "Narok": (2.9, 0.4), "Naivasha": (4.1, 2.3), "Nyeri": (6.0, 4.6),
    "Nairobi": (5.6, 1.0), "Thika": (7.3, 2.2),
}


def neighbours(road_map):
    """Turn {(a, b): km} into {a: {b: km}} with roads in both directions."""
    nbrs = {}
    for (a, b), d in road_map.items():
        nbrs.setdefault(a, {})[b] = d
        nbrs.setdefault(b, {})[a] = d
    return nbrs
