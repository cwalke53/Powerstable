while True:
#Enters a number to create a table of powers
    number = int(input("Enter a number: "))

    print("Number", " ", "Squared", " ", "Cubed")

    for num in range(1, number + 1):
        print(number, " " * 6, number * number, " " * 7, number ** 3)
#ask the user if they would like to continue
    keep_going = input("Would you like to continue? Y/N: ")
#check users response
    if keep_going == "y":
        continue
    elif keep_going == "n":
        print("Thanks for playing.")
        break
    else:
        print("Try again")
        break
