# ------------------------------------------------------------------
# Cross-Platform Environment Verification Script (macOS & Windows)
# ------------------------------------------------------------------
# Checks your Python version, OS platform, and verifies whether core
# Machine Learning and Data Science libraries are installed.

import platform

os_name = "macOS" if platform.system() == "Darwin" else platform.system()
pip_cmd = "python -m pip install" if platform.system() == "Windows" else "pip3 install"

print("Python Environment Verification:")
print(f"Python Version : {platform.python_version()}")
print(f"Platform       : {os_name} ({platform.machine()})")
print("\nChecking Core Data Science & ML Packages:")

packages = [
    ("numpy", "NumPy (Numerical computing)"),
    ("pandas", "Pandas (Data manipulation)"),
    ("matplotlib", "Matplotlib (Plotting)"),
    ("seaborn", "Seaborn (Statistical plotting)"),
    ("sklearn", "Scikit-Learn (Machine learning)"),
]

for mod_name, label in packages:
    try:
        mod = __import__(mod_name)
        version = getattr(mod, "__version__", "installed")
        print(f"[OK]      {label:<32} (v{version})")
    except ImportError:
        print(f"[MISSING] {label:<32} -> {pip_cmd} {mod_name}")

# --- Run Command ---
# macOS / Linux: python3 00-setup/verify_setup.py
# Windows:       python 00-setup/verify_setup.py

# --- Output ---
# Python Environment Verification:
# Python Version : 3.13.13
# Platform       : macOS (arm64)
# 
# Checking Core Data Science & ML Packages:
# [MISSING] NumPy (Numerical computing)      -> pip3 install numpy
# [MISSING] Pandas (Data manipulation)       -> pip3 install pandas
# [MISSING] Matplotlib (Plotting)            -> pip3 install matplotlib
# [MISSING] Seaborn (Statistical plotting)   -> pip3 install seaborn
# [MISSING] Scikit-Learn (Machine learning)  -> pip3 install sklearn
