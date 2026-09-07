@echo off
REM Setup script for Windows (Command Prompt / PowerShell)

echo === Setting up Python environment (Windows) ===
python -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r 00-setup\requirements.txt

echo.
echo === Running verification ===
python 00-setup\verify_setup.py
pause

