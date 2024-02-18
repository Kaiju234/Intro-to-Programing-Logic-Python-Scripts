
par = int(input())
strokes = int(input())


if par not in range(3, 6):
    print('Error')
elif (par - strokes) < -1:
    print('Error')

if par - strokes == 2:
    print('Eagle')
elif par - strokes == 1:
    print('Birdie')
elif par == strokes:
    print('Par')
elif par - strokes == -1:
    print('Bogey')