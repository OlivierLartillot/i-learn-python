# error
try:
    x = 10/0
except:
    print("Tu ne peux pas diviser un nommbre par 0")
else:
    print(x)

# file not found
file = "fichier_manquant.txt"
try:
    with open(file,"r") as f:
        content = f.read()
except FileNotFoundError:
    print("Ce fichier n'existe pas")
else:
    print(content)

# Exception silencieuse avec pass
file = "fichier_manquant.txt"
try:
    with open(file,"r") as f:
        content = f.read()
except FileNotFoundError:
    pass
else:
    print(content)