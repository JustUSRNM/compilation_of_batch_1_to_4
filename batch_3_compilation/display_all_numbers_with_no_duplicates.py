inputted_number = [int(input("Enter a number ")) for i in range(10)]
print (inputted_number)

times_inpputed = {}
for individual_number in inputted_number:
    times_inpputed[individual_number] = times_inpputed.get(individual_number, 0) + 1

print (times_inpputed)