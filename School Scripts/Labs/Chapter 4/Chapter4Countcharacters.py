user_string = input()
character, phrase = user_string[0], user_string[1:]
count = phrase.count(character)

print(f"{count} {character}" + ("'s" if count != 1 else ''))