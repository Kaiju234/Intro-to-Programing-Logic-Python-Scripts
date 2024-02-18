valid_letters = ["X Y Z A B C"]

user_letter = input("enter a letter:")

while user_letter.upper not in valid_letters:
    print('invalid letter')
    user_letter = input()

print(f" you entered{user_letter.upper}")