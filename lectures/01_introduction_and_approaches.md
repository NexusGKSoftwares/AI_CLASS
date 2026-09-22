# Lecture 01: Introduction & Historical Approaches to AI

---

## 1. What is Artificial Intelligence?

The term **Artificial Intelligence (AI)** was coined by **John McCarthy** in **1956** at the historic **Dartmouth Conference**, where he defined it as:
> *"The science and engineering of making intelligent machines, especially intelligent computer programs."*

### Key Historical Definitions

| Scholar / Source | Year | Definition | Focus |
| :--- | :--- | :--- | :--- |
| **John McCarthy** | 1956 | The science and engineering of making intelligent machines, especially intelligent computer programs. | General Engineering |
| **Ray Kurzweil** | 1990 | The art of creating machines that perform functions that require intelligence when performed by people. | Human emulation |
| **Patrick Winston** | 1992 | The study of the computations that make it possible to perceive, reason, and act. | Computational loop |
| **Robert Schalkoff**| 1990 | A field of study that seeks to explain and emulate intelligent behavior in terms of computational processes. | Computational processes |
| **Luger & Stubblefield** | 1993 | The branch of computer science that is concerned with the automation of intelligent behavior. | Computer science & automation |

---

## 2. The Four Approaches to AI

Historically, AI research has followed four distinct paths based on two dimensions:
1. **Human Performance** vs. **Ideal Rationality**
2. **Internal Thought Processes** vs. **External Behavior**

### Table 1: Matrix of Historical Approaches to AI

```
                         HUMAN-LIKE                   RATIONAL
               +-----------------------------+-----------------------------+
   THINKING    |    Thinking Humanly         |      Thinking Rationally    |
               |  (Cognitive Modeling)       |      (Laws of Thought)      |
               +-----------------------------+-----------------------------+
    ACTING     |     Acting Humanly          |       Acting Rationally     |
               |      (Turing Test)          |       (Rational Agents)     |
               +-----------------------------+-----------------------------+
```

| Approach | Focus | Key Concept |
| :--- | :--- | :--- |
| **Acting Humanly** | Turing Test | Building systems that can act indistinguishably from humans in conversation and interaction. |
| **Thinking Humanly** | Cognitive Modeling | Emulating human neural and mental mechanisms using introspection, psychological experiments, and brain imaging. |
| **Thinking Rationally**| Laws of Thought | Applying formal computational logic and syllogisms to derive indisputably correct inferences. |
| **Acting Rationally** | Rational Agents | Acting to achieve the best expected outcome given available information and constraints. |

---

## 3. Deep Dive into the Approaches

### 3.1 Acting Humanly: The Turing Test Approach

Proposed by **Alan Turing (1950)** in his seminal paper *"Computing Machinery and Intelligence"*, the test assesses whether a machine can exhibit intelligent behavior indistinguishable from that of a human.

#### The Test Setup
- A human interrogator interacts with both a human and a computer via text terminal.
- If the interrogator cannot reliably tell which entity is the machine, the computer passes the test.

#### Capabilities Required for the Turing Test:
1. **Natural Language Processing (NLP)**: To communicate and parse questions/answers fluently in human language.
2. **Knowledge Representation**: To store facts, experiences, and contextual information.
3. **Automated Reasoning**: To use stored knowledge to answer questions and draw new conclusions.
4. **Machine Learning**: To adapt to new circumstances, learn from patterns, and extrapolate knowledge.

#### The Total Turing Test
To assess physical perception and interaction with the world, the **Total Turing Test** adds:
5. **Computer Vision**: To perceive and identify physical objects and environments.
6. **Robotics**: To manipulate objects, navigate physical spaces, and interact physically.

---

### 3.2 Thinking Humanly: The Cognitive Modeling Approach

Rather than merely outputting human-like answers, this approach requires machines to **mimic the internal reasoning and thought processes** of the human brain.

- Bridges **AI** and **Cognitive Psychology** to develop a computational theory of mind.
- **Validation Methods**:
  1. **Introspection**: Tracking and recording our own cognitive thought steps as they happen.
  2. **Psychological Experiments**: Observing human subjects performing tasks (measuring reaction times, error distributions, cognitive loads).
  3. **Brain Imaging**: Using MRI, fMRI, and EEG scans to observe physical neurobiological activity in real time.
- **Crucial Distinction**: Getting the right answer is not enough if the underlying algorithm diverges from human cognition.
  - *Example*: A chess engine evaluating 10 billion moves per second behaves intelligently, but it is **not** thinking humanly because human masters use selective heuristics and pattern recognition rather than brute-force combinatorial search.

---

### 3.3 Thinking Rationally: The Laws of Thought Approach

Based on the study of mental faculties through **computational logic** and irrefutable inference rules.

- **Roots in Aristotelian Syllogisms**:
  - *Premise 1*: Socrates is a man.
  - *Premise 2*: All men are mortal.
  - *Conclusion*: Therefore, Socrates is mortal.
- By the 19th and 20th centuries, formal notations were developed for propositional and first-order predicate logic.
- In 1965, general theorem provers demonstrated that, in principle, any solvable problem formulated in first-order logic could be resolved computationally.

#### Major Limitations:
1. **Handling Uncertainty**: Pure formal logic requires crisp true/false values; it struggles with incomplete, ambiguous, or probabilistic real-world knowledge.
2. **Computational Complexity**: Many logical inference tasks are computationally intractable ($NP$-hard or undecidable). A solution solvable "in principle" may take billions of years in practice.
3. **Representational Gap**: Translating messy, colloquial real-world facts into strict mathematical logic notations without loss of context is extremely difficult.
