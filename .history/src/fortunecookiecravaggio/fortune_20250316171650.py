import random
from datetime import date 

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