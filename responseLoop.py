import wikipedia
import webbrowser
import os, random
import wolframalpha
import threading
from googlesearch import search
import time
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from speachModule import speak, assistantAbility
from takecommandModule import takeCommand
from movierecoModule import moviee_reco, else_Say_this
from greetingsModule import greetings, wishMe
from weatherModule import know_weather
from remainderModule import take_note, read_notes
from timeModule import my_time, my_date
from calculateModule import calculator
from checkupModule import medical_report
from whatisModule import whatIs, whoIs
from newsModule import news
from flipkartModule import flipkart
from netflixModule import netflix
from sendEmailModule import send_mail
from restaurantModule import rec_restaurant
from homeautomateModule import homeautomate
from smartBulb import turnOn, turnOff
from musicModule import play_music
from findmeModule import find_me
from whatsappModule import whatsapp
from jokeModule import tellmeajoke

GREETINGS_QUERY = ['hello','greetings','hi', "howdy", "welcome", "bonjour", "good day", "hi-ya", "howdy-do", "what's happening","what's up"]
RECOMMEND = ['recommend', 'suggest', 'recommended']
CALCULATOR = ['calculate', 'answer', 'equation', 'solve']
MEDICAL = ['prescription', 'medical', 'report']
FLIPKART = ['buy', 'purchase']
JOKE = ['joke', 'humor', 'laugh']
MOVIE = ['movie']
MUSIC = ['music', 'songs', 'song', 'listen', 'play']
NETFLIX = ['netflix', 'watch', 'play']
NEWS = ['news']
REMAINDER = ['note', 'remember', 'write']
RESTAURANT = ['dinner', 'breakfast', 'lunch', 'restaurant', 'eat', 'place']
READNOTES = ['read', 'notes', 'remember']
EMAIL = ['email', 'mail', 'send', 'gmail']
TIMEANDDATE = ['time', 'date']
WEATHER = ['weather', 'temperature', 'today']
QUESTION = ['who', 'when', 'what', 'where', 'how']
WHATSAPP = ['whatsapp', 'message']
HOMEAUTOMATE = ['turn']
OPEN_UI = ['open']
IDENTITY = ['yourself']

flag = 1

def responseloop(response):
    did_it_work = 0
    tokens = word_tokenize(response)
    stop_words = set(stopwords.words('english'))
    clean_tokens = [w for w in tokens if not w in stop_words]
    print(clean_tokens)
    
    for word in clean_tokens:
        if word in GREETINGS_QUERY:
            speak(greetings())
            did_it_work = 1
            break
            
        elif word in IDENTITY:
            assistantAbility()
            did_it_work = 1
            break
                        
        elif word in OPEN_UI:
            try:
                site = response.split(" ")
                webbrowser.open(site[1]+".com")
                did_it_work = 1
                break
            except IndexError:
                speak("What do you want to open")
                site = takeCommand(flag).lower()
                webbrowser.open(site+".com")
                did_it_work = 1
                break
                        
        elif word in MOVIE:
            #print("movie re working")
            if "movie" in response and "recommend" in response:
                moviee_reco()
                did_it_work = 1
                break
            
            elif "restaurant" in response:
                print("up")
                rec_restaurant()
                did_it_work = 1
                break

        elif word in MEDICAL:
            medical_report()
            did_it_work = 1
            break
        
        elif word in READNOTES:
            read_notes()
            did_it_work = 1
            break

        elif word in REMAINDER:
            take_note()
            did_it_work = 1
            break

        elif word in CALCULATOR:
            speak(calculator(response))
            did_it_work = 1
            break
        
        elif word in WEATHER:
            know_weather()
            did_it_work = 1
            break

        elif word in NEWS:
            print("news loop working")
            news()
            did_it_work = 1
            break

        elif response in IDENTITY:
            speak("I am Serah.... Your Personal Assistant")
            did_it_work = 1
            break

                    #elif word in FLIPNET:
        elif word in FLIPKART:
            flipkart(response)
            did_it_work = 1
            break

        elif word in EMAIL:
            send_mail()
            did_it_work = 1
            break

        elif word in RESTAURANT:
            rec_restaurant()
            did_it_work = 1
            break

        elif word in HOMEAUTOMATE:
            if "on" in response:
                turnOn()
                did_it_work = 1
                break

            elif "off" in response:
                turnOff()
                did_it_work = 1
                break


        elif 'play' in word:
            if 'movie' in clean_tokens or 'netflix' in clean_tokens:
                print('this')
                netflix()
                did_it_work = 1
                break
            elif 'music' in clean_tokens:
                play_music()
                did_it_work = 1
                break

            else:
                speak('What do you want me to play... music or a movie?')
                reply = takeCommand(flag).lower()
                if 'movie' in reply:
                    print('that')
                    netflix()
                    did_it_work = 1
                    break
                elif 'music' in reply:
                    play_music()
                    did_it_work = 1
                    break

        elif word in NETFLIX:
            netflix()
            did_it_work = 1
            break

        elif word in MUSIC:
            if 'music' in response:
                play_music()
                did_it_work = 1
                break
            elif 'movie' in response:
                print('last')
                netflix()
                did_it_work = 1
                break

        elif word in WHATSAPP:
            whatsapp()
            did_it_work = 1
            break

        elif word in JOKE:
            tellmeajoke()
            did_it_work = 1
            break

        elif word in TIMEANDDATE:
            if 'time' in response:
                speak(my_time())
                did_it_work = 1
                break

            elif 'date' in response:
                speak(my_date())
                did_it_work = 1
                break

        elif word in QUESTION:
            if 'time' in response:
                speak(my_time())
                did_it_work = 1
                break

            elif 'date' in response:
                speak(my_date())
                did_it_work = 1
                break
            
            elif 'news' in response:
                news(response)
                did_it_work = 1
                break

            elif response in WEATHER:
                know_weather()
                did_it_work = 1
                break

            elif "what" in response or "what's" in response:
                whatIs(response)
                did_it_work = 1
                break

            elif "who" in response or "who's" in response:
                whoIs(response)
                did_it_work = 1
                break
    
    if did_it_work == 0:
        
        try:    
            print(response)
            if (response == "none"):
                speak("")
            else:
                app_id = "RQ73V4-XW9VQEVHXW" 
                client = wolframalpha.Client(app_id) 
                res = client.query(response) 
                answer = next(res.results).text
                print(answer) 
                speak(answer)
        except:
            t1 = threading.Thread(target = speak("sure...please give me a moment"))
            t2 = threading.Thread(target = find_me,args=(response,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()