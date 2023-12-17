import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Miss JPS : Good Morning Boss")
        speak("Good Morning BOSS")
    elif hour>=12 and hour<17:
        print("Miss JPS : Good Afernoon Boss")
        speak("Good Afternoon BOSS")
    elif hour>=17 and hour<21:
        print("Miss JPS : Good Evening Boss")
        speak("Good Evening BOSS")
    else :
        print("Miss JPS : Good Night Boss")
        speak("Good Night BOSS")


def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("wait for few moment..")
        query=r.recognize_google(audio, language='en-in')
        print(f"you just said: {query}\n")
    except Exception as e:
        print(e)
        speak("please repeat again")
        query="none"
    return query



def wakeupcommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Miss JPS is SLEEPING!!..")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print(f'user said : {query}\n')
    except Exception as e:
        query="none"
    return query

if __name__ =="__main__":
    #wishings()
    while True:
        query=wakeupcommand().lower()
        if 'wake up' in query:
            wishings()
            speak("Yes boss , what can i do for you")
            while True:
                query=commands().lower()
                if 'time' in query:
                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strtime)
                    speak(f"sir, the time is {strtime}")

                elif 'open chrome' in query:
                    speak("opening chrome Appliation sir...")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    while True:
                        chromequery = commands().lower()
                        if 'search ' in chromequery:
                            youtubequery=chromequery
                            youtubequery=youtubequery.replace("search","")
                            pyautogui.write(youtubequery)
                            pyautogui.press('enter')
                            speak('searching...')
                        elif 'close chrome' in chromequery or 'close google' in chromequery:
                            pyautogui.hotkey('ctrl','w')
                            speak("closing Google Chrome Sir...")
                            break
                elif ' hello' in query:
                    speak("Hello Boss , i Am here for you")
                elif 'introduce' in query:
                    speak("Hello Dear Humans , I am Miss JPS an AI voice Assistant of jain public school Created by Master Aniked.i have been programed to do task.  ")
                elif 'jarvis' in query:
                    speak("Who is JArvis BOss, I am YOur Miss JPS ")

                elif 'what can you do for me' in query:
                    speak("Yes Sir, Nice question")
                    speak("as per my program , I\'m a bot which can perform tasks through your voice command")
                elif 'cool' in query or ' nice' in query or 'great' in query or 'awesome' in query or 'thank you' in query or 'thank' in query:
                    speak("yes sir, thats my pleasure")
                elif "minimize" in query:
                    speak("minimizing Boss")
                    pyautogui.hotkey('win','down','down')
                elif "maximize" in query:
                    speak("maximizing Boss")
                    pyautogui.hotkey('win', 'up', 'up') 
                elif 'chrome' in query:
                    speak("searhing in chrome...")
                    try:
                        query=query.replace("chrome","")
                        results = wikipedia.summary(query,sentences=5)
                        speak("According to chrome,")
                        print(results)
                        speak(results)
                    except:
                        speak("No result found..")
                        print("No result found..")
                elif 'play' in query:
                    query=query.replace('play','')
                    speak('playing'+query)
                    pywhatkit.playonyt(query)
                elif 'saravanan' in query:
                    query=query.replace('sarvanan','')
                    print('''Principal of Jain Public school and he is a great person''')
                    speak('''Principal of Jain Public school and he is a great person''')

                elif 'joke' in query:
                    joke=pyjokes.get_joke()
                    print(joke)
                    speak(joke)
                elif 'mute' in query:
                    speak("i am Muting Boss..")
                    break

                elif 'exit program' in query or 'exit the program' in query:
                    speak("i am leaving boss,  BYEEE!")
                    quit()

                    