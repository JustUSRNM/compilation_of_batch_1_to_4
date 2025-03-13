from collections import Counter

number_list = []
while True:
    try:
        inputted_number = int(input("Please enter a number "))
        number_list.append(inputted_number)
    except ValueError:
        duplicates_counter = Counter(number_list)
        most_duplicates = max(duplicates_counter, key=duplicates_counter.get)
        print (most_duplicates)
        break