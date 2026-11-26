"""
CSC 315 search library from Lab 2 (reference version).
Replace this file with your own mysearch.py from Lab 2 if your code passed all the tests.
"""
import heapq
import math
from collections import deque


class Problem:
    """Abstract search problem. Subclasses override actions and result,
    and may override is_goal and action_cost."""

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        return state == self.goal

    def action_cost(self, state, action, result):
        return 1

    def h(self, node):
        """Heuristic estimate of cost to a goal (used from Lab 3 on)."""
        return 0

    def track(self, frontier):
        """Hook for instrumentation; does nothing here."""
        pass


class Node:
    """A node in a search tree."""

    def __init__(self, state, parent=None, action=None, path_cost=0.0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1

    def __repr__(self):
        return f"<Node {self.state} g={self.path_cost}>"

    def __lt__(self, other):
        return self.path_cost < other.path_cost


failure = Node("failure", path_cost=math.inf)  # no solution exists
cutoff = Node("cutoff", path_cost=math.inf)    # depth limit reached


def expand(problem, node):
    """Yield the child nodes of node."""
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)


def path_actions(node):
    """The actions from the root to node."""
    actions = []
    while node is not None and node.parent is not None:
        actions.append(node.action)
        node = node.parent
    return actions[::-1]


def path_states(node):
    """The states from the root to node."""
    states = []
    while node is not None:
        states.append(node.state)
        node = node.parent
    return states[::-1]


def is_cycle(node):
    """True if node's state appears earlier on its own path."""
    s, p = node.state, node.parent
    while p is not None:
        if p.state == s:
            return True
        p = p.parent
    return False


def breadth_first_search(problem):
    """BFS with an early goal test (AIMA 4e, Fig. 3.9)."""
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node
    frontier = deque([node])
    reached = {node.state}
    while frontier:
        problem.track(frontier)
        node = frontier.popleft()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.append(child)
    return failure


def depth_first_search(problem):
    """Graph-search DFS: a LIFO frontier plus a reached set."""
    node = Node(problem.initial)
    frontier = [node]
    reached = {node.state}
    while frontier:
        problem.track(frontier)
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            if child.state not in reached:
                reached.add(child.state)
                frontier.append(child)
    return failure


def uniform_cost_search(problem):
    """Best-first search with f(n) = g(n); the goal test is applied when a node is popped."""
    node = Node(problem.initial)
    frontier = [(node.path_cost, 0, node)]
    reached = {node.state: node}
    counter = 1  # tie-breaker so heapq never compares Nodes with equal cost
    while frontier:
        problem.track(frontier)
        _, _, node = heapq.heappop(frontier)
        if problem.is_goal(node.state):
            return node
        if node.path_cost > reached[node.state].path_cost:
            continue  # a stale entry: we already found a cheaper path to this state
        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (child.path_cost, counter, child))
                counter += 1
    return failure


def depth_limited_search(problem, limit=10):
    """Tree-like DFS that stops at depth `limit` and skips paths that loop back on themselves."""
    frontier = [Node(problem.initial)]
    result = failure
    while frontier:
        problem.track(frontier)
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        if node.depth >= limit:
            result = cutoff
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)
    return result


def iterative_deepening_search(problem, max_depth=100):
    """Run depth-limited search with limits 0, 1, 2, ... until it does not hit the cutoff."""
    for limit in range(max_depth + 1):
        result = depth_limited_search(problem, limit)
        if result is not cutoff:
            return result
    return cutoff


# --- Problems used in the lab ----------------------------------------------

class EightPuzzle(Problem):
    """State: tuple of 9 numbers, row by row, 0 = blank. Actions move the blank."""

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        super().__init__(initial, goal)

    def actions(self, state):
        i = state.index(0)
        row, col = divmod(i, 3)
        acts = []
        if row > 0: acts.append("Up")
        if row < 2: acts.append("Down")
        if col > 0: acts.append("Left")
        if col < 2: acts.append("Right")
        return acts

    def result(self, state, action):
        i = state.index(0)
        j = i + {"Up": -3, "Down": 3, "Left": -1, "Right": 1}[action]
        s = list(state)
        s[i], s[j] = s[j], s[i]
        return tuple(s)


def solvable(state):
    """An 8-puzzle state can reach the standard goal iff its inversion count is even."""
    tiles = [t for t in state if t]
    inv = sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inv % 2 == 0


class MazeProblem(Problem):
    """Find a path from maze.start to maze.goal. Moving onto mud costs more."""

    MOVES = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}

    def __init__(self, maze):
        super().__init__(maze.start, maze.goal)
        self.maze = maze

    def actions(self, state):
        r, c = state
        return [a for a, (dr, dc) in self.MOVES.items() if self.maze.is_open((r + dr, c + dc))]

    def result(self, state, action):
        dr, dc = self.MOVES[action]
        return (state[0] + dr, state[1] + dc)

    def action_cost(self, state, action, result):
        return self.maze.cost(result)
