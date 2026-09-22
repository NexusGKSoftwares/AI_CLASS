"""
Lab 05: NLP Fundamentals & Chain-of-Thought (CoT) Reasoning
Course: Introduction to Artificial Intelligence
Associated Lecture: Lecture 03 (NLP & Reasoning Components: Deductive, Inductive, CoT)

Concepts Demonstrated:
- NLP Pipeline: Tokenization, Stopword Filtering, Vocabulary Indexing
- Semantic Similarity via TF-IDF & Cosine Distance
- Chain-of-Thought (CoT) vs. Direct Answer Prediction
- Eliminating Hallucination & Arithmetic Drift in LLM Prompts
"""

import math
import re
from collections import Counter
from typing import List, Dict

# ------------------------------------------------------------------------------
# 1. NLP Pipeline: Tokenization & TF-IDF Vectorization
# ------------------------------------------------------------------------------
class SimpleNLPEngine:
    def __init__(self, corpus: List[str]):
        self.corpus = corpus
        self.vocabulary: Dict[str, int] = {}
        self.idf: Dict[str, float] = {}
        self.build_index()

    def tokenize(self, text: str) -> List[str]:
        """Lowers text and extracts alphabetic tokens."""
        return re.findall(r'\b[a-z]{2,}\b', text.lower())

    def build_index(self):
        # 1. Build Vocabulary
        all_tokens = set()
        tokenized_docs = [self.tokenize(doc) for doc in self.corpus]
        for tokens in tokenized_docs:
            all_tokens.update(tokens)
        self.vocabulary = {word: idx for idx, word in enumerate(sorted(all_tokens))}

        # 2. Compute Inverse Document Frequency (IDF)
        n_docs = len(self.corpus)
        for word in self.vocabulary:
            doc_freq = sum(1 for tokens in tokenized_docs if word in tokens)
            self.idf[word] = math.log((1 + n_docs) / (1 + doc_freq)) + 1.0

    def compute_tfidf_vector(self, text: str) -> List[float]:
        tokens = self.tokenize(text)
        counts = Counter(tokens)
        vec = [0.0] * len(self.vocabulary)
        for word, count in counts.items():
            if word in self.vocabulary:
                idx = self.vocabulary[word]
                tf = count / len(tokens) if tokens else 0
                vec[idx] = tf * self.idf[word]
        return vec

    def cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)


# ------------------------------------------------------------------------------
# 2. Chain of Thought (CoT) Simulation (Lecture 03 Math Problem)
# ------------------------------------------------------------------------------
def simulate_chain_of_thought():
    problem_text = (
        "A baker has 4 loaves of dough. She cuts each into 8 slices. "
        "An order takes 18 slices, and she eats 2 slices. "
        "She packages the rest into bags of 3. How many bags can she fill?"
    )

    print("\n--- Chain of Thought Reasoning Demo ---")
    print(f"Problem Statement:\n\"{problem_text}\"\n")

    # Simulation 1: Standard Direct Prompting (Hallucination Failure Mode)
    print("[1] Standard Direct Prompting (Failure Mode):")
    print("    Prompt : \"Directly output the final number of bags without steps.\"")
    hallucinated_answer = 5 # As observed in lecture notes failure mode
    print(f"    Output : {hallucinated_answer} bags")
    print("    Result : ❌ INCORRECT (Caused by simultaneous multi-operation drift)\n")

    # Simulation 2: Chain of Thought Prompting (Decomposed Token Generation)
    print("[2] Chain of Thought (CoT) Step-by-Step Execution:")
    steps = [
        ("Step 1 (Total slices produced)", "4 loaves * 8 slices/loaf", 4 * 8, "slices"),
        ("Step 2 (Total slices consumed)", "18 order slices + 2 eaten slices", 18 + 2, "slices used"),
        ("Step 3 (Slices remaining)", "32 produced - 20 used", 32 - 20, "slices left"),
        ("Step 4 (Bagging quotient)", "12 slices / 3 slices per bag", 12 // 3, "full bags")
    ]

    for label, formula, result, unit in steps:
        print(f"    - {label:<32}: {formula:<32} = {result} {unit}")

    final_cot_answer = steps[-1][2]
    print(f"\n    Final Verifiable Answer: {final_cot_answer} bags")
    print("    Result: ✅ 100% CORRECT (Conditioned on verifiable previous tokens)")


def main():
    print("=" * 65)
    print("      LAB 05: NLP PIPELINE & CHAIN-OF-THOUGHT REASONING     ")
    print("=" * 65)

    # NLP Document Search Demo
    knowledge_docs = [
        "Artificial intelligence systems use perception and reasoning to act.",
        "Convolutional neural networks and deep learning excel in computer vision.",
        "SWI-Prolog performs symbolic logic reasoning through unification.",
        "Reinforcement learning trains agents using rewards and trial and error."
    ]

    engine = SimpleNLPEngine(knowledge_docs)
    query = "How do deep neural networks handle vision and perception?"

    print("NLP Corpus Search with TF-IDF:")
    print(f"Query: \"{query}\"\n")

    query_vec = engine.compute_tfidf_vector(query)
    scores = []
    for i, doc in enumerate(knowledge_docs):
        doc_vec = engine.compute_tfidf_vector(doc)
        sim = engine.cosine_similarity(query_vec, doc_vec)
        scores.append((sim, doc))

    scores.sort(reverse=True, key=lambda x: x[0])
    for rank, (sim, doc) in enumerate(scores, 1):
        print(f"  Rank {rank} (Sim: {sim:.4f}): \"{doc}\"")

    # Run CoT Demo
    simulate_chain_of_thought()
    print("=" * 65)

if __name__ == "__main__":
    main()
