import itertools
import string
import time


# Target password (known only to the attacker during the simulation)
target_password = "abc"


# Character set to try
characters = string.ascii_lowercase


# Start the timer
start_time = time.time()


# Brute force loop
attempts = 0
for length in range(1, 5):  # Try lengths from 1 to 4
    for guess in itertools.product(characters, repeat=length):
        attempts += 1
        guess_str = ''.join(guess)

        if guess_str == target_password:
            end_time = time.time()
            print(f"Password found: {guess_str}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            exit()