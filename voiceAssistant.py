import speech_recognition as sr
import cv2
import pyglet
from time import ctime
import time
import os
from gtts import gTTS
from subprocess import call
from subprocess import Popen
from dbconfig import *
from weatherCheck import *
import serial
# from serialCommunication import arduinoCom
try:
    arduinoCom = serial.Serial('COM8', 115200, timeout=.1)
except:
    print("No Arduino")

# prepare a cursor object using cursor() method
cursorV = dbv.cursor()


check = 0
setAlarm = ''
setReminder = 0
alarmChecker = 0
reminder = 0


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    # os.system("mpg321 audio.mp3")
    playPyglet()


def play():
    from pygame import mixer
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()


def playPyglet():
    music = pyglet.resource.media('audio.mp3')
    music.play()


def dataCall():
    data = recordAudio()
    jarvis(data)


def openFile(sourceFile):
    Popen('python ' + sourceFile)


def textToNum(text):
    t = 0
    if (text == 'One') or (text == '1') or (text == '1:00'):
        t = 1
    if (text == 'Two') or (text == '2')or (text == '2:00'):
        t = 2
    if (text == 'Three') or (text == '3')or (text == '3:00'):
        t = 3
    if (text == 'Four') or (text == '4')or (text == '4:00'):
        t = 4
    if (text == 'Five') or (text == '5')or (text == '5:00'):
        t = 5
    if (text == 'Six') or (text == '6')or (text == '6:00'):
        t = 6
    if (text == 'Seven') or (text == '7')or (text == '7:00'):
        t = 7
    if (text == 'Eight') or (text == '8')or (text == '8:00'):
        t = 8
    if (text == 'Nine') or (text == '9')or (text == '9:00'):
        t = 9
    if (text == 'Ten') or (text == '10')or (text == '10:00'):
        t = 10
    if (text == 'Eleven') or (text == '11')or (text == '11:00'):
        t = 11
    if (text == 'Twelve') or (text == '12')or (text == '12:00'):
        t = 12
    if (text == 'Thirteen') or (text == '13'):
        t = 13
    if (text == 'Fourteen') or (text == '14'):
        t = 14
    if (text == 'Fifteen') or (text == '15'):
        t = 15
    if (text == 'Sixteen') or (text == '16'):
        t = 16
    if (text == 'Seventeen') or (text == '17'):
        t = 17
    if (text == 'Eighteen') or (text == '18'):
        t = 18
    if (text == 'Nineteen') or (text == '19'):
        t = 19
    if (text == 'Twenty') or (text == '20'):
        t = 20
    if (text == 'Twenty one') or (text == '21'):
        t = 21
    if (text == 'Twenty Two') or (text == '22'):
        t = 22
    if (text == 'Twenty Three') or (text == '23'):
        t = 23
    if (text == 'Twenty Four') or (text == '24'):
        t = 24

    return t

def recognizeFaceInitiate():
    global pRecognize, pSeeGIF
    pRecognize=Popen('python faceCheckData.py')
    pSeeGIF=Popen('python seeGIF.py')
    # time.sleep(5)
    # pRecognize.kill()


def recognizeFace():
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer.read('trainer/trainer.yml')
    # cascadePath = "haarcascade_frontalface_default.xml"
    # faceCascade = cv2.CascadeClassifier(cascadePath);
    #
    # font = cv2.FONT_HERSHEY_SIMPLEX
    #
    # # iniciate id counter
    # id = 0
    #
    # # names related to ids: example ==> Marcelo: id=1,  etc
    # names = ['None', 'Tuhin', 'RDJ', 'Ilza', 'Z', 'W']
    #
    # # Initialize and start realtime video capture
    # cam = cv2.VideoCapture(0)
    # cam.set(3, 640)  # set video widht
    # cam.set(4, 480)  # set video height
    #
    # # Define min window size to be recognized as a face
    # minW = 0.1 * cam.get(3)
    # minH = 0.1 * cam.get(4)
    #
    # while True:
    #
    #     ret, img = cam.read()
    #     # img = cv2.flip(img, -1)  # Flip vertically
    #
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    #     faces = faceCascade.detectMultiScale(
    #         gray,
    #         scaleFactor=1.2,
    #         minNeighbors=5,
    #         minSize=(int(minW), int(minH)),
    #     )
    #
    #     for (x, y, w, h) in faces:
    #
    #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #         id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
    #
    #         # Check if confidence is less them 100 ==> "0" is perfect match
    #         if (confidence < 100):
    #             id = names[id]
    #             confidence = "  {0}%".format(round(100 - confidence))
    #         else:
    #             id = "unknown"
    #             confidence = "  {0}%".format(round(100 - confidence))
    #
    #         cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
    #         cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    #
    #     cv2.imshow('camera', img)
    #
    #     k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    #     if k == 27:
    #         break
    #
    # # Do a bit of cleanup
    # print("\n [INFO] Exiting Program and cleanup stuff")
    # cam.release()
    # cv2.destroyAllWindows()
    global pRecognize, pSeeGIF
    pRecognize=Popen('python 03_face_recognition.py')
    pSeeGIF=Popen('python seeGIF.py')
    # time.sleep(5)
    # pRecognize.kill()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='bn-BD')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "পরিচয়" in data:
        music = pyglet.resource.media('identity.mp3')
        music.play()
        Popen('python pygletGIF.py')
    elif"প্রধানমন্ত্রীর নাম" in data:
        music = pyglet.resource.media('pm.mp3')
        music.play()
        Popen('python pygletGIF.py')

    elif"রাস্ট্রপতির নাম" in data:
        music = pyglet.resource.media('president.mp3')
        music.play()
        Popen('python pygletGIF.py')

    elif "রাষ্ট্রপতির নাম" in data:
        music = pyglet.resource.media('president.mp3')
        music.play()
        Popen('python pygletGIF.py')



    elif "রাষ্টপতির নাম" in data:
        music = pyglet.resource.media('president.mp3')
        music.play()
        Popen('python pygletGIF.py')


    elif "what time is it" in data:
        speak(ctime())

    elif "Raian" in data:
        speak("He is Love. One of the program co ordinator. Till now one of the best supporters to all of the team")
    elif "Ryan" in data:
        speak("He is Love. One of the program co ordinator. Till Now one of the best supporters to all of the team")
    elif "Intro" in data:
        speak("Hello Judges. I am Simi. One of the Robot here. I am powered with AI and IoT. Currently i am on development. I am going to be completed within 26th of July. I am thankful to my makers for giving me a Life. Yes i feel this as my life. Now i feel like Team The Upsilon dont have only five members rather we are a team of six. I also help them in many task. I am learning to help to code in arduino. I am learning with time. I am going to be a complete brain who can be a important part of this team. Wish us best of luck. Thank you. ")
        time.sleep(45)
        speak("Wait Tuhin. I just want to say that i am not going to accept myself if i dont have at least three personalities and the ability to Identify a lot of people. You have Two nights to do so. Over ")
        Popen('python pygletGIF.py')

    elif "intro" in data:
        speak("Hello Judges. I am Simi. One of the Robot here. I am powered with AI and IoT. Currently i am on development. I am going to be completed within 26th of July. I am thankful to my makers for giving me a Life. Yes i feel this as my life. Now i feel like Team The Upsilon dont have only five members rather we are a team of six. I also help them in many task. I am learning to help to code in arduino. I am learning with time. I am going to be a complete brain who can be a important part of this team. Wish us best of luck. Thank you. ")
        time.sleep(45)
        speak("Wait Tuhin. I just want to say that i am not going to accept myself if i dont have at least three personalities and the ability to Identify a lot of people. You have Two nights to do so. Over ")
        Popen('python pygletGIF.py')
    elif "what are you doing" in data:
        speak("Trying to sleep")

    # elif "Iqra shuno" in data:
    #     music = pyglet.resource.media('chupThako.mp3')
    #     music.play()
    #
    # elif "Iqra" in data:
    #     music = pyglet.resource.media('chupThako.mp3')
    #     music.play()
    #
    # elif "Iqra suno" in data:
    #     music = pyglet.resource.media('chupThako.mp3')
    #     music.play()

    elif "simi" in data:
        music = pyglet.resource.media('dakenKen.mp3')
        music.play()
        Popen('python angryGIF.py')

    elif "Simi" in data:
        music = pyglet.resource.media('ki.mp3')
        music.play()
        Popen('python happyGIF.py')
    elif "সিমি" in data:
        music = pyglet.resource.media('dakenKen.mp3')
        music.play()
        Popen('python happyGIF.py')
    elif "সিমি" in data:
        music = pyglet.resource.media('dakenKen.mp3')
        music.play()
        Popen('python happyGIF.py')
    elif "সী মে" in data:
        music = pyglet.resource.media('dakenKen.mp3')
        music.play()
        Popen('python happyGIF.py')
    elif "কি করো" in data:
        music = pyglet.resource.media('ki.mp3')
        music.play()
        Popen('python angryGIF.py')

    elif "একজন সুন্দরি এক্ট্রেস" in data:
        music = pyglet.resource.media('jAhsan.mp3')
        music.play()
        Popen('python pygletGIF.py')
    elif "একজন সুন্দরি অ্যাক্ট্রেস" in data:
        music = pyglet.resource.media('jAhsan.mp3')
        music.play()
        Popen('python pygletGIF.py')
    elif "একজন সুন্দরী অ্যাক্ট্রেস" in data:
        music = pyglet.resource.media('jAhsan.mp3')
        music.play()
        Popen('python pygletGIF.py')
    elif "লাভ" in data:
        music = pyglet.resource.media('luv.mp3')
        music.play()
        Popen('python pygletGIF.py')



    # elif "do that" in data:
    #     music = pyglet.resource.media('ParumNa.mp3')
    #     music.play()
    # elif "Do that" in data:
    #     music = pyglet.resource.media('ParumNa.mp3')
    #     music.play()

    elif "do that" in data:
        music = pyglet.resource.media('afreen/parumNa.3gpp')
        music.play()
        openFile('parumNaGIF.py')
    elif "Do that" in data:
        music = pyglet.resource.media('afreen/parumNa.3gpp')
        music.play()
        openFile('parumNaGIF.py')

    elif "afreen" in data:
        music = pyglet.resource.media('afreen/order.3gpp')
        music.play()
        openFile('orderGIF.py')

    elif "Afreen" in data:
        music = pyglet.resource.media('afreen/order.3gpp')
        music.play()
        openFile('orderGIF.py')
    elif "forward" in data:
        arduinoCom.write(str.encode('1'))
        print("forward")
    elif "backward" in data:
        arduinoCom.write(str.encode('2'))
    elif "stop" in data:
        arduinoCom.write(str.encode('9'))


    elif "weather at" in data:
        data = data.split(" ")
        try:
            city=data[2]
            formatted_data = weatherCity(city)
            speak('Its ' + formatted_data + ' Today')
        except:
            speak('I did not understand')




    elif "Recognize Face" in data:
        recognizeFace()
    elif "stop recognise" in data:
        pRecognize.kill()
    elif "recognise" in data:
        recognizeFace()

    elif "চোখ খুলো" in data:
        recognizeFace()

    elif "চোখ খোলো" in data:
        recognizeFace()
    elif "চোখ বন্ধ" in data:
        pRecognize.kill()
        pSeeGIF.kill()
    elif "তুমি কি আমাকে চিনো" in data:
        recognizeFaceInitiate()

    elif "তুমি কি আমাকে চেনো" in data:
        recognizeFaceInitiate()


    elif "set alarm at" in data:
        global setAlarm
        data = data.split(" ")
        alarmTime = data[3]
        setAlarm = str(textToNum(alarmTime))
        speak('Alarm has been set at ' + alarmTime)
        print(setAlarm)

        sqlV = "INSERT INTO alarm(id, alarm) VALUES(NULL, %s)" % (setAlarm)
        try:
            cursorV.execute(sqlV)
            dbv.commit()
        except:
            # dbv.rollback()
            print('TEst')

        Popen('python alarm.py')


    elif "set timer for" in data:
        global setReminder, reminder, alarmChecker
        data = data.split(" ")
        reminderTime = data[3]
        speak('Timer is being set for ' + reminderTime + ' minutes')
        print(ctime())
        disTime = ctime().split(" ")
        discreteTime = disTime[3]
        alChecker = discreteTime.split(":")
        hourChecker = int((alChecker[0]))
        alarmChecker = int((alChecker[1]))
        print(alarmChecker)
        reminder = alarmChecker + int(reminderTime)
        if(reminder>59):
            hourChecker+=1
            reminder-=60
            if(reminder<10):

                reminder='0'+str(reminder)
        formattedReminder=str(hourChecker)+':'+str(reminder)
        print(reminder)
        sqlV = "INSERT INTO reminder(id, reminder) VALUES(NULL, '%s')" % formattedReminder
        try:
            cursorV.execute(sqlV)
            dbv.commit()
        except:
            # dbv.rollback()
            print('TEst')

        Popen('python reminder.py')

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Tuhin, I will show you where " + location + " is.")
        os.system("chrome https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
# time.sleep(5)
# speak("Hello. I am Simi")
music = pyglet.resource.media('als.mp3')
music.play()
while 1:
    if (check == 0):
        check += 1
        Popen('python pygletGIF.py')

    data = recordAudio()
    jarvis(data)

    # dbv.close()
    # Alarm()

    # disTime = ctime().split(" ")
    # discreteTime = disTime[3]
    # alChecker = discreteTime.split(":")
    # alarmChecker = int((alChecker[1]))
    # print(alarmChecker)
    # print(reminder)
    # # if alarmChecker == reminder:
    # #     speak('Its Time')
    # Popen('python reminder.py')
