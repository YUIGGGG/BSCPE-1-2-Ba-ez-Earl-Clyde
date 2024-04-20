def even_numbers(number):
    return number % 2 == 0

with open("numbers.txt", "r") as the_integers:
    for line in the_integers:
        number = int(line.strip())
        if even_numbers(number):
            print("The even numbers are", number)
        else:
            print("The odd numbers are", number)
