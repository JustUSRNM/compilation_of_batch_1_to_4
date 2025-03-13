while True:
    try:
        inputted_number = int(input("Please enter a number "))
    except ValueError:
        break