
from random import randint

def sum_user_numbers():
    numb_list = []
    result = 0
    count = 1

    n = int(input("Choisis un nombre de chiffres à faire apparaitre. Ta réponse doit se situer entre 2 et 5 : "))
    while n > 5 or n < 2:
        n = int(input("Le nombre de chiffres doit se trouver entre 2 et 5 : "))

    for _ in range(n):
        random_number = randint(0,20)
        numb_list.append(random_number) 
        result += random_number 

    user_result = int(input(f"Quelle est la somme de tous tes nombres {numb_list} ? " ))
    
    while user_result != result:
        user_result = int(input(f"Malheureusement, ta réponse n'est pas correcte 😒 Essaye encore {numb_list} : "))
        count += 1
    if user_result == result:
        print(f"Yeah ! Tu as trouvé directement 🏆 Tu as trouvé au bout de {count} tentative(s).")

sum_game = sum_user_numbers()
