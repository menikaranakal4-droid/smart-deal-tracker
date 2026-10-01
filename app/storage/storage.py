import json
from pathlib import Path
DATA_FILE=Path("data/products.json")
def load_products():
    with open(DATA_FILE,"r") as file:
        return json.load(file)

def save_products(products):
    with open(DATA_FILE,"w") as file:
        json.dump(products,file,indent=4)