inputted_number = [int(input("Enter a number ")) for i in range(10)]

times_inputted = {}
for individual_number in inputted_number:
    times_inputted[individual_number] = times_inputted.get(individual_number, 0) + 1

unique_numbers = [individual_number for individual_number in inputted_number if times_inputted[individual_number]==1]

print (unique_numbers)