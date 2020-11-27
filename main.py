import speech_recognition as sr
import os
from googletrans import Translator
from gtts import gTTS 
import os
from playsound import playsound
def autotranslate(sourcelang, destlang):
    translator = Translator()
    r = sr.Recognizer()
    file = "file.mp3"
    harvard = sr.AudioFile('OSR_us_000_0010_8k.wav')
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("say anything: ") 
        audio = r.listen(source)
    print("Speech Recognized")   
    b = r.recognize_google(audio, language = sourcelang)
    try:
        x = translator.translate(b)
        speech = gTTS(text = x.text, lang = destlang, slow = False)
        speech.save("text.mp3")
        playsound('text.mp3')
    except:
        print("There was an error. Please try again.")
autotranslate("Es", "En")