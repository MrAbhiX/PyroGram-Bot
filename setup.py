import pathlib
from setuptools import setup

#installing requirements

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyrogram-bot",
    version="1.4.0",
    description="HELP FOR PyROGRAM",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrAbhiX/pyrogram-bot",
    author="ABHISHEK THAKUR",
    author_email="mrabhixd03ail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["pyrogram-bot"],
    include_package_data=True,
    install_requires=["requests"],
)
