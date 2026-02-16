# 🥌 Curling Chatbot - Free MVP

A fully functional chatbot that answers questions about Olympic curling with internet search capabilities. **100% free** - no API costs, no subscriptions!

## ✨ Features

- 🤖 **Local LLM** - Uses Ollama (runs on your machine)
- 🔍 **Web Search** - DuckDuckGo integration for current information
- 💬 **Conversational** - Maintains chat history
- 🎨 **Beautiful UI** - Streamlit web interface
- 🔒 **Private** - All processing happens locally
- 💰 **Free** - Zero ongoing costs

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+**
   ```bash
   python --version
   ```

2. **Ollama** - Download and install from [ollama.ai](https://ollama.ai/download)
   
   **macOS:**
   ```bash
   brew install ollama
   ```
   
   **Linux:**
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```
   
   **Windows:**
   Download installer from [ollama.ai/download](https://ollama.ai/download)

### Installation

1. **Clone or download this project**
   ```bash
   cd curling-chatbot
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate it:
   # macOS/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download an Ollama model**
   ```bash
   # Recommended: Llama 3.2 (2GB)
   ollama pull llama3.2
   
   # Alternatives:
   # ollama pull mistral      # 4GB
   # ollama pull phi3         # 2GB
   # ollama pull gemma2       # 5GB
   ```

5. **Verify Ollama is running**
   ```bash
   ollama list
   ```
   
   You should see your downloaded model(s) listed.

### Running the Chatbot

#### Option 1: Web UI (Recommended)

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

#### Option 2: Command Line

```bash
python curling_agent.py
```

Simple CLI interface for testing.

## 📖 Usage Guide

### Web Interface

1. **Initialize the chatbot** using the sidebar
2. **Select your model** (llama3.2 recommended)
3. **Adjust temperature** (0.7 is good default)
4. **Start chatting!**

### Example Questions

- "What are the basic rules of curling?"
- "Who won gold in curling at the 2022 Olympics?"
- "Explain the strategy behind curling"
- "What is a 'hammer' in curling?"
- "Tell me about the history of Olympic curling"
- "What are the different types of curling shots?"

### Features

- **Web Search**: The bot automatically searches the internet when needed
- **Conversation Memory**: Maintains context throughout the chat
- **Source Citations**: Shows where information comes from
- **Clear History**: Reset conversation anytime

## 🛠️ Troubleshooting

### "Failed to initialize Ollama"

**Solution:**
1. Make sure Ollama is installed
2. Check if Ollama is running: `ollama list`
3. Try pulling the model again: `ollama pull llama3.2`
4. Restart Ollama service

### "Model not found"

**Solution:**
```bash
# Download the model
ollama pull llama3.2

# Verify it's available
ollama list
```

### "Connection refused to localhost:11434"

**Solution:**
- Ollama service isn't running
- On macOS/Linux: Ollama should start automatically
- On Windows: Check if Ollama is running in system tray
- Try restarting your computer

### Slow responses

**Solutions:**
- Use a smaller model (phi3 or llama3.2)
- Reduce temperature
- Close other applications
- Ensure you have enough RAM (8GB+ recommended)

### Import errors

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📁 Project Structure

```
curling-chatbot/
├── app.py                 # Streamlit web interface
├── curling_agent.py       # Core chatbot logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── PROJECT_PLAN.md       # Detailed project planning
└── .gitignore            # Git ignore rules
```

## 🔧 Configuration

### Change Model

Edit in the UI sidebar or modify `curling_agent.py`:

```python
chatbot = CurlingChatbot(
    model_name="mistral",  # Change this
    temperature=0.7
)
```

### Adjust Search Results

In `curling_agent.py`, modify the `_search_web` method:

```python
def _search_web(self, query: str, max_results: int = 5):  # Change max_results
```

### Customize Prompts

Edit the prompt template in `curling_agent.py` to change the bot's personality or focus.

## 🚀 Next Steps

### Enhancements You Can Add

1. **Knowledge Base**: Add a vector database with curling facts
2. **Image Support**: Show curling diagrams and photos
3. **Video Links**: Embed YouTube tutorials
4. **Multi-language**: Support other languages
5. **Voice Input**: Add speech-to-text
6. **Export Chat**: Save conversations

### Upgrade to Paid Services (Optional)

If you need better performance:
- **OpenAI GPT-4**: Better reasoning (~$0.01/query)
- **Tavily AI**: Better search results ($5/month)
- **Cloud Hosting**: Deploy to Hugging Face Spaces (free tier available)

See [`PROJECT_PLAN.md`](PROJECT_PLAN.md) for detailed upgrade paths.

## 💡 Tips

1. **First query is slow**: The model needs to load (30-60 seconds)
2. **Subsequent queries are fast**: Model stays in memory
3. **Use specific questions**: Better results than vague queries
4. **Check sources**: Bot cites where information comes from
5. **Reset if confused**: Clear conversation history to start fresh

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit improvements
- Share your experience

## 📝 License

This project is open source and available for personal and educational use.

## 🆘 Support

If you encounter issues:

1. Check this README's troubleshooting section
2. Verify Ollama is running: `ollama list`
3. Check Python version: `python --version` (need 3.10+)
4. Reinstall dependencies: `pip install -r requirements.txt`

## 🎯 Project Goals

This MVP demonstrates:
- ✅ Free LLM integration (Ollama)
- ✅ Free web search (DuckDuckGo)
- ✅ Agent-based architecture (LangChain)
- ✅ User-friendly interface (Streamlit)
- ✅ Conversation memory
- ✅ Source citations

**Total Cost: $0/month** 🎉

---

Made with ❤️ for curling enthusiasts and AI learners!