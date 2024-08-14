@echo off

:: Check if a file path was provided as an argument
if "%~1"=="" (
    echo Usage: %~nx0 ^<Scriptname.py^>
    exit /b 1
)

:: Store the provided file path
set PYTHON_FILE_PATH=%~1

:: Run the first Python script
python getreqs.py "%PYTHON_FILE_PATH%"

:: Install the required modules
pip install -r requirements.txt

echo Modules installed successfully.



