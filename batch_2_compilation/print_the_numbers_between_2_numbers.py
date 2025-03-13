first_number = int(input("Please enter a number "))
second_number = int(input("Please enter another number "))

if first_number > second_number:
    greater_number = first_number
    lesser_number = second_number
elif second_number > first_number:
    greater_number = second_number
    lesser_number = first_number

current_number = greater_number - 1
while current_number != lesser_number:
    print (current_number)
    current_number -= 1
