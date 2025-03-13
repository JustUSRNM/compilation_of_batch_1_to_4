number_list=[]

while True:
    try:
        inputted_number = int(input("Please enter a number "))
        number_list.append(inputted_number)
    except ValueError:
        average = sum(number_list)/len(number_list)
        print (int(average))
        break