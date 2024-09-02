import yaml
import os
from dotenv import load_dotenv

class ConfigManager:
    _config = None

    @classmethod
    def get_config(cls):
        load_dotenv()
        if cls._config is None:
            cls._load_config()
        return cls._config

    @classmethod
    def _load_config(cls):
        with open('config/config.yaml', 'r') as file:
            cls._config = yaml.safe_load(file)
        cls._resolve_variables()

    @classmethod
    def _resolve_variables(cls):
        for key, value in cls._config.items():
            if isinstance(value, str):
               #Resolve .env variables
               if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                   env_var = value[2:-1]  # Extract the variable name
                   cls._config[key] = os.getenv(env_var)  # Get the environment variable value
               else:
                   #Resolve any nested YAML variables
                   cls._config[key] = value.format(**cls._config)   
                
               #Then, expand OS environment variables
               cls._config[key] = os.path.expandvars(cls._config[key])

#Usage 
config = ConfigManager.get_config()

# To run the config manager
if __name__ == "__main__":
    config = ConfigManager.get_config()
    print(config)

