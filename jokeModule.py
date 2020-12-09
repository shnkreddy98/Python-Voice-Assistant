from jokeapi import Jokes
from speachModule import speak

def tellmeajoke():
    j = Jokes()
    joke = j.get_joke(blacklist=['nsfw','racist','sexist'])
    joke_type = joke['type']
    print(joke_type)
    if joke_type == 'single':
        joke = joke['joke']
        speak(joke)
    else:
        setup = joke['setup']
        speak(setup)
        delivery = joke['delivery']
        speak(delivery)