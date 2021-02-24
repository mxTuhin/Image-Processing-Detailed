from gtts import gTTS
import pyglet
import time


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    # os.system("mpg321 audio.mp3")
    playPyglet()

def playPyglet():
    music = pyglet.resource.media('audio.mp3')
    music.play()
    time.sleep(2)

speak("Unknown")