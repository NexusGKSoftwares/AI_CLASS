# Lecture 02: Rational Agents & Modern State of the Art (SOTA)

---

## 1. Acting Rationally: The Rational Agent

In contemporary AI, **acting rationally** is the dominant framework.

### Definition of a Rational Agent
> A **rational agent** is an entity that perceives its environment through sensors and acts upon that environment through actuators to **maximize its expected performance measure**, given the percept sequence and its built-in knowledge base.

- **Percept**: The agent's perceptual inputs at any given instant.
- **Percept Sequence**: The complete history of everything the agent has ever perceived.
- **Performance Measure**: An objective criterion used to evaluate how successful an agent's behavior is in achieving its goals.

```
                  +-----------------------------------+
                  |            ENVIRONMENT            |
                  +-----------------------------------+
                       |                         ^
              Percepts |                         | Actions
                       v                         |
                  +---------+               +-----------+
                  | SENSORS |               | ACTUATORS |
                  +---------+               +-----------+
                       |                         ^
                       v                         |
                  +-----------------------------------+
                  |          RATIONAL AGENT           |
                  |  Selects action to maximize       |
                  |  expected performance measure     |
                  +-----------------------------------+
```

### Advantages of the Rational Agent Approach
1. **Generality**: Correct logical inference is only one mechanism to achieve rationality. Reflex actions (e.g., pulling a hand away from a hot stove) can also be rational without deliberate logical derivation if they yield high expected utility.
2. **Mathematical Amenability**: Rationality is formulated around a precise, quantifiable standard (**expected utility / performance maximization**), avoiding subjective or ambiguous human comparisons.

---

## 2. Categorization of AI Systems

### 2.1 Categorization by Breadth of Capacity

```
+--------------------------------------------------------------------------------+
|  1. Artificial Narrow Intelligence (ANI)                                       |
|     - Solves single/specific domain tasks (chess, spam filters, vision).       |
+--------------------------------------------------------------------------------+
                                        │
                                        ▼
+--------------------------------------------------------------------------------+
|  2. Artificial General Intelligence (AGI)                                      |
|     - Human-level cross-domain reasoning, learning, and adaptability.          |
+--------------------------------------------------------------------------------+
                                        │
                                        ▼
+--------------------------------------------------------------------------------+
|  3. Artificial Superintelligence (ASI)                                         |
|     - Surpasses human intellect across all domains, scientific and creative.   |
+--------------------------------------------------------------------------------+
```

| Category | Also Known As | Scope & Characteristics | Current Status |
| :--- | :--- | :--- | :--- |
| **Artificial Narrow Intelligence (ANI)** | **Weak AI** | Designed for a dedicated, specific task (e.g., spam detection, chess/Go engines, facial recognition). Can outperform humans within that task, but cannot generalize outside of it. | **Everywhere today** (Autonomous vehicles, recommendation systems, medical diagnostics). |
| **Artificial General Intelligence (AGI)** | **Strong AI** | Systems capable of learning, reasoning, and transferring knowledge across any intellectual discipline at or above human level. | **Active frontier research** (OpenAI, Anthropic, Google DeepMind, etc.). |
| **Artificial Superintelligence (ASI)** | **Superintelligence** | A hypothetical system whose cognitive capacity surpasses the brightest human minds in every field (science, philosophy, creativity, social strategy). | **Theoretical / Safety research** frontier. |

> [!NOTE]
> **AI Alignment**: The discipline and science of ensuring that advanced AI systems pursue outcomes that are safe, beneficial, and reliably aligned with human intentions and ethics.

---

## 3. Foundation Models

A **Foundation Model** is a large-scale model trained on vast, diverse datasets via self-supervised learning that can be adapted to hundreds of downstream tasks.

- **Foundational Architecture**: Built primarily on the **Transformer architecture** (*Vaswani et al., 2017: "Attention Is All You Need"*).
- **Core Capability**: **Zero-shot** and **Few-shot** generalization—performing novel tasks directly from natural language prompts or minimal context examples without task-specific retraining.

### Two-Step Training Paradigm
1. **Pre-training**: Training on massive datasets (web text, code, images, audio) using unsupervised/self-supervised objectives to learn deep representations of the world.
2. **Fine-Tuning / Adaptation**: Refining the base model using:
   - **Supervised Fine-Tuning (SFT)** & **RLHF** (Reinforcement Learning from Human Feedback).
   - **Parameter-Efficient Fine-Tuning (PEFT)** (e.g., LoRA, Adapters).
   - **In-Context Prompting** and **Retrieval-Augmented Generation (RAG)**.

### Examples of Foundation Models across Modalities
- **Text & Multimodal**: GPT series, Claude, Gemini, LLaMA, Mistral, Qwen.
- **Image Generation**: DALL-E, Midjourney, Stable Diffusion, Imagen.
- **Video Generation**: Sora, Veo, Runway Gen-3.
- **Scientific / Biological**: AlphaFold (protein 3D structure prediction).

---

## 4. AI State of the Art (SOTA)

Four primary interconnected paradigms characterize modern AI:

1. **Large Language Models (LLMs)**:
   - Trained on trillions of tokens.
   - Exhibit emergent capabilities: in-context learning, multi-step chain-of-thought reasoning, code generation, and function/tool calling.
2. **Multimodal Models**:
   - Single unified architectures processing audio, speech, high-resolution imagery, text, and video simultaneously.
3. **Agentic AI**:
   - Systems that combine LLM reasoning cores with **planners, long-term memory, external APIs, and code execution environments** to autonomously solve multi-step workflows.
4. **Generative AI**:
   - Deep generative models producing high-fidelity text, audio, images, video, and 3D assets on demand.
