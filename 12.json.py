import json

names = ["Olivier", "Estelle","Lucas","Lilie"]

with open("./json/numbers.json","w") as f:
    json.dump(names, f)
try:
    with open("./json/numbers.json") as f:
        names = json.load(f)
except:
    print('Le fichier spécifié est introuvable')
else:
    print(names)