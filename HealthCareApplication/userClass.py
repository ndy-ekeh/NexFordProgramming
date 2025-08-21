import pandas as pd
from pymongo import MongoClient


class User:
    def __init__(self,age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

        
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["participants"]

data = list(collection.find({}, {"_id": 0}))

# Convert to DataFrame
df = pd.json_normalize(data)

# Save to CSV
df.to_csv("surveydata.csv", index=False)
print("Data completed and exported to surveydata.csv")
