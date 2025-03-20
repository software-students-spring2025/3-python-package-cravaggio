# Fortune Cookie Cravaggio

[![log github events](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/event-logger.yml/badge.svg?branch=main)](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/event-logger.yml)
[![CI / CD](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/build.yml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-cravaggio/actions/workflows/build.yml)

Team members: [Nina Li](https://github.com/nina-jsl), [Sirui Wang](https://github.com/siruiii), [Bohan Yin](https://github.com/Hans-Yin), [Nick Zhu](https://github.com/NickZhuxy)

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage Examples](#usage-examples)
4. [Contributing](#contributing)

## Description
A package that generates “fortune cookie” messages, programming wisdom, or absurd advice when called.

You can find the package here: https://pypi.org/project/fortunecookiecravaggio/

## Installation

Below is how you can import the Fortune Cookie Generator package into your own projects using pip.

**1. Install the package**
```
pip install fortunecookiecravaggio
```

**2. Import the functions in your Python code**
```
from fortunecookiecravaggio import get_fortune, fortune_of_the_day, custom_fortune, fortune_with_ascii_art
```
**3. Add a fortunes.txt in the directory**

Create your own or download the predefined list [fortunes.txt](https://github.com/software-students-spring2025/3-python-package-cravaggio/blob/main/src/fortunecookiecravaggio/fortunes.txt)

## Usage Examples
See [example.py](https://github.com/software-students-spring2025/3-python-package-cravaggio/blob/main/example.py)

**1. Get a random fortune based on user input: `get_fortune("Any word, phrase, or thought")`**

```python
user_input = input("Enter a word, phrase, or thought to receive your fortune: ")
print(get_fortune(user_input))
```

**2. Discover the daily prophecy: `fortune_of_the_day()`**
```python
print("Fortune of the Day:", fortune_of_the_day())
```

**3. Add your own fortune messages: `custom_fortune("Custom message")`**
```python
custom_msg = input("Enter your custom fortune message: ")
added_msg = custom_fortune(custom_msg)
print("Custom fortune added:", added_msg)
```

**4. Get a fortune with an ASCII fortune cookie: `fortune_with_ascii_art()`**
```python
print(fortune_with_ascii_art())
```

## Contributing
Here’s how you can help:

**1. Clone the repository**
```
git clone https://github.com/software-students-spring2025/3-python-package-cravaggio
cd 3-python-package-cravaggio
```

**2. Create a branch**
```
git checkout -b yourbranchname
```

**3. Set up virtual environment**
```
pip install pipenv
pipenv install --dev
pipenv shell
```

**4. Make your changes**

**5. Commit and Push**
```
git add .
git commit -m "your changes"
git push origin yourbranchname
```
**6. Submit a pull request with your changes**

**7. (optional) Test, build and upload**
```
pytest
python -m build
twine upload -r pypi dist/*
```