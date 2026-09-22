# Artificial Intelligence Course Notes & Practical Laboratory

Welcome to the **Artificial Intelligence (AI)** course repository. This repository contains organized lecture notes, conceptual breakdowns, comparative tables, and a complete suite of hands-on lab practicals.

---

## 🛠️ Lab Environment & Installed Software

- **PyTorch Stack**: `torch (2.2.2)`, `torchvision (0.17.2)`, `torchaudio (2.2.2)`
- **Scientific Computing & Data**: `numpy (1.26.4)`, `scipy (1.13.1)`, `pandas (2.3.3)`, `matplotlib (3.9.4)`
- **Interactive Labs**: `jupyterlab (4.5.11)`
- **Symbolic Logic Engine**: `swi-prolog (10.0.2)` (`swipl`) & Python bridge `pyswip`

### Quick Start for Labs
```bash
# 1. Navigate & Activate Virtual Environment
cd /Users/ba/TEKVORA_SOFFTWARES/AI_CLASS
source .venv/bin/activate

# 2. Launch Interactive Jupyter Notebook
jupyter lab labs/interactive_ai_lab.ipynb
```

---

## 🔬 Practical Laboratory Suite (`labs/`)

Detailed step-by-step instructions can be found in the [**Lab Manual (`labs/LAB_MANUAL.md`)**](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/LAB_MANUAL.md).

| Lab | Practical Topic | Language | File Link |
| :--- | :--- | :--- | :--- |
| **Lab 01** | **Symbolic AI & Expert Systems**<br>• Knowledge representation, facts, rules, Aristotelian syllogisms<br>• Recursive ancestor queries & Medical diagnostic expert system | Prolog | [`labs/lab01_prolog_knowledge_base.pl`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab01_prolog_knowledge_base.pl) |
| **Lab 02** | **Rational Agents & Environment Simulation**<br>• Russell & Norvig's 2-State Vacuum Cleaner World<br>• Performance measures, percept sequences & state models<br>• Reflex Agent vs. Rational Model-Based Agent | Python | [`labs/lab02_rational_agent_simulation.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab02_rational_agent_simulation.py) |
| **Lab 03** | **Problem Solving & Heuristic Search**<br>• State-space graph & obstacle grid pathfinding<br>• Uninformed BFS vs. Informed $A^*$ Search with Manhattan heuristics<br>• Exploration efficiency and ASCII path visualization | Python | [`labs/lab03_search_algorithms_astar.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab03_search_algorithms_astar.py) |
| **Lab 04** | **Neural Networks & Soft Computing**<br>• PyTorch Multi-Layer Perceptron (MLP) architecture<br>• Forward pass, ReLU activations, CrossEntropyLoss & Backprop<br>• Non-linear decision boundary & loss curve generation | PyTorch | [`labs/lab04_pytorch_neural_network.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab04_pytorch_neural_network.py) |
| **Lab 05** | **NLP Pipeline & Chain of Thought (CoT)**<br>• Text tokenization, TF-IDF vectorization & cosine similarity<br>• Chain-of-Thought (CoT) problem decomposition<br>• Eliminating hallucinations on the lecture baker dough problem | Python | [`labs/lab05_nlp_and_chain_of_thought.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab05_nlp_and_chain_of_thought.py) |
| **Lab 06** | **Paradigm Showdown: Symbolic AI vs. Neural Networks**<br>• Direct benchmark on medical diagnosis<br>• Symbolic AI (Hard Computing) vs. Neural Nets (Soft Computing)<br>• Clean deterministic data vs. noisy real-world data tolerance | Python + Prolog | [`labs/lab06_symbolic_vs_neural_showdown.py`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/lab06_symbolic_vs_neural_showdown.py) |
| **Interactive** | **Jupyter Lab Notebook**<br>Interactive live code execution for all lab modules | Python | [`labs/interactive_ai_lab.ipynb`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/labs/interactive_ai_lab.ipynb) |

---

## 📚 Course Syllabus & Lecture Index

| Lecture | Title & Key Topics | File |
| :--- | :--- | :--- |
| **Lecture 01** | **Introduction & Historical Approaches to AI**<br>• Core definitions (McCarthy, Kurzweil, Winston, etc.)<br>• The Four Approaches to AI<br>• The Turing Test & Total Turing Test<br>• Cognitive Modeling & Laws of Thought | [`lectures/01_introduction_and_approaches.md`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/lectures/01_introduction_and_approaches.md) |
| **Lecture 02** | **Rational Agents & Modern State of the Art (SOTA)**<br>• Acting Rationally & Rational Agents<br>• Categorization by breadth (ANI, AGI, ASI)<br>• AI Alignment<br>• Foundation Models (Transformers, pre-training, fine-tuning)<br>• Current SOTA developments (LLMs, Multimodal, Agentic AI, GenAI) | [`lectures/02_rational_agents_and_modern_ai.md`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/lectures/02_rational_agents_and_modern_ai.md) |
| **Lecture 03** | **Core Components of AI Systems**<br>• Perception (Computer Vision, Audio, Sensor Fusion)<br>• Knowledge Representation (Semantic Networks, Ontologies, Logic, Embeddings)<br>• Learning (Supervised, Unsupervised, Self-Supervised, Meta, RL, Transfer)<br>• Reasoning (Deductive, Inductive, Abductive, Chain of Thought)<br>• Problem Solving (Search, A*, Minimax, CSP)<br>• Natural Language Processing (NLU, NLG, Transformers) | [`lectures/03_components_of_ai.md`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/lectures/03_components_of_ai.md) |
| **Lecture 04** | **Computational Intelligence vs. Symbolic AI**<br>• Symbolic AI / "Hard Computing" (Top-down, rules, logic)<br>• Computational Intelligence / "Soft Computing" (Bottom-up, neural nets, evolutionary algorithms)<br>• Detailed Comparison Table | [`lectures/04_computational_intelligence_vs_symbolic_ai.md`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/lectures/04_computational_intelligence_vs_symbolic_ai.md) |

---

## 📢 Important Notices & Schedule

- **Upcoming Class**: Thursday at 10:00 AM
- **Lab Requirements**:
  - Find a lab partner
  - Carry your laptop to class
- See details in [`announcements/schedule_and_notices.md`](file:///Users/ba/TEKVORA_SOFFTWARES/AI_CLASS/announcements/schedule_and_notices.md).
