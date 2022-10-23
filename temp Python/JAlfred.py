import speech_recognition as sr
import pyttsx3
import pyautogui as ms
import time as t
import sounddevice as sd
from scipy.io.wavfile import write
import pyjokes as jk
from AppOpener import run
from selenium import webdriver
import os
import webbrowser as web

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.1)
    audio = r.listen(source)
    
    MyText = r.recognize_google(audio)
    MyText = str(MyText.lower())
    
    try: 
        if MyText == "education":
          SpeakText('school mode activated')
          run("google chrome")
          t.sleep(1)
          ms.moveTo(864, 65)
          ms.click()
          ms.write("https://webcourses.ucf.edu/")
          t.sleep(1)
          ms.press('enter')
          
        elif MyText == "gamer":
          SpeakText('going gamer mode')
          run("steam")
          t.sleep(1)
          run("discord")
          run("league of legends")
          
        elif MyText == "covert ops":
            SpeakText('going ninja mode')
            c = webdriver.ChromeOptions()
            c.add_argument("--incognito")
            driver = webdriver.Chrome(executable_path="C:\\Users\\natha\\Documents\\chromedriver.exe", options=c)
            driver.implicitly_wait(0.5)
            driver.get("https://www.google.com/")
            
        elif MyText == "gas prices":
          SpeakText('pulling up gassed up')
          web.open_new_tab("http://127.0.0.1:5001")
          
        else:
            SpeakText('opening ' + MyText)
            run(MyText)
            
    except Exception as e:
        print("Error: " + str(e))
    

    