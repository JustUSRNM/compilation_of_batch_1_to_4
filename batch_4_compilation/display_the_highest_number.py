highest_number= None
while True:
    try:
        inputted_number = int(input("Please enter a number "))
        if  highest_number is None or inputted_number > int(highest_number) :
            highest_number = int(inputted_number)
    except ValueError:
        print (highest_number)
        break   