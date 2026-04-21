import json
from pathlib import Path

def read_config(env: str = None):
    config_path = Path(__file__).parent.parent / "configurations" / "config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
    if env:
        return config.get(env)
    return config
