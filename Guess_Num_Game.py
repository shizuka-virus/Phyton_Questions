import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
