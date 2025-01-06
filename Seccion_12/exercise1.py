import pandas as pd
import os

path = "../supermarkets/supermarkets.json"


if os.path.exists(path):
    data = pd.read_json(path)
    print(data)
