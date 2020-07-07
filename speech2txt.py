import speech_recognition as sr
from gtts import tts
import os
import time
import playsound

r=sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say Something... or Say Exit to Quit: ")
        audio = r.listen(source)
        text=r.recognize_google(audio)
        print("You said:    "+text)
        
        if("exit" in text):
            break

print("Thank You")
