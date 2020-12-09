import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def assistantAbility():
	speak('i am still learning .. but i can do many things ')
	speak('like recommend a movie on netflix ....... browse youtube ....... take notes....... i can also tell the time and date for starters')
	speak('now tell me what can i do for you.')