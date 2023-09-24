# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os



def read_str(readthis):
    myobj = gTTS(text=readthis, lang='en', slow=False)
    myobj.save("vizproject.mp3")
    os.system("afplay vizproject.mp3")


