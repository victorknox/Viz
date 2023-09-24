# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
from playsound import playsound



def read_str(readthis):

    if os.path.exists("vizproject.mp3"):
        os.remove("vizproject.mp3")
    
    myobj = gTTS(text=readthis, lang='en', slow=False)
    myobj.save("vizproject.mp3")

    #mac
    #os.system("afplay vizproject.mp3")

    #windows
    #os.system("ffmpeg vizproject.mp3")


    playsound('vizproject.mp3')
    #linux
    #os.system("vizproject.mp3")

