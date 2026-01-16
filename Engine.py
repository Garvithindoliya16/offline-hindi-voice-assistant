from speaker import speak
from stt import listen
from intent import predict_intent
from number_parser import extract_number


class Engine:
    def __init__(self):
        self.intent = None
        self.name = None
        self.account = None
        self.amount = None

    # get the intent of the user and store in self.intent and return boolean value according to results
    def getIntent(self):
        while True :
            speak("आप क्या करना चाहते हैं")
            print("Listening for intent...")
            text = listen()
            print("User:", text)

            intent = predict_intent(text)
            print(intent)
            if intent in ["deposit","withdraw","balance","passbook","open_account"]:
                self.intent = intent
                
                if intent == "deposit":
                    speak("आप पैसे जमा करना चाहते हैं")
                else:
                    speak("आप पैसे निकालना चाहते हैं")

                break
            else:
                speak("माफ कीजिये, समझ नहीं आया, कृपया साफ़ बोलिए")
                continue
        
    # store name in self.name return boolean
    def getName(self):
        while True :
            speak("कृपया अपना पूरा नाम बताइए")
            print("Listening for intent...")
            name = listen()
            print("name: ",name)
            if len(name) > 2:
                self.name = name
                break
            else:
                speak("नाम सही नहीं है, कृपया फिर से बोलिए")
                continue
        
    def getAccount(self):
        while True:
            speak("कृपया खाता नंबर बताइए")
            print("Listening for intent...")
            raw = listen()
            account = extract_number(raw)
            print("account: ", account)
            if account.replace(" ", "").isdigit():
                self.account = account
                break
            else:
                speak("खाता नंबर सही नहीं है, कृपया फिर से बोलिए")
                continue
        
    def getAmount(self):
        while True:
            if self.intent == "deposit":
                speak("कितनी राशि जमा करनी है")
            else:
                speak("कितनी राशि निकालनी है")
            print("Listening for intent...")
            raw = listen()
            amount = extract_number(raw)
            print("amount: ", amount)
            if amount.replace(" ", "").isdigit():
                self.amount = amount
                break
            else : 
                speak("राशि सही नहीं है, कृपया फिर से बोलिए")
                continue

    def print(self):
        print(self.intent)
        print(self.name)
        print(self.account)
        print(self.amount)

    
engine = Engine()

engine.getIntent()
engine.getName()
engine.getAccount()
engine.getAmount()
engine.print()