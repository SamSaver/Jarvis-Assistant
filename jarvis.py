#! /usr/bin/env python3

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import time as tf
import pyautogui
import shelve
import psutil
import pyjokes
import json, requests
import random
import calendar
import pywhatkit as kit

#Global variables
i=0
voice_property = 'com.apple.speech.synthesis.voice.karen'

def speak(speech, voice_property):
    engine = pyttsx3.init()
    engine.setProperty('voice',voice_property)
    engine.say(speech)
    engine.runAndWait()

# speak("This is jarvis A.I. Assistant")
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S%p")
    timeString = "Current time is "+ time
    return timeString

def date():
    year = str(datetime.datetime.today().year)
    month = str(datetime.datetime.today().month)
    day = str(datetime.datetime.today().day)
    dateString = "Today's date is: " + day + "," + month + "," + year
    return dateString

def wishme():
    info = date()+" and "+time()
    speak("Welcome Sir! " + info, voice_property)
    hour = datetime.datetime.now().hour
    if voice_property == 'com.apple.speech.synthesis.voice.karen':
        name = 'Friday'
    else:
        name = 'Jarvis'
    greet = ""
    if hour >= 6 and hour < 12:
        greet = "Good Morning sir! "
    elif hour >= 12 and hour < 18:
        greet = "Good Afternoon sir! "
    elif hour >= 18 and hour <24:
        greet = "Good Evening sir! "
    else:
        greet = "Why are you awake so late at night sir?"
    speak(greet + f"{name} at your service. Please tell me how can I help you ?", voice_property)

def takeCommand():
    recognizer = sr.Recognizer()

    print('Listening...')
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again please.", voice_property)
            return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('riemeltm@gmail.com',"vlhftsabujujofvn")
    server.sendmail('riemeltm@gmail.com', to, content)
    server.close()

def screenshot():
    global i
    i += 1
    pyautogui.screenshot().save('/Users/samarthsinghpawar/Desktop/ss'+ str(i) +'.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('C.P.U is at ' + usage, voice_property)
    battery_percent,secs, is_plugged  = psutil.sensors_battery()
    speak(' Battery percentage is ' + str(battery_percent) + ' and ' + str(round((int(secs)/3600),2)) + ' hours are left.   Plug in status is ' + str(is_plugged), voice_property)

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j, voice_property)

def weather(location):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=107aaa207a0a45998a0829cef92379e3&units=metric")
    response.raise_for_status()
    pythonValue = json.loads(response.text)
    print("Today's Weather Report is:")
    print(f"Temperature: {pythonValue['main']['temp']}")
    print(f"Description: {pythonValue['weather'][0]['description']}")
    speak(f"Today's Weather Report is as follows: Temperature is: {pythonValue['main']['temp']} Description is: {pythonValue['weather'][0]['description']}", voice_property)

def magicBallGame():
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    print(r'  __  __          _____ _____ _____    ___  ')
    print(r' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
    print(r' | \  / |  /  \ | |  __  | || |      | (_) |')
    print(r' | |\/| | / /\ \| | |_ | | || |       > _ < ')
    print(r' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
    print(r' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
    print('')
    print('')
    print('')
    speak('Welcome, I am the Magic 8 Ball, What is your name?', voice_property)
    name = takeCommand()
    while name == 'None':
        name = takeCommand()
    speak('hello ' + name, voice_property)
    print('hello ' + name)
    speak('Ask me a question.', voice_property)
    takeCommand()
    result = answers[random.randint(0, len(answers)-1)]
    print (result)
    speak (result, voice_property)
    speak('I hope that helped!', voice_property)
    speak ('Do you have another question ? ', voice_property)
    reply = takeCommand().lower().split()
    while reply == 'None':
        reply = takeCommand().lower().split()
    if 'y' in reply:
        magicBallGame()
    else:
        speak('Thanks! I hope you enjoyed', voice_property)

def camera():
    try:
        subprocess.Popen('open /System/Applications/Photo\ Booth.app', shell=True)
        tf.sleep(5)
        pyautogui.click(743,793)
        speak('Lookin smart Sir!', voice_property)
    except Exception as e:
        print(e)
        speak('Unable to capture photo', voice_property)

if __name__ == "__main__":
    # wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            speak(time(), voice_property)

        elif 'how are you' in query:
            speak("I'm fine. What about you ?", voice_property)

        elif 'hello friday' in query or 'hey friday' in query or 'hello jarvis' in query or 'hey jarvis' in query:
            speak('Hello there, how may I help you ?', voice_property)

        elif 'date' in query:
            speak(date(), voice_property)

        elif 'wikipedia' in query:
            try:
                speak("Searching...", voice_property)
                query = query.replace("wikipedia",'')
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result, voice_property)
            except Exception as e:
                print(e)
                speak('Sorry, Page does not exists', voice_property)

        elif 'send email' in query:
            try:
                speak('To whom you want to send mail', voice_property)
                to = takeCommand().lower()
                to = to.replace(" ","")
                speak('What message you want to send', voice_property)
                content = takeCommand()
                sendEmail(to, content)
                speak('Email successfully sent!', voice_property)
            except Exception as e:
                print(e)
                speak('Unable to send the email', voice_property)

        elif 'search in chrome' in query:
            speak('What would you like to search ?', voice_property)
            search = takeCommand().lower()
            wb.MacOSX('default').open_new_tab("https://www.google.com.tr/search?q={}".format(search))

        #When you're a super user
        # elif 'logout' in query:
        #     os.system("shutdown -l")

        # elif 'restart' in query:
        #     os.system("shutdown /r /t 1")

        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t 1")

        elif 'spotify' in query:
            subprocess.Popen('open /Applications/Spotify.app/', shell=True)
            tf.sleep(5)
            # pyautogui.click(743,793)
            # pyautogui.doubleClick(743,793)
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')

        elif 'youtube' in query:
            speak('Please tell the youtube video title', voice_property)
            title = takeCommand()
            kit.playonyt(title)
            speak('Here you Go!', voice_property)

        elif 'remember this thing' in query:
            speak("What do you want me to remember ?", voice_property)
            data = takeCommand()
            speak('What is the key for this memory ?', voice_property)
            key = takeCommand().lower()
            shelfFile = shelve.open('myMemory')
            shelfFile[key] = data
            shelfFile.close()
            speak('Data Noted Sir!', voice_property)


        elif 'remember something' in query:
            shelfFile = shelve.open('myMemory')
            speak('The keys for your memory are ' + '  '.join(shelfFile.keys())+ '  Do you want me to search the memory keys for you ?', voice_property)
            res = takeCommand().lower()
            if res == 'yes':
                speak('Yes Sir. Tell me the key', voice_property)
                key = takeCommand().lower()
                speak('You told me to remember that ' + shelfFile[key], voice_property)
            else:
                speak('Alright sir !', voice_property)
            shelfFile.close()

        elif 'clear memory' in query:
            shelfFile = shelve.open('myMemory')
            shelfFile.clear()
            shelfFile.close()
            speak('Done Sir.', voice_property)

        elif 'screenshot' in query:
            screenshot()
            speak('Done Sir.', voice_property)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'weather' in query:
            speak('Please tell me the location: ', voice_property)
            try:
                location = takeCommand()
                weather(location)
            except Exception as e:
                print(e)
                speak(f'Unable to fetch details for {location}', voice_property)

        elif 'magic ball' in query:
            magicBallGame()

        elif 'capture' in query:
            camera()
        
        elif 'calendar' in query:
            speak('Do you want me to show you full year calendar or this month ?', voice_property)
            res = takeCommand().lower()
            if 'full' in res:
                speak("Here's your result.", voice_property)
                print(calendar.prcal(datetime.datetime.today().year))
            elif 'month' in res:
                speak("Here's your result.", voice_property)
                print(calendar.prmonth(datetime.datetime.today().year, datetime.datetime.today().month))
            else:
                speak("Couldn't get it", voice_property)

        elif 'change assistant' in query:
            if voice_property == 'com.apple.speech.synthesis.voice.karen':
                voice_property = 'com.apple.speech.synthesis.voice.Alex'
                speak("Hello there, I'm Jarvis at your service.", voice_property)
            else:
                voice_property = 'com.apple.speech.synthesis.voice.karen'
                speak("Hello there, I'm Friday at your service.", voice_property)
        elif 'offline' in query:
            speak('Have a good Day Sir. ', voice_property)
            quit()
