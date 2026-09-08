import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty("rate", 150)  # Speed percent (can go over 100)
print("Hello, I am a text-to-speech engine.")

engine.runAndWait()