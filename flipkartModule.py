from speachModule import speak
from selenium import webdriver
import time
import os
from googlesearch import search
import webbrowser

def flipkart(query):
    filepath = os.getcwd()
    item = [""+query+""]
    a = (item[0].split())
    product = a[-2]+" "+a[-1]
    speak("sure let me find "+product+" for you")
    new_query = "buy "+product
    try:
        # driver = webdriver.Chrome(executable_path= filepath + "\\chromedriver.exe")
        # driver.get ("https://www.flipkart.com/")
        # time.sleep(3)
        # btn = driver.find_element_by_class_name('_2AkmmA')
        # btn.click()
        # search = driver.find_element_by_class_name('LM6RPg')
        # search.send_keys(product)
        
        # sbtn = driver.find_element_by_class_name('vh79eN')
        # sbtn.click()
        for j in search(new_query, tld="co.in", num=10, stop=1, pause=2): 
            print(j) 
        webbrowser.open_new(j)
    except:
        speak("i think the internet is slow please try again")
        flipkart(query)