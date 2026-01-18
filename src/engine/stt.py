import pyaudio, json, time
from vosk import Model, KaldiRecognizer
from intent import predict_intent
# model = Model("models/vosk-hi")
model = Model("models/vosk-model-small-hi-0.22")

def listen():
    time.sleep(0.3)
    rec = KaldiRecognizer(model,16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())['text']
            stream.stop_stream()
            stream.close()
            mic.terminate()
            return text
