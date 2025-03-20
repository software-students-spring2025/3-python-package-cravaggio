# Fortune Cookie Cravaggio

[![log github events](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/event-logger.yml/badge.svg?branch=main)](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/event-logger.yml)

[![log github events](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/build.yml)

Team members: [Nina Li](https://github.com/nina-jsl), [Sirui Wang](https://github.com/siruiii), [Bohan Yin](https://github.com/Hans-Yin), [Nick Zhu](https://github.com/NickZhuxy)

## TABLE OF CONTENTS
1. [Description](#description)
2. [Installation](#installation)
3. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
4. [Usage Examples](#usage-examples)
5. [Contributing](#contributing)

## Description
A package that generates “fortune cookie” messages, programming wisdom, or absurd advice when called.

You can find the package here:

## Installation

You can import the Fortune Cookie Generator package into your own projects using pip. Below is how to install the package:

**1. Install the package from PyPI**
```
pip install fortunecookiecravaggio
```

**2. Import the functions in your Python code**
```
from fortunecookiecravaggio import get_fortune, load_fortunes, fortune_of_the_day, custom_fortune, fortune_with_ascii_art
```
## Virtual Environment & Dependencies
how to configure and run all parts of your project for any developer on any platform 
how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.

## Usage Examples
see example.py

**1. get_fortune**
```python
user_input = input("Enter a word, phrase, or thought to receive your fortune: ")
print(get_fortune(user_input))
```

**2. fortune_of_the_day**
```python
print("Fortune of the Day:", fortune_of_the_day())
```

**3. custom_fortune**
```python
custom_msg = input("Enter your custom fortune message: ")
added_msg = custom_fortune(custom_msg)
print("Custom fortune added:", added_msg)
```

**4. fortune_with_ascii_art**
```python
print(fortune_with_ascii_art())
```

## Contributing
We welcome contributions! Here’s how you can help: