# Define a list, my_list, containing the user inputs: my_flower1, my_flower2, and my_flower3 in the same order.

my_flower1 = input("enter the first flower ")
my_flower2 = input("enter the second flower ")
my_flower3 = input("enter the third flower")
my_list = [my_flower1,my_flower2,my_flower3]


# Define a list, your_list, containing the user inputs, your_flower1 and your_flower2, in the same order.

your_flower1 = input("enter your first flower")
your_flower2 = input("enter your second flower")

your_list = [your_flower1,your_flower2]

# Define a list, our_list, by concatenating my_list and your_list. 

our_list = my_list + your_list


# Append the user input, their_flower, to the end of our_list.

their_flower = input("Enter their_flower: ")

our_list.append(their_flower)

# Change my_flower2 in our_list with their_flower.

our_list[1] = their_flower

# Remove the first occurrence of their_flower from our_list without using index().

for i in range(len(our_list)):
    if our_list[i] == their_flower:
        our_list.remove(our_list[i])
        break

# Remove the second element of our_list.

our_list.pop(1)

# Print the Results 
print(our_list)
print(my_list)
print(your_list)