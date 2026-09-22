# AI Practical Laboratory Manual

Welcome to the **Artificial Intelligence Lab Practical Course**. This manual guides you and your lab partner through hands-on exercises directly corresponding to Lectures 1 through 4.

---

##  Lab Objectives

By completing these laboratory assignments, you will:
1. Master **Symbolic Logic & Knowledge Representation** using **SWI-Prolog** (`swipl`).
2. Simulate and evaluate **Rational Agents** interacting with an environment based on percept sequences and utility metrics.
3. Implement classical **Problem-Solving & Heuristic Search ($A^*$)** algorithms.
4. Build, train, and evaluate a **Deep Neural Network** using **PyTorch** (`torch`).
5. Explore **Natural Language Processing (NLP)** and **Chain-of-Thought (CoT)** reasoning.
6. Contrast **Hard Computing (Symbolic AI)** with **Soft Computing (Computational Intelligence)** on a real-world task.

---

## 📋 Laboratory Curriculum & Files

| Lab # | Topic | Primary File | Language | Associated Lecture |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | Symbolic AI & Expert Systems | [`lab01_prolog_knowledge_base.pl`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab01_prolog_knowledge_base.pl) | Prolog | Lecture 01 & 04 |
| **Lab 02** | Rational Agents & Environment Simulation | [`lab02_rational_agent_simulation.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab02_rational_agent_simulation.py) | Python | Lecture 02 |
| **Lab 03** | Problem Solving & $A^*$ Heuristic Search | [`lab03_search_algorithms_astar.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab03_search_algorithms_astar.py) | Python | Lecture 03 |
| **Lab 04** | Neural Networks & Soft Computing | [`lab04_pytorch_neural_network.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab04_pytorch_neural_network.py) | Python (PyTorch) | Lecture 03 & 04 |
| **Lab 05** | NLP Pipeline & Chain of Thought (CoT) | [`lab05_nlp_and_chain_of_thought.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab05_nlp_and_chain_of_thought.py) | Python | Lecture 03 |
| **Lab 06** | Paradigm Showdown: Symbolic vs. Neural | [`lab06_symbolic_vs_neural_showdown.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab06_symbolic_vs_neural_showdown.py) | Python + Prolog | Lecture 04 |

---

## 🚀 Getting Started

Before beginning any lab exercise, activate the course virtual environment in your terminal:
```bash
cd /Users/ba/TEKVORA_SOFFTWARES/AI_CLASS
source .venv/bin/activate
```

---

## Lab 01: Prolog Knowledge Base & Inference
- **Task**: Load the knowledge base, inspect facts, and execute queries using unification and resolution.
- **Run**:
  ```bash
  swipl -s labs/lab01_prolog_knowledge_base.pl
  ```
- **Key Queries**:
  ```prolog
  ?- diagnose(Patient, flu).
  ?- can_fly(X).
  ?- grandparent_of(Grandparent, Grandchild).
  ```

---

## Lab 02: Rational Agent Simulation
- **Task**: Compare a simple Reflex Agent against a Rational Goal-Oriented Agent in the classic Vacuum World.
- **Run**:
  ```bash
  python labs/lab02_rational_agent_simulation.py
  ```
- **Partner Discussion**: How does the performance measure change under partial vs. full observability?

---

## Lab 03: Heuristic Search ($A^*$, BFS, DFS)
- **Task**: Run grid pathfinding. Observe how Manhattan distance heuristics guide the search space compared to uninformed breadth-first search.
- **Run**:
  ```bash
  python labs/lab03_search_algorithms_astar.py
  ```

---

## Lab 04: PyTorch Neural Network
- **Task**: Train an MLP on non-linear multi-class data. Plot decision boundaries and training loss progression.
- **Run**:
  ```bash
  python labs/lab04_pytorch_neural_network.py
  ```

---

## Lab 05: NLP & Chain-of-Thought
- **Task**: Test tokenization, n-grams, TF-IDF vectorization, and step-by-step arithmetic decomposition preventing hallucination.
- **Run**:
  ```bash
  python labs/lab05_nlp_and_chain_of_thought.py
  ```

---

## Lab 06: Symbolic AI vs. Neural Network Showdown
- **Task**: Compare the exact same classification problem solved with:
  1. Strict human-defined logical inference rules (Hard Computing).
  2. A trained neural network learning from noisy data (Soft Computing).
- **Run**:
  ```bash
  python labs/lab06_symbolic_vs_neural_showdown.py
  ```
