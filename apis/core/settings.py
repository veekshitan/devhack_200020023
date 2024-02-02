import os
import yaml
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "../../"))

_cached_config_data = None
def load_config():
    global _cached_config_data
    if _cached_config_data is not None:
        return _cached_config_data

    config_path = f"../config/config.yaml"
    config_file_path = os.path.join(current_directory, config_path)
    with open(config_file_path, "r") as f:
        config_data = yaml.safe_load(f)

    _cached_config_data = config_data
    return config_data

CONFIG = load_config()
HOST = CONFIG.get("host", "0.0.0.0")
PORT = CONFIG.get("port", "8000")
POSTGRES_USER=CONFIG.get("postgres_user", "postgres")
POSTGRES_PASSWORD=CONFIG.get("postgres_password", "root")
POSTGRES_HOST=CONFIG.get("postgres_host", "localhost")
POSTGRES_PORT= CONFIG.get("postgres_port", "5432")
POSTGRES_DBNAME= CONFIG.get("postgres_dbname", "postgresdb")
