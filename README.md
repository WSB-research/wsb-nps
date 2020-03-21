# NPORT-P Python Scraper

## Setup

I currently use Python 3.8.1 but I would imagine most Python versions would work.

You will need to install pip: https://pip.pypa.io/en/stable/installing/

Run: `pip install -r requirements.txt`

## Running

From the python_scraper folder run: `scrapy crawl sec_nport_p`

## Config Options

In `python_scraper/python_scraper/settings.py` you can adjust how fast the spider requests pages and other spider
settings.