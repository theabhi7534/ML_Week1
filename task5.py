"""Challenge: Write a number guessing game where the user has 5 attempts. Use break to end early if the guess is right, and continue to skip invalid input. in py"""
import random

target = random.randint(1, 100)

for _ in range(5):
    guess = input("guess a number (1-100): ")
    if not guess.isdigit():
        print("invalid input")
        continue

    guess = int(guess)
    if guess == target:
        print("correct!")
        break
    print("too high" if guess > target else "too low")

print(f"the number was {target}")
