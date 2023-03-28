from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:123@dan.lkkvmub.mongodb.net/test")
db = client.blog
