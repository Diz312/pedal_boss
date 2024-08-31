import yaml
import os

class ConfigManager:
    _config = None

    @classmethod
    def get_config(cls):
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
                # First, apply string formatting
                cls._config[key] = value.format(**cls._config)
                # Then, expand environment variables
                cls._config[key] = os.path.expandvars(cls._config[key])

#Usage 
config = ConfigManager.get_config()

# To run the config manager
if __name__ == "__main__":
    config = ConfigManager.get_config()
    print(config)

