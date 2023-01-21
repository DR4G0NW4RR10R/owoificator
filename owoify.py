import json
from random import random
  
with open("settings.json", "r") as f:
    settings = json.load(f)

with open("keylog.txt","r") as f:
    text = f.read()

text = text.split()

out = []

for word in text:
    if random() < settings["wordFrequency"]:
        if settings["replaceOw"]:
            word = word.replace("ow","owo")
        if settings["replaceFer"]:
            word = word.replace("fer","fu§")
            word = word.replace("Fer","fu§")
        if settings["replaceFor"]:
            word = word.replace("for","fu§")
            word = word.replace("For","Fu§")
        if random() < settings["replaceL"]:
            word = word.replace("l","w")
            word = word.replace("L","W")
        if random() < settings["replaceR"]:
            word = word.replace("r","w")
            word = word.replace("R","W")
        word = word.replace("§","r")
    if "." in word and random() < settings["uwuFrequency"]:
        if random() < settings["replaceUwuWithOwo"]:
            word = word.replace(".", " owo.")
        else:
            word = word.replace(".", " uwu.")
    
    out.append(word)
print(" ".join(out))
with open("keylog.txt","w") as f:
    f.write(" ".join(out))