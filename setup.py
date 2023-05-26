from setuptools import setup, find_packages

setup(
    name="pyom",
    version="0.0.1",
    description="Package for working with OpenMeteo API in Python",
    author="Artur Wegrzyn",
    packages=find_packages(),
    install_requires="requirements.txt"
)

