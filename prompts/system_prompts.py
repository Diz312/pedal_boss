# Configuration setup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import ConfigManager
config = ConfigManager.get_config()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub

model = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=config["openai_api_key"])
prompt_template = hub.pull("ohkgi/superb_system_instruction_prompt")

chain = prompt_template | model 

# Get the response from the chain
response = chain.invoke({"goal": config["write_resume"]})

# Print the response in a readable format
print("Response from the AI model:")
print("-" * 50)
print(response.content.strip())
print("-" * 50)


 
