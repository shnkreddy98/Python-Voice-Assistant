import datetime
import subprocess
from speachModule import speak
from takecommandModule import takeCommand
from firebase_admin import firestore
from userPref import db

flag = 1

def take_note():
    speak("what is it about?")
    title = takeCommand(flag).lower()
    speak("what should i remember")
    note_it = takeCommand(flag).lower()
    speak("ok i will remember it")
    #Saving on the device
    try:
        date = datetime.datetime.now()
        file_name = title + "-note.txt"
        with open(file_name,"w") as f:
            f.write(note_it)
        subprocess.Popen(["notepad.exe",file_name])
    except:
        take_note()
    #Saving in the firebase notes
    docs = db.collection(u'current').stream()
    for doc in docs:
        a = doc.to_dict()["email"]

    if(a == ""):
        speak("you are not logged in")
    else:
        data = {
        u'user': a,
        u'title': title,
        u'content': note_it
        }
        # Add a new doc in collection 'cities' with ID 'LA'
        db.collection(u'Notes').document().set(data)

def read_notes():
    # dir = "C:\\Users\\Satyam Kumar Pandey\\Desktop\\assistant\\github\\Assistant\\My_Testing\\KEY.json"
    # cred = credentials.Certificate(""+dir+"")
    # firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = db.collection(u'current').stream()
    for doc in docs:
        a = doc.to_dict()["email"]

    if(a == ""):
        speak("you are not logged in.......... i cannot read your notes")
    else:
        lst = []
        c_lst = []
        docs = db.collection(u'Notes').where(u'user', u'==', a).stream()
        for doc in docs:
            id = doc.to_dict()["title"].lower()
            cn = doc.to_dict()["content"]
            lst.append(id)
            c_lst.append(cn)
        speak("you have notes on.... ")
        for item in lst:
        	speak(item)
        speak("..which one should i read")
        try:
            z = takeCommand(flag).lower()
            a = lst.index(z)
            speak(c_lst[a])
        except:
            speak("There are no notes found by that name.... Please try again")
            read_notes()