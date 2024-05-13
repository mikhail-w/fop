number_to_guess = int(input("Enter the integer for the player to guess: "))
tries = 0
guess = int(input("Enter your guess: "))
while True:
    tries += 1
    if guess == number_to_guess:
        if tries == 1:
            print("You guessed it in 1 try.")
        else:
            print(f"You guessed it in {tries} tries.")
        break
    elif guess > number_to_guess:
        guess = int(input("Too high - try again: "))
    elif guess < number_to_guess:
        guess = int(input("Too low - try again: "))
