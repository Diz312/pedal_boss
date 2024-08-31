import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    

from langchain_community.llms import CTransformers
from config.config_manager import config

def load_local_model(model_type: str, model_path: str, n_gpu_layers: int) -> CTransformers:
    """
    Load a local model using LangChain based on the provided parameters.

    Args:
        model_type (str): The type of the model (e.g., 'llama', 'mistral').
        model_path (str): The path to the local model file.
        n_gpu_layers (int): The number of GPU layers to use.

    Returns:
        CTransformers: An instance of the loaded model.
    """
    try:
        model = CTransformers(
            model=model_path,
            model_type=model_type,
            config={
                'gpu_layers': n_gpu_layers,
                'context_length': 2048,
            }
        )
        return model
    except Exception as e:
        print(f"Error loading the model: {e}")
        raise

class Mistral:
    def __init__(self, model_path: str, n_gpu_layers: int):
        self.model_path = model_path
        self.n_gpu_layers = n_gpu_layers

    def create_instance(self) -> CTransformers:
        return load_local_model('mistral', self.model_path, self.n_gpu_layers)
    
if __name__ == "__main__":
    mistral = Mistral(model_path=config['latest_mistral_model'], n_gpu_layers=int(config['n_gpu_layers']))
    model = mistral.create_instance()
    print(model)    