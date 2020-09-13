from gtts import gTTS
import os
Text=input()
language='en'
obj=gTTS(text=Text,lang=language,slow=True)
obj.save('text.mp3')
os.system("text.mp3")
