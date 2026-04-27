from random import randint

VALUES = ["pierre", "papier", "ciseaux"]

def game():
    print("1 = pierre, 2 = papier, 3 = ciseaux")
    user_choice = int(input("Choisis un chiffre entre 1 et 3 : "))

    while user_choice > 3 or user_choice < 1:
        print("1 = pierre, 2 = papier, 3 = ciseaux")    
        user_choice = int(input("Ton chiffre doit se trouver entre 1 et 3 : "))

    pc_choice = randint(0, 2)
    user_choice -= 1

    message = f"Vous : : {VALUES[user_choice]} | PC : : {VALUES[pc_choice]}"

    if user_choice == pc_choice:
        print(f"{message} | Egalité")
    elif user_choice == 1 and pc_choice == 3 or user_choice == 2 and pc_choice == 1 or user_choice == 3 and pc_choice == 2:
        print(f"{message} | Vous avez gagné 🏆")
    else:
        print(f"{message} | Vous avez perdu ... 😒")

start_game = game()
