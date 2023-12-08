# Sitemap Scraper and CSV Exporter

This Python script allows you to scrape URLs from sitemaps and export them to a CSV file. It supports sitemaps divided into posts and pages and formats the last modified date as "22 October 2022."

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

To install the required Python libraries, open a terminal or command prompt and run the following command:

```bash
pip install requests beautifulsoup4
```
## Usage

1. Clone this repository or download the Python script.
2. Navigate to the directory where you have saved the Python script.
3. Open a terminal or command prompt in that directory.
4. Run the script using the following command:

```bash
   python sitemap_scraper.py
```

1. You will be prompted to enter the URL of the main sitemap index. Enter the URL and press Enter.

2. The script will start scraping URLs from the sitemaps and formatting the last modified date.

3. Once the scraping is complete, the script will save the data to a CSV file named "sitemap_data.csv" in the same directory.

4. You can find the scraped data in the "sitemap_data.csv" file.


### Output
1. The CSV file "sitemap_data.csv" will contain the following columns:

2. Serial Number: A unique identifier for each URL.
3. URL: The URL extracted from the sitemap.
4. Last Modified Date: The last modified date in the format "22 October 2022."
