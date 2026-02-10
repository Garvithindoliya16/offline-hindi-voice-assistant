STOP_WORDS = {
    "मेरा", "मेरी", "मेरे",
    "पूरा", "नाम", "है", "हैं",
    "जी", "का", "की", "से",
    "बताइए", "बताओ", "बताइये"
}

def extract_name(text: str) -> str:
    words = text.strip().split()
    name_words = []

    for w in words:
        if w not in STOP_WORDS:
            name_words.append(w)

    return " ".join(name_words)