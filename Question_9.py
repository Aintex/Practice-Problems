secret_number = 7

guessing_number = 0
guess_count = 0

while guessing_number != secret_number:

    guessing_number = int(input("Please enter guess: "))
    guess_count += 1
    if guessing_number < secret_number:
        print("The number you enter is too small.")
    elif guessing_number > secret_number:
        print("The number you enter is too large.")
    else:
        print(f"Correct! You guessed the number in {guess_count} tries")
        break

