
# # # word = 'Stack'
# # # for char in word:
# # #     print(char, end='/')
# # # print()

# # weights = [8, 7, 1, 2]
# # result = 0
# # for weight in weights:
# #     result += weight
# # print(result)


# colors = ['red', 'gold', 'grey']
# for color in reversed(colors):
#     print(color)

cities = {
    'Toronto': 982,
    'Austin': 3435,
    'London': 309,
    'Paris': 958,
    'Montreal': 584,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)