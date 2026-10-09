balance = 1000

while True:
    print("\n=== БАНКОМАТ ===")
    print("1 — Переглянути баланс")
    print("2 — Поповнити рахунок")
    print("3 — Зняти кошти")
    print("4 — Вийти")

    choice = input("\nВаш вибір: ")

    if choice == '1':
        print(f"Ваш баланс: {balance} грн")

    elif choice == '2':
        amount = int(input("Сума поповнення: "))
        if amount > 0:
            balance += amount
            print(f"Рахунок поповнено.\nБаланс: {balance} грн")
        else:
            print("Сума має бути більшою за 0.")

    elif choice == '3':
        amount = int(input("Сума для зняття: "))
        if amount <= 0:
            print("Сума має бути більшою за 0.")
        elif amount > balance:
            print("Недостатньо коштів.")
        else:
            balance -= amount
            print(f"Операція успішна.\nБаланс: {balance} грн")

    elif choice == '4':
        print("Дякуємо за використання банкомата!")
        break

    else:
        print("Неправильний пункт меню.")