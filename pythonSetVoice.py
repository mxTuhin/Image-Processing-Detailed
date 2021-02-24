import pyttsx3, time

engine = pyttsx3.init()
sound = engine.getProperty('voices')
engine.setProperty('voice', sound[1].id)
engine.say('ki.mp3')

engine.runAndWait()