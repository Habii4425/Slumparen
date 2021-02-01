klader = [
    "Jeansbyxor med vit t-shirt, Svart hoody och bumber jacka.", 
    "Svarta byxor med vithoody och Peak jacka.", 
    "Tygbyxor med tygtröja och klassik jacka."
    ]
t-shirt = [
    "svart hoody",
    "vit tröja med bumber jacka",
    ""
]
skor = [
        "Vita",
        "Svarta",
        "Röda"
    ]
Halsband = [
    "Guld",
    "Silver"
]
Klocka = [
    "Guld",
    "Silver"
]



dag = 0
dagar = ["måndag","tisdag","onsdag","torsdag","fredag"]


import random

for i in range(0, 5):
    kladerval = random.randint(0, len(klader)-1)
    skorval = random.randint(0, len(skor)-1)

    print(f"{dagar[dag].capitalize()}")
    print(f"Dagens Kläder: {klader[kladerval]}")
    print(f"Dagens Skor: {skor[skorval]}")
    print(f"{dagar[i].upper()}: {klader[kladerval]} med {skor[skorval]} skor\n")
    dag += 1
    if klader == 

