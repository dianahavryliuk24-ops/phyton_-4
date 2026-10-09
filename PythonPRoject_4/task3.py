n = int(input("Введіть N: "))
total_sum = 0
even_sum = 0
odd_sum = 0
sequence = ""

for i in range(1, n + 1):
    total_sum += i

    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

    if i == n:
        sequence += str(i)
    else:
        sequence += f"{i} + "

print(f"\n{sequence} = {total_sum}")
print(f"\nСума: {total_sum}")
print(f"Сума парних: {even_sum}")
print(f"Сума непарних: {odd_sum}")