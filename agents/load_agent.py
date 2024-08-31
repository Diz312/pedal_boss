import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    

from langchain_community.llms import CTransformers
from config.config_manager import config

class Mistral:
    
    def __init__(self):
        self.model_type = 'mistral'
        self.context_length = 2048
        self.max_new_tokens = 512
        self.temperature = 0.7  # Increased from 0.0 to allow some creativity
        self.top_p = 0.95
        self.top_k = 40
        self.repetition_penalty = 1.1
        self.model_path = config['latest_mistral_model']
        self.n_gpu_layers = int(config['n_gpu_layers'])
    def create_instance(self) -> CTransformers:
        try:
            model = CTransformers(
                model=self.model_path,
                model_type=self.model_type,
                config={
                    'gpu_layers': self.n_gpu_layers,
                    'context_length': self.context_length,
                    'max_new_tokens': self.max_new_tokens,
                    'temperature': self.temperature,
                    'top_p': self.top_p,
                    'top_k': self.top_k,
                    'repetition_penalty': self.repetition_penalty
                }
            )
            return model
        except Exception as e:
            print(f"Error creating Mistral instance: {e}")
            raise

# Test the model with user input and print output
if __name__ == "__main__":
    model = Mistral().create_instance()
    print(model)