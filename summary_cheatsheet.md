# AI Class Quick Revision Cheatsheet

A high-yield study sheet summarizing the core definitions, comparisons, and mechanisms from Lectures 1 to 4.

---

## 1. Core Definitions to Remember

- **Artificial Intelligence (John McCarthy, 1956)**: The science and engineering of making intelligent machines, especially intelligent computer programs.
- **Rational Agent**: An entity that acts to maximize its expected performance measure given its percept sequence and built-in knowledge base.
- **Turing Test (Alan Turing, 1950)**: Measures operational human indistinguishability through text.
  - *Standard Requirements*: NLP, Knowledge Representation, Automated Reasoning, Machine Learning.
  - *Total Turing Test Requirements*: Computer Vision + Robotics.
- **AI Alignment**: Ensuring AI behavior remains strictly safe, controllable, and consistent with human values.

---

## 2. The 4 Approaches to AI Matrix

| | **Human-Like** | **Rational** |
| :--- | :--- | :--- |
| **Thinking** | **Cognitive Modeling**: Emulates brain mechanics (introspection, fMRI/EEG, experiments). | **Laws of Thought**: Syllogisms and formal logic provers (Aristotle, Russell). |
| **Acting** | **Turing Test**: External behavioral mimicry indistinguishable from humans. | **Rational Agent**: Maximizes expected utility via percept-action cycles (dominant view). |

---

## 3. Categories by Scope

1. **ANI (Artificial Narrow / Weak AI)**: Specialized single-domain systems (chess bots, spam filters, face recognition). Currently prevalent.
2. **AGI (Artificial General / Strong AI)**: Human-equivalent cross-domain versatility and transfer learning.
3. **ASI (Artificial Superintelligence)**: Exceeds the entirety of human intellect across every creative and analytical discipline.

---

## 4. Modern SOTA & Foundation Models

- **Architecture**: Transformer (`Vaswani et al., 2017`).
- **Phases**:
  1. *Pre-training*: Large-scale self-supervised learning on massive web data.
  2. *Fine-tuning / Alignment*: SFT, RLHF, PEFT (LoRA), prompt engineering.
- **4 Pillars of SOTA AI**:
  1. *Large Language Models (LLMs)*
  2. *Multimodal Models* (Text + Image + Audio + Video)
  3. *Agentic AI* (LLM core + Memory + Tools + Autonomous Planners)
  4. *Generative AI* (High-fidelity synthetic asset creation)

---

## 5. The 6 Core Components of AI

1. **Perception**: Computer vision, speech recognition, multi-sensor fusion.
2. **Knowledge Representation**: Semantic networks, knowledge graphs, ontologies, dense vector embeddings, first-order logic.
3. **Learning**:
   - *Supervised*: Labeled $(X, Y)$ pairs.
   - *Unsupervised*: Latent patterns, clustering without targets.
   - *Self-Supervised*: Reconstructing masked/hidden tokens (e.g., BERT, GPT).
   - *Meta-Learning*: Learning how to learn (few-shot optimization).
   - *Reinforcement Learning*: Sequential decision-making guided by rewards/penalties.
   - *Transfer Learning*: Repurposing domain knowledge into another domain.
4. **Reasoning**:
   - *Deductive*: General $\to$ Specific (guaranteed true if premises true).
   - *Inductive*: Specific $\to$ General (probabilistic, counterexamples possible).
   - *Abductive*: Best plausible explanation given partial evidence.
   - *Chain of Thought (CoT)*: Step-by-step intermediate token decomposition to avoid hallucinations.
5. **Problem Solving**:
   - State-space search ($A^*$, Minimax, MCTS), CSP (Constraint Satisfaction), automated planning.
6. **Natural Language Processing (NLP)**:
   - NLU, NLG, Machine Translation, Dialogue Systems, Tokenization, Attention.

---

## 6. Computational Intelligence vs. Symbolic AI

| Feature | Computational Intelligence (Soft Computing) | Symbolic AI (Hard Computing) |
| :--- | :--- | :--- |
| **Approach** | Bottom-Up | Top-Down |
| **Data Format** | Numerical vectors, weights, continuous values | Discrete symbols, rules, logical predicates |
| **Pillars** | Neural networks, fuzzy logic, evolutionary algorithms | Expert systems, logic programming, search trees |
| **Environment** | Handles noisy, ambiguous real-world data | Needs crisp, clean, deterministic rules |
| **Explainability** | Low (Black box parameter distributions) | High (Explicit inference chains) |
