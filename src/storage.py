import json
import os

def save_to_json(data, filename="output/data/dataBarang.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "W") as f:
        json.dump(data, f, indent=4)
        