#!/usr/bin/env python3
"""
Example Usage of the Fortune Cookie Package

Configuration:
- Make sure you have installed the package dependencies (using pipenv or your preferred environment).
- Ensure that the 'fortunes.txt' file is located in the 'src/fortunecookiecravaggio/' directory.
- No additional environment variables or database starter data are required.
- To run this example, execute:
    python example.py
"""

from fortunecookiecravaggio.fortune import get_fortune, fortune_of_the_day, custom_fortune, fortune_with_ascii_art

def main():
    # Example for get_fortune
    print("=== Example for get_fortune ===")
    user_input = input("Enter a word, phrase, or thought to receive your fortune: ")
    fortune = get_fortune(user_input)
    print("Your fortune is:", fortune)
    
    # Example for fortune_of_the_day
    print("\n=== Example for fortune_of_the_day ===")
    print("Fortune of the Day:", fortune_of_the_day())
    
    # Example for custom_fortune
    print("\n=== Example for custom_fortune ===")
    custom_msg = input("Enter a custom fortune message to add: ")
    added_message = custom_fortune(custom_msg)
    print("Added custom fortune:", added_message)
    
    # Example for fortune_with_ascii_art
    print("\n=== Example for fortune_with_ascii_art ===")
    ascii_fortune = fortune_with_ascii_art()
    print(ascii_fortune)

if __name__ == "__main__":
    main()
