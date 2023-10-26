def is_prime(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(f"{number} is a prime number.")
        # return True
    else:
        print(f"{number} is not a prime number.")
        # return False


# Input a number from the user
num = int(input("Enter a number: "))

is_prime(num)

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")