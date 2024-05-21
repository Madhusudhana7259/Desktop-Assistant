import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


a = pyttsx3.init('sapi5')
voi = a.getProperty('voices')
a.setProperty('voice',voi[1].id)

def speak(text):
    a.say(text)
    a.runAndWait()


def takecomm():
    """
        This function recognisez the voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone() as scr:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(scr)

        try:
            print("Recognising")
            tex = r.recognize_google(audio, language="en-in")
            # print(tex)
        
        
        except Exception as e:
            print("Say again")
            return "None"
        return tex

text = takecomm()
speak(text)