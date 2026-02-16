#!/bin/bash
# Quick setup script for Curling Chatbot

set -e  # Exit on error

echo "🥌 Curling Chatbot - Setup Script"
echo "=================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $python_version"

# Check if Ollama is installed
echo ""
echo "📋 Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "✓ Ollama is installed"
    ollama_version=$(ollama --version 2>&1 || echo "unknown")
    echo "  Version: $ollama_version"
else
    echo "❌ Ollama is not installed"
    echo ""
    echo "Please install Ollama first:"
    echo "  macOS:   brew install ollama"
    echo "  Linux:   curl -fsSL https://ollama.ai/install.sh | sh"
    echo "  Windows: Download from https://ollama.ai/download"
    exit 1
fi

# Check if model is downloaded
echo ""
echo "📋 Checking for Ollama models..."
if ollama list | grep -q "llama3.2"; then
    echo "✓ llama3.2 model found"
else
    echo "⚠️  llama3.2 model not found"
    echo ""
    read -p "Would you like to download llama3.2 now? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📥 Downloading llama3.2 (this may take a few minutes)..."
        ollama pull llama3.2
        echo "✓ Model downloaded successfully"
    else
        echo "⚠️  You'll need to download a model manually:"
        echo "   ollama pull llama3.2"
    fi
fi

# Create virtual environment
echo ""
echo "📦 Setting up Python virtual environment..."
if [ -d "venv" ]; then
    echo "✓ Virtual environment already exists"
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing Python dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the chatbot:"
echo ""
echo "   1. Activate the virtual environment:"
echo "      source venv/bin/activate"
echo ""
echo "   2. Run the web interface:"
echo "      streamlit run app.py"
echo ""
echo "   Or run the CLI version:"
echo "      python curling_agent.py"
echo ""
echo "Happy chatting! 🥌"

# Made with Bob
