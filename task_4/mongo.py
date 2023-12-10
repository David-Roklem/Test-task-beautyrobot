import pymongo
import datetime

# Establish connection with MongoDB
client = pymongo.MongoClient('mongodb://localhost:2717/')
db = client['task_db']
collection = db['task_db_collection']

# Insert data into collection
data = {'email': 'first@mail.ru', 'created_at': datetime.datetime.utcnow()}
collection.insert_one(data)
print('Data:', collection.find_one())


# Create TTL index on 'created_at' field
collection.create_index(
    'created_at',
    expireAfterSeconds=86400
)  # 24h == 86400s

# print('Data:', collection.find_one())
# Data will be deleted by MongoDB in 24 hours - <Data: None>

# P.S. Pay attention that if you want to check whether the code is correct
# with some 'expireAfterSeconds' time set up for less than a min, it may take
# a bit more time than you expect for the data to be deleted by MongoDB:
'''
The background task that removes expired documents runs every 60 seconds.
As a result, documents may remain in a collection during the period between
the expiration of the document and the running of the background task.
MongoDB starts deleting documents 0 to 60 seconds after the index completes.
'''
