# Configuration setup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import ConfigManager
config = ConfigManager.get_config()

# OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain import hub


model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
# model = ChatOllama(model="mistral-nemo:latest", temperature=0)

prompt = hub.pull("ohkgi/superb_system_instruction_prompt")

chain = prompt | model | StrOutputParser()

print(chain.invoke({"goal": "read a pdf file, extract list of electrical components listed in the pdf by carefully identifying the components based on ISO standard used to specify the component type and unit of measure. Then, generate a table output including the component types, values, ISO standard unit of measure and total quantity"}))


