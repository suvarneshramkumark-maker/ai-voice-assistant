import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        speak("You said " + command)
    except:
        print("Sorry, could not understand")
        speak("Sorry, could not understand")