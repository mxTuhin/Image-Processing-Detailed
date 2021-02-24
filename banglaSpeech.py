from gtts import gTTS
import pyglet
import time

# tts = gTTS(text='আমি তুহিন', lang='bn')
# tts.save("good.mp3")
# # os.system("mpg321 good.mp3")
# # playsound.playsound('good.mp3', True)
# music = pyglet.resource.media('audio.mp3')
# music.play()


tts = gTTS(text='আমি তুহিন। আমি জি পি এইচ ইস্পাতের একজন কম্পিটিটর। ', lang='bn')
# tts.setPitch()
tts.save("audio.mp3")
# os.system("mpg321 audio.mp3")
music = pyglet.resource.media('audio.mp3')
music.play()
time.sleep(5)