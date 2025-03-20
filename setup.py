from setuptools import setup, find_packages

setup(
    name="fortunecookiecravaggio",
    version="0.1",
    author="Nina Li, Sirui Wang, Bohan Yin, Nick Zhu",
    author_email="jl13999@nyu.edu, sw5546@nyu.edu, by2179@nyu.edu, xz4687@nyu.edu",
    description="A fortune cookie message generator.",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["fortune cookie"],
    url="https://github.com/software-students-spring2025/3-python-package-cravaggio",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
