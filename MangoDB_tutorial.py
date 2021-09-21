
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    try:
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('xyz', 'xyz123'))
        print("connection successful", myclient)

        # # create new database in mongodb
        mydb = myclient['Test']
        # print("Database Created !!!!!!!", mydb)
        print("____________________________________________________________")
        #
        # # # create collection
        # collection = mydb['student']
        # record = {
        #     "_id": 0,
        #     "name": "raj",
        #     "roll_number": 101,
        #     "branch": "cse",
        #     "marks": 40
        # }
        #
        # record_1 = collection.insert_one(record)
        # print("Records made...", record_1)

        # list down the databases
        list_of_db = myclient.list_database_names()
        print("databases available in mongodb after creation", list_of_db)

        records = {
            "record1": {
                "_id": 17,
                "name": "rohan",
                "roll_number": 103,
                "branch": "cse",
                "marks": 45
            },
            "record2": {
                "_id": 18,
                "name": "ram",
                "roll_number": 104,
                "branch": "cse",
                "marks": 55
            }
        }
        # #create collection
        # collection = mydb['student']
        # for record in records.values():
        #     collection.insert_one(record)

        mylist = [
            {
                "_id": 19,
                "name": "john",
                "roll_number": 103,
                "branch": "cse",
                "marks": 45
            },
            {
                "_id": 20,
                "name": "jenny",
                "roll_number": 108,
                "branch": "cse",
                "marks": 55
            },
            {
                "_id": 21,
                "name": "joe",
                "roll_number": 105,
                "branch": "cse",
                "marks": 55
            }

        ]
        collection = mydb['student']
        # collection.insert_many(mylist)

        # 3 find the  document display document or retreive
        # x = collection.find_one()
        # print("record", x)

        all_document = collection.find()
        for each_record in all_document:
            print("doc", each_record)

        # for x in collection.find({}, {"_id": 0, "name": 1, "branch": 1}):
        #     print("Only fields with 1", x)

        # # Greater than Operator
        # curson = collection.find({"marks": {"$gt": 45}})
        # print("The records greater than 45")
        # for record in curson:
        #   print("records:", record)
        #
        # curson = collection.find({"marks": {"$lt": 50}})
        # print("The records LESSER than 50")
        # for record in curson:
        #     print("records:", record)
        #
        # # search or display records in between
        #
        # ob = collection.find({"$and":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
        # print("AND conditions records----------")
        # for record in ob:
        #    print("records", record)
        #
        # ob = collection.find({"$or":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
        # print("OR conditions records-------------")
        # for record in ob:
        #    print("records", record)

        # # sorting
        # mydoc =  collection.find().sort("name")
        # for x in mydoc:
        #    print("Ascending sorting..", x)
        # mydoc =  collection.find().sort("name", -1)
        # for x in mydoc:
        #    print("Descending sorting..", x)

        # # update
        # filter = {'name': 'rohan'}
        # newvalues={"$set":{"marks":35}}
        # collection.update_one(filter, newvalues)
        # all_document = collection.find()
        # for each_record in all_document:
        #    print("doc", each_record)

        # # upsert  (it also update but if data is not present then it insert also)
        # collection.update_many(
        #     {
        #         "marks": {
        #             "$gt": 40
        #         }
        #     },
        #     {
        #         "$set": {
        #             "address": "pune"
        #         }
        #     }
        # )
        # print("---------Updated records------------")
        # cursor = collection.find()
        # for record in cursor:
        #     print(record)





    except ConnectionFailure as e:
        print("error", e)

if __name__ == '__main__':
     main()