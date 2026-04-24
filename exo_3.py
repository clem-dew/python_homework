from random import randint

VALUES = ["pierre", "papier", "ciseaux"]

def game():
    choice = int(input("Choisis un chiffre entre 1 et 3 : "))

    while choice > 3 or choice < 1:
        choice = int(input("Ton chiffre doit être 1, 2 ou 3 : "))

    random_choice = randint(1, 3)
    user_choice = VALUES[choice - 1]
    pc_choice = VALUES[random_choice - 1]

    if choice == random_choice:
        print("Vous : " + user_choice + " | PC : " + pc_choice + " | Egalité")
    elif (choice == 1 and random_choice == 3) or (choice == 2 and random_choice == 1) or (choice == 3 and random_choice == 2):
        print("Vous : " + user_choice + " | PC : " + pc_choice + " | Vous avez gagné 🏆")
    else:
        print("Vous : " + user_choice + " | PC : " + pc_choice + " | Vous avez perdu ... 😒")

start_game = game()