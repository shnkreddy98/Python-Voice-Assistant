from speachModule import speak, assistantAbility
from takecommandModule import takeCommand
from greetingsModule import wishMe
from responseLoop import responseloop
from automationModule import automated_greetings
from userPref import db, current_user
import winsound
from time import sleep
from nltk.corpus import stopwords
from nltk import word_tokenize


docs = db.collection(u'Custom').where(u'user', u'==', current_user).stream()
for doc in docs:
    wakey = doc.to_dict()["wake_word"].lower()
    wakey_wakey = wakey
WAKE = wakey_wakey.split(",")
USER_GREETING = ['good morning', 'morning', 'night', 'evening']
#print(WAKE)

if __name__ == "__main__":
    while True:
            
        doc_ref = db.collection(u'mode').document(current_user)
        doc = doc_ref.get()
        Mode = doc.to_dict()["mode"]
        flag = 3
        if Mode != 'HOME':
            doc_ref = db.collection(u'actv_query').document(current_user)
            doc = doc_ref.get()
            query = doc.to_dict()["query"]
            res = query.lower()      #ye tera query for away mode
            print(query)
            if(query == "NA"):
                print("do nothing")
                doc_ref = db.collection(u'mode').document(current_user)
                doc = doc_ref.get()
                mode = doc.to_dict()["mode"]
                print("mode :- "+mode)
            else:
                print("execute query")
                print(res)
                responseloop(res)
                data = {
                u'query': u'NA'
                }
                doc_ref = db.collection(u'actv_query').document(current_user).set(data)           

        else: 
            flag = 0
            #response = input()
            response = takeCommand(flag).lower()
            #query = response.split(" ")
            tokens = word_tokenize(response)
            stop_words = set(stopwords.words('english'))
            query = [w for w in tokens if not w in stop_words]
            #print(query)
            if response:
                for idx, word in enumerate(query):
                    print(word)
                    if word in WAKE:
                        #winsound.PlaySound("response.wav", winsound.SND_ASYNC)
                        #sleep(0.5)
                        #speak(response)
                        flag = 1
                        next_word = idx + 1
                        #print(next_word)
                        try:
                            if query[next_word] != '':
                                #print(word)                        
                                indx = response.lower().split().index(word)
                                #print(indx)
                                response = response.split()[indx + 1:]
                                res = (' '.join(response))
                                #print(res)
                                if res in USER_GREETING:
                                    automated_greetings(res)
                                    break
                                else:
                                    #print(res)
                                    responseloop(res)
                                    break
                            
                        except IndexError:
                            print("working")
                            speak(wishMe(flag))
                            short_query = takeCommand(flag).lower()
                            if short_query in USER_GREETING:
                                automated_greetings(short_query)
                                break
                            else:
                                #speak(short_query)
                                responseloop(short_query)
                                break