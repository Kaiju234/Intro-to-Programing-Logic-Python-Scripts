def get_month(Month):
    if Month.lower() == 'halloween':
        return 'October'
    elif Month.lower() == 'thanksgiving':
        return 'November'
    else:
        return 'Holiday not recognized'

# Get user input
user_Month = input("Enter the holiday: ")

# Display the corresponding month
result = get_month(user_Month)
print(f"The month for {user_Month} is {result}")
