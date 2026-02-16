@echo off
REM Quick setup script for Curling Chatbot (Windows)

echo 🥌 Curling Chatbot - Setup Script
echo ==================================
echo.

REM Check Python version
echo 📋 Checking Python version...
python --version
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.10+ from python.org
    pause
    exit /b 1
)
echo ✓ Python found
echo.

REM Check if Ollama is installed
echo 📋 Checking Ollama installation...
where ollama >nul 2>&1
if errorlevel 1 (
    echo ❌ Ollama is not installed
    echo.
    echo Please install Ollama first:
    echo   Download from: https://ollama.ai/download
    pause
    exit /b 1
)
echo ✓ Ollama is installed
echo.

REM Check if model is downloaded
echo 📋 Checking for Ollama models...
ollama list | findstr "llama3.2" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  llama3.2 model not found
    echo.
    set /p download="Would you like to download llama3.2 now? (y/n): "
    if /i "%download%"=="y" (
        echo 📥 Downloading llama3.2 (this may take a few minutes)...
        ollama pull llama3.2
        echo ✓ Model downloaded successfully
    ) else (
        echo ⚠️  You'll need to download a model manually:
        echo    ollama pull llama3.2
    )
) else (
    echo ✓ llama3.2 model found
)
echo.

REM Create virtual environment
echo 📦 Setting up Python virtual environment...
if exist venv (
    echo ✓ Virtual environment already exists
) else (
    python -m venv venv
    echo ✓ Virtual environment created
)
echo.

REM Activate virtual environment and install dependencies
echo 🔄 Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo 🚀 To start the chatbot:
echo.
echo    1. Activate the virtual environment:
echo       venv\Scripts\activate
echo.
echo    2. Run the web interface:
echo       streamlit run app.py
echo.
echo    Or run the CLI version:
echo       python curling_agent.py
echo.
echo Happy chatting! 🥌
echo.
pause

@REM Made with Bob
