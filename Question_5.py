number = int(input("Enter a number: "))
choice = str(input("Please choose between Sum or Product: "))
selection = choice.capitalize()

n = 1
total_sum = 0
product = 1

if selection == "Sum":
    while n <= number:
        total_sum += n
        n += 1
    print(f"The Sum of numbers from 1 to {number} = {total_sum}")
elif selection == "Product":
    while n <= number:
        product *= n
        n += 1
    print(f"The Product of numbers from 1 to {number} = {product}")
else:
    print("Wrong choice!")