from setuptools import setup

# Setup script for Podium project

setup(
    name='PodiumInterview',
    description='Podium interview web crawler and review analyzer.',
    version='1.0',
    packages=['ReviewObjects', 'ScraperStrategies', 'ReviewAnalysisStrategies', 'UnitTest'],
    install_requires=['pyasn1', 'textblob', 'requests', 'bs4', 'cryptography', 'incremental', 'scrapy', 'coverage'],
    url='',
    long_description='This project requires Python 3.6',
    license='',
    author='bentzedwards',
    author_email='bentzjedwards@yahoo.com'
)
