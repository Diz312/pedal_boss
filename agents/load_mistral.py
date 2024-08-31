import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    

from langchain_community.llms import LlamaCpp
from config.config_manager import config

class Mistral:
    def __init__(
        self,
        model_path: str,
        n_gpu_layers: int = 1,
        n_batch: int = 512,
        n_ctx: int = 2048,
        temperature: float = 0, 
        verbose: bool = False
    ):
        self.model_path = model_path
        self.n_gpu_layers = n_gpu_layers
        self.n_batch = n_batch
        self.n_ctx = n_ctx
        self.verbose = verbose
        self.temperature = temperature

    def create_instance(self) -> LlamaCpp:
        """
        Creates and returns a local Llama instance using LlamaCpp.

        Returns:
            LlamaCpp: An instance of the local Llama model.
        """
        llm = LlamaCpp(
            model_path=self.model_path,
            n_gpu_layers=self.n_gpu_layers,
            n_batch=self.n_batch,
            n_ctx=self.n_ctx,
            verbose=self.verbose,
            temperature=self.temperature
        )
        
        return llm

if __name__ == "__main__":
    model = Mistral(model_path=config['latest_mistral_model'])
    llama_instance = model.create_instance()
    print(llama_instance)