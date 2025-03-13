inputted_number = [int(input("Enter a number ")) for i in range(10)]

used_numbers=set()
list_of_numbers = []

for individual_number in inputted_number:
    if individual_number not in used_numbers:
        list_of_numbers.append(individual_number)
        used_numbers.add(individual_number)

print (list_of_numbers)