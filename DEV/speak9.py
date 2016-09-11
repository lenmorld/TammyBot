import subprocess
from gtts import gTTS

audio_file = "hello.mp3"
tts = gTTS(text='Hello. Good morning. Blippp.', lang='en')
tts.save(audio_file)
return_code = subprocess.call(["omxplayer", '-o', 'local', audio_file])
print(return_code)
