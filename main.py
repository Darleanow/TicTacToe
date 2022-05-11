from random import choice
print("""                                                               BONJOUR ET BIENVENUE !!!!

Voici comment le jeu se déroulera :
    -Tu choisiras de commencer ou pas
    -Tu écrira X ou O quand ce sera ton tour
    -la grille ressemblera a ça : [ ][ ][ ]
                                  [ ][ ][ ]
                                  [ ][ ][ ]
""")
place=0
vainqueur=""
grille_jeu={7:[" "],4:[" "],1:[" "],8:[" "],5:[" "],2:[" "],9:[" "],6:[" "],3:[" "]}
class jeu:
    flag="False"
class user:
    name=""
    tour=""
    def __init__():
        choix_user=int(input("Choisissez :"))
        available_possibilities.remove(choix_user)
        grille_jeu[choix_user].clear()
        grille_jeu[choix_user].append(user.tour)
class bot:
    name="Bot"
    tour=""
    def choice_ordi():
        return choice(available_possibilities) 
    def __init__():
        choix=bot.choice_ordi()
        print(f"Le bot a choisi {choix}")
        available_possibilities.remove(choix)
        grille_jeu[choix].clear()
        grille_jeu[choix].append(bot.tour)
def grille():
    print(f"{grille_jeu[7]}{grille_jeu[8]}{grille_jeu[9]}")
    print(f"{grille_jeu[4]}{grille_jeu[5]}{grille_jeu[6]}")
    print(f"{grille_jeu[1]}{grille_jeu[2]}{grille_jeu[3]}")

def check():
    global vainqueur
    if grille_jeu[1]== ["X"]  and grille_jeu[2]== ["X"]  and grille_jeu[3]== ["X"]  or grille_jeu[4]== ["X"]  and grille_jeu[5]== ["X"]  and grille_jeu[6]== ["X"]  or grille_jeu[7]== ["X"]  and grille_jeu[8]== ["X"]  and grille_jeu[9]== ["X"]  or grille_jeu[1]== ["X"]  and grille_jeu[4]== ["X"]  and grille_jeu[7]== ["X"]  or grille_jeu[2]== ["X"]  and grille_jeu[5]== ["X"]  and grille_jeu[8]== ["X"]  or grille_jeu[3]== ["X"]  and grille_jeu[6]== ["X"]  and grille_jeu[9]== ["X"] or grille_jeu[7]== ["X"] and grille_jeu[5]== ["X"] and grille_jeu[3]== ["X"] or grille_jeu[9]== ["X"] and grille_jeu[5]== ["X"] and grille_jeu[1]== ["X"] :
        if user.tour=="X":
            vainqueur=user.name
        else:
            vainqueur=bot.name
        jeu.flag="True"

    elif grille_jeu[1]== ["O"] and grille_jeu[2]== ["O"] and grille_jeu[3]== ["O"] or grille_jeu[4]== ["O"] and grille_jeu[5]== ["O"] and grille_jeu[6]== ["O"] or grille_jeu[7]== ["O"] and grille_jeu[8]== ["O"] and grille_jeu[9]== ["O"] or grille_jeu[1]== ["O"] and grille_jeu[4]== ["O"] and grille_jeu[7]== ["O"] or grille_jeu[2]== ["O"] and grille_jeu[5]== ["O"] and grille_jeu[8]== ["O"] or grille_jeu[3]== ["O"] and grille_jeu[6]== ["O"] and grille_jeu[9]== ["O"] or grille_jeu[7]== ["O"]  and grille_jeu[5]== ["O"] and grille_jeu[3]== ["O"] or grille_jeu[9]== ["O"] and grille_jeu[5] and grille_jeu[1]== ["O"] :
        if user.tour=="O":
            vainqueur=user.name
        else:
            vainqueur=bot.name
        jeu.flag="True"
    
user.name=input("Rentres ton prénom pour commencer -->")
print("\n")
user.tour=input(f"D'accord {user.name}, Maintenant choisis si tu veux etre les X ou les O -->").upper()
if user.tour=="X":
    user.tour="X"
    bot.tour="O"
else:
    user.tour="O"
    bot.tour="X"
def game():
    global available_possibilities
    available_possibilities=[1,2,3,4,5,6,7,8,9]
    print(available_possibilities)
    grille()
    while jeu.flag=="False":
        if user.tour=="X":
            user.__init__()
            grille()
            bot.__init__()
            grille()
            check()
            print([i for i in available_possibilities],sep=" ")
            
        else:
            bot.__init__()
            grille()
            print([i for i in available_possibilities],sep=" ")
            user.__init__()
            grille()
            check()
    print(f"Le vainqueur est {vainqueur}")

game()


