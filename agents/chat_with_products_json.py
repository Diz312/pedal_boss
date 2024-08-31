
import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config_manager import config
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def create_local_llama_instance(
    model_path: str,
    n_gpu_layers: int = 1,
    n_batch: int = 512,
    n_ctx: int = 2048,
    verbose: bool = False
) -> LlamaCpp:
    """
    Creates and returns a local Llama instance using LlamaCpp.

    Args:
        model_path (str): Path to the Llama model file.
        n_gpu_layers (int): Number of GPU layers to use.
        n_batch (int): Number of batches.
        n_ctx (int): Context window size.
        verbose (bool): Whether to enable verbose output.

    Returns:
        LlamaCpp: An instance of the local Llama model.
    """
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    llm = LlamaCpp(
        model_path=model_path,
        n_gpu_layers=n_gpu_layers,
        n_batch=n_batch,
        n_ctx=n_ctx,
        callback_manager=callback_manager,
        verbose=verbose,
    )
    
    return llm

if __name__ == "__main__":
       
    llama_instance = create_local_llama_instance(config['latest_mistral_model'])
    print(llama_instance)


