import hashlib
import random
from datetime import date
import os
import json

FORTUNE_FILE = os.path.join(os.path.dirname(__file__), 'custom_fortunes.json')

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


def fortune_of_the_day(file_path="fortunes.txt"):
    # Seed with today's ordinal date so the fortune changes daily
    random.seed(date.today().toordinal())

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            fortunes = [line.strip() for line in file if line.strip()]
        return random.choice(fortunes)
    except FileNotFoundError:
        return ["Error: Fortune file not found. Please create a 'fortunes.txt' file."]

def custom_fortune(message: str, author: str) -> dict:
    """
    Adds a custom fortune message to a local JSON file.

    Parameters:
        message (str): The custom fortune message to add.
        author (str): The author of the fortune message.

    Returns:
        dict: A dictionary representing the added fortune, e.g.,
              {"message": "Your custom message", "author": "Your Name"}

    Raises:
        ValueError: If either `message` or `author` is empty or only whitespace.
        Exception: If there is an error reading from or writing to the file.
    """
    # Validate inputs
    if not message or not message.strip():
        raise ValueError("Fortune message cannot be empty.")
    if not author or not author.strip():
        raise ValueError("Author cannot be empty.")

    # Initialize fortunes list
    fortunes = []
    # Read existing fortunes from file, if it exists
    if os.path.exists(FORTUNE_FILE):
        try:
            with open(FORTUNE_FILE, 'r', encoding='utf-8') as f:
                fortunes = json.load(f)
                if not isinstance(fortunes, list):
                    fortunes = []
        except json.JSONDecodeError:
            fortunes = []
        except Exception as e:
            raise Exception(f"Error reading fortunes file: {e}")

    new_fortune = {"message": message.strip(), "author": author.strip()}
    fortunes.append(new_fortune)

    # Write fortunes back to file
    try:
        with open(FORTUNE_FILE, 'w', encoding='utf-8') as f:
            json.dump(fortunes, f, indent=4)
    except Exception as e:
        raise Exception(f"Error writing fortunes file: {e}")

    return new_fortune

def fortune_with_ascii_art():
    """Returns a fortune message with random ASCII art."""
    art_list = [
        """
        (\_/)
        (o.o)
        (")(")
        """,
        """
        _______
       /       \\ 
      |  🥠  |
       \\_______/
        """,
        """
        ʕ•ᴥ•ʔ
        """,
        """
          __    __
        o-''))_____\\ 
        "--__/ * * * )
        c_c__/-c____/
        """,
        """
         /^ ^\ 
        / 0 0 \ 
        V\ Y /V
        / - \ 
        |    \ 
        || (__V
        """,
        """
         /\_/\ 
        ( o.o )
         > ^ <
        """,
        """
                      /|      __
*             +      / |   ,-~ /             +
     .              Y :|  //  /                .         *
         .          | jj /( .^     *
               *    >-"~"-v"              .        *        .
*                  /       Y
   .     .        jo  o    |     .            +
                 ( ~T~     j                     +     .
      +           >._-' _./         +
               /| ;-"~ _  l
  .           / l/ ,-"~    \     +
              \//\/      .- \ 
       +       Y        /    Y
               l       I     !
               ]\      _\    /"\ 
              (" ~----( ~   Y.  )
          ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
    ]
    
    ascii_art = random.choice(art_list)
    fortune = get_fortune()
    return f"{ascii_art}\n🍀 Fortune: {fortune}"
