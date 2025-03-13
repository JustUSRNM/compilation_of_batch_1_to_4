used_numbers = set()

while True:
    try:
        inputted_number = int(input("Please enter a number "))
        if inputted_number not in used_numbers:
            print ('Unique')
            used_numbers.add(inputted_number)
        else:
            print ('duplicate')
    except ValueError:
        break