import os

from dotenv import load_dotenv
from pymongo import MongoClient

from map_reduce.create_data_collection import create_data_collection
from map_reduce.map_reduce import map_reduce
from map_reduce.naive_bayes import naive_bayes_classifier
from map_reduce.confusion_matrix import confusion_matrix

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
conn = MongoClient(MONGODB_URI)
db = conn.email_spam_filtering # db chính
db1 = conn.sample_email_test# db dùng để show quá trình xử lý của naive bayes

create_data_collection(trainned=True, db=db)
map_reduce(trained=True, db=db)
naive_bayes_classifier(show=True, db=db, db1=db1)
a = confusion_matrix(db=db)
print(a)
