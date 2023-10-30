import random
import pickle
import keyboard


# print(random.randint(entrev[0], entrev[1]));

# Fonction pour créer un nombre caché dans l'intervalle donné
def créer_nombre_caché(entrev):
    return random.randint(entrev[0], entrev[1])


# Fonction pour charger les données des joueurs à partir d'un fichier pickle
def charger_données_joueur():
    try:
        with open('donnees_joueurs.pkl', 'rb') as f:
            données = pickle.load(f)
    except (FileNotFoundError, EOFError):
        données = {}
    return données


# Fonction pour sauvegarder les données des joueurs dans un fichier pickle
def sauvegarder_données_joueur(données):
    with open('donnees_joueurs.pkl', 'wb') as f:
        pickle.dump(données, f)


# Fonction pour jouer une partie
def jouer_partie(entrev, pseudo):
    nombre_caché = créer_nombre_caché(entrev)
    # print(nombre_caché)
    essais_restants = 5

    print(f"Bonjour, {pseudo}! Bienvenue au jeu du nombre caché. Vous avez 5 essais.")

    while essais_restants > 0:
        try:
            guess = int(input(f"Entrez un nombre entre {entrev[0]} et {entrev[1]} : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess < nombre_caché:
            print("Désolé, le nombre que vous avez saisi est trop bas.")
        elif guess > nombre_caché:
            print("Désolé, le nombre que vous avez saisi est trop élevé.")
        else:
            score = essais_restants * 30
            print(f"Bravo, vous avez gagné! Le nombre caché était {nombre_caché}. Votre score est de {score} points.")
            return score

        essais_restants -= 1
        print(f"Essais restants : {essais_restants}")

    print(f"Désolé, vous avez perdu. Le nombre caché était {nombre_caché}.")
    return 0


# Fonction principale du jeu
def jeu_du_nombre_caché():
    données_joueurs = charger_données_joueur()

    while True:
        pseudo = input("Entrez votre pseudo : ")
        if pseudo not in données_joueurs:
            données_joueurs[pseudo] = 0

        score_partie = jouer_partie((0, 50), pseudo)
        données_joueurs[pseudo] += score_partie

        print(f"Score total de {pseudo} : {données_joueurs[pseudo]} points")

        sauvegarder_données_joueur(données_joueurs)

        continuer = input("Voulez-vous continuer à jouer ? (Oui/Non) : ")
        if continuer.lower() != "oui":
            print(f"Au revoir, {pseudo}! Votre score total est de {données_joueurs[pseudo]} points.")
            break


# Détecter la touche "K" pour arrêter le jeu
keyboard.add_hotkey('k', lambda: exit())

# Lancer le jeu
if __name__ == "__main__":
    jeu_du_nombre_caché()