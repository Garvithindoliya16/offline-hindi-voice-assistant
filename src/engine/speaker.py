import pyttsx3, time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)

    voices = engine.getProperty('voices')
    for v in voices:
        if "hindi" in v.name.lower() or "hi-in" in v.id.lower():
            engine.setProperty('voice', v.id)
            break

    engine.say(text)
    engine.runAndWait()
    # time.sleep(0.3)
