import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib  #this module is used used to send an email

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")

    elif hour>=12 and hour<18:
        print("Good Afternoon")

    else:
        print("Good Night")

    speak("Hi I'm Jarvis, Please tell me that how I can help you")

def takeCommand():   # it will take the input from the user and return the output as string

    r=sr.Recognizer()   #it will help to recognize the audio
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold=1  # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        # print(e)

        print("say it again please.......")
        return "None"
    return query

def read_password_from_file(filename='password.txt'): # fuction to read the password from the text file
    try:
        with open(filename, 'r') as file:
            password = file.read().strip()
            return password
    except FileNotFoundError:
        print(f"Password file '{filename}' not found.")
        return None

def sendEmail(to, content):   # function to send an email
    password = read_password_from_file('password.txt')

    if password:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('kajalprashar278@gmail.com', password)
            server.sendmail('kajalprashar278@gmail.com', to, content)
            server.close()
            print("Email has been sent.")
        except Exception as e:
            print(e)
            print("Sorry! Currently, I'm unable to process your request.")
    else:
        print("No password found. Please set up a password file.")


if __name__=='__main__':  # main Fuction
    wishMe()
    
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'play music' in query:
            music_dir="C:\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            code_path="C:\\Users\\kajal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'send email to Kajal' in query:
            try:
                speak("What should I do?")
                content=takeCommand()
                to='kajalparashar278@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry! Currently I'm unable to process your request.")

        

        