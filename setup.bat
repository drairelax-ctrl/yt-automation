@echo off
setlocal
cd /d "%~dp0"
call "..\shared-tools\env.bat"
if not exist ".venv\Scripts\python.exe" "..\shared-tools\python\cpython-3.12.14-windows-x86_64-none\python.exe" -m venv .venv
if errorlevel 1 exit /b %errorlevel%
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
if errorlevel 1 exit /b %errorlevel%
".venv\Scripts\python.exe" windows_models.py
