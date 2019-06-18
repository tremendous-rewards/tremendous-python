from setuptools import setup, find_packages
import tremendous


url = ''

setup(
    name='tremendous-python',
    version=tremendous.__version__,
    description='Python API client for Tremendous',
    long_description='',
    keywords='api, gift cards, rewards, incentives, tremendous',
    author='Tremendous',
    author_email='developers@tremendous.com',
    url='https://github.com/GiftRocket/tremendous-python/',
    license='MIT',
    packages=find_packages(exclude='tests'),
    package_data={'README': ['README.md']},
    install_requires=['requests==2.7.0'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)
