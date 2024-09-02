import sys
import os 
from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import config

# llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0,api_key=config['open_api_key'])

print (config['openai_api_key'])

# class Joke(BaseModel):
#     setup: str= Field(description="The setup to the joke")
#     punchline: str = Field(description="The punchline to the joke")
#     rating: Optional[int] = Field(default=None, description="The rating of the joke from 1 to 10")

# structured_llm = llm.with_structured_output(Joke)
# structured_llm.invoke("Tell me a joke about LLMs")
