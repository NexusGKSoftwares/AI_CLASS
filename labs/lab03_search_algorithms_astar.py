"""
Lab 03: Problem Solving & Heuristic Search (A* vs. BFS)
Course: Introduction to Artificial Intelligence
Associated Lecture: Lecture 03 (Problem Solving Component: Search Algorithms & Planning)

Concepts Demonstrated:
- State Space Representation & Graph / Grid Search
- Uninformed Search: Breadth-First Search (BFS)
- Informed (Heuristic) Search: A* Search with f(n) = g(n) + h(n)
- Manhattan Distance Heuristic Admissibility
- Nodes Explored vs. Path Optimality
"""

from collections import deque
import heapq
from typing import List, Tuple, Optional, Dict

# Grid Representation:
# 0 = Free cell
# 1 = Wall / Obstacle
# 'S' = Start (0, 0)
# 'G' = Goal (5, 6)

GRID = [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0]
]

START = (0, 0)
GOAL = (5, 6)

def get_neighbors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Returns valid 4-directional neighboring coordinates (Up, Down, Left, Right)."""
    r, c = pos
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors


def reconstruct_path(came_from: Dict[Tuple[int, int], Tuple[int, int]], current: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Traces back from goal to start to produce the final path."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def bfs_search(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]):
    """Uninformed Breadth-First Search (Explores layer-by-layer without heuristics)."""
    queue = deque([start])
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    visited = {start}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, nodes_explored

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    return None, nodes_explored


def manhattan_heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Admissible heuristic: Manhattan distance |r1 - r2| + |c1 - c2|."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_search(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]):
    """
    Informed A* Search Algorithm:
    Evaluates nodes using f(n) = g(n) + h(n)
    where g(n) is the exact cost from start, and h(n) is the heuristic estimate to goal.
    """
    # Priority Queue stores: (f_score, counter, current_node)
    counter = 0
    open_set = [(manhattan_heuristic(start, goal), counter, start)]
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}

    g_score = {start: 0}
    nodes_explored = 0
    closed_set = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)
        if current in closed_set:
            continue
        closed_set.add(current)
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, nodes_explored

        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_heuristic(neighbor, goal)
                counter += 1
                heapq.heappush(open_set, (f_score, counter, neighbor))

    return None, nodes_explored


def print_grid_with_path(grid: List[List[int]], path: List[Tuple[int, int]], start: Tuple[int, int], goal: Tuple[int, int]):
    path_set = set(path)
    print("   +" + "---+" * len(grid[0]))
    for r in range(len(grid)):
        row_str = "   |"
        for c in range(len(grid[0])):
            if (r, c) == start:
                row_str += " S |"
            elif (r, c) == goal:
                row_str += " G |"
            elif (r, c) in path_set:
                row_str += " * |"
            elif grid[r][c] == 1:
                row_str += " # |"
            else:
                row_str += "   |"
        print(row_str)
        print("   +" + "---+" * len(grid[0]))


def main():
    print("=" * 65)
    print("      LAB 03: PROBLEM SOLVING & SEARCH ALGORITHMS (A* vs BFS)   ")
    print("=" * 65)
    print(f"Start State: {START} | Goal State: {GOAL}")
    print("Obstacles (#) present in the grid.\n")

    # Run BFS
    bfs_path, bfs_nodes = bfs_search(GRID, START, GOAL)
    print(f"[1] Breadth-First Search (BFS):")
    print(f"    - Path Found Length : {len(bfs_path) if bfs_path else 0} steps")
    print(f"    - Nodes Explored    : {bfs_nodes} nodes (Uninformed)")

    # Run A*
    astar_path, astar_nodes = astar_search(GRID, START, GOAL)
    print(f"\n[2] A* Heuristic Search:")
    print(f"    - Path Found Length : {len(astar_path) if astar_path else 0} steps")
    print(f"    - Nodes Explored    : {astar_nodes} nodes (Informed with Manhattan Heuristic)")

    efficiency_gain = ((bfs_nodes - astar_nodes) / bfs_nodes) * 100
    print(f"\n[✓] Search Space Reduction by A*: {efficiency_gain:.1f}% fewer explored states!")

    print("\nVisualizing Optimal Path (* = Path Step, # = Wall):")
    if astar_path:
        print_grid_with_path(GRID, astar_path, START, GOAL)
    print("=" * 65)

if __name__ == "__main__":
    main()
