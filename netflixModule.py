from selenium import webdriver
import time
from speachModule import speak
from takecommandModule import takeCommand
from userPref import current_user, db
import os

flag = 1
def netflix():
    if(current_user == ""):
        print("looks like you have not logged in to the app.......please log in first")                            

    else:
        speak("which movie you would like to watch")
        movie_to_watch = takeCommand(flag)
                                
        docs = db.collection(u'Netflix').where(u'user', u'==', current_user).stream()
        for doc in docs:
            try:
                id = doc.to_dict()["userid"]
                ps = doc.to_dict()["acc_pass"]
                movie_netflix(id,ps,movie_to_watch)
            except:
                speak("looks like you dont have a netflix account registered in my app........please register an account")

def movie_netflix(email,pas,mov):
    filepath = os.getcwd()
    try:
        driver = webdriver.Chrome(executable_path=filepath + "\\chromedriver.exe")
        driver.get('https://www.netflix.com/browse')

        username = email
        password = pas
        m = mov

        user_box = driver.find_element_by_id('id_userLoginId')
        pass_box = driver.find_element_by_id('id_password')
        user_box.send_keys(username)
        pass_box.send_keys(password)
        btn = driver.find_element_by_class_name('login-button')
        btn.click()
        time.sleep(3)

        watching = driver.find_element_by_class_name('profile-icon')
        watching.click()
        time.sleep(2)
        search = driver.find_element_by_class_name('icon-search')
        search.click()
        movie = driver.find_element_by_name('searchInput')
        movie.send_keys(m)
        time.sleep(5)
        gotit = driver.find_element_by_class_name('boxart-size-16x9')
        time.sleep(5)
        gotit.click()
        atlast = driver.find_element_by_class_name('button-primary')
        time.sleep(5)
        atlast.click()
        
    except:
        speak("sorry something went wrong, please try again")