@echo off

:: Check if a project name and script name were provided as arguments
if "%~1"=="" (
    echo Usage: %~nx0 projectName scriptName.py
    exit /b 1
)

:: Store the project name and script name
set PROJECT_NAME=%~1
set SCRIPT_NAME=%~2

:: Step 1: Create a virtual environment with the given project name
python -m venv %PROJECT_NAME%

:: Step 2: Change to the project directory
cd %PROJECT_NAME%

:: Step 3: Activate the virtual environment
call Scripts\activate

:: Step 4: Move the necessary files to the project directory
move ..\installmod.bat .
move ..\getreqs.py .
move ..\libfinder.py .

:: Step 5: Run the installmod.bat script with the given script name
call installmod.bat %SCRIPT_NAME%

python3 -m PyInstaller --onefile %SCRIPT_NAME%
echo Script completed successfully.
