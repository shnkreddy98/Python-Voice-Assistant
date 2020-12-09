import json,requests
import geocoder

from speachModule import speak

g = geocoder.ip('me')

def know_weather():
	try:
		city_name = g.city
		api_key = "eaef440ac230e0cc85d7dab8e9bc4b65"
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
		response = requests.get(complete_url)                
		x = response.json()
		print(x)
		if x["cod"] != "404":
			y = x["main"]
			current_temperature = y["temp"]
			current_pressure = y["pressure"]
			current_humidiy = y["humidity"]
			z = x["weather"]
			weather_description = z[0]["description"]
			c = current_temperature - 273.15
			celcius_temp = format(c,'.1f')
			speak("Today's weather in "+city_name+" is "+str(weather_description)+'..... current temperature is'+celcius_temp+'degree celcius ....the humidity today is'+str(current_humidiy)+'percent')
		else:
			speak(" I could not find a matching city  ")

	except:
		know_weather()