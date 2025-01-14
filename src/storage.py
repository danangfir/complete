import json
import os

def save_to_json(data, filename="output/data/results.json"):
    if not data:
        print("No data to save.")
        return

    print(f"Saving data to {filename}...")

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully!")
    