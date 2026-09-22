"""
PyTorch & Environment Health Check Script
Run with: source .venv/bin/activate && python labs/sample_pytorch_test.py
"""

import torch
import torchvision
import numpy as np
import scipy
import matplotlib
import pandas as pd

def main():
    print("=" * 60)
    print("       AI Class Environment - Installation Health Check")
    print("=" * 60)
    print(f"[✓] PyTorch Version     : {torch.__version__}")
    print(f"[✓] Torchvision Version : {torchvision.__version__}")
    print(f"[✓] NumPy Version       : {np.__version__}")
    print(f"[✓] SciPy Version       : {scipy.__version__}")
    print(f"[✓] Pandas Version      : {pd.__version__}")
    print(f"[✓] Matplotlib Version  : {matplotlib.__version__}")

    # Tensor computation test
    a = torch.tensor([[2.0, 3.0], [4.0, 5.0]], requires_grad=True)
    b = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    c = torch.matmul(a, b)
    loss = c.sum()
    loss.backward()

    print("\n[✓] Autograd Gradient Test : Successful")
    print(f"    Gradients d(loss)/da   :\n{a.grad}")
    print("\nEnvironment is 100% ready for class!")
    print("=" * 60)

if __name__ == "__main__":
    main()
