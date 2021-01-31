import pandas as pd
import json

df = pd.read_csv ("/app/Model/bad-words.csv")
abuse = {}

for i in df.iloc[:, 0].values:
    abuse[i.lower()] = 1

abuse["jigaboo"] = 1