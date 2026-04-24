numbers_list = [1, 2, ]
i = 0

length_list = int(input("De quelle longueur doit être la liste ? "))
if length_list <= 1:
    length_list = int(input("Ta réponse doit être supérieure à 1 : "))

for _ in range(length_list - 2):
    next_number = numbers_list[i] + numbers_list[i + 1]
    numbers_list.append(next_number)
    i += 1

print(numbers_list)