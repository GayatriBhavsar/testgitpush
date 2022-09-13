import pymongo

client = pymongo.MongoClient("mongodb+srv://gayatribhavsar:mongodb123@gayatribhavsar.t4nkn6d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
var_dict = {
    'key1':'[1,2,3,4,5,[11,22,33,44,555,6],4435,566,(4,5,6,7,8)]',
    'key2':'{"s":"device","s1":"laptop"}'
}



database = client['test2']
collect = database['list1']
collect.insert_one(var_dict)


