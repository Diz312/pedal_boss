import sys
import os 
#Initialize the environment including the .env file
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import config

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain import hub
from langgraph.prebuilt import create_react_agent
from langchain_core.agents import AgentExecutor
from langchain_core.tools import Tool


prompt = """You wil be givne a sitemap URL. Extract only the URLs that contain the {sitemap_url}.
            For each of the extracted URLs perform the following logic:
            - check if the page contains a PDF file with {pdf_build_keyword} in its name
            - if the page does not contain a PDF file, move to the next URL
            - if the page contains the desired PDF file, scrape the content of the page and store the text in {scraped_text_dir}
            Your final output should be a list of URLs and an indication of whether a PDF file was found on each page.
            """
prompt_template = PromptTemplate (template=prompt, input_variables=['sitemap_url', 'pdf_build_keyword', 'scraped_text_dir'])     
react_prompt = hub.pull("hwchase17/react")

# Tools for the agent
tools = [
    Tool(
        name="Scrape URLs",
        description="Useful when you need to check a URL and scrape the content of a URL if it contains the {pdf_build_keyword} in its name",
        function="?"
    )
]

# Initialize the OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0,api_key=config['openai_api_key'])

agent = create_react_agent(llm, prompt_template)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)





