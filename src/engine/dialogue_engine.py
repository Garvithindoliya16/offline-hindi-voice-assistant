from speaker import speak
from stt import listen
from intent import predict_intent
from number_parser import extract_number

print("System Ready")

# -------- INTENT --------
speak("नमस्ते")
while True:
    speak("आप क्या करना चाहते हैं")
    print("Listening for intent...")
    text = listen()
    print("User:", text)

    intent = predict_intent(text)
    print(intent)
    if intent in ["deposit","withdraw","balance","passbook","open_account"]:
        break
    if intent=="other":
        speak("माफ कीजिये, समझ नहीं आया, कृपया साफ़ बोलिए")
        continue


if intent == "deposit":
    speak("आप पैसे जमा करना चाहते हैं")
else:
    speak("आप पैसे निकालना चाहते हैं")

# -------- NAME --------
while True:
    speak("कृपया अपना पूरा नाम बताइए")
    print("Listening for intent...")
    name = listen()
    print("name: ",name)
    if len(name) > 2:
        break
    speak("नाम सही नहीं है, कृपया फिर से बोलिए")

# -------- ACCOUNT --------
while True:
    speak("कृपया खाता नंबर बताइए")
    print("Listening for intent...")
    raw = listen()
    print("raw: ",raw)
    account = extract_number(raw)
    print("account: ", account)
    if account.replace(" ", "").isdigit():
        break
    speak("खाता नंबर सही नहीं है, कृपया फिर से बोलिए")

# -------- AMOUNT --------
while True:
    if intent == "deposit":
        speak("कितनी राशि जमा करनी है")
    else:
        speak("कितनी राशि निकालनी है")
    print("Listening for intent...")
    raw = listen()
    amount = extract_number(raw)
    print("amount: ", amount)
    if amount.replace(" ", "").isdigit():
        break
    speak("राशि सही नहीं है, कृपया फिर से बोलिए")

# -------- PHONE --------
while True:
    speak("आपका मोबाइल नंबर बताइए")
    print("Listening for intent...")
    raw = listen()
    phone = extract_number(raw)
    print("phone: ", phone)
    if phone.replace(" ", "").isdigit():
        break
    speak("मोबाइल नंबर सही नहीं है, कृपया फिर से बोलिए")

speak("धन्यवाद, आपकी पर्ची तैयार है")

print("\nFINAL DATA")
print("Intent:", intent)
print("Name:", name)
print("Account:", account)
print("Amount:", amount)
print("Phone:", phone)




