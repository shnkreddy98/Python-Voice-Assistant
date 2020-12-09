from googlesearch import search 
import wolframalpha
import wikipedia
import webbrowser

from speachModule import speak
from takecommandModule import takeCommand

flag = 1

def whatIs(query):
    try:
        speak('wait a second')
        question = query
        app_id = "RQ73V4-XW9VQEVHXW"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
        speak(answer)

    except:
        if "what is" in question:
            try:
                new_query = question.replace("what is","")
                results = wikipedia.summary(new_query,sentences = 2)
                speak(results)
            except:
                speak("i couldn't find anything ..... do you want me to perform online search ?")
                query = takeCommand(flag).lower()
                if('yes' in query):
                    speak("sure...please give me a moment")
                    query = question
                    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
                        print(j)
                        webbrowser.open_new(j)
        else:
            speak("sorry i couldn't find anything ..... please try again")

def whoIs(query):
    try:
        speak('wait a second')
        question = query
        app_id = "RQ73V4-XW9VQEVHXW"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
        speak(answer)

    except:
        if "who is" in question:
            try:
                new_query = question.replace("who is","")
                results = wikipedia.summary(new_query,sentences = 2)
                speak(results)
            except:
                speak("i couldn't find anything ..... do you want me to perform online search ?")
                query = takeCommand(flag).lower()
                if('yes' in query):
                    speak("sure...please give me a moment")
                    query = question
                    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
                        print(j)
                        webbrowser.open_new(j)
        else:
            speak("sorry i couldn't find anything ..... please try again")