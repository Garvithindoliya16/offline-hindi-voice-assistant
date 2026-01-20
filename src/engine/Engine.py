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

        # to maintain the state of the speaker
        self.speaking = False 


    # functino to maintain the state of speaker 
    # if not maintained it will throw async error of run loop already running
    # for example 
    # if speaker is already running from getIntent method and again called from getName
    # speaker will need to process to text at a single time which will cause the error 

    def speak(self, text):
        # hold while the speaker is running by the while loop
        # if any functino sets the `self.speaker = False` the while condition will get broken 
        # and hold will be cleared and speaker can be used again 
        while (self.speaking): None 
        # set the speaker is speaking
        self.speaking = True 

        speak(text)

        # set the speaker is free again to break the hold for other uses 
        self.speaking = False 

    
    def getIntent(self):
            print("getIntent")

            self.speak("आप क्या करना चाहते हैं")
        

            print("Listening for intent...")
            text = listen()
            print("User:", text)

            self.intent = predict_intent(text)
            print(self.intent)
            if self.intent in ["deposit","withdraw","balance","passbook","open_account"]:                
                
                if self.intent == "deposit":
                    self.speak("आप पैसे जमा करना चाहते हैं")
                else:
                    self.speak("आप पैसे निकालना चाहते हैं")

                return True
            else:
                self.intent = None
                self.speak("माफ कीजिये, समझ नहीं आया, कृपया साफ़ बोलिए")
                return False

        
    
    def getName(self):
        # while True :
            
            self.speak("कृपया अपना पूरा नाम बताइए")
            
            print("Listening for name...")
            name = listen()
            print("name: ",name)
            if len(name) > 2:
                self.name = name
                return True
            else:
                self.speak("नाम सही नहीं है, कृपया फिर से बोलिए")
                return False
        
    def getAccount(self):
        
            
            self.speak("कृपया खाता नंबर बताइए")
            
            print("Listening for account...")
            raw = listen()
            account = extract_number(raw)
            print("account: ", account)
            if account.replace(" ", "").isdigit():
                self.account = account
                return True
            else:
                self.speak("खाता नंबर सही नहीं है, कृपया फिर से बोलिए")
                return False
    

        
    def getAmount(self):
        # while True:
            if self.intent == self.DEPOSIT: cmd = "कितनी राशि जमा करनी है"
                
            elif self.intent == self.WITHDRAW: cmd = "कितनी राशि निकालनी है"

            self.speak(cmd)

            print("Listening for amount...")
            raw = listen()
            amount = extract_number(raw)
            print("amount: ", amount)
            if amount.replace(" ", "").isdigit():
                self.amount = amount
                return True
            else : 
                self.speak("राशि सही नहीं है, कृपया फिर से बोलिए")
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