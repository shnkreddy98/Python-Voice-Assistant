from speachModule import speak
from takecommandModule import takeCommand
import random
from bs4 import BeautifulSoup
import requests
import geocoder

flag = 1

g = geocoder.ip('me')

def rec_restaurant():
    try:
        speak("do you want recommendations for your current location")
        a = takeCommand(flag).lower()
        if "yes" in a:
            city = g.city.lower()
        else: 
            speak("give me a city name")
            city = takeCommand(flag).lower()
        
        speak("what kind of dish or food you like")
        dish = takeCommand(flag).lower()
        speak("sure....let me find something for you")
        print(dish,city)
        url = 'https://www.zomato.com/'+city+'/restaurants/'+dish+'?category=0'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

        response = requests.get(url,headers=header)
        html = response.text

        soup = BeautifulSoup(html,'lxml')

        top_rest = soup.find('div',class_="orig-search-list-container")
        restaurant = []
        rating = []

        rsts = top_rest.find_all('a',class_="result-title")
        rate = top_rest.find_all('span',class_="rating-value") 
        for i in rate:
            x = i.text.replace("\n"," ").strip()
            rating.append(x)
        for i in rsts:
            x = i.text.replace("\n"," ").strip()
            restaurant.append(x)
        speak("Here are some place that you should try")
        for i in range(0,5):
            print(restaurant[i]+" rating "+rating[i])
            speak(restaurant[i]+" rating "+rating[i])
        r = random.randrange(0,5,1)
    
        speak("but i think you should try "+restaurant[r]+" they have a good rating of "+rating[r])
    except:
        speak("sorry something went wrong....please try again")