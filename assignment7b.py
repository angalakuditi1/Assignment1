#!/usr/bin/env python
# coding: utf-8

# 
# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use
# MongoDB over SQL databases?
# 
# MongoDB is a NoSQL database that stores data in a document-oriented format. Instead of using tables and rows as in SQL databases, MongoDB uses collections and documents. Documents are stored in JSON-like format.
# 
# Non-relational databases, also known as NoSQL databases, are databases that do not follow the traditional table-based relational model.
# 
# If the  application requires frequent changes to data structure or schema,Ideal for storing hierarchical or nested data due to its document-based structure (JSON/BSON).preferred for applications dealing with big unstructured  data

# Q2. State and Explain the features of MongoDB.
# 
# MongoDB stores data in BSON (Binary JSON) format, which is a binary representation of JSON-like documents.
# 
# Unlike traditional relational databases, MongoDB is schema-less
# 
# it supports horizontal scalability through sharding and ensures high availability with replication

# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.
# 
# from pymongo import MongoClient
# 
# try:
#     client = MongoClient("mongodb://localhost:27017/") 
#     print("Connected to MongoDB successfully!")
# except Exception as e:
#     print(f"Error: {e}")
#     exit()
# 
# db_name = "vinaydoc" 
# database = client[db_name]
# print(f"Database '{db_name}' created!")
# 
# collection_name = "vinaycoll"  
# collection = database[collection_name]
# print(f"Collection '{collection_name}' created!")
# 
# sample_document = {
#     "name": "vinay",
#     "age": 29,
#     "email": "virajruben32@gmail.com",
#     "skills": ["Python", "MongoDB"]
# }
# 
# insert_result = collection.insert_one(sample_document)
# print(f"Document inserted with ID: {insert_result.inserted_id}")
# 

# Q4. Using the database and the collection created in question number 3, write a code to insert one record,
# and insert many records. Use the find() and find_one() methods to print the inserted record.
# 
# from pymongo import MongoClient
# 
# try:
#     client = MongoClient("mongodb://localhost:27017/")
#     print("Connected to MongoDB successfully!")
# except Exception as e:
#     print(f"Error: {e}")
#     exit()
# 
# 
# db_name = "vinaydoc"  
# collection_name = "vinaycoll"  
# database = client[db_name]
# collection = database[collection_name]
# 
# 
# one_record = {
#     "name": "raghu",
#     "age": 25,
#     "email": "nandan23@gmail.com",
#     "skills": ["CA"]
# }
# one_result = collection.insert_one(one_record)
# print(f"One record inserted with ID: {one_result.inserted_id}")
# 
# many_records = [
#     {
#         "name": "SIMEON",
#         "age": 30,
#         "email": "simeon33@gmail.com",
#         "skills": ["banking"]
#     },
#     {
#         "name": "bhagyam",
#         "age": 26,
#         "email": "raje@gmail.com",
#         "skills": ["marketing"]
#     },
#     
# ]
# many_result = collection.insert_many(many_records)
# print(f"Many records inserted with IDs: {many_result.inserted_ids}")
# 
# print("\nUsing find_one() to retrieve a record:")
# found_one = collection.find_one({"name": "simeon"})
# print(found_one)
# 
# print("\nUsing find() to retrieve all records:")
# all_records = collection.find()
# for record in all_records:
#     print(record)

# Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to
# demonstrate this.
# 
# 
# from pymongo import MongoClient
# 
# 
# client = MongoClient("mongodb://localhost:27017/")  
# 
# db = client["vinaydoc"] 
# collection = db["vinaycoll"]  
# 
# collection.insert_many([
#     {"name": "raghu", "age": 28, "city": "guntur"},
#     {"name": "Bobby", "age": 30, "city": "vetapalem"},
#     {"name": "bhagyam", "age": 22, "city": "cpt"}
# ])
# 
# 
# all_docs = collection.find()
# print("All Documents:")
# for doc in all_docs:
#     print(doc)
# 

# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
# 
# The sort method is used to arrange documents in ascending or descending order based on a specified field. It is applied after a query to control the order of the result set.
# 
# players = [
#   { "name": "Virat", "score": 90 },
#   { "name": "Rohit", "score": 120 },
#   { "name": "Dhoni", "score": 85 }
# ]
# 
# db.players.find().sort({ score: -1 });
# 

# Q7. Explain why delete_one(), delete_many(), and drop() is used.
# 
# 
# delete_one(): Deletes a single document matching the filter criteria.have to  Use this when you want to remove just one document.
# 
# delete_many(): Deletes all documents matching the filter criteria. Useful for bulk deletions.
# 
# drop(): Removes an entire collection, including all its documents and indexes. Use this to delete the entire dataset of a collection.

# In[ ]:




