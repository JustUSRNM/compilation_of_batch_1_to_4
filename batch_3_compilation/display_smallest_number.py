smallest_number= None
while True:
    try:
        inputted_number = int(input("Please enter a number "))
        if  smallest_number is None or inputted_number < int(smallest_number) :
            smallest_number = int(inputted_number)
    except ValueError:
        print (smallest_number)
        break   