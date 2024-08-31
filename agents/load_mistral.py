import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    

from langchain_community.llms import CTransformers
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

    def create_instance(self) -> CTransformers:
        """
        Creates and returns a local Llama instance using CTransformers.

        Returns:
            CTransformers: An instance of the local Llama model.
        """
        return CTransformers(
            model=self.model_path,
            model_type="mistral",
            config={
                'max_new_tokens': 1024,
                'temperature': self.temperature,
                'gpu_layers': self.n_gpu_layers,
            }
        )

if __name__ == "__main__":
    model = Mistral(model_path=config['latest_mistral_model'])
    llama_instance = model.create_instance()
    print(llama_instance)