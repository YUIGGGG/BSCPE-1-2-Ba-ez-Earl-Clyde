with open("numbers_to_double_and_triple.txt", "r") as the_square_and_cube:
    with open("double.txt", "w") as double_output:
        for line in the_square_and_cube:
            number = int(line.strip())
            squared_number = number ** 2
            double_output.write(f"{squared_number}\n")
        print("Doubled numbers are written to double.txt")

    with open("triple.txt", "w") as triple_output:
        the_square_and_cube.seek(0)
        for line in the_square_and_cube:
            number = int(line.strip())
            cubed_number = number ** 3
            triple_output.write(f"{cubed_number}\n")
        print("Tripled numbers are written to triple.txt")

print("Doubled numbers:")
with open("double.txt", "r") as double_file:
    for line in double_file:
        print(line.strip())

# Read and display the contents of triple.txt
print("\nTripled numbers:")
with open("triple.txt", "r") as triple_file:
    for line in triple_file:
        print(line.strip())
