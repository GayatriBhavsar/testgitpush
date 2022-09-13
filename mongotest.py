import pymongo

client = pymongo.MongoClient("mongodb+srv://gayatribhavsar:mongodb123@gayatribhavsar.t4nkn6d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron",
    "surname" : "kumar",
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)