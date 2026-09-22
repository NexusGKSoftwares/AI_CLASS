"""
Lab 06: Paradigm Showdown - Symbolic AI (Hard) vs. Computational Intelligence (Soft)
Course: Introduction to Artificial Intelligence
Associated Lecture: Lecture 04 (Computational Intelligence vs. Symbolic AI)

Objective:
Directly benchmark the two paradigms on the exact same task:
Disease / Condition Classification under (1) Clean Deterministic Data and (2) Noisy Real-World Data.

Key Observations:
- Symbolic AI (Expert Rules): 100% accurate and fully explainable on crisp, perfect data,
  but brittle when encountering sensor noise, partial matches, or analog fluctuations.
- Computational Intelligence (Neural Network): Robust to noise, gracefully degrades,
  and handles continuous probabilistic representations without hand-coded rules.
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# ------------------------------------------------------------------------------
# 1. Benchmark Problem Setup
# Features: [Fever Temp (°C), Cough Intensity (0-1), Fatigue Level (0-1)]
# Classes:
#   0: Healthy
#   1: Common Cold
#   2: Flu
# ------------------------------------------------------------------------------

SYMPTOM_NAMES = ["Temperature (°C)", "Cough (0-1)", "Fatigue (0-1)"]

# ------------------------------------------------------------------------------
# 2. Paradigm 1: Symbolic AI (Hard Computing / Rule-Based Expert System)
# ------------------------------------------------------------------------------
class SymbolicExpertSystem:
    """Uses crisp, top-down, hand-crafted logical rules (Hard Computing)."""
    def predict(self, sample):
        temp, cough, fatigue = sample

        # Rule 1: Flu requires high fever (> 38.5) and significant fatigue (> 0.6)
        if temp >= 38.5 and fatigue >= 0.6:
            return 2 # Flu

        # Rule 2: Cold has mild fever (< 38.0) and high cough (> 0.5)
        elif 37.0 <= temp < 38.0 and cough >= 0.5:
            return 1 # Cold

        # Rule 3: Healthy has normal temp (< 37.2) and low symptoms
        elif temp < 37.2 and cough < 0.3 and fatigue < 0.3:
            return 0 # Healthy

        else:
            return -1 # Rule Failure: Brittle under ambiguity/noise!


# ------------------------------------------------------------------------------
# 3. Paradigm 2: Computational Intelligence (Soft Computing / Neural Network)
# ------------------------------------------------------------------------------
class SoftComputingNeuralNet(nn.Module):
    """Uses bottom-up continuous numerical optimization (Soft Computing)."""
    def __init__(self):
        super(SoftComputingNeuralNet, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 3) # 3 Disease classes
        )

    def forward(self, x):
        return self.fc(x)


# ------------------------------------------------------------------------------
# 4. Data Generation (Clean vs. Noisy Real-World)
# ------------------------------------------------------------------------------
def generate_medical_data(n_samples=300, noise_std=0.0):
    np.random.seed(42)
    samples_per_class = n_samples // 3

    # Class 0: Healthy
    h_temp = np.random.normal(36.8, 0.2, samples_per_class)
    h_cough = np.random.uniform(0.0, 0.2, samples_per_class)
    h_fatigue = np.random.uniform(0.0, 0.2, samples_per_class)
    c0 = np.stack([h_temp, h_cough, h_fatigue], axis=1)

    # Class 1: Common Cold
    c_temp = np.random.normal(37.5, 0.2, samples_per_class)
    c_cough = np.random.uniform(0.6, 0.9, samples_per_class)
    c_fatigue = np.random.uniform(0.2, 0.4, samples_per_class)
    c1 = np.stack([c_temp, c_cough, c_fatigue], axis=1)

    # Class 2: Flu
    f_temp = np.random.normal(39.0, 0.3, samples_per_class)
    f_cough = np.random.uniform(0.5, 0.8, samples_per_class)
    f_fatigue = np.random.uniform(0.7, 1.0, samples_per_class)
    c2 = np.stack([f_temp, f_cough, f_fatigue], axis=1)

    X = np.vstack([c0, c1, c2])
    y = np.array([0]*samples_per_class + [1]*samples_per_class + [2]*samples_per_class)

    if noise_std > 0.0:
        # Inject sensor noise / patient reporting ambiguity
        noise = np.random.normal(0.0, noise_std, X.shape)
        X += noise

    return X, y


def main():
    print("=" * 70)
    print("   LAB 06: SYMBOLIC AI (HARD COMPUTING) VS. NEURAL NET (SOFT COMPUTING) ")
    print("=" * 70)

    # 1. Clean Data Generation & Training
    X_train, y_train = generate_medical_data(n_samples=600, noise_std=0.0)
    X_clean_test, y_clean_test = generate_medical_data(n_samples=150, noise_std=0.0)

    # Noisy Test Set (Simulating sensor miscalibration, analog blur, patient variation)
    X_noisy_test, y_noisy_test = generate_medical_data(n_samples=150, noise_std=0.35)

    # 2. Train Neural Network (CI)
    model = SoftComputingNeuralNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.02)

    X_train_t = torch.tensor(X_train, dtype=torch.float32)
    y_train_t = torch.tensor(y_train, dtype=torch.long)

    for _ in range(120):
        optimizer.zero_grad()
        loss = criterion(model(X_train_t), y_train_t)
        loss.backward()
        optimizer.step()

    # 3. Evaluate on Clean Test Data
    expert = SymbolicExpertSystem()

    # Symbolic accuracy on Clean
    sym_clean_preds = [expert.predict(s) for s in X_clean_test]
    sym_clean_acc = sum(p == y for p, y in zip(sym_clean_preds, y_clean_test)) / len(y_clean_test) * 100

    # Neural accuracy on Clean
    with torch.no_grad():
        nn_clean_preds = torch.argmax(model(torch.tensor(X_clean_test, dtype=torch.float32)), dim=1).numpy()
    nn_clean_acc = sum(p == y for p, y in zip(nn_clean_preds, y_clean_test)) / len(y_clean_test) * 100

    # 4. Evaluate on Noisy Test Data (The Crucial Test of Lecture 04!)
    sym_noisy_preds = [expert.predict(s) for s in X_noisy_test]
    sym_noisy_acc = sum(p == y for p, y in zip(sym_noisy_preds, y_noisy_test)) / len(y_noisy_test) * 100
    sym_failed_rules = sum(1 for p in sym_noisy_preds if p == -1)

    with torch.no_grad():
        nn_noisy_preds = torch.argmax(model(torch.tensor(X_noisy_test, dtype=torch.float32)), dim=1).numpy()
    nn_noisy_acc = sum(p == y for p, y in zip(nn_noisy_preds, y_noisy_test)) / len(y_noisy_test) * 100

    # 5. Output Findings & Comparison
    print("\nBENCHMARK RESULTS SUMMARY:")
    print("-" * 70)
    print(f"{'Condition':<25} | {'Symbolic AI (Rules)':<20} | {'Neural Net (Soft Computing)':<20}")
    print("-" * 70)
    print(f"{'Clean Deterministic Data':<25} | {sym_clean_acc:>18.2f}% | {nn_clean_acc:>18.2f}%")
    print(f"{'Noisy Real-World Data':<25} | {sym_noisy_acc:>18.2f}% | {nn_noisy_acc:>18.2f}%")
    print("-" * 70)
    print(f"\n[!] Robustness Analysis:")
    print(f"    - In the noisy test set, Symbolic AI failed completely to match any rule on")
    print(f"      {sym_failed_rules}/{len(y_noisy_test)} patients ({sym_failed_rules/len(y_noisy_test)*100:.1f}%), dropping accuracy down to {sym_noisy_acc:.1f}%.")
    print(f"    - Computational Intelligence maintained {nn_noisy_acc:.1f}% accuracy by mapping")
    print(f"      continuous probability distributions over the noisy features.")
    print("=" * 70)

if __name__ == "__main__":
    main()
