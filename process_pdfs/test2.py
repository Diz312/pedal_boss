# Configuration setup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import ConfigManager
config = ConfigManager.get_config()

# OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, trim_messages
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory 
from langchain_core.runnables import RunnableWithMessageHistory, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from operator import itemgetter

model = ChatOllama(model="mistral-nemo:latest", temperature=0)

session_store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

with_message_history = RunnableWithMessageHistory(model, get_session_history)   
config={"configurable": {"session_id": "sesh1"}}
config2={"configurable": {"session_id": "sesh2"}}

trimmer = trim_messages(
    max_tokens=65,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert agent in sports medicine and health and your job is to provide answers specific to this topic.'"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# chain = RunnablePassthrough.assign(messages=itemgetter("messages")|trimmer) | prompt | model 

chain = prompt | model
with_message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="messages")

# Chat loop
print("Welcome to the Sports Medicine Chat! Type 'exit' to end the conversation.")
session_id = "user_session"
config = {"configurable": {"session_id": session_id}}

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        print("\nChat History:")
        for message in session_store[session_id].messages:
            print(f"{message.type}: {message.content}")
        break
    
    response = with_message_history.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config=config
    )
    
    print(f"AI: {response.content}")
    
    # Print the full context window that went into the model and total token count
    print("\nFull Context Window:")
    for message in session_store[session_id].messages:
        print(f"{message.type.capitalize()}: {message.content}")
    print()  # Add an extra line for readability
    
        
   