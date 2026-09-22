"""
Lab 02: Rational Agents & Environment Simulation
Course: Introduction to Artificial Intelligence
Associated Lecture: Lecture 02 (Acting Rationally - The Rational Agent)

Concepts Demonstrated:
- Agent Architecture: Sensors -> Decision Logic -> Actuators
- Percept Sequences & State Estimation
- Performance Measures & Expected Utility Maximization
- Simple Reflex Agent vs. Rational Goal-Based Agent
"""

import random
from typing import Tuple, List, Dict

class Environment:
    """The Two-State Vacuum World Environment (Russell & Norvig, 4th ed.)"""
    def __init__(self):
        # Locations: 'A' and 'B'
        # States: 'Clean' or 'Dirty'
        self.locations: Dict[str, str] = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }

    def get_percept(self, agent_location: str) -> Tuple[str, str]:
        """Returns the current percept: (Current Location, Status of Current Location)"""
        return agent_location, self.locations[agent_location]

    def execute_action(self, agent_location: str, action: str) -> Tuple[str, int]:
        """
        Executes an action in the environment.
        Actions: 'Suck', 'Right', 'Left', 'NoOp'
        Returns: (New Location, Step Cost / Reward)
        """
        penalty = 0

        if action == 'Suck':
            if self.locations[agent_location] == 'Dirty':
                self.locations[agent_location] = 'Clean'
                reward = 10  # Cleaned a dirty room
            else:
                reward = -1  # Wasted energy sucking clean room
            return agent_location, reward

        elif action == 'Right':
            new_loc = 'B' if agent_location == 'A' else 'B'
            penalty = -1 # Energy cost to move
            return new_loc, penalty

        elif action == 'Left':
            new_loc = 'A' if agent_location == 'B' else 'A'
            penalty = -1 # Energy cost to move
            return new_loc, penalty

        elif action == 'NoOp':
            return agent_location, 0

        return agent_location, 0

    def is_all_clean(self) -> bool:
        return all(status == 'Clean' for status in self.locations.values())


class SimpleReflexAgent:
    """
    A Simple Reflex Agent selects actions based solely on the CURRENT percept,
    ignoring the rest of the percept sequence history.
    """
    def __init__(self, name: str = "Simple Reflex Agent"):
        self.name = name
        self.location = 'A'
        self.total_score = 0
        self.percept_history: List[Tuple[str, str]] = []

    def choose_action(self, percept: Tuple[str, str]) -> str:
        loc, status = percept
        self.percept_history.append(percept)

        # Condition-Action Rules
        if status == 'Dirty':
            return 'Suck'
        elif loc == 'A':
            return 'Right'
        elif loc == 'B':
            return 'Left'
        return 'NoOp'


class RationalModelBasedAgent:
    """
    A Rational Agent that maintains an internal MODEL of the world state,
    remembers which rooms are already clean, and maximizes performance.
    """
    def __init__(self, name: str = "Rational Model-Based Agent"):
        self.name = name
        self.location = 'A'
        self.total_score = 0
        self.world_model: Dict[str, str] = {'A': 'Unknown', 'B': 'Unknown'}

    def choose_action(self, percept: Tuple[str, str]) -> str:
        loc, status = percept
        # Update internal belief state
        self.world_model[loc] = status

        # If current room is dirty, clean it
        if status == 'Dirty':
            return 'Suck'

        # If other room is dirty or unknown, move there
        other_loc = 'B' if loc == 'A' else 'A'
        if self.world_model[other_loc] != 'Clean':
            return 'Right' if loc == 'A' else 'Left'

        # If all known rooms are clean, do nothing to save movement energy!
        return 'NoOp'


def run_simulation(steps: int = 8):
    print("=" * 65)
    print("      LAB 02: RATIONAL AGENTS IN VACUUM CLEANER WORLD        ")
    print("=" * 65)

    # Test 1: Simple Reflex Agent
    env1 = Environment()
    env1.locations = {'A': 'Dirty', 'B': 'Dirty'} # Standardized benchmark
    agent1 = SimpleReflexAgent()

    print(f"\n[1] Testing: {agent1.name}")
    print(f"    Initial Environment State: {env1.locations}")
    for step in range(1, steps + 1):
        percept = env1.get_percept(agent1.location)
        action = agent1.choose_action(percept)
        new_loc, score_delta = env1.execute_action(agent1.location, action)
        agent1.location = new_loc
        agent1.total_score += score_delta
        print(f"    Step {step:02d}: Percept={percept} -> Action={action:<5} | Score={agent1.total_score:>3} | Rooms={env1.locations}")

    # Test 2: Rational Model-Based Agent
    env2 = Environment()
    env2.locations = {'A': 'Dirty', 'B': 'Dirty'} # Same benchmark
    agent2 = RationalModelBasedAgent()

    print(f"\n[2] Testing: {agent2.name}")
    print(f"    Initial Environment State: {env2.locations}")
    for step in range(1, steps + 1):
        percept = env2.get_percept(agent2.location)
        action = agent2.choose_action(percept)
        new_loc, score_delta = env2.execute_action(agent2.location, action)
        agent2.location = new_loc
        agent2.total_score += score_delta
        print(f"    Step {step:02d}: Percept={percept} -> Action={action:<5} | Score={agent2.total_score:>3} | Rooms={env2.locations}")

    print("\n" + "=" * 65)
    print("                       FINAL EVALUATION                      ")
    print("=" * 65)
    print(f"Simple Reflex Agent Final Score       : {agent1.total_score}")
    print(f"Rational Model Agent Final Score      : {agent2.total_score}")
    diff = agent2.total_score - agent1.total_score
    print(f"Rational Agent Performance Advantage : +{diff} points")
    print("Reason: Once both rooms are clean, the Rational Agent performs NoOp")
    print("        while the simple reflex agent oscillates endlessly, wasting energy.")
    print("=" * 65)

if __name__ == "__main__":
    run_simulation()
