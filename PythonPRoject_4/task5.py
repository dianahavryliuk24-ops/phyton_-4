secret_number = 7
attempts = 0

while True:
    guess = int(input("Введіть число: "))
    attempts += 1

    if guess > secret_number:
        print("Загадане число менше.\n")
    elif guess < secret_number:
        print("Загадане число більше.\n")
    else:
        print("Ви вгадали!")
        print(f"Кількість спроб: {attempts}")
        break