import random
# this was game that user should guess the number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f"Gueess a number between 0 and {x}: ")
        if guess < random_number:
            print("It's to lOW!!")
        elif guess > random_number:
            print("It's to HIGH!!")
    print(f"YAY, welldone. you guessed the number CORRECTLY!! {random_number} is correct!!")
guess(10)

