from speaker import speak
from stt import listen
from intent import predict_intent
from number_parser import extract_number

import time

class Engine:
    def __init__(self):
        self.intent = None
        self.name = None
        self.account = None
        self.amount = None

        # hardcoated values
        self.WITHDRAW = "withdraw"
        self.DEPOSIT = "deposit"

    
    def getIntent(self):
        while True :
            print("getIntent")
            time.sleep(0.5)
            speak("आप क्या करना चाहते हैं")
            print("Listening for intent...")
            text = listen()
            print("User:", text)

            self.intent = predict_intent(text)
            print(self.intent)
            if self.intent in ["deposit","withdraw","balance","passbook","open_account"]:                
                
                if self.intent == "deposit":
                    speak("आप पैसे जमा करना चाहते हैं")
                else:
                    speak("आप पैसे निकालना चाहते हैं")

                break
            else:
                self.intent = None
                speak("माफ कीजिये, समझ नहीं आया, कृपया साफ़ बोलिए")
                continue

        
    
    def getName(self):
        # while True :
            speak("कृपया अपना पूरा नाम बताइए")
            print("Listening for name...")
            name = listen()
            print("name: ",name)
            if len(name) > 2:
                self.name = name
                return True
            else:
                speak("नाम सही नहीं है, कृपया फिर से बोलिए")
                return False
        
    def getAccount(self):
        while True:
            speak("कृपया खाता नंबर बताइए")
            print("Listening for account...")
            raw = listen()
            account = extract_number(raw)
            print("account: ", account)
            if account.replace(" ", "").isdigit():
                self.account = account
                return True
            else:
                speak("खाता नंबर सही नहीं है, कृपया फिर से बोलिए")
                return False
        
    def getAmount(self):
        while True:
            if self.intent == "deposit":
                speak("कितनी राशि जमा करनी है")
            else:
                speak("कितनी राशि निकालनी है")
            print("Listening for amount...")
            raw = listen()
            amount = extract_number(raw)
            print("amount: ", amount)
            if amount.replace(" ", "").isdigit():
                self.amount = amount
                return True
            else : 
                speak("राशि सही नहीं है, कृपया फिर से बोलिए")
                return False

    def print(self):
        print(self.intent)
        print(self.name)
        print(self.account)
        print(self.amount)

    
# engine = Engine()

# engine.getIntent()
# engine.getName()
# engine.getAccount()
# engine.getAmount()
# engine.print()