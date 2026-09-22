# Lecture 03: Core Components of AI Systems

---

## Overview: The Cognitive Architecture of AI

Intelligent behavior in AI systems is driven by an interconnected cycle of **six core components**:

```
                         +-------------------+
                         |    PERCEPTION     |  <--- Gathers raw sensory inputs
                         +-------------------+
                                   │
                                   ▼
                         +-------------------+
                         |     KNOWLEDGE     |  <--- Structures & stores facts
                         |  REPRESENTATION   |
                         +-------------------+
                                   │
             +---------------------+---------------------+
             │                     │                     │
             ▼                     ▼                     ▼
     +---------------+     +---------------+     +---------------+
     |   LEARNING    |     |   REASONING   |     |PROBLEM SOLVING|
     | (Adaptation & |     |  (Inference   |     |  (Search &    |
     | Optimization) |     |  Derivation)  |     |  Planning)    |
     +---------------+     +---------------+     +---------------+
             │                     │                     │
             +---------------------+---------------------+
                                   │
                                   ▼
                         +-------------------+
                         | NATURAL LANGUAGE  |  <--- Human-machine interface
                         |    PROCESSING     |
                         +-------------------+
```

---

## 1. Perception
Perception converts raw, unstructured signals from the physical or digital environment into structured representations. It acts as the "senses" of the agent.

- **Key Subfields**:
  - **Computer Vision**: Image recognition, object detection, spatial segmentation.
  - **Audio & Speech Processing**: Acoustic modeling, automated speech recognition (ASR), pitch/tone extraction.
  - **Sensor Fusion**: Combining heterogeneous streams (e.g., LiDAR, radar, cameras, IMUs) into a single coherent environmental map.

---

## 2. Knowledge Representation (KR)
The formal system used to encode information about the world in a machine-readable format for algorithmic retrieval and inference.

- **Common Techniques**:
  1. **Semantic Networks**: Graph structures with nodes (concepts) and labeled edges (relations).
  2. **Knowledge Graphs**: Large-scale factual triples `(entity, relation, entity)` like `(Paris, isCapitalOf, France)`.
  3. **Ontologies**: Formal specifications of concepts, taxonomy hierarchies, and domain axioms (e.g., OWL, Protégé).
  4. **Vector Embeddings**: Dense continuous vector spaces where semantic similarity correlates with geometric proximity (e.g., cosine similarity).
  5. **Propositional Logic**: Boolean logic dealing with complete declarative statements without internal variables.
  6. **First-Order Predicate Logic (FOL)**: Rich logic using predicates, objects, functions, and quantifiers ($\forall, \exists$).

---

## 3. Learning
The capacity to adapt and improve task performance over time based on data, experience, or environment feedback without hardcoded rules.

| Paradigm | Training Signal | Objective / Mechanism | Real-World Example |
| :--- | :--- | :--- | :--- |
| **Supervised Learning** | Labeled pairs $(X, Y)$ | Learns a mapping function $f: X \to Y$. | Spam classification, medical diagnosis prediction. |
| **Unsupervised Learning** | Unlabeled data $X$ | Discovers latent structures, clusters, or probability distributions. | Customer segmentation, dimensionality reduction (PCA, t-SNE). |
| **Self-Supervised Learning** | Raw unlabeled data with masked/corrupted tokens | Generates supervisory signals internally by predicting hidden portions. | Masked language modeling in BERT, next-token prediction in GPT. |
| **Meta-Learning** | Tasks across task distributions | "Learning how to learn"; optimizes the learning algorithm for rapid few-shot adaptation. | Few-shot image recognition (MAML). |
| **Reinforcement Learning** | Scalar reward/penalty signals | Learns an optimal policy $\pi(s)$ via trial-and-error sequential interactions. | AlphaGo, robotic locomotion, RLHF in language models. |
| **Transfer Learning** | Knowledge from a source domain | Repurposes learned representations to a target domain with minimal extra training. | Fine-tuning a vision model trained on ImageNet for specialized CT scan analysis. |

---

## 4. Reasoning
The computational process of applying logic and rules to existing knowledge to deduce new facts or evaluate hypotheses.

### 4.1 Forms of Reasoning

#### A. Deductive Reasoning (General $\to$ Specific)
- **Rule**: If premises are true and the syllogism is valid, the conclusion **must** be true. There is zero uncertainty.
- **Example**:
  - *Premise 1*: All planets in our solar system orbit the Sun.
  - *Premise 2*: Jupiter is a planet in our solar system.
  - *Conclusion*: Jupiter orbits the Sun.

#### B. Inductive Reasoning (Specific $\to$ General)
- **Rule**: Infers general principles from historical observations. Premises provide probabilistic support, but **do not guarantee** absolute truth.
- **Example**:
  - *Observation*: The shop opened at 7:00 AM on Monday through Sunday.
  - *Conclusion*: The shop always opens at 7:00 AM every day.
  - *(Caveat: A single counterexample—such as a holiday or illness—invalidates the rule).*

#### C. Abductive Reasoning (Inference to the Best Explanation)
- **Rule**: Starts with an incomplete set of observations and derives the most likely or plausible explanation.
- **Example**:
  - *Observation*: The grass is wet only inside the garden perimeter.
  - *Hypothesis 1*: A localized rain cloud rained solely over the garden.
  - *Hypothesis 2*: The garden sprinkler ran before dawn.
  - *Conclusion*: Hypothesis 2 is selected as the best plausible explanation.

#### D. Chain of Thought (CoT) Reasoning in Modern LLMs
- **Definition**: A prompting and fine-tuning mechanism that instructs language models to generate sequential intermediate reasoning steps before arriving at a final answer.
- **Why it matters**: Autoregressive models generate one token at a time conditioned on previous tokens. Decomposing calculations eliminates compounding reasoning drift and arithmetic hallucinations.

```
Problem:
"A baker has 4 loaves of dough. She cuts each into 8 slices.
 An order takes 18 slices, and she eats 2 slices.
 She packages the rest into bags of 3. How many bags can she fill?"

❌ Standard Prompting (Failure Mode):
   LLM attempts direct single-step leap -> "5 bags" (Incorrect hallucination)

✅ Chain of Thought Execution (Step-by-Step):
   Step 1 (Total slices)    : 4 * 8 = 32 slices
   Step 2 (Slices consumed) : 18 + 2 = 20 slices used
   Step 3 (Slices remaining): 32 - 20 = 12 slices left
   Step 4 (Bagging)         : 12 / 3 = 4 bags
   Final Output             : 4 bags
```

---

## 5. Problem Solving
The deliberate process of selecting a sequence of actions that transforms a system from a known **initial state** to a desired **goal state**.

- **Approaches**:
  1. **Search Algorithms**:
     - Heuristic Search: **A\*** (optimal pathfinding combining cost-so-far and estimated remaining distance).
     - Adversarial Search: **Minimax** with Alpha-Beta pruning, **Monte Carlo Tree Search (MCTS)**.
  2. **Constraint Satisfaction Problems (CSP)**:
     - Solving variables subject to explicit constraints (e.g., Sudoku, job scheduling, map coloring).
  3. **Automated Planning**:
     - Formulating STRIPS/PDDL state transitions to determine complex action plans.
- **Categorization**:
  - **General-Purpose Methods**: Applicable across diverse problems (e.g., general tree/graph search engines).
  - **Special-Purpose Methods**: Tailored and optimized for specific domains (e.g., dedicated chess evaluation functions, route optimization engines).

---

## 6. Natural Language Processing (NLP)
The computational discipline enabling machines to parse, comprehend, generate, and translate human natural languages.

### Core NLP Tasks
1. **Natural Language Understanding (NLU)**: Syntactic parsing, intent classification, and semantic analysis.
2. **Natural Language Generation (NLG)**: Transforming structured data into coherent, grammatically fluent human text.
3. **Machine Translation**: Translating source text across different languages while preserving semantics.
4. **Dialogue Systems**: Managing multi-turn contextual conversations and user state.

### Key NLP Techniques & Pipeline
- **Tokenization**: Breaking raw text into subword or word units.
- **Part-of-Speech (POS) Tagging**: Labeling nouns, verbs, adjectives.
- **Named Entity Recognition (NER)**: Identifying entities (e.g., people, locations, order IDs, dates).
- **Transformer Self-Attention**: Computing contextual token dependencies across long sequences.
- **Autoregressive Generation**: Iteratively sampling next-token probability distributions.
