#!/usr/bin/env python3
try:
    import pandas as pd
    pandas_ok = True
except ImportError:
    pandas_ok = False

try:
    import numpy as np
    numpy_ok = True
except ImportError:
    numpy_ok = False

try:
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib_ok = True
except ImportError:
    matplotlib_ok = False

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")
print("\nDependency Management Comparison:")
print("pip:    pip install -r requirements.txt")
print("Poetry: poetry install")
print("pip uses version ranges from requirements.txt")
print("Poetry locks exact versions in poetry.lock\n")

if pandas_ok:
    print(f"[OK] pandas {pd.__version__} - Data manipulation ready")
else:
    print("[MISSING] pandas - install with: pip install pandas")

if numpy_ok:
    print(f"[OK] numpy {np.__version__} - Numerical computation ready")
else:
    print("[MISSING] numpy - install with: pip install numpy")

if matplotlib_ok:
    print(f"[OK] matplotlib {matplotlib.__version__} - Visualization ready")
else:
    print("[MISSING] matplotlib - install with: pip install matplotlib")

if not (pandas_ok and numpy_ok and matplotlib_ok):
    print("Install missing packages and try again.")
else:
    print("Analyzing Matrix data...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["matrix_signal"])
    print("Processing 1000 data points...")
    print("Generating visualization...")
    df["matrix_signal"].plot(title="Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
