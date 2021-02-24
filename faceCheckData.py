''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18

'''

import cv2
import numpy as np
import os
import serial
from gtts import gTTS
import pyglet
from subprocess import Popen
import time
global idCheck
idCheck=0

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    # os.system("mpg321 audio.mp3")
    playPyglet()

def playPyglet():
    music = pyglet.resource.media('audio.mp3')
    music.play()



# from serialCommunication import arduinoCom
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['Unknown', 'Tuhin', 'Tahmid Abir', 'Mahdi', 'W', 'T1', 'T2','Ferdous Vaia', 'Jaya Ahsan Api']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized
#
# as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while (idCheck==0):

    ret, img = cam.read()
    # img = cv2.flip(img, -1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        checkFidence=int(confidence)

        # Check if confidence is less them 100 ==> "0" is perfect match
        # if checkFidence > 0 & checkFidence < 100:
        if checkFidence<100:
                printID= names[id]
                confidence = "{0}%".format(round(100 - confidence))
                # Popen('python speaker.py')
                if(printID=='Ferdous Vaia'):
                    idCheck=1
                elif(printID=='Jaya Ahsan Api'):
                    idCheck=2
            # if(checkFidence<30):
            #     id = "unknown"
            #     confidence = "  {0}%".format(round(100 - confidence))
        else:
            printID = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))


        cv2.putText(img, str(printID), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
if(idCheck==1):
    music = pyglet.resource.media('ferdous.mp3')
    music.play()
    time.sleep(10)
elif(idCheck==2):
    music = pyglet.resource.media('jAhsan2.mp3')
    music.play()
    time.sleep(17)
cam.release()
cv2.destroyAllWindows()