from random import randint
import datetime
import sys,os
from userPref import b, current_user

GREETINGS = ['Hi, How are you?', 'Heyya', 'Hello there', 'Hi, I am serah']

def greetings():
    try:
        VALUE = randint(0, len(GREETINGS)-1)
        print(VALUE)
        return(GREETINGS[VALUE])
    except:
        greetings()

#initial greeting
def wishMe(flag):
    hour = int(datetime.datetime.now().hour)
    if flag == 1:
        if hour>=4 and hour<12:
            return("good morning "+b+".... what can i do for you")

        elif hour>=12 and hour<16:
            return("good afternoon "+b+".... what can i do for you")

        elif hour>=16 and hour<24:
            return("good evening "+b+".... what can i do for you")

        else:
            return(f"Its {hour}'o clock !!!Can't sleep, tell me about it !")

    else:
        if hour>=4 and hour<12:
            return("good morning.... "+b+"")

        elif hour>=12 and hour<16:
            return("good afternoon ...."+b+"")
        
        elif hour>=16 and hour<21:
            return("good evening ...."+b+"")
        
        else:
            return("good night..."+b+"")
