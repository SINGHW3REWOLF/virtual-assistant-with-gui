from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from AppOpener import run
import os


def main():
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey' in command:
                command = command.replace('hey', '')
                print(command)
            if 'rick' in command:
                command = command.replace('rick', '')
                print(command)
            if 'hirak' in command:
                command = command.replace('hirak', '')
                print(command)

        return command

    def run_rick():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open' in command:
            app = command.replace('open', '')
            talk('opening' + app)
            run(app)
        elif 'name' in command:
            talk('Hello, my name is rick')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'open' in command:
            open = command.replace('open', '')
            talk('opening ' + open)
            pywhatkit.search(open)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'translator' in command:
            talk('opening translator')
            pywhatkit.search('translator')
        elif 'weather' in command:
            talk('searching for weather in your area')
            pywhatkit.search('weather')
        elif 'date' in command:
            date = datetime.date.today()
            talk(date)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'search' in command:
            search = command.replace('search', '')
            talk('searching for', search)
            pywhatkit.search(search)
        elif 'what' in command:
            what = command
            talk('searching for it')
            pywhatkit.search(what)
        elif 'say' in command:
            say = command.replace('say', '')
            talk(say)
        elif 'se' in command:
            se = command.replace('se', '')
            talk(se)
        elif 'shutdown' in command:
            talk('shutting system down in 30 seconds')
            os.system("shutdown /s")
        elif 'shutdown now' in command:
            talk('shutting system down')
            os.system("shutdown /s /t")
        elif 'restart' in command:
            talk('restarting system in 30 seconds')
            os.system("shutdown /r")
        elif 'log out' in command:
            talk('logging out, bye have a great day')
            os.system("shutdown -l")
        elif 'thank you' in command:
            talk('Its my pleasure to serve you')
        elif 'thanks' in command:
            talk('Its my pleasure to serve you')
        elif 'do' in command:
            talk('I serve as a virtual assistant to angad')
        else:
            talk(
                'I do not have any answers for that. would you like to search it on the internet?')
            elsestate = command
            if 'yes' in command:
                pywhatkit.search(elsestate)
            else:
                talk('Could you repeat what you said?')

    while True:
        run_rick()


root = Tk()

root.geometry('200x200')

root.title('Virtual Assistant')

root.configure(background='black')

root.iconbitmap("D:\Angad\icon.ico")

lbl = Label(root, text='Virtual Assistant', font='Lato', background='white')

lbl.pack()

btn = Button(root, text='Start', bd='5', background='white',
             command=main)

btn.pack(pady=20)

btn = Button(root, text='Stop', bd='5', background='white',
             command=root.destroy)

btn.pack(side='bottom')

root.mainloop()
