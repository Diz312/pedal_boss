
import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config_manager import config
from agents.load_agent import Mistral                             

if __name__ == "__main__":
    model_instance = Mistral(model_path=config['latest_mistral_model'],n_gpu_layers=10).create_instance()
    print(model_instance)


