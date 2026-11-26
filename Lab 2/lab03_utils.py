"""
CSC 315 Lab 3: helper code for informed and local search.

You do NOT need to edit this file. It re-exports everything from lab02_utils
(instrumentation, 8-puzzle, mazes, road map) and adds:
  - straight-line distances between the road-map towns (SLD_TO_THIKA, straight_line)
  - effective_branching_factor(n_nodes, depth)
  - 8-queens helpers: random_queens, queen_conflicts, show_queens
"""
import math
import random

from lab02_utils import *  # noqa: F401,F403
from lab02_utils import ROAD_MAP, TOWN_XY, neighbours  # noqa: F401

# ---------------------------------------------------------------------------
# Straight-line distances on the Kenyan road map
# ---------------------------------------------------------------------------

# Approximate town-centre coordinates (latitude, longitude in degrees).
TOWN_LATLON = {
    "Kisumu": (-0.0917, 34.7680), "Kakamega": (0.2827, 34.7519), "Eldoret": (0.5143, 35.2698),
    "Nakuru": (-0.3031, 36.0800), "Kericho": (-0.3689, 35.2863), "Narok": (-1.0783, 35.8601),
    "Naivasha": (-0.7167, 36.4333), "Nyeri": (-0.4201, 36.9476), "Nairobi": (-1.2921, 36.8219),
    "Thika": (-1.0333, 37.0693),
}


def straight_line(a, b):
    """Great-circle ('as the crow flies') distance in km between two towns, rounded down."""
    (la1, lo1), (la2, lo2) = TOWN_LATLON[a], TOWN_LATLON[b]
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return math.floor(2 * 6371 * math.asin(math.sqrt(h)))


SLD_TO_THIKA = {town: straight_line(town, "Thika") for town in TOWN_LATLON}

# ---------------------------------------------------------------------------
# Effective branching factor
# ---------------------------------------------------------------------------

def effective_branching_factor(n_nodes, depth, tol=1e-6):
    """Solve n_nodes + 1 = 1 + b + b^2 + ... + b^depth for b (by bisection).

    n_nodes is the number of nodes generated; depth is the solution depth.
    """
    if depth == 0:
        return float("nan")
    def total(b):
        return sum(b ** i for i in range(depth + 1))
    lo, hi = 1.0, max(2.0, float(n_nodes))
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if total(mid) < n_nodes + 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

# ---------------------------------------------------------------------------
# 8-queens (complete-state formulation)
# ---------------------------------------------------------------------------
# A state is a tuple of n row numbers: state[c] is the row of the queen in column c.

def random_queens(n=8, rng=random):
    """A random state with one queen in each column."""
    return tuple(rng.randrange(n) for _ in range(n))


def queen_conflicts(state):
    """Number of pairs of queens that attack each other (same row or same diagonal)."""
    n = len(state)
    count = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            r1, r2 = state[c1], state[c2]
            if r1 == r2 or abs(r1 - r2) == c2 - c1:
                count += 1
    return count


def show_queens(state, title=None, ax=None):
    """Draw a board with the queens; attacked queens are shown in red."""
    import matplotlib.pyplot as plt
    n = len(state)
    if ax is None:
        _, ax = plt.subplots(figsize=(3, 3))
    for r in range(n):
        for c in range(n):
            ax.add_patch(plt.Rectangle((c, n - 1 - r), 1, 1, color="#f0d9b5" if (r + c) % 2 == 0 else "#b58863"))
    for c, r in enumerate(state):
        attacked = any(state[c2] == r or abs(state[c2] - r) == abs(c2 - c) for c2 in range(n) if c2 != c)
        ax.text(c + 0.5, n - 0.5 - r, "♛", ha="center", va="center", fontsize=180 / n,
                color="#c62828" if attacked else "black")
    ax.set_xlim(0, n); ax.set_ylim(0, n); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title if title is not None else f"{queen_conflicts(state)} attacking pairs")
    return ax
