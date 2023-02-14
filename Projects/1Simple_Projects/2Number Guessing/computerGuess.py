import random
# Now computer should guess the number

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guees = low
        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            
    print("YAY! The computer guess the correct, {guess}, correctly!" )

computer_guess(20)
