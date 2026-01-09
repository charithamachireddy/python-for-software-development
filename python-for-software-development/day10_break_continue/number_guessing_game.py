secret_number = 7

while True:
    guess = int(input("Guess the number (1 to 10): "))

    if guess < 1 or guess > 10:
        print("Invalid input, try again.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Wrong guess, try again.")
