number = int(input("Enter a number: "))

n = 1
sum = 0
while n <= number:
    sum = sum + n
    n += 1

print(f"The sum of numbers from 1 to {number} = {sum}")