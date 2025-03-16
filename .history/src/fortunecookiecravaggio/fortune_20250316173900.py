import random
from datetime import date
import os
import json

FORTUNE_FILE = os.path.join(os.path.dirname(__file__), 'custom_fortunes.json')

def get_fortune():
    print("testing fortune")

def fortune_of_the_day():
    # Seed with today's ordinal date so the fortune changes daily
    random.seed(date.today().toordinal())

    fortunes = [
        "Today is your lucky day!",
        "An unexpected event will soon bring you fortune.",
        "You will find the solution you’ve been looking for.",
        "A dream you have will come true.",
        "Your hard work will pay off very soon.",
        "A pleasant surprise is waiting for you.",
        "Success will come to you in the near future.",
        "Happiness begins with facing life with a smile and a wink.",
        "Your abilities will shortly be recognized by others.",
        "A new venture will bring you great success."
    ]
    return random.choice(fortunes)

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