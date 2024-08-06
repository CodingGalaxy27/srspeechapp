from django.shortcuts import render
from django.http import  HttpResponse
import pyttsx3
import speech_recognition as sr
import pyaudio

# Create your views here.
def  speech(request):
            
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Function to speak text
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Function to recognize speech
        def recognize_speech():
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                try:
                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I did not understand that.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

        # Speak "Hello World"
        speak("Hello World")

        # Recognize speech and repeat it
        recognized_text = recognize_speech()
        if recognized_text:
            speak(f"You said: {recognized_text}")


            


