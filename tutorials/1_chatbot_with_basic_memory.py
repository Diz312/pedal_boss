# This is a simple chatbot that uses LangGraph to create a chatbot with basic memory

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

model_config = {
    "model": "mistral-nemo:latest"
}

model = ChatOllama(**model_config)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    MessagesPlaceholder(variable_name="messages"),
])

def call_model (state: MessagesState):
    chain = prompt | model
    response = chain.invoke(state)
    return {"messages": response}

graph = StateGraph(state_schema=MessagesState)
graph.add_node("model", call_model)
graph.add_edge(START, "model")

memory = MemorySaver()
app=graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "123"}}

while True:
    user_input = input("You: ")
    if user_input.lower() == "/exit":
        print("Exiting the chatbot. Goodbye!")
        break
    response = app.invoke({"messages": [HumanMessage(content=user_input)]}, config=config)
    for message in response["messages"]:
        message.pretty_print()
