# coding: utf-8
import os

from setuptools import setup, find_packages

PYTHON_REQUIRES = ">=3.8"

data = {}
root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "tremendous", "version.py")) as f:
    exec(f.read(), data)

setup(
    name="tremendous-python",
    version=data["__version__"],
    description="Python API client for Tremendous",
    long_description="Python API client for Tremendous",
    author="Tremendous",
    author_email="developers@tremendous.com",
    url="https://github.com/tremendous-rewards/tremendous-python",
    keywords=["Api", "Gift cards", "Rewards", "Incentives", "Tremendous"],
    install_requires=[
        "urllib3 >= 2.1.0, < 3.0.0",
        "python-dateutil",
        "pydantic >= 2",
        "typing-extensions >= 4.7.1",
    ],
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    package_data={'README': ['README.md'], "tremendous": ["py.typed"]},
)
