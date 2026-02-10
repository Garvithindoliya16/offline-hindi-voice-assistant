import pyttsx3, time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)

    voices = engine.getProperty('voices')
    print(voices)
    # for v in voices:
    #     if "hindi" in v.name.lower() or "hi-in" in v.id.lower():
    #         engine.setProperty('voice', v.id)
    #         print(v.id)
    #         break
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM")

    engine.say(text)
    engine.runAndWait()
    # time.sleep(0.3)

if __name__ == "__main__":
    speak("आप क्या करना चाहते हैं")

# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM