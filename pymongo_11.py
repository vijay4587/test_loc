import pymongo
from datetime import datetime

my_client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.9szl5lh.mongodb.net/?retryWrites=true&w=majority")

mydb = my_client["sample_mflix"]

my_collection = mydb["comments"]

post1 = {"_id":267,"name":"tim","email":"vijaym269@gmail.com","movie_id":"","text":"this is the newest data","date":datetime.now().isoformat()}
post2 = {"_id":268,"name":"vijayma","email":"vijayma269@gmail.com","movie_id":"","text":"this is the newest data","date":datetime.now().isoformat()}
my_query = {"name":{"$regex":"ma$"}}
x = my_collection.delete_many(my_query)
print(x.deleted_count, " documents deleted.")
# my_collection.insert_many([post1,post2])
# for i in a:
#   print(i)
# my_collection.update_one({"_id":267},{"$set":{"name":"tim"}})
# a = my_collection.find().sort("name", -1)

# for i in a:
#   print(i)
# print(mydb)