
def sum_user_numbers():
    numb_list = []
    result = 0
    count = 1

    n = int(input("Combien de chiffres vas-tu devoir additionner : "))
    while n > 20 or n < 0:
        n = int(input("Ta réponse doit se trouver entre 0 et 20 : "))

    for _ in range(n):
        user_numb = int(input("Choisis un chiffre entre 2 et 5 : "))
        while user_numb > 5 or user_numb < 2:
            user_numb = int(input("Ton chiffre doit se trouver entre 2 et 5 : "))
        numb_list.append(user_numb) 
        result += user_numb  


    user_result = int(input("Quelle est la somme de tous tes nombres " + str(numb_list) + " ? " ))
    
    while user_result != result:
        user_result = int(input("Malheureusement, ta réponse n'est pas correcte 😒 Essaye encore " + str(numb_list) + " : "))
        count += 1
    if user_result == result:
        print("Yeah ! Tu as trouvé directement 🏆 Tu as trouvé au bout de " + str(count) + " tentative(s).")





sum_game = sum_user_numbers()