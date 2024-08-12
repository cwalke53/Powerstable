while True:
    # Enters a number to create a table of powers
    number = int(input("Enter a number: "))

    print("Number", " ", "Squared", " ", "Cubed")

    for number in range(1, number + 1):
        print(number, " " * 6, number * number, " " * 7, number ** 3)
    # ask the user if they would like to continue
    keep_going = input("Would you like to continue? Y/N: ")
    # check users response
    if keep_going == "y":
        continue
    elif keep_going == "n":
        print("Thanks for playing.")
        break
    else:
        print("Try again")
        break
    # Multiplication table

number = int(input("Enter a number to create a times table: "))

print(" " * 5, "1", " " * 6, "2", " " * 7, "3", " " * 8, "4")
print(" " * 5, "_", " " * 6, "_", " " * 7, "_", " " * 8, "_")
for num in range(1, number + 1):

    print(num, "|", " ", num * 1, " " * 6, num * 2, " " * 6, num * 3, " " * 7, num * 4)