length_list = int(input("De quelle longueur doit être la liste ? "))

if length_list <= 1:
    length_list = int(input("Ta réponse doit être supérieure à 1 : "))

numbers = "1, 2"
first_number = 1
second_number = 2

for _ in range(length_list - 2):
    next_number = first_number + second_number
    numbers += f", {next_number}"

    first_number = second_number
    second_number = next_number

print(numbers)
