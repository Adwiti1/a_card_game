import speech_recognition as sr
import pyaudio

# Initialize the recognizer
my_recognizer = sr.Recognizer()

#my_recognizer.recognize_google()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
   audio = my_recognizer.record(source)