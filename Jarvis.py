import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import time
import pyjokes
import sys
import requests, json
import pywhatkit
import wolframalpha
import urllib.request
 
 
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def weather(city):
    # Enter your API key here
    api_key = "67ea885767696169650db19aaebab5a7"
 
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
    # Give city name
    city_name = city
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
 
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
 
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]
 
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
 
        # store the value corresponding
        # to the "pressure" key of y
        # current_pressure = y["pressure"]
 
        # store the value corresponding
        # to the "humidity" key of y
        # current_humidiy = y["humidity"]
 
        # store the value of "weather"
        # key in variable z
        # z = x["weather"]
 
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        # weather_description = z[0]["description"]
        return str(current_temperature)
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
 
    else:
        speak("Good Evening!")
 
    speak("Hello I am your friend jarvis. I am here to help you")
 
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
 
def takeCommand():
    #It takes microphone input from the user and returns string output
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
 
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Is there a problem, sir")
        return "None"
    return query
 
 
if __name__ == "__main__":
 
    wishMe()
    username()
    while True:
 
        query = takeCommand().lower()
 
        # Logic for executing tasks based on query
        
        if 'who is your creator' in query or 'created' in query:
            speak('Mr Purvak Baliyan, Mr Yash Dewan and Mr Shivansh Sharma is my creator ')
        
        elif 'who is' in query:
            speak('Searching Wikipedia...')
            command = query.replace("who is", "")
            results = wikipedia.summary(command,2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
 
        elif 'what can you do' in query:
            speak('Hello Master, thank you for using me I am your virtual assistant I can help you with a lot of things like'
                  'searching, playing music, opening google, telling the time and weather, and many more too.')
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
 
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif 'play' in query:
            song = query.replace('play' , '')
            speak('playing'+song)
            speak('Is my work done, Sir')
            out = takeCommand()
            pywhatkit.playonyt(song)
            if 'yes' in out or 'Yup' in out:
                sys.exit()
 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Is my work done, Sir')
            if 'Yes' in query or 'Yup' in query:
                speak('ok thak you master')
                sys.exit()
 
        elif 'open google' in query:
            webbrowser.open("google.com")
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
 
        elif "wait" in query or "pause" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            speak('time off')
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you Sir")
 
        elif 'i am fine' in query or "i am good" in query:
            speak("It's good to know that your fine")
 
        elif 'who are you' in query:
            speak("I am a Virtual assistant created by maddy for his project in college")
 
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
 
        elif "what is" in query:
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("XJUXHL-EJ76AJTPUU")
            res = client.query(query)
 
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
 
        elif "love" in query:
          pywhatkit.playonyt('Love is a Waste Of Time | PK | Whatsapp Status | #shorts')
 
        elif "search for" in query:
            query =query.replace("search", "")
            webbrowser.open(query)
 
        elif 'joke' in query:
            speak(pyjokes.get_joke())
 
        elif 'weather' in query:
            speak('Please tell name of city')
            city = takeCommand()
            weather_api = weather(city)
            speak(weather_api + 'degree fahrenheit')
 
        elif 'news' in query:
 
            query_params = {
                "source": "bbc-news",
                "sortBy": "top",
                "apiKey": "63d3e5a050fd41e88f72e53695cd9401"
            }
            main_url = " https://newsapi.org/v1/articles"
 
            # fetching data in json format
            res = requests.get(main_url, params=query_params)
            open_bbc_page = res.json()
 
            # getting all articles in a string article
            article = open_bbc_page["articles"]
 
            # empty list which will
            # contain all trending news
            results = []
 
            for ar in article:
                results.append(ar["title"])
 
            for i in range(len(results)):
                # printing all trending news
                print(i + 1, results[i])
 
            # to read the news out loud for us
            from win32com.client import Dispatch
 
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak(results)

        elif 'stop' in query or 'shutdown' in query:
            speak('shutting down, Thanks for your time')
            sys.exit()
 

    else:
            speak("Sorry did not get that")