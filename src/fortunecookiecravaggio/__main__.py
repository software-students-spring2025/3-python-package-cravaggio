from fortune import get_fortune, fortune_of_the_day, custom_fortune, fortune_with_ascii_art

def main():
    print("""
🌟 Welcome to Fortune Cookie Cravaggio! 🍪✨

Get a randomly generated fortune, programming wisdom, or a bit of absurd advice.

🔮 Features:
- Get a random fortune based on user input: `get_fortune("Any word, phrase, or thought")`
- Add your own fortune messages: `custom_fortune("Custom message")`
- Get a fortune with an ASCII fortune cookie: `fortune_with_ascii_art()`
- Discover the daily prophecy: `fortune_of_the_day()`

Unwrap your fortune now! 🥠
    """)

if __name__ == "__main__":
    main()