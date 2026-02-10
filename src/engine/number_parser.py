# word_to_num = {
#     "शून्य":0,"एक":1,"दो":2,"तीन":3,"चार":4,"पाँच":5,"छह":6,"छः":6,"सात":7,"आठ":8,"नौ":9,
#     "दस":10,"ग्यारह":11,"बारह":12,"तेरह":13,"चौदह":14,"पंद्रह":15,"सोलह":16,"सत्रह":17,"अठारह":18,"उन्नीस":19,
#     "बीस":20,"इक्कीस":21,"बाईस":22,"तेईस":23,"चौबीस":24,"पच्चीस":25,"छब्बीस":26,"सत्ताईस":27,"अट्ठाईस":28,"उनतीस":29,
#     "तीस":30,"इकतीस":31,"बत्तीस":32,"तैंतीस":33,"चौंतीस":34,"पैंतीस":35,"छत्तीस":36,"सैंतीस":37,"अड़तीस":38,"उनतालीस":39,
#     "चालीस":40,"इकतालीस":41,"बयालीस":42,"तैंतालीस":43,"चवालीस":44,"पैंतालीस":45,"छियालीस":46,"सैंतालीस":47,"अड़तालीस":48,"उनचास":49,
#     "पचास":50,"इक्यावन":51,"बावन":52,"तिरपन":53,"चौवन":54,"पचपन":55,"छप्पन":56,"सत्तावन":57,"अट्ठावन":58,"उनसठ":59,
#     "साठ":60,"इकसठ":61,"बासठ":62,"तिरसठ":63,"चौंसठ":64,"पैंसठ":65,"छियासठ":66,"सड़सठ":67,"अड़सठ":68,"उनहत्तर":69,
#     "सत्तर":70,"इकहत्तर":71,"बहत्तर":72,"तिहत्तर":73,"चौहत्तर":74,"पचहत्तर":75,"छिहत्तर":76,"सतहत्तर":77,"अठहत्तर":78,"उन्यासी":79,
#     "अस्सी":80,"इक्यासी":81,"बयासी":82,"तिरासी":83,"चौरासी":84,"पचासी":85,"छियासी":86,"सत्तासी":87,"अट्ठासी":88,"नवासी":89,
#     "नब्बे":90,"इक्यानवे":91,"बानवे":92,"बानो":92,"तिरानवे":93,"चौरानवे":94,"पचानवे":95,"छियानवे":96,"सत्तानवे":97,"अट्ठानवे":98,"निन्यानवे":99,
#     "सौ":100,"हजार":1000,"हज़ार":1000,"लाख":100000,"करोड़":10000000
# }

# def extract_number(text):
#     words = text.split()
#     results = []
    
#     total = 0      # Holds the final accumulated number
#     current = 0    # Holds the temporary number before a multiplier (e.g., the '5' in '5 Thousand')

#     for i, w in enumerate(words):
#         if w not in word_to_num:
#             continue
            
#         val = word_to_num[w]

#         # Break detection: Check if we should start a new distinct number
#         # If current word is a base number (<100) and the previous was also a base number
#         if i > 0 and words[i-1] in word_to_num:
#             prev_val = word_to_num[words[i-1]]
#             if val < 100 and prev_val < 100:
#                 results.append(str(total + current))
#                 total = 0
#                 current = 0

#         # Multiplier Logic
#         if val >= 100:
#             if current == 0: current = 1 # Handles cases like "सौ" (One Hundred)
            
#             if val == 100:
#                 # Hundred is usually the last small multiplier, we keep it in current
#                 current *= 100
#             else:
#                 # For Thousand, Lakh, Crore: Multiply and lock into total
#                 total += (current * val)
#                 current = 0
#         else:
#             # It's a base number 0-99
#             current += val

#     # Append the last result
#     if total + current > 0:
#         results.append(str(total + current))
        
#     return " ".join(results)


























# word_to_num = {
#     "शून्य":0,"एक":1,"दो":2,"तीन":3,"चार":4,"पाँच":5,"छह":6,"छः":6,"सात":7,"आठ":8,"नौ":9,
#     "दस":10,"ग्यारह":11,"बारह":12,"तेरह":13,"चौदह":14,"पंद्रह":15,"सोलह":16,"सत्रह":17,"अठारह":18,"उन्नीस":19,
#     "बीस":20,"इक्कीस":21,"बाईस":22,"तेईस":23,"चौबीस":24,"पच्चीस":25,"छब्बीस":26,"सत्ताईस":27,"अट्ठाईस":28,"उनतीस":29,
#     "तीस":30,"इकतीस":31,"बत्तीस":32,"तैंतीस":33,"चौंतीस":34,"पैंतीस":35,"छत्तीस":36,"सैंतीस":37,"अड़तीस":38,"उनतालीस":39,
#     "चालीस":40,"इकतालीस":41,"बयालीस":42,"तैंतालीस":43,"चवालीस":44,"पैंतालीस":45,"छियालीस":46,"सैंतालीस":47,"अड़तालीस":48,"उनचास":49,
#     "पचास":50,"इक्यावन":51,"बावन":52,"तिरपन":53,"चौवन":54,"पचपन":55,"छप्पन":56,"सत्तावन":57,"अट्ठावन":58,"उनसठ":59,
#     "साठ":60,"इकसठ":61,"बासठ":62,"तिरसठ":63,"चौंसठ":64,"पैंसठ":65,"छियासठ":66,"सड़सठ":67,"अड़सठ":68,"उनहत्तर":69,
#     "सत्तर":70,"इकहत्तर":71,"बहत्तर":72,"तिहत्तर":73,"चौहत्तर":74,"पचहत्तर":75,"छिहत्तर":76,"सतहत्तर":77,"अठहत्तर":78,"उन्यासी":79,
#     "अस्सी":80,"इक्यासी":81,"बयासी":82,"तिरासी":83,"चौरासी":84,"पचासी":85,"छियासी":86,"सत्तासी":87,"अट्ठासी":88,"नवासी":89,
#     "नब्बे":90,"इक्यानवे":91,"बानवे":92,"बानो":92,"तिरानवे":93,"चौरानवे":94,"पचानवे":95,"छियानवे":96,"सत्तानवे":97,"अट्ठानवे":98,"निन्यानवे":99,
#     "सौ":100,"सो":100,"हजार":1000,"हज़ार":1000,"लाख":100000,"करोड़":10000000
# }

# # Fraction keywords
# FRACTIONS = {"साढ़े", "ढाई","ढई", "डेढ़", "पौने","पौन"}

# def extract_number(text):
#     words = text.split()
#     results = []

#     total = 0
#     current = 0
#     i = 0

#     while i < len(words):
#         w = words[i]

#         # ---------- FRACTION HANDLING ----------
#         if w == "साढ़े" and i+1 < len(words):
#             base = word_to_num.get(words[i+1], 0)
#             current += base + 0.5
#             i += 2
#             continue

#         if w == "ढाई" or w == "ढई":
#             current += 2.5
#             i += 1
#             continue

#         if w == "डेढ़":
#             current += 1.5
#             i += 1
#             continue

#         if w == "पौने" or w == "पौन" and i+1 < len(words):
#             base = word_to_num.get(words[i+1], 0)
#             current += base - 0.25
#             i += 2
#             continue

#         # ---------- NORMAL WORDS ----------
#         if w not in word_to_num:
#             i += 1
#             continue

#         val = word_to_num[w]

#         # Break detection (multiple numbers in one sentence)
#         if i > 0 and words[i-1] in word_to_num:
#             prev_val = word_to_num[words[i-1]]
#             if val < 100 and prev_val < 100:
#                 results.append(str(int(total + current)))
#                 total = 0
#                 current = 0

#         # Multiplier logic
#         if val >= 100:
#             if current == 0:
#                 current = 1

#             if val == 100:
#                 current *= 100
#             else:
#                 total += int(current * val)
#                 current = 0
#         else:
#             current += val

#         i += 1

#     if total + current > 0:
#         results.append(str(int(total + current)))

#     return " ".join(results)


# word_to_num = {
#     "शून्य":0,"एक":1,"दो":2,"तीन":3,"चार":4,"पाँच":5,"छह":6,"छः":6,"सात":7,"आठ":8,"नौ":9,
#     "दस":10,"ग्यारह":11,"बारह":12,"तेरह":13,"चौदह":14,"पंद्रह":15,"सोलह":16,"सत्रह":17,"अठारह":18,"उन्नीस":19,
#     "बीस":20,"इक्कीस":21,"बाईस":22,"तेईस":23,"चौबीस":24,"पच्चीस":25,"छब्बीस":26,"सत्ताईस":27,"अट्ठाईस":28,"उनतीस":29,
#     "तीस":30,"इकतीस":31,"बत्तीस":32,"तैंतीस":33,"चौंतीस":34,"पैंतीस":35,"छत्तीस":36,"सैंतीस":37,"अड़तीस":38,"उनतालीस":39,
#     "चालीस":40,"इकतालीस":41,"बयालीस":42,"तैंतालीस":43,"चवालीस":44,"पैंतालीस":45,"छियालीस":46,"सैंतालीस":47,"अड़तालीस":48,"उनचास":49,
#     "पचास":50,"इक्यावन":51,"बावन":52,"तिरपन":53,"चौवन":54,"पचपन":55,"छप्पन":56,"सत्तावन":57,"अट्ठावन":58,"उनसठ":59,
#     "साठ":60,"इकसठ":61,"बासठ":62,"तिरसठ":63,"चौंसठ":64,"पैंसठ":65,"छियासठ":66,"सड़सठ":67,"अड़सठ":68,"उनहत्तर":69,
#     "सत्तर":70,"इकहत्तर":71,"बहत्तर":72,"तिहत्तर":73,"चौहत्तर":74,"पचहत्तर":75,"छिहत्तर":76,"सतहत्तर":77,"अठहत्तर":78,"उन्यासी":79,
#     "अस्सी":80,"इक्यासी":81,"बयासी":82,"तिरासी":83,"चौरासी":84,"पचासी":85,"छियासी":86,"सत्तासी":87,"अट्ठासी":88,"नवासी":89,
#     "नब्बे":90,"इक्यानवे":91,"बानवे":92,"बानो":92,"तिरानवे":93,"चौरानवे":94,"पचानवे":95,"छियानवे":96,"सत्तानवे":97,"अट्ठानवे":98,"निन्यानवे":99,
#     "सौ":100,"सो":100,"हजार":1000,"हज़ार":1000,"लाख":100000,"करोड़":10000000
# }

# # Fraction keywords
# FRACTIONS = {"साढ़े", "ढाई","ढई", "डेढ़", "पौने","पौन"}

# def extract_number(text):
#     words = text.split()
#     results = []

#     total = 0
#     current = 0
#     i = 0

#     while i < len(words):
#         w = words[i]

#         # ---------- FRACTION HANDLING ----------
#         if w == "साढ़े" and i+1 < len(words):
#             base = word_to_num.get(words[i+1], 0)
#             current += base + 0.5
#             i += 2
#             continue

#         if w == "ढाई" or w == "ढई":
#             current += 2.5
#             i += 1
#             continue

#         if w == "डेढ़":
#             current += 1.5
#             i += 1
#             continue

#         if (w == "पौने" or w == "पौन") and i+1 < len(words):
#             base = word_to_num.get(words[i+1], 0)
#             current += base - 0.25
#             i += 2
#             continue

#         # ---------- NORMAL WORDS ----------
#         if w not in word_to_num:
#             i += 1
#             continue

#         val = word_to_num[w]

#         # SPECIAL CASE: "सौ पाँच" → 100 5
#         if (w == "सौ" or w == "सो") and current == 0:
#             if i+1 < len(words) and words[i+1] in word_to_num and word_to_num[words[i+1]] < 100:
#                 results.append("100")
#                 total = 0
#                 current = 0
#                 i += 1
#                 continue

#         # Break detection (multiple numbers)
#         if i > 0 and words[i-1] in word_to_num:
#             prev_val = word_to_num[words[i-1]]
#             if val < 100 and prev_val < 100:
#                 results.append(str(int(total + current)))
#                 total = 0
#                 current = 0
#         # SPECIAL CASE: standalone "सौ" at end → 100
#         if (w == "सौ" or w == "सो") and i == len(words) - 1:
#             if total + current > 0:
#                 results.append(str(int(total + current)))
#                 total = 0
#                 current = 0
#             results.append("100")
#             i += 1
#             continue


#         # Multiplier logic
#         if val >= 100:
#             if current == 0:
#                 current = 1

#             if val == 100:
#                 current *= 100
#             else:
#                 total += int(current * val)
#                 current = 0
#         else:
#             current += val

#         i += 1

#     if total + current > 0:
#         results.append(str(int(total + current)))

#     return " ".join(results)












word_to_num = {
    "शून्य":0,"एक":1,"दो":2,"तीन":3,"चार":4,"पाँच":5,"छह":6,"छः":6,"सात":7,"आठ":8,"नौ":9,
    "दस":10,"ग्यारह":11,"बारह":12,"तेरह":13,"चौदह":14,"पंद्रह":15,"सोलह":16,"सत्रह":17,"अठारह":18,"उन्नीस":19,
    "बीस":20,"इक्कीस":21,"बाईस":22,"तेईस":23,"चौबीस":24,"पच्चीस":25,"छब्बीस":26,"सत्ताईस":27,"अट्ठाईस":28,"उनतीस":29,
    "तीस":30,"इकतीस":31,"बत्तीस":32,"तैंतीस":33,"चौंतीस":34,"पैंतीस":35,"छत्तीस":36,"सैंतीस":37,"अड़तीस":38,"उनतालीस":39,
    "चालीस":40,"इकतालीस":41,"बयालीस":42,"तैंतालीस":43,"चवालीस":44,"पैंतालीस":45,"छियालीस":46,"सैंतालीस":47,"अड़तालीस":48,"उनचास":49,
    "पचास":50,"इक्यावन":51,"बावन":52,"तिरपन":53,"चौवन":54,"पचपन":55,"छप्पन":56,"सत्तावन":57,"अट्ठावन":58,"उनसठ":59,
    "साठ":60,"इकसठ":61,"बासठ":62,"तिरसठ":63,"चौंसठ":64,"पैंसठ":65,"छियासठ":66,"सड़सठ":67,"अड़सठ":68,"उनहत्तर":69,
    "सत्तर":70,"इकहत्तर":71,"बहत्तर":72,"तिहत्तर":73,"चौहत्तर":74,"पचहत्तर":75,"छिहत्तर":76,"सतहत्तर":77,"अठहत्तर":78,"उन्यासी":79,
    "अस्सी":80,"इक्यासी":81,"बयासी":82,"तिरासी":83,"चौरासी":84,"पचासी":85,"छियासी":86,"सत्तासी":87,"अट्ठासी":88,"नवासी":89,
    "नब्बे":90,"इक्यानवे":91,"बानवे":92,"बानो":92,"तिरानवे":93,"चौरानवे":94,"पचानवे":95,"छियानवे":96,"सत्तानवे":97,"अट्ठानवे":98,"निन्यानवे":99,
    "सौ":100,"सो":100,
    "हजार":1000,"हज़ार":1000,
    "लाख":100000,"करोड़":10000000
}

def extract_number(text: str) -> str:
    words = text.split()
    results = []

    total = 0
    current = 0
    i = 0

    while i < len(words):
        w = words[i]

        # ---------- FRACTIONS ----------
        if w == "साढ़े" and i+1 < len(words):
            current += word_to_num.get(words[i+1], 0) + 0.5
            i += 2
            continue

        if w in {"ढाई","ढई"}:
            current += 2.5
            i += 1
            continue

        if w == "डेढ़":
            current += 1.5
            i += 1
            continue

        if w in {"पौने","पौन"} and i+1 < len(words):
            current += word_to_num.get(words[i+1], 0) - 0.25
            i += 2
            continue

        # ---------- SKIP UNKNOWN ----------
        if w not in word_to_num:
            i += 1
            continue

        val = word_to_num[w]

        # ---------- STANDALONE सौ ----------
        if w in {"सौ","सो"}:
            # valid multiplier ONLY if prefixed by 1–9
            if 1 <= current <= 9:
                current *= 100
                i += 1
                continue
            else:
                # flush previous number
                if total + current > 0:
                    results.append(str(int(total + current)))
                # add standalone 100
                results.append("100")
                total = 0
                current = 0
                i += 1
                continue

        # ---------- BREAK BETWEEN SMALL NUMBERS ----------
        if i > 0 and words[i-1] in word_to_num:
            prev_val = word_to_num[words[i-1]]
            if val < 100 and prev_val < 100:
                results.append(str(int(total + current)))
                total = 0
                current = 0

        # ---------- THOUSAND / LAKH / CRORE ----------
        if val >= 1000:
            if current == 0:
                current = 1
            total += int(current * val)
            current = 0
        else:
            current += val

        i += 1

    if total + current > 0:
        results.append(str(int(total + current)))

    return " ".join(results)












