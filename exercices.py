import os      # pour clear le terminal
from termcolor import colored, cprint
import random  # pour l'exo 10

##########################################################################################################################################
#                                                           Début Exercices                                                              #
##########################################################################################################################################

#Exercice 1
def ex1(stringas,lettre):
    incr = 0 # nombre de lettre correspondante 
    for index, caractere in enumerate(stringas):  # index = numéro de 
        if caractere == lettre:
            print(colored(f"le caractère n°{index+1} est un {caractere}","green"))
            incr += 1 
    if incr == 0 :
        print(colored(f"\nPas de '{lettre}' à l'horizon !","red")) 
    depart()


#Exercice 2
def ex2(stringas):
    chaine_modifiee = "*".join(stringas)
    print(colored(f"\nEt voilà :","green")+colored(f"{chaine_modifiee}\n","yellow"))
    depart()


#Exercice 3
def ex3(stringas):
    chaine_inverse = ""
    for caractere in stringas:
        chaine_inverse = caractere + chaine_inverse
    print(colored(f"\nEt voilà : {chaine_inverse}\n","green"))
    depart()


#Exercice 4
def ex4(stringas):
    longueur = len(stringas)
    for i in range(longueur):
        espace = " " * (i * 2)
        partie = stringas[:longueur - i]
        print(espace + partie)
    print(colored("\nEt voilà !","green")) 
    depart()


#Exercice 5
def ex5(numbas):
    for i in range(1, numbas+1):
        resultat = i * 7
        if resultat % 3 == 0:
            colored(print(resultat, end="* "),"green")
        else:
            print(resultat, end=" ")
    print(colored("\nEt voilà ! ","green"))       
    depart()


#Exercice 6
def ex6(numbas):
    prompt = input(colored("Prix hors taxes? (€) : ","blue"))
    prompt=prompt.replace(",",".") # POUR LES FR qui utilisent des virgules lol

    reduc={
        "1":1.2,
        "2":1.1,
        "3":1.055,
        "4":1.021,
    }

    if is_float(prompt) :
        prix = float(prompt)
        if str(numbas) in reduc.keys():
            print(colored(f"\nTaux de TVA à {round((reduc[str(numbas)] %1)*100,3)} % - Le prix TTC est ","green")+colored(f"{round(prix*reduc[str(numbas)],3)} €","yellow")+colored("\nEt voilà !","green"))
        elif numbas==5:
            print(colored(f"\nTaux de TVA entre 2,1 et 20% - Le prix TTC est","green")+colored(f" entre {round(prix*1.021,3)} et {round(prix*1.20,3)} €","yellow")+colored("\nEt voilà !","green"))
        
    else:
        print(colored("Merci d'entrer un prix en chiffres.","red"))
        ex6(numbas)
    depart()


#Exercice 7
def ex7(numbas):
    dt={"1": {"name":"Euro","symbol":"€"},"2": {"name":"Dollar (USD)","symbol":"$"}}
    money = float(input (f'{dt[str(numbas)]["name"]} ({dt[str(numbas)]["symbol"]}) : '))
    print(colored(f'\nEn  {dt["1" if numbas==2 else "2"]["name"]  }: {round(money*1.06,3) if numbas==1 else  round(money*1/1.06,3)}{dt["1" if numbas==2 else "2"]["symbol"]}\nEt voilà !'))
    depart()


#Exercice 8
def ex8(numbas):
    fibo = [0,1]
    for i in range (0, numbas):
        print (fibo[i])
        fibo.append(fibo[i]+fibo[i+1])
    print(colored("\nEt voilà ! ","green"))
    depart()


#Exercice 9
def ex9(stringas):
    resultat = liquidation(float(stringas))
    for nom, quantite in resultat.items():
        print(f"{round(quantite)} x {nom}")
    print(colored("\nEt voilà !","green"))  
    depart()

def liquidation(somme):
    decompose = {}
    dictio_liquide = {
        500: "Billet de 500€",200: "Billet de 200€",100: "Billet de 100€",50: "Billet de 50€",20: "Billet de 20€",10: "Billet de 10€",5: "Billet de 5€",
        2: "Pièce de 2€",1: "Pièce de 1€",0.5: "Pièce de 0.50€",0.2: "Pièce de 0.20€",0.1: "Pièce de 0.10€",0.05: "Pièce de 0.05€",0.02: "Pièce de 0.02€",0.01: "Pièce de 0.01€"}

    for valeur, nom in dictio_liquide.items():
        if somme >= valeur:
            quantite = somme // valeur
            somme -= quantite * valeur
            decompose[nom] = quantite
    return decompose


#Exercice 10
def ex10(choix_joueur):
       
    min_range = 1
    max_range = 100
    coups = 0
    
    while True:
        coups += 1
        nombre_propose = random.randint(min_range, max_range)
        reponse = input(colored(f"Je propose {nombre_propose}... +, - ou GG ? ","purple"))
        
        if reponse == "+":
            min_range = nombre_propose + 1
        elif reponse == "-":
            max_range = nombre_propose - 1
        elif reponse == "GG":
            if nombre_propose == choix_joueur:
                print(colored(f"\nJ'ai trouvé {choix_joueur} en {coups} coups ! \nEt voilà ! ","green"))
                depart()
                return
                break
            else:
                print(colored("\nBruh ! La réponse précédente était incorrecte.","orange"))
                depart()
                return
                break
        else:
            print(colored("Veuillez répondre avec '+', '-', ou 'GG'.","red"))

##########################################################################################################################################
#                                                           Fin Exercices                                                                #
##########################################################################################################################################


# Opti
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def input_int(msg):
    while True:
        user_input = input(msg)
        if user_input.isnumeric():
            if int(user_input) <= 10000:
                return int(user_input)
            elif int(user_input) > 10000 :
                print(colored("\nMerci d'utiliser un nombre inférieur ou égal à 10.000","red"))
        else:
            print(colored("\nJe veux un NOMBRE ENTIER !\n","red"))

def feedback(choix_menu):
    return "\n\nExercice " + choix_menu + " sélectionné. \n"


# Menu principal
def choix_exo (choice:str):
    if choice == "1":
        print(feedback(choice))
        texte = input(colored("Entrez un mot ou une phrase pour la recherche : ","blue"))
        symbole = input(colored("Entrez un symbole à rechercher (une lettre ou un chiffre) : ","blue"))
        if len(symbole) == 1 :
            ex1(texte,symbole)
        else :
            print(colored("Merci de n'entrer qu'un seul symbole","red"))
            choix_exo("1")

    elif choice == "2":
        print(feedback(choice))
        ex2(input(colored("Entrez un mot ou une phrase à remplir d'astérisques : ","blue")))

    elif choice == "3":
        print(feedback(choice))
        ex3(input(colored("Entrez du texte à inverser : ","blue")))

    elif choice == "4":
        print(feedback(choice))
        ex4(input(colored("Entrez un mot ou une phrase à pyramider (lol) : ","blue")))

    elif choice == "5":
        print(feedback(choice))
        ex5(input_int(colored("Entrez le nombre de multiples de 7 à vérifier si ils sont également multiples de 3 (nombre entier) : ","blue")))

    elif choice == "6":
        print(feedback(choice))
        code = input_int("Code 1 : Boissons alcoolisées. Confiserie, chocolat et produits chocolatés, etc. Publications interdites aux mineurs.\nCode 2 : Restauration et vente de produits alimentaires/boissons sans alcool à consommation immédiate. Produits pour l’alimentation animale. Sites culturels. Hébergement. Rénovation d’un logement. Transports. Médicaments non remboursables.\nCode 3 : Cantines. Boissons sans alcool et eau à emporter. Chocolat. Produits alimentaires préparés. Ventes d’œuvres d’art. Billetterie de spectacles. Livres. Autotests VIH. Préservatifs. Protection menstruelle.\nCode 4 : Animaux vivants de boucherie et de charcuterie. Billetterie des spectacles vivants. Contribution à l’audiovisuel public. Publications de presse CPPAP. Médicaments remboursables.\nCode 5 : Je ne sais pas.\n\nEntrez le code produit pour calculer son prix TTC (nombre entier) : ")
        if code == 1 or code == 2 or code == 3 or code == 4 or code == 5 :
            ex6(code)
        else :
            print(colored("\nMerci d'entrer un code entre 1 et 5 (entier)","red")) 
            choix_exo("6")

    elif choice == "7":
        print(feedback(choice))
        code = input_int("1 : Conversion € -> $\n2 : Conversion $ -> €\n\nChoix ? : ")
        if code == 1 or code == 2 :
            ex7(code)
        else :
            print("\nMerci d'entrer 1 ou 2")  
            choix_exo("7")

    elif choice == "8":
        print(feedback(choice))
        ex8(input_int("Entrez le nombre termes dans votre suite de Fibonacci (nombre entier) : "))

    elif choice == "9":
        print(feedback(choice))
        bag = input("Entrez la somme à décomposer en liquide : ").replace(",",".")
        if is_float(bag) and float(bag) > 0:
            ex9(bag)
        else :
            print(colored("\nMerci d'entrer une somme d'argent","red"))  
            choix_exo("9")

    elif choice == "10":
        print(feedback(choice))
        nb = input_int("Entrez un nombre entre 1 et 100, je vais essayer de le retrouver.\nGuidez moi et ne trichez pas ensuite...\nNombre à deviner : ")
        if nb <= 100 and nb >= 1 :
            ex10(nb)
        else :
            print(colored("\nMerci d'entrer un nombre entier entre 1 et 100","red"))
            choix_exo("10")

    elif choice == "help":
        print ("\n\nExplication des exos:\n  •  Exercice 1 : un script qui détermine la ou les positions d'un caractère dans un texte donné (à la base fallait juste dire si le texte contenait 'e').\n  •  Exercice 2 : un script qui recopie une chaîne, en insérant des astérisques entre les caractères.\n  •  Exercice 3 : Un script qui recopie une chaîne en l'inversant.\n  •  Exercice 4 : Un programme qui, à partir d'une chaine quelconque, affiche les caractères de cette chaine sous la forme d’une suite pyramidale.\n  •  Exercice 5 : Un programme qui affiche les n premiers termes de la table de multiplication par 7, en signalant au passage (à l'aide d’un astérisque) ceux qui sont des multiples de 3.\n  •  Exercice 6 : Un programme ou vous devez entrer un prix HT et affichez sa valeur TTC (tous les taux de TVA françaises).\n  •  Exercice 7 : Un programme qui convertit des euro(s) en dollar(s).\n  •  Exercice 8 : Un programme qui fournit la série de Fibonacci pour obtenir les valeurs de n termes.\n  •  Exercice 9 : Une fonction qui décompose une somme d'argent en un minimum de billets et pièces nécessaires pour recomposer ladite somme.\n  •  Exercice 10 : Le joueur choisis un nombre entre 1 et 100 et l'ordinateur essaye de le retrouver. À chaque étape, le joueur indique si le nombre proposé est plus petit ou plus grand que le nombre à trouver.\n\n")
        depart()

    elif choice == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Au revoir !\n\n","blue"))
        return

    else :
        print(colored("\nRecommencez\n","red"))
        depart()

def depart ():
    choix_exo(input(colored("\n\nBienvenue dans les exos de Python! \n\n'help' pour connaitre la nature des exercices. \n'quit' pour quitter.\n\nQuel exercice voulez-vous ? (1 à 10) : ","blue")))


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    depart()
