import random

with open("the_line.txt", "r") as the_lines:
    read_lines = the_lines.readlines()
    print(random.choice(read_lines))

    while True:
        asking_the_user = input("Do you want another quote line? (Y/N): ")
        if asking_the_user.upper() == "Y":
            print(random.choice(read_lines))
        elif asking_the_user.upper() == "N":
            print("Thank you!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
