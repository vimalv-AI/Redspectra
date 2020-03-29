from gtts import gTTS
import os
a = 35
tts = gTTS(text="The Current Temperature Is ,Less Then 18 Degree Celsius, Cooling State)", lang='en')
tts.save("tmpc.mp3")
os.system("mpg321 tmpc.mp3")
