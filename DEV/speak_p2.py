from gtts import gTTS
blabla = ("Spoken textd daasdsadasasd dasdsa")
tts = gTTS(text=blabla, lang="en")
tts.save('test.mp3')
