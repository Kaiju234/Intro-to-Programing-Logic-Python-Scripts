curr_value = int(input())

minimum_value = curr_value

while curr_value > 0:
    if curr_value < minimum_value:
        minimum_value = curr_value
    curr_value = int(input())

print(f'Min value: {minimum_value}')