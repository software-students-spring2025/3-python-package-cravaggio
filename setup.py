from setuptools import setup, find_packages

setup(
    name="fortunecookiecravaggio",
    version="1.0.3",
    author="Cravaggio",
    description="A package that generates “fortune cookie” messages, programming wisdom, or absurd advice when called.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/software-students-spring2025/3-python-package-cravaggio", 
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)