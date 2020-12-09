import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import smtplib
import os

filepath = os.getcwd()
cred = credentials.Certificate(filepath + "\\KEY.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
mode= ''

docs = db.collection(u'current').stream()
for doc in docs:
    a = doc.to_dict()["email"]

if(a == ""):
    print("no user logged in")
else:
    
    doc_ref = db.collection(u'mode').document(a)
    doc = doc_ref.get()
    Mode = doc.to_dict()["mode"]

if (Mode == "HOME"):
    print("normal query sab chalega")
else:
    while (mode == "AWAY"):
        doc_ref = db.collection(u'actv_query').document(a)
        doc = doc_ref.get()
        query = doc.to_dict()["query"]      #ye tera query for away mode
        print(query)
        if(query == "NA"):
            print("do nothing")
            doc_ref = db.collection(u'mode').document(a)
            doc = doc_ref.get()
            mode = doc.to_dict()["mode"]
            print("mode :- "+mode)
        else:
            print("execute query")
            data = {
            u'query': u'NA'
            }
            doc_ref = db.collection(u'actv_query').document(a).set(data)
            