def get_valid_number():
    while True:
         try:
             number = int(input("Please Enter the Number Between 0 to 10 (inclusive): "))
             if 0 <= number <= 10:
                 return number
             else:
                 print("Invalid Number. Please Try Agian")
         except ValueError:
             print("Invalid Input. please Enter Valid Input")

if __name__ == "__main__":
            valid_number = get_valid_number()

            print("You entered", valid_number)

