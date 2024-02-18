# Write python code which prompts the user to enter a number between 0 and 10 (include 10), validates the input, if the input is invalid display invalid number and prompt the user to enter a number between 0 and 10, and displays You entered #, once the number is valid.

number = 0 
number = int(input("enter a number between 0 and 10: "))

while number <= 0 or number > 10:
    print("Invalid number")
    number = int(input("enter a number between 0 and 10: "))
    if number <= 0 or number > 10:
        print("Invalid Number")
        number = 0
        number = int(input("enter a number between 0 and 10:"))
    else:
        print("you entered", number)
    break
