entered_age = int(input())

while (entered_age < 18 or entered_age > 65):
    if entered_age < 18:
        print('5% discount')
    else:
         print('10% discount')
    entered_age = int(input())

print('Regular ticket price')