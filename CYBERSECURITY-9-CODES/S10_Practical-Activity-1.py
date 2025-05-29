import itertools
import string
import time



# Set a simple target password for simulation
target = "pass"
# Characters to try
chars = string.ascii_lowercase


# Start timer
start = time.time()
attempts = 0


# Brute force logic
for length in range(1, 5):
    for guess in itertools.product(chars, repeat=length):
        attempts += 1

        if ''.join(guess) == target:
            end = time.time()

            print(f"[✔] Password found: {''.join(guess)}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end - start:.2f} seconds")

            exit()