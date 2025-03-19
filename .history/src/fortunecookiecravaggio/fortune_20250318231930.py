import hashlib
import random
from datetime import date
import os

# fortunes imported from fortune cookie database: http://www.fortunecookiemessage.com/archive.php
def load_fortunes(file_path="fortunes.txt"):
    """Reads fortunes from a text file and returns a list."""
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            fortunes = [line.strip() for line in file if line.strip()]
        return fortunes
    except FileNotFoundError:
        return ["Error: Fortune file not found. Please create a 'fortunes.txt' file."]

def get_fortune(user_input, file_path="fortunes.txt"):
    """Returns a fortune based on the user input by hashing the input to pick a fortune."""
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.dirname(__file__), file_path)
    fortunes = load_fortunes(file_path)

    if not fortunes or "Error" in fortunes[0]:
        return fortunes[0]  # Return error message if file is missing

    # Create a hash of the input to determine the fortune index
    hash_value = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    index = hash_value % len(fortunes)

    return fortunes[index]


def fortune_of_the_day(file_path="fortunes.txt"):
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.dirname(__file__), file_path)
    # Seed with today's ordinal date so the fortune changes daily
    random.seed(date.today().toordinal())

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            fortunes = [line.strip() for line in file if line.strip()]
        return random.choice(fortunes)
    except FileNotFoundError:
        return ["Error: Fortune file not found. Please create a 'fortunes.txt' file."]

def custom_fortune(message: str) -> str:
    """
    Adds a custom fortune message to the fortunes.txt file.
 
    Parameters:
        message (str): The custom fortune message to add.
 
    Returns:
        str: The added fortune message.
 
    Raises:
        ValueError: If the message is empty or only whitespace.
        Exception: If there is an error writing to the file.
    """
    # Validate input
    if not message or not message.strip():
        raise ValueError("Fortune message cannot be empty.")
 
    message = message.strip()
    file_path = os.path.join(os.path.dirname(__file__), 'fortunes.txt')
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(message + "\n")
    except Exception as e:
        raise Exception(f"Error writing fortune to file: {e}")
 
    return message

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
    fortune = get_fortune("random")
    return f"{ascii_art}\n🍀 Fortune: {fortune}"
