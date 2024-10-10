my_string = input("Ваши игровые предпочтения? ")
print("Количество букв:", len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
call = my_string.split()
for word in call:
    print(f"{word[0]}, {word[-1]}")