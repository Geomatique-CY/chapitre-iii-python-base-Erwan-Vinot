            ########################################################################
        #                                                                              #
    #                          Credits: Erwan Vinot                                        #
    #                                   Yanis Rafik (ma muse)                              #
        #                                                                              #
            ########################################################################


# Définition de la fonction validate_input pour vérifier l'âge et le nom
def validate_input(age, name):

    # Vérifie si l'âge n'est pas composé de chiffres
    if not age.isdigit():
        return False

    # Vérifie si le nom ne contient pas de caractères spéciaux ou de chiffres
    if not name.isalpha():
        return False

    # Si les deux conditions sont remplies, les données sont valides
    return True



# Définition de la fonction demo_xor pour la démonstration de XOR
def demo_xor(age, name):

    # Vérifie la validité des données d'entrée en utilisant la fonction de validation
    if not validate_input(age, name):
        print("Merci d'écrire ton âge en chiffres et ton nom en lettres.")
        return

    # Convertit l'âge en un nombre entier
    age = int(age)

    # Vérifie si l'utilisateur est éligible (âge >= 18)
    if age >= 18:
        print("Bienvenue " + name + "! Tu es éligible pour une démonstration de XOR en Python.")
        print("")
        print("XOR en Python : a ^ b")
        print("")

        # Liste de valeurs booléennes (True = 1, False = 0)
        un_zero = [1, 0]

        # Effectue toutes les combinaisons possibles de XOR et affiche les résultats
        for a in un_zero:
            for b in un_zero:
                result = a ^ b
                print(f"{a} XOR {b} = {result}")
        print("")

    else:
        # Message si l'utilisateur n'est pas éligible en raison de son âge
        print("Désolé " + name + ", tu n'es pas éligible. Tu dois avoir au moins 18 ans pour avoir une démonstration de XOR en Python.")
        print("")

# Fonction d'initialisation qui demande à l'utilisateur son âge et son nom
def ini():

    print("Bienvenue sur la démonstration de l'opérateur XOR en Python")
    print("")

    user_age = input("Entre ton âge : ")
    user_name = input("Entre ton prénom : ")
    
    # call la fonction de démonstration de XOR avec les données de l'utilisateur
    demo_xor(user_age, user_name)

# call la fonction d'initialisation pour démarrer le programme
ini()