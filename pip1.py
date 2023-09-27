import pyttsx3

engine = pyttsx3.init()
engine.say("This is Text-To-Speech Engine Pyttsx3")
engine.runAndWait()
engine.stop()