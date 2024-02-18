total_product = 1

entered_value = int(input())

while entered_value > 0:
    total_product = total_product * entered_value
    entered_value = int(input())

print(f'Product: {total_product}')