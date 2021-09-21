import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.son import SON
import pprint

def main():
    try:

        # myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('xyz', 'xyz123'))
        # print("connection successful", myclient)
        #
        # my_db = myclient['tests']
        # collection = my_db['agg_example']
        #
        #
        # profiles = [
        #     {"user": "ram", "title": "Python"},
        #     {"user": "raj", "title": "Javascript"},
        #     {"user": "ram", "title": "C++"},
        #     {"user": "john", "title": "MongoDB"},
        #     {"user": "rohan", "title": "Python"},
        # ]
        #
        # collection.insert_many(profiles)
        #
        # agg_result = collection.aggregate(
        #     [
        #         {
        #             "$group": {
        #                 "_id": "$title",
        #                 "occurrences": {"$sum": 1}
        #             }
        #         }
        #     ]
        #
        # )
        # for i in agg_result:
        #     print(i)

        ####################################################################################################

        # collection.drop()  [code for deleting the collection]

        ########################################################################################################
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('xyz', 'xyz123'))
        mydatabase = myclient['database']

        mycollection = mydatabase['test3']

        sample_data = [
                      {"x" : "1", "tags": ["dog", "cat"]},
                      {"x" : "2", "tags": ["cat"]},
                      {"x" : "2", "tags": ["mouse", "dog", "cat"]},
                      {"x" : "3", "tags": []}
                       ]

        mycollection.insert_many(sample_data)

        pipeline = [
                      {
                          "$unwind":"$tags"
                      },
                      {
                          "$group":{"_id":"$tags","count":{"$sum":1}}
                      },

                ]
        pprint.pprint(list(mycollection.aggregate(pipeline)))

    except ConnectionFailure as e:
        print("Error:", e)

if __name__ == '__main__':
        main()