"""
Streamlit UI for Curling Chatbot
A user-friendly web interface for the curling chatbot
"""

import streamlit as st
from curling_agent import CurlingChatbot
import time


# Page configuration
st.set_page_config(
    page_title="🥌 Curling Chatbot",
    page_icon="🥌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False


def initialize_chatbot(model_name: str, temperature: float):
    """Initialize the chatbot with given parameters."""
    try:
        with st.spinner("🔄 Initializing chatbot... This may take a moment."):
            chatbot = CurlingChatbot(
                model_name=model_name,
                temperature=temperature
            )
        st.session_state.chatbot = chatbot
        st.session_state.initialized = True
        st.success("✅ Chatbot initialized successfully!")
        return True
    except Exception as e:
        st.error(f"❌ Failed to initialize chatbot: {str(e)}")
        st.info("""
        **Troubleshooting:**
        1. Make sure Ollama is installed: https://ollama.ai/download
        2. Run: `ollama pull llama3.2` (or your chosen model)
        3. Ensure Ollama is running (it should start automatically)
        4. Check if Ollama is accessible at http://localhost:11434
        """)
        return False


def display_message(role: str, content: str):
    """Display a chat message."""
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <div class="message-header">🧑 You</div>
            <div>{content}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <div class="message-header">🥌 Curling Bot</div>
            <div>{content}</div>
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main application function."""
    initialize_session_state()
    
    # Header
    st.title("🥌 Curling Chatbot")
    st.markdown("*Your AI assistant for all things Olympic curling!*")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Model selection
        model_name = st.selectbox(
            "Select Ollama Model",
            ["llama3.2", "llama3.1", "mistral", "phi3", "gemma2"],
            help="Choose the LLM model. Make sure it's downloaded in Ollama."
        )
        
        # Temperature slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher values make responses more creative, lower values more focused."
        )
        
        # Initialize button
        if not st.session_state.initialized:
            if st.button("🚀 Initialize Chatbot", type="primary", use_container_width=True):
                initialize_chatbot(model_name, temperature)
        else:
            st.success("✅ Chatbot is ready!")
            if st.button("🔄 Restart Chatbot", use_container_width=True):
                st.session_state.chatbot = None
                st.session_state.initialized = False
                st.rerun()
        
        st.markdown("---")
        
        # Clear conversation button
        if st.session_state.initialized and st.session_state.messages:
            if st.button("🗑️ Clear Conversation", use_container_width=True):
                st.session_state.messages = []
                if st.session_state.chatbot:
                    st.session_state.chatbot.reset_conversation()
                st.rerun()
        
        st.markdown("---")
        
        # Information
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot uses:
        - **Ollama** (local LLM)
        - **DuckDuckGo** (web search)
        - **LangChain** (orchestration)
        
        **100% Free & Private!**
        
        All processing happens locally on your machine.
        """)
        
        st.markdown("---")
        
        # Example questions
        st.header("💡 Example Questions")
        example_questions = [
            "What are the basic rules of curling?",
            "Who won the gold medal in curling at the 2022 Olympics?",
            "Explain the strategy behind curling",
            "What is a 'hammer' in curling?",
            "Tell me about famous curling teams"
        ]
        
        for question in example_questions:
            if st.button(question, key=f"example_{question}", use_container_width=True):
                if st.session_state.initialized:
                    st.session_state.messages.append({"role": "user", "content": question})
                    st.rerun()
    
    # Main chat area
    if not st.session_state.initialized:
        st.info("👈 Please initialize the chatbot using the sidebar to get started!")
        
        # Show setup instructions
        with st.expander("📋 Setup Instructions", expanded=True):
            st.markdown("""
            ### Prerequisites
            
            1. **Install Ollama**
               ```bash
               # Visit https://ollama.ai/download
               # Or use package manager:
               # macOS: brew install ollama
               # Linux: curl -fsSL https://ollama.ai/install.sh | sh
               ```
            
            2. **Download a Model**
               ```bash
               ollama pull llama3.2
               ```
            
            3. **Verify Ollama is Running**
               ```bash
               ollama list
               ```
            
            4. **Install Python Dependencies**
               ```bash
               pip install -r requirements.txt
               ```
            
            5. **Run the App**
               ```bash
               streamlit run app.py
               ```
            """)
    else:
        # Display chat history
        for message in st.session_state.messages:
            display_message(message["role"], message["content"])
        
        # Chat input
        user_input = st.chat_input("Ask me anything about curling...")
        
        if user_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            display_message("user", user_input)
            
            # Get bot response
            with st.spinner("🤔 Thinking..."):
                try:
                    response = st.session_state.chatbot.chat(user_input)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    display_message("assistant", response)
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            st.rerun()


if __name__ == "__main__":
    main()

# Made with Bob
