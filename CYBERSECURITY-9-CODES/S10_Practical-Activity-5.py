import hashlib
import itertools
import string
import time



# Target password (hashed using SHA-256)
original_password = "abc"
target_hash = hashlib.sha256(original_password.encode()).hexdigest()


# Characters to try
characters = string.ascii_lowercase


# Start time
start_time = time.time()



# Brute force attempt
attempts = 0
for length in range(1, 5):
    for guess in itertools.product(characters, repeat=length):
        guess_str = ''.join(guess)
        guess_hash = hashlib.sha256(guess_str.encode()).hexdigest()
        attempts += 1

        if guess_hash == target_hash:
            end_time = time.time()
            print(f"Password cracked: {guess_str}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            exit()