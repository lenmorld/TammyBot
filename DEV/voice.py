#import pyttsx
#engine = pyttsx.init()
#engine.say('Good night.')
#engine.runAndWait()

from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg221 good.mp3")
