from speachModule import speak
from selenium import webdriver
from userPref import db
from takecommandModule import takeCommand
import random
import os

flag = 1

def play_music():
    filepath = os.getcwd()

    docs = db.collection(u'current').stream()
    for doc in docs:
        a = doc.to_dict()["email"]

    if(a == ""):
        speak("you are not logged in")
    else:
        docs = db.collection(u'Custom').where(u'user', u'==', a).stream()
        for doc in docs:
            music = doc.to_dict()["music"].lower().split(",")
        print(music)
    speak("should i play songs which i like ?")
    z = takeCommand(flag).lower()
    if(z == 'yes'):
        #random bajega gaana 
        try:
            a = len(music)-1
            r = random.randrange(0,a,1)

            driver = webdriver.Chrome(executable_path=filepath + "\\chromedriver.exe")
            driver.get('https://www.jiosaavn.com/search/'+music[r]+'%20music')

            play = driver.find_element_by_class_name('art')
            play.click()
            
        except:
            speak("sorry i could not play songs at the moment")
    else:
        #on user choice
        speak("which song you want me to play")
        music = takeCommand(flag).lower().replace(" ","%20")
        speak("okay")
        
        try:
        
            driver = webdriver.Chrome(executable_path=filepath + "\\chromedriver.exe")
            driver.get('https://www.jiosaavn.com/search/'+music)

            play = driver.find_element_by_class_name('art')
            play.click()
            
        except:
            speak("sorry i could not play songs at the moment")