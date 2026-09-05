@echo off
setlocal
cd /d "%~dp0"
call "..\shared-tools\env.bat"
".venv\Scripts\python.exe" "..\shared-tools\launch.py" windows_run.py %*
