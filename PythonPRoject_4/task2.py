n = int(input("Введіть N: "))
even_count = 0
odd_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} — парне")
        even_count += 1
    else:
        print(f"{i} — непарне")
        odd_count += 1
print(f"Парних чисел: {even_count}")
print(f"Непарних чисел: {odd_count}")
