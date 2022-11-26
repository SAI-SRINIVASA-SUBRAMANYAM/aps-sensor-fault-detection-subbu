import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATA_FILEPATH = "aps_failure_training_set1.csv"


if __name__ == "__main__":
    db = client[DATABASE_NAME]
    coll = db[COLLECTION_NAME]
    data = pd.read_csv(DATA_FILEPATH)
    print(data.shape)
    data.reset_index(drop=True, inplace=True)
    print(data.shape)
    payload = list(json.loads(data.T.to_json()).values())
    print(payload[0])
    coll.insert_many(payload)