from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# when you insert one record then it cannnot be inserTED again, it will throw ERROR
# so you have to first delete record or collection then again try to insert and RUN
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('xyz', 'xyz123'))
print("connection successful", myclient)
mydb = myclient['test5']
print("Database Created !!!!!!!", mydb)
collection = mydb['student']
mylist = [
            {
                "_id": 19,
                "name": "john",
                "roll_number": 103,
                "branch": "eee",
                "marks": 45
            },
            {
                "_id": 20,
                "name": "jenny",
                "roll_number": 108,
                "branch": "cse",
                "marks": 65
            },
            {
                "_id": 21,
                "name": "joe",
                "roll_number": 105,
                "branch": "cse",
                "marks": 55
            }

        ]




# collection.drop()




record_1 = collection.insert_many(mylist)
print("Records...", record_1)

# # delete ONE
# myquery = {"_id": 21}
# collection.delete_one(myquery)

# delete MANY
collection.delete_many({"id":{"$gt":"19"}})

x = collection.find()
for each_record in x :
    print("doc", each_record)
