@echo off
cls
echo Checking for Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed.
    echo Please install Python from https://www.python.org/downloads/ and ensure it's added to PATH.
    pause
    exit /b
)

echo Python is installed.
echo Updating pip...
python -m ensurepip --upgrade
python -m pip install --upgrade pip

echo Installing Eel...
pip install eel

echo Downloading application files from GitHub...
powershell -command "Invoke-WebRequest -Uri 'https://github.com/LucasSMPL/reporter/archive/refs/heads/main.zip' -OutFile '%USERPROFILE%\Desktop\reporter.zip'"
powershell -command "Expand-Archive -Path '%USERPROFILE%\Desktop\reporter.zip' -DestinationPath '%USERPROFILE%\Desktop\'"

echo Application setup is complete.
pause
