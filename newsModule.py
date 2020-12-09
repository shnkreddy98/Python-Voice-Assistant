import requests, json

from userPref import current_user, db

from speachModule import speak
from takecommandModule import takeCommand

flag = 1

keywords = ''
def news():
    print("before for")
    docs = db.collection(u'Custom').stream()
    for doc in docs:
        keywords = doc.to_dict()["news"].lower().split(",")
    print(keywords)

    for keyword in keywords:
        if(keyword):
            print(keyword)
            api_key = "ae472856c08a413288b2feac62f3a74d"
            base_url = "http://newsapi.org/v2/top-headlines?country=in&"
            complete_url = base_url + "q=" + keyword + "&sortBy=popularity&apiKey=" + api_key

        else:
            api_key = "ae472856c08a413288b2feac62f3a74d"
            base_url = "http://newsapi.org/v2/top-headlines?country=in&sortBy=popularity&"
            complete_url = base_url + "apikey=" + api_key 

        response = requests.get(complete_url)
        x = response.json()


        if x['status'] == "ok":
            y = x['articles']
            top = 0
            for i in y:
                if top < 3:
                    source = i['source']
                    name = source['name']
                    author = i['author']
                    title = i['title']
                    description = i['description']

                    speak(title)
                    top += 1
                    flag = 2
                    speak('Say yes to know more about this...')
                    response = takeCommand(flag)
                
                if response:
                    speak(description)
                    continue
                else:
                    continue