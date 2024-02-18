isValid = False
 
while isValid == False:
    num1 = input("Input Num1:")
    if num1.isdigit():
        num1 = int(num1)
        isValid = True
    else:
        print("Invalid Number!!!")

isValid = False
while isValid == False:
    num2 = input("Input Num2: " )
    if num2.isdigit() and int(num2) > num1:
        num2 = int(num2)
        isValid = True


for numbers in range(num1, num2+1,5):
    print(numbers)