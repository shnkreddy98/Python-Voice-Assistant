import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

filepath = os.getcwd()
cred = credentials.Certificate(filepath + "\\KEY.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection(u'current').stream()
for doc in docs:
    current_user = doc.to_dict()["email"]
    name = doc.to_dict()["name"]
item = [""+name+""]
a = (item[0].split())
b = a[0]
print(current_user,b)