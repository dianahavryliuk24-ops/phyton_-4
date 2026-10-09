while True:
    n = int(input("Введіть число: "))
    if n < 1:
        print("Число має бути 1 або більше.")
    else:
        break
print()
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
