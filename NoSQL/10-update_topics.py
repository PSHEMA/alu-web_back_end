#!/usr/bin/env python3
""" a Python function that changes all topics of a school document based on the name """

def update_topics(mongo_collection, name, topics):
    """ changes the name of a collection based on the name """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
