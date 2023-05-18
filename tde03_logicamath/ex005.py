# beecrowd | 1987
# Divisibilidade Por 3
# Por Alex Paixão, UNIME BR Brazil

# Timelimit: 1

number_of_count = int(input())
all_numbers = []
sum_numbers = 0

for i in range(1, number_of_count + 1):
    typed_number = input()
    all_numbers.insert(i-1, typed_number)

for i in range(0, len(all_numbers)):
   sum_numbers = sum_numbers + int(all_numbers[i])


if sum_numbers % 3 == 0:
    print(f"{sum_numbers} sim")
else:
    print(f"{sum_numbers} nao")