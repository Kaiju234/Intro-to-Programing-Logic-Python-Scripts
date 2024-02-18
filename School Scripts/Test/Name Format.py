full_name = input().split()

if len(full_name) == 2:
    first_name = full_name[0]
    last_name = full_name[1]
    print(f'{last_name}, {first_name[0]}.')
elif len(full_name) == 3:
    first_name = full_name[0]
    middle_name = full_name[1]
    last_name = full_name[2]
    print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')