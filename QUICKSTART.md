# 🚀 Quick Start Guide - Curling Chatbot

Get your curling chatbot running in **5 minutes**!

## Step 1: Install Ollama

### macOS
```bash
brew install ollama
```

### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Windows
Download from: https://ollama.ai/download

## Step 2: Download AI Model

```bash
# Download Llama 3.2 (recommended, ~2GB)
ollama pull llama3.2

# Verify it's installed
ollama list
```

## Step 3: Install Python Dependencies

```bash
# Navigate to project directory
cd curling-chatbot

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## Step 4: Run the Chatbot

### Web Interface (Recommended)
```bash
streamlit run app.py
```

Opens at: http://localhost:8501

### Command Line
```bash
python curling_agent.py
```

## Step 5: Start Chatting!

Try these questions:
- "What are the basic rules of curling?"
- "Who won gold in curling at the 2022 Olympics?"
- "Explain curling strategy"

## ✅ Verification Checklist

- [ ] Ollama installed and running
- [ ] Model downloaded (`ollama list` shows llama3.2)
- [ ] Python 3.10+ installed
- [ ] Dependencies installed (`pip list` shows langchain, streamlit, etc.)
- [ ] App launches without errors

## 🆘 Common Issues

### "Ollama not found"
```bash
# Check if Ollama is installed
which ollama  # macOS/Linux
where ollama  # Windows

# If not found, reinstall from ollama.ai
```

### "Model not found"
```bash
# Download the model
ollama pull llama3.2

# Check available models
ollama list
```

### "Import errors"
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### "Port already in use"
```bash
# Use different port
streamlit run app.py --server.port 8502
```

## 🎯 Next Steps

1. ✅ Got it working? Great!
2. 📖 Read the full [README.md](README.md) for advanced features
3. 🔧 Customize the bot in `curling_agent.py`
4. 🎨 Modify the UI in `app.py`
5. 📊 Check [PROJECT_PLAN.md](PROJECT_PLAN.md) for upgrade options

## 💡 Pro Tips

- **First query is slow** (30-60s) - model is loading
- **Subsequent queries are fast** - model stays in memory
- **Use specific questions** for better answers
- **Check sources** - bot shows where info comes from
- **Reset conversation** if bot gets confused

## 🎉 You're Ready!

Your free, private, local curling chatbot is now running!

**Cost: $0/month** | **Privacy: 100% local** | **Limits: None**

---

Need help? Check [README.md](README.md) troubleshooting section.