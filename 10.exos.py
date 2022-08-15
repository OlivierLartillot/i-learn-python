'''this file contains some bugs'''
file = './textes/guest.txt'
    
specials_characters = [",", "!", "?"]
while 1 == 1:
    name = input('Bonjour, dis moi quel est ton nom\n')
    if name == 'q':
        break
    with open(file, "a", encoding='utf-8') as f:
        f.write(f'\n{name}')
        print(f"Merci {name} Je viens de t'enregistrer dans un fichier :p")

#! probleme, il me laisse toujours 1 caractere special dans le lot !!!
with open(file, "r") as f:
    content = f.read()
    words_array = content.split()
    print(f'ceci est le tableau : {words_array}')

    for word in words_array:
        print(f"Le mot {word} est il a supprimer ?")
        if word in specials_characters:
            print(f"Oui, {word} est à supprimer")
            words_array.remove(word)
            print(f'ceci est le tableau apres pop {words_array}')
        else:
            print(f'{word} n est pas un mot à supprimer')
            print(f'ceci est le tableau {words_array}')

    number_words = len(words_array)
    print(f"Le nombre de mots est environ de {number_words}")

