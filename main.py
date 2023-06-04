import random

def play_game():
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess the number?")
    print("--------------------------------------")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number correctly!")
            break
        
        attempts += 1
        print("Attempts remaining:", max_attempts - attempts)
        print("--------------------------------------")
    
    if attempts == max_attempts:
        print("Game over! You couldn't guess the number. The secret number was:", secret_number)

play_game()