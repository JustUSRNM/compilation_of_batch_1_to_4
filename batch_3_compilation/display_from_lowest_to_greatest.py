number_list = []
while True:
    try:
        inputted_number = int(input("Please enter a number "))
        number_list.append(inputted_number)
    except ValueError:
        number_list.sort()
        print (number_list)
        break