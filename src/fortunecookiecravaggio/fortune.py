import hashlib
import random

# fortunes imported from fortune cookie database: http://www.fortunecookiemessage.com/archive.php
def load_fortunes(file_path="fortunes.txt"):
    """Reads fortunes from a text file and returns a list."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            fortunes = [line.strip() for line in file if line.strip()]
        return fortunes
    except FileNotFoundError:
        return ["Error: Fortune file not found. Please create a 'fortunes.txt' file."]

def get_fortune(user_input, file_path="fortunes.txt"):
    """Returns a fortune based on the user input by hashing the input to pick a fortune."""
    fortunes = load_fortunes(file_path)

    if not fortunes or "Error" in fortunes[0]:
        return fortunes[0]  # Return error message if file is missing

    # Create a hash of the input to determine the fortune index
    hash_value = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    index = hash_value % len(fortunes)

    return fortunes[index]