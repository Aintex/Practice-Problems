table_size = 12

for i in range(1, table_size + 1):
    print(f"Table of {i}: \n")
    for j in range(1, table_size + 1):
        multiplication = i * j
        print(f"{i} * {j} = {multiplication}")

# number = int(input("Enter a number: \n"))
#
# print(f"Table of {number}: \n")
#
# n = 1
# while n <= table_size:
#     multiplication = number * n
#     print(f"{number} * {n} = {multiplication}")
#     n += 1
