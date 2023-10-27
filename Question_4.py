number = 17

n = 1
total_sum = 0
while n <= 17:
    if n % 3 == 0 or n % 5 == 0:
        total_sum += n
    n += 1

print(f"The sum of numbers from {n} to {number} that are multiples of 3 or 5 = {total_sum}")