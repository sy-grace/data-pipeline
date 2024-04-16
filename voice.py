from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from util import time_generator
import time

def tts(txt, filename, lan='ko'):
    tts = gTTS(
        text = txt,
        lang = lan, slow = False
    )
    voice_file = f'./data/{filename}_{time_generator()}.mp3'
    tts.save(voice_file)
    time.sleep(1)
    playsound(voice_file)

def stt(lan='ko'):
    Recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = Recognizer.listen(source)
    try:
        data = Recognizer.recognize_google(audio, language=lan)
    except:
        err = "Sorry. I didn't understand. Please try again."
        print(err)
        tts(err, "stt_err")
    return data