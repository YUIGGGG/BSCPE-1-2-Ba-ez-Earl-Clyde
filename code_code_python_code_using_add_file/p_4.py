#hi

with open("numbers_to_double_and_triple.txt", "r") as the_square_and_cube:
    with open("double.txt", "w") as double_output:
        with open("triple.txt", "w") as triple_output:
            for line in the_square_and_cube:
                number = int(line.strip())
                if even_numbers(number):
                    number = int(number ** 2)
                    print("The doubled number is", number)
                    double_output_numbers = number
                    if number:
                        double_output.write("Even\n")
                else:
                    print("The odd numbers are", number)
                    if number:
                        number = int(number ** 3)
                        odd_output.write("Odd\n")