import speech_recognition as sr
from speachModule import speak

null = 0
def takeCommand(flag):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        if flag==2:
            return null  
        elif flag==1:
            speak(" ")
            return"None"
        else:
            print("Say the wake word to activate me")
            return"None"
    return query