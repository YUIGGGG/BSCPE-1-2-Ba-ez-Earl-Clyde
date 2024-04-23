
def even_numbers(number):
    return number % 2 == 0


with open("numbers.txt", "r") as the_integers:
    with open("even.txt", "w") as even_output:
        with open("odd.txt", "w") as odd_output:
            for line in the_integers:
                number = int(line.strip())
                if even_numbers(number):
                    print("The even numbers are", number)
                    even_output_numbers = number
                    if number:
                        even_output.write("Even\n")
                else:
                    print("The odd numbers are", number)
                    if number:
                        odd_output.write("Odd\n")