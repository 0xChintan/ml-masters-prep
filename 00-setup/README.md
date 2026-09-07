## Environment Setup & Verification

<small>Instructions to configure, activate, and verify the Python environment on both <b>macOS</b> and <b>Windows</b>.</small>

---

### Option 1: Conda (Recommended for both macOS & Windows)

```bash
# 1. Create environment from file
conda env create -f 00-setup/environment.yml

# 2. Activate environment
conda activate ml-prep

# 3. Verify setup
python 00-setup/verify_setup.py
```

---

### Option 2: Python `venv` + `pip`

#### 🍏 For macOS / Linux

```bash
# 1. Create virtual environment
python3 -m venv .venv

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Install packages
pip install -r 00-setup/requirements.txt

# 4. Verify setup
python3 00-setup/verify_setup.py
```

<small>💡 <i>Or simply run the one-click script:</i> <code>./00-setup/setup_mac.sh</code></small>

---

#### 🪟 For Windows (PowerShell / Command Prompt)

```powershell
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
# In PowerShell:
.venv\Scripts\Activate.ps1
# In Command Prompt (cmd):
.venv\Scripts\activate.bat

# 3. Install packages
pip install -r 00-setup\requirements.txt

# 4. Verify setup
python 00-setup\verify_setup.py
```

<small>💡 <i>Or double-click:</i> <code>00-setup\setup_windows.bat</code></small>

<small>⚠️ <b>Windows Note:</b> If PowerShell blocks script activation, run this once:
<code>Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass</code></small>

---

### Files in this Directory

| File | Platform | Description |
| :--- | :--- | :--- |
| [`verify_setup.py`](./verify_setup.py) | macOS & Windows | <small>Cross-platform script that checks Python version and ML libraries</small> |
| [`requirements.txt`](./requirements.txt) | macOS & Windows | <small>Standard pip dependency list</small> |
| [`environment.yml`](./environment.yml) | macOS & Windows | <small>Conda environment file (`ml-prep`, Python 3.11)</small> |
| [`setup_mac.sh`](./setup_mac.sh) | macOS / Linux | <small>One-click bash setup script</small> |
| [`setup_windows.bat`](./setup_windows.bat) | Windows | <small>One-click batch setup script</small> |
