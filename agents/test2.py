# Configuration setup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import ConfigManager
config = ConfigManager.get_config()

# Tavily Search
from langchain_community.tools.tavily_search import TavilySearchResults

# OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

# Define a simple tool
search = TavilySearchResults(max_results=2, tavily_api_key=config["tavily_api_key"])
# search_results = search.invoke("what is the weather in SF")
# print(search_results)

# Add the tool to the list
tools = [search]

# Define the LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,api_key=config["openai_api_key"])
llm = ChatOllama(model="mistral-nemo:latest", temperature=0)

# # Invoke the LLM
# response = llm.invoke([HumanMessage(content="What is the weather in SF?")])
# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")

# # Invoke the LLM with tools
# # Bind the tool to the LLM
# llm_with_tools = llm.bind_tools(tools)
# response_with_tools = llm_with_tools.invoke([HumanMessage(content="What is the weather in SF?")])
# print(f"ContentString: {response_with_tools.content}")
# print(f"ToolCalls: {response_with_tools.tool_calls}")

agent_executor = create_react_agent(llm, tools)
response = agent_executor.invoke({"messages":[HumanMessage(content="Hello")]})

print(response)

