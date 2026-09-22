"""
Lab 04: Computational Intelligence - Deep Learning with PyTorch
Course: Introduction to Artificial Intelligence
Associated Lecture: Lecture 03 (Learning Component) & Lecture 04 (Soft Computing)

Concepts Demonstrated:
- Multi-Layer Perceptron (MLP) Architecture
- Activation Functions (Non-linear transformations via ReLU)
- Loss Formulation (Cross-Entropy) & Backpropagation via Autograd
- Gradient Descent Optimization (Adam Optimizer)
- Generalization, Epochs, and Accuracy Metrics
"""

import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib
matplotlib.use('Agg') # Headless mode for clean chart generation
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# ------------------------------------------------------------------------------
# 1. Dataset Generation: Non-linear 2D Classification (Soft Computing Benchmark)
# ------------------------------------------------------------------------------
def generate_synthetic_data(n_samples=600):
    """Generates two concentric non-linearly separable rings."""
    n_per_ring = n_samples // 2

    # Inner circle (Class 0)
    r1 = np.random.uniform(0.0, 0.4, n_per_ring)
    theta1 = np.random.uniform(0, 2 * np.pi, n_per_ring)
    X1 = np.stack([r1 * np.cos(theta1), r1 * np.sin(theta1)], axis=1)
    y1 = np.zeros(n_per_ring)

    # Outer ring (Class 1)
    r2 = np.random.uniform(0.7, 1.1, n_per_ring)
    theta2 = np.random.uniform(0, 2 * np.pi, n_per_ring)
    X2 = np.stack([r2 * np.cos(theta2), r2 * np.sin(theta2)], axis=1)
    y2 = np.ones(n_per_ring)

    X = np.vstack([X1, X2])
    y = np.concatenate([y1, y2])

    # Shuffle
    indices = np.random.permutation(n_samples)
    X, y = X[indices], y[indices]

    # Convert to PyTorch Tensors
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.long)

    # Split train (80%) and test (20%)
    split = int(0.8 * n_samples)
    return X_tensor[:split], y_tensor[:split], X_tensor[split:], y_tensor[split:]


# ------------------------------------------------------------------------------
# 2. Neural Network Architecture (MLP)
# ------------------------------------------------------------------------------
class SimpleClassifierMLP(nn.Module):
    def __init__(self, input_dim=2, hidden_dim=16, num_classes=2):
        super(SimpleClassifierMLP, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        return self.network(x)


# ------------------------------------------------------------------------------
# 3. Training & Evaluation
# ------------------------------------------------------------------------------
def main():
    print("=" * 65)
    print("      LAB 04: PYTORCH NEURAL NETWORK & SOFT COMPUTING       ")
    print("=" * 65)

    X_train, y_train, X_test, y_test = generate_synthetic_data()
    print(f"Data Prepared:")
    print(f"  - Training Set : {X_train.shape[0]} samples")
    print(f"  - Test Set     : {X_test.shape[0]} samples")

    model = SimpleClassifierMLP(input_dim=2, hidden_dim=32, num_classes=2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    epochs = 100
    loss_history = []
    accuracy_history = []

    print("\nTraining Multi-Layer Perceptron (Backprop & Optimization):")
    for epoch in range(1, epochs + 1):
        model.train()
        optimizer.zero_grad()

        # Forward pass
        logits = model(X_train)
        loss = criterion(logits, y_train)

        # Backward pass
        loss.backward()
        optimizer.step()

        loss_history.append(loss.item())

        # Evaluate train accuracy
        with torch.no_grad():
            preds = torch.argmax(logits, dim=1)
            acc = (preds == y_train).float().mean().item() * 100
            accuracy_history.append(acc)

        if epoch % 20 == 0 or epoch == 1:
            print(f"  Epoch [{epoch:03d}/{epochs}] | Loss: {loss.item():.4f} | Train Acc: {acc:.2f}%")

    # Final Test Set Evaluation
    model.eval()
    with torch.no_grad():
        test_logits = model(X_test)
        test_loss = criterion(test_logits, y_test)
        test_preds = torch.argmax(test_logits, dim=1)
        test_acc = (test_preds == y_test).float().mean().item() * 100

    print("\n" + "-" * 65)
    print(f"[✓] Final Test Accuracy: {test_acc:.2f}% | Test Loss: {test_loss.item():.4f}")
    print("-" * 65)

    # Plot & save loss curve
    fig, ax1 = plt.subplots(figsize=(8, 4.5))
    ax1.set_title("Lab 04: PyTorch Neural Network Training Dynamics")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss", color='tab:red')
    ax1.plot(loss_history, color='tab:red', label='Cross-Entropy Loss', linewidth=2)
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Accuracy (%)", color='tab:blue')
    ax2.plot(accuracy_history, color='tab:blue', label='Train Accuracy', linewidth=2, linestyle='--')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    plt.tight_layout()
    plot_path = os.path.join(os.path.dirname(__file__), "lab04_loss_curve.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"[✓] Training plot successfully generated: {plot_path}")
    print("=" * 65)

if __name__ == "__main__":
    main()
