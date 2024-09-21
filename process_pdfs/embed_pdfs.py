import sys
import os 
#Initialize the environment including the .env file
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config_manager import config

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_redis import RedisVectorStore
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor

def process_pdf(filename):  # Define a new function to process each PDF
    loader = PyPDFLoader(os.path.join(config["pdf_file_path"], filename))
    pages = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200, add_start_index=True)
    chunks = text_splitter.split_documents(pages)

    embedding = OpenAIEmbeddings()  
    embedding.embed_documents([chunk.page_content for chunk in chunks])
    index_name = filename.replace('.pdf', '')  # Use the file name as the index name

    # Initialize Redis vector store
    vector_store = RedisVectorStore.from_documents(chunks, embedding, index_name=index_name)
    print(index_name, "added ", vector_store)

with ThreadPoolExecutor() as executor:  # Use ThreadPoolExecutor for parallel processing
    executor.map(process_pdf, [filename for filename in os.listdir(config["pdf_file_path"]) if filename.endswith(".pdf")])

    # Wait for all threads to complete
    executor.shutdown(wait=True)

    print("All PDF files have been processed and indexed.")
