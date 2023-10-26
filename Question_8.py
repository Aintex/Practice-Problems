def is_prime(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


# Input a number from the user
def print_all_primes(limit):
    print(f"Prime numbers up to {limit} are:")
    for num in range(1, limit + 1):
        if is_prime(num):
            print(num)


limit_1 = int(input("Enter the limit for prime numbers: "))
print_all_primes(limit_1)