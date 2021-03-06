# Podium Review Scraper and Analyzer

Requirements
============

* Python 3.6

Install
========

Clone the repository and, from the project directory, run:

    sudo python setup.py install  

(There is an OS X bug that will sometimes cause the setup.py to fail the first time due to an incorrect installation order of the dependencies listed in the setup file. Repeating the install should clean this up if it occurs)

Brief Overview
========

Welcome to the Podium web scraper and review analyzer. I can only imagine the excitement you must be experiencing as you delve into this README. This program scrapes reviews off the website of the [McKaig Chevrolet Buick Dealership](http://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-review-23685/) and prints out the reviews that were the most overly positive.

To run the program, execute the following command:

    python ReviewAnalyzerEngine.py

Upon doing this, you will be prompted to choose the method to use for review scoring and web scraping, the number of pages to crawl, and the number of reviews to display at the end. Once you've selected all your options, the report of the most positive reviews found on the crawled pages will be printed out to the terminal.

For more information on review scoring and web scraping methods, see the following sections.

Review Positivity Ranking
========

There are two methods that can be used to score the positivity of the reviews. These are sentiment classifiers from the [Pattern module](http://www.clips.ua.ac.be/pages/pattern-en) and the [NLTK python library](http://www.nltk.org/) respectively. Below is a brief description of the two sentiment analyzers:

### 1. PatternAnalyzer
This sentiment analyzer is a python extension of "Pattern", which uses fast part-of-speech tagging to quickly analyze sentences and return a polarity and subjectivity score. The module bundles a lexicon of adjectives (e.g., good, bad, amazing, irritating, ...) that occur frequently in product reviews, annotated with scores for sentiment polarity (positive ↔ negative) and subjectivity (objective ↔ subjective). When using this analyzer, reviews with the higher polarity (more positive) scores, will be ranked above those with lower polarity scores.

### 2. NaiveBayesAnalyzer
This sentiment analyzer is a module from the NLTK platform. It uses a Naive Bayes model trained on a corpus of movie reviews. After the model has been trained, it classifies strings of text on the likelihood that they are positive reviews or negative reviews. When using this analyzer, reviews with a higher likelihood of being positive are more ranked above those with a lower likelihood of being positive.

Web Scraping
========

There are two methods that can be used to scrape the dealership page for reviews. The first is a simple, single-threaded review scraper that uses the [BeautifulSoup library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to grab text from a retrieved webpage.

The second uses the [Scrapy framework](https://scrapy.org/) which allows you to create multiple webcrawlers, allowing you to gather information on reviews more quickly.

Running the Testing Suite
========

To run the test suite, from the project directory run: 

    coverage run -m unittest discover -s UnitTest/ 

This will generate a [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/) file that you can use to dig deeper into the code coverage given by the unit tests. After you've run the above code, if you want to see a basic report of the code coverage, run:

    coverage report 

To generate a more visual report of the code coverage, run:

    coverage html
              
This will generate html files showing exactly which lines were covered and which were missed.


