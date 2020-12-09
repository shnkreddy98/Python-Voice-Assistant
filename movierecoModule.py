import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
import random
from googlesearch import search
import webbrowser

from speachModule import speak
from takecommandModule import takeCommand

flag = 1

def moviee_reco():
    speak("what's your Favourite movie")
    movie_name = takeCommand(flag)
    speak("okay .......so you can try movies like ")
    try:
        movie_reco(movie_name)
    except:
        else_Say_this(movie_name)
        

########## RECOMMENDATION ALGORITHM ##########
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
  
df = pd.read_csv("movie_dataset.csv")

features = ['keywords','cast','genres','director']

for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:", row)	

df["combined_features"] = df.apply(combine_features,axis=1)
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def movie_reco(movie_name):
    movie_user_likes = movie_name
    movie_index = get_index_from_title(movie_user_likes)

    similar_movies =  list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
    i=1
    
    array_movie = []
    for element in sorted_similar_movies:
            speak(get_title_from_index(element[0]))
            array_movie.append(get_title_from_index(element[0]))
           
            i=i+1
            if i>5:
                print(array_movie)
                speak('but i will recommend'+ array_movie[3])
                break

##########ENDALGORITHM##########            

def else_Say_this(query):
    try:
        a = query
        m = a.replace(" ","+")
        url = 'https://www.movie-map.com/'+m
    
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

        response = requests.get(url,headers=header)
        html = response.text

        soup = BeautifulSoup(html,'lxml')

        movie = []
        suggest = []

        group = soup.find_all('a',class_="S")

        for i in group:
            x = i.text.replace("\n"," ").strip()
            movie.append(x)
        
        # speak("you can try movies like")
        for i in range(0,5):
            r = random.randrange(0,20,1)
            speak(movie[r])
            print(movie[r])
            suggest.append(movie[r])

        i = random.randrange(0,4,1)
        speak("but i will suggest.."+suggest[i]+"..my personal favourite")
    except:
        speak("sorry i could not find any related movies...should i search online")
        z = takeCommand(flag).lower()
        if "yes" in z:
            new_query = "movies similar to"+query
            for j in search(new_query, tld="co.in", num=10, stop=1, pause=2): 
                print(j) 
            webbrowser.open_new(j)