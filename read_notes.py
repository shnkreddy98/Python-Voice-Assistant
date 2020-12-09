import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def read_notes(query):
    dir = "C:\\Users\\Satyam Kumar Pandey\\Desktop\\assistant\\github\\Assistant\\My_Testing\\KEY.json"  #edhar se niche 3 line comment agar error diya toh
    cred = credentials.Certificate(""+dir+"")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = db.collection(u'current').stream()
    for doc in docs:
        a = doc.to_dict()["email"]

    if(a == ""):
        speak("you are not logged in")
    else:
        lst = []
        c_lst = []
        docs = db.collection(u'Notes').where(u'user', u'==', a).stream()
        for doc in docs:
            id = doc.to_dict()["title"].lower()
            cn = doc.to_dict()["content"]
            lst.append(id)
            c_lst.append(cn)
        speak("you have note on.... ")
        speak(lst)
        speak("..which one should i read")
        z = takeCommand(flag).lower()
        a = lst.index(z)
        speak(c_lst[a])
