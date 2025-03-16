# import fortunecookiecravaggio.fortune as fortune
from .fortune import fortune_of_the_day

def main():
    print("""
🌟 Welcome to Python Fortune Cookie! 🍪✨

Get a randomly generated fortune, programming wisdom, or a bit of absurd advice.

🔮 Features:
- Get a random fortune: `get_fortune('random')`
- Add your own fortune messages: `custom_fortune("Your message", "Author")`
- Get a fortune with an ASCII fortune cookie: `fortune_with_ascii_art()`
- Discover the daily prophecy: `fortune_of_the_day()`

Unwrap your fortune now! 🥠
    """)
    fortune = fortune_of_the_day()
    print("Fortune Cookie says...")
    print(f"{fortune}")

if __name__ == "__main__":
    main()