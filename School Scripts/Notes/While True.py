def get_valid_number():
    while True:
        try:
            number = int(input("Please enter a number between 0 and 10 (inclusive): "))
            if 0 <= number <= 10:
                return number
            else:
                print("Invalid number. Please enter a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program
if __name__ == "__main__":
    valid_number = get_valid_number()
    print("You entered:", valid_number)
