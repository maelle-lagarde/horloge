import time

heures = 0
minutes = 0
secondes = 0
heure = (heures, minutes, secondes)
heures_alarme = 0
minutes_alarme = 0
secondes_alarme = 0

menu = """
+-------------+
1. Mode 24h
2. Mode 12h
3. Quitter
+-------------+
"""

# afficher heure 24.
def affiche_heure_24(heures, minutes, secondes):
    while True:
        print("\nHORLOGE > renseignez une heure : ")
        heures = int(input("Entrez les heures : "))
        if heures >= 24 or heures < 0:
            heures = int(input("Entrez des heures valides : "))

        minutes = int(input("Entrez les minutes : "))
        if minutes >= 60 or minutes < 0:
            minutes = int(input("Entrez des minutes valides : "))

        secondes = int(input("Entrez les secondes : "))
        if secondes >= 60 or secondes < 0:
            secondes = int(input("Entrez des secondes valides : "))
        break

    # système incrémentation 24.
    while True:
        if secondes == 59:
            secondes = 00
            minutes += 1
        else:
            secondes += 1

        if minutes == 60:
            minutes = 00
            heures += 1

        if heures == 24:
            heures = 00

        heure = (heures, minutes, secondes)

        # Affichage de l'heure :
        print("\r", "%02d" % (heures,), ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), end="")

        time.sleep(1)  # maj de l'heure toutes les secondes avant de reprendre la boucle.

        alarme = alarme_24(heures_alarme, minutes_alarme, secondes_alarme)

        if alarme == heure:
            print("\nDriiiiiing !!!")

# afficher heure 12.
def affiche_heure_12(heures, minutes, secondes):
    print("\nHORLOGE > renseignez une heure : ")
    heures = int(input("Entrez les heures : "))
    while heures >= 12 or heures < 0:
        heures = int(input("Entrez des heures valides : "))

    minutes = int(input("Entrez les minutes : "))
    while minutes >= 60 or minutes < 0:
        minutes = int(input("Entrez des minutes valides : "))

    secondes = int(input("Entrez les secondes : "))
    while secondes >= 60 or secondes < 0:
        secondes = int(input("Entrez des secondes valides : "))

    # système incrémentation 12.
    while True:
        if secondes == 59:
            secondes = 00
            minutes += 1
        else:
            secondes += 1

        if minutes == 60:
            minutes = 00
            heures += 1

        if heures == 12:
            heures = 00

        heure = (heures, minutes, secondes)

        time.sleep(1)  # maj de l'heure toutes les secondes avant de reprendre la boucle.

        alarme = alarme_12(heures_alarme, minutes_alarme, secondes_alarme)

        if alarme == heure:
            print("\nDriiiiiing !!!")

# régler alarme en mode 24.
def alarme_24(heures_alarme, minutes_alarme, secondes_alarme):
    while True:
        print("\nALARME > renseignez une heure : ")
        heures_alarme = int(input("Entrez les heures : "))
        if heures_alarme >= 24 or heures_alarme < 0:
            heures_alarme = int(input("Entrez des heures valides : "))

        minutes_alarme = int(input("Entrez les minutes : "))
        if minutes_alarme >= 60 or minutes_alarme < 0:
            minutes_alarme = int(input("Entrez des minutes valides : "))

        secondes_alarme = int(input("Entrez les secondes : "))
        if secondes_alarme >= 60 or secondes_alarme < 0:
            secondes_alarme = int(input("Entrez des secondes valides : "))
        break

    print("\r", "%02d" % (heures_alarme,), ":", "%02d" % (minutes_alarme,), ":", "%02d" % (secondes_alarme,), end="")

# régler alarme en mode 12.
def alarme_12(heures_alarme, minutes_alarme, secondes_alarme):
    print("\nALARME > renseignez une heure : ")
    heures_alarme = int(input("Entrez les heures : "))
    while heures_alarme >= 12 or heures_alarme < 0:
        heures_alarme = int(input("Entrez des heures valides : "))

    minutes_alarme = int(input("Entrez les minutes : "))
    while minutes_alarme >= 60 or minutes_alarme < 0:
        minutes_alarme = int(input("Entrez des minutes valides : "))

    secondes_alarme = int(input("Entrez les secondes : "))
    while secondes_alarme >= 60 or secondes_alarme < 0:
        secondes_alarme = int(input("Entrez des secondes valides : "))

    print("\r", "%02d" % (heures_alarme,), ":", "%02d" % (minutes_alarme,), ":", "%02d" % (secondes_alarme,), end="")

# mettre en pause l'horloge.
def pause():
    print("L'horloge est en pause.")
    reprendre = input("Voulez-vous relancer l'horloge ? répondre par 'Oui' ou 'Non' : ")
    if reprendre == "Oui":
        main()
    else:
        main()

# menu principal.
def main():
    print(menu)
    print("Choisissez votre option : ")
    choice = input("> ")
    if choice == "1":
        affiche_heure_24(heures, minutes, secondes)
        alarme_24(heures_alarme, minutes_alarme, secondes_alarme)
    elif choice == "2":
        affiche_heure_12(heures, minutes, secondes)
        alarme_12(heures_alarme, minutes_alarme, secondes_alarme)
    elif choice == "3":
        print("Bye bye !")
    else:
        print("Choix invalide.")

main()