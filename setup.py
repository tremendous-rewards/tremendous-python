# coding: utf-8
from setuptools import setup, find_packages
from tremendous import __version__

PYTHON_REQUIRES = ">=3.7"

setup(
    name="tremendous-python",
    version=__version__,
    description="Python API client for Tremendous",
    author="Tremendous",
    author_email="developers@tremendous.com",
    url="https://github.com/tremendous-rewards/tremendous-python",
    keywords=["Api", "Gift cards", "Rewards", "Incentives", "Tremendous"],
    install_requires=[
        "urllib3 >= 1.25.3, < 2.1.0",
        "python-dateutil",
        "pydantic >= 2",
        "typing-extensions >= 4.7.1",
    ],
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    package_data={'README': ['README.md'], "tremendous": ["py.typed"]},
)
