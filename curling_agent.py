"""
Curling Chatbot Agent with Internet Search Capabilities
Uses Ollama (free local LLM) and DuckDuckGo (free search)
"""

import os
from typing import List, Dict, Any
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_community.llms import Ollama
from langchain import hub
from langchain.memory import ConversationBufferMemory
from duckduckgo_search import DDGS


class CurlingChatbot:
    """A chatbot specialized in answering questions about Olympic curling."""
    
    def __init__(self, model_name: str = "llama3.2", temperature: float = 0.7):
        """
        Initialize the Curling Chatbot.
        
        Args:
            model_name: Ollama model to use (default: llama3.2)
            temperature: LLM temperature for response generation
        """
        self.model_name = model_name
        self.temperature = temperature
        self.llm = None
        self.agent_executor = None
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Initialize the chatbot
        self._initialize_llm()
        self._initialize_agent()
    
    def _initialize_llm(self):
        """Initialize the Ollama LLM."""
        try:
            self.llm = Ollama(
                model=self.model_name,
                temperature=self.temperature,
                base_url="http://localhost:11434"
            )
            print(f"✓ Initialized Ollama with model: {self.model_name}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to initialize Ollama. Make sure Ollama is running.\n"
                f"Error: {str(e)}\n"
                f"Install: https://ollama.ai/download\n"
                f"Then run: ollama pull {self.model_name}"
            )
    
    def _search_web(self, query: str, max_results: int = 5) -> str:
        """
        Search the web using DuckDuckGo.
        
        Args:
            query: Search query
            max_results: Maximum number of results to return
            
        Returns:
            Formatted search results as a string
        """
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=max_results))
            
            if not results:
                return "No search results found."
            
            # Format results
            formatted_results = []
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                body = result.get('body', 'No description')
                link = result.get('href', 'No link')
                
                formatted_results.append(
                    f"{i}. **{title}**\n"
                    f"   {body}\n"
                    f"   Source: {link}\n"
                )
            
            return "\n".join(formatted_results)
            
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def _initialize_agent(self):
        """Initialize the LangChain agent with tools."""
        
        # Define tools
        tools = [
            Tool(
                name="WebSearch",
                func=self._search_web,
                description=(
                    "Search the internet for current information about curling. "
                    "Use this ONLY for recent events, competitions, or facts you don't know. "
                    "Input should be a clear search query."
                )
            )
        ]
        
        # Store tools for later use
        self.tools = tools
        
        # Use the standard ReAct prompt from LangChain hub with custom instructions
        try:
            prompt = hub.pull("hwchase17/react")
        except:
            # Fallback: create a basic ReAct prompt if hub is unavailable
            from langchain.prompts import PromptTemplate
            
            template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
            
            prompt = PromptTemplate.from_template(template)
        
        # Create agent
        agent = create_react_agent(
            llm=self.llm,
            tools=tools,
            prompt=prompt
        )
        
        # Create agent executor with better configuration
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3,  # Reduced to prevent loops
            early_stopping_method="generate",  # Stop early if possible
            return_intermediate_steps=False  # Cleaner output
        )
        
        print("✓ Agent initialized with web search capabilities")
    
    def chat(self, user_input: str) -> str:
        """
        Process user input and generate a response.
        
        Args:
            user_input: User's question or message
            
        Returns:
            Chatbot's response
        """
        try:
            response = self.agent_executor.invoke({"input": user_input})
            return response.get("output", "I couldn't generate a response.")
        except Exception as e:
            return f"Error processing your question: {str(e)}"
    
    def reset_conversation(self):
        """Clear conversation history."""
        self.memory.clear()
        print("✓ Conversation history cleared")


def main():
    """Simple CLI interface for testing."""
    print("=" * 60)
    print("🥌 Curling Chatbot - CLI Mode")
    print("=" * 60)
    print("\nInitializing chatbot...")
    
    try:
        chatbot = CurlingChatbot()
        print("\n✓ Chatbot ready! Ask me anything about curling.")
        print("Commands: 'quit' to exit, 'reset' to clear history\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThanks for chatting about curling! 🥌")
                break
            
            if user_input.lower() == 'reset':
                chatbot.reset_conversation()
                continue
            
            print("\nChatbot: ", end="", flush=True)
            response = chatbot.chat(user_input)
            print(response)
            print()
            
    except KeyboardInterrupt:
        print("\n\nGoodbye! 🥌")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure Ollama is installed and running:")
        print("1. Install from: https://ollama.ai/download")
        print("2. Run: ollama pull llama3.2")
        print("3. Ollama should be running on http://localhost:11434")


if __name__ == "__main__":
    main()

# Made with Bob
