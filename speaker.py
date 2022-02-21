import pyttsx3

speaker=pyttsx3.init()

word=speaker.say('Hello,world!')

speaker.runAndWait()