while True:
    try:
        # Code that might raise an exception
        x = int(input("Please enter a number: "))
        print("You entered:", x)
        break  # Break out of the loop if input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
