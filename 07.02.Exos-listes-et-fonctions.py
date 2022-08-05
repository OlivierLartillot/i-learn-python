#Exercices

## transmettre une liste de messages à une fonction show_messages
messages = ["coucou c'est nous", "Bonjour à vous", "Les françcaises parlent aux français"]


def show_messages(messages):
    '''renvoie les messages d'une liste en argument'''
    print("\nVoici la liste des messages qui ont été envoyé")
    for message in messages:
        print(f"- {message}")

show_messages(messages)

## Utiliser une deuxieme fonctions
print("\nDeux fonctions :\n\t- La première envoie les messages\n\t- La deuxième affiche la liste des messages envoyés les messages\n")
send_messages = ["coucou c'est nous", "Bonjour à vous", "Les françcaises parlent aux français"]
sent_messages = []

def send(liste_d_envoi, envoye):
    while liste_d_envoi:
        message_to_send = liste_d_envoi.pop()
        print(f"Ce message est en cours d'envoi:\n\t{message_to_send}")
        envoye.append(message_to_send)

# Pour conserver la liste de bases utiliser send_messages[:] (tranche, copie)
send(send_messages, sent_messages)
show_messages(sent_messages)

print(f"la liste des messages a envoyé est maintenant = a : {send_messages}")

