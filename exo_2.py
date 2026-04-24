def multiplication_table():
    table = int(input("Choisis une table : "))
    while table > 10 or table < 1:
        table = int(input("Ton nombre doit être compris entre 1 et 10 : "))
    for n in range(1, 11):
        result = table * n
        print(str(n) + " x " + str(table) + " = " + str(result))

result_table = multiplication_table()