import pymongo

uri = "mongodb+srv://root:toor@databaseserver.rgq5c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

connection = pymongo.MongoClient(uri)
database = connection["myDB"]
collection = database["DatabaseServer"]

data = {'WinHtut': 'CrazyCoder', 'age': 27, 'Hobby': 'BuildingTools'}
try:
    collection.insert_one(data)
    print("Data Successfully inserted")
except Exception as err:
    print(err)