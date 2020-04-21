from gtts import gTTS
import os

text1 = 'Tamil'
language = 'en'

obj = gTTS(text=text1, lang=language, slow=True)

obj.save("Tamil_Slow.mp3")

os.system("start Tamil_Slow.mp3")
