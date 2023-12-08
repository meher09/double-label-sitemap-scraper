import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL of the main sitemap index
main_sitemap_url = input("Enter your Sitemap url: ") 

# Function to download URLs from a sitemap and format the last modified date
def download_urls_from_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "xml")
            urls = []

            # Find and extract URLs from <loc> tags and last modified date
            for loc in soup.find_all("loc"):
                url = loc.text
                lastmod_str = loc.find_next("lastmod").text

                # Convert the last modified date to the desired format
                lastmod_date = datetime.strptime(lastmod_str, "%Y-%m-%dT%H:%M:%S+00:00")
                formatted_lastmod = lastmod_date.strftime("%d %B %Y")

                urls.append((url, formatted_lastmod))

            return urls
        else:
            print(f"Failed to retrieve sitemap. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Function to scrape and download all URLs
def scrape_and_download_all_urls(main_sitemap_url):
    try:
        response = requests.get(main_sitemap_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "xml")
            sitemap_urls = []

            # Find and extract sitemap URLs from <loc> tags
            for loc in soup.find_all("loc"):
                sitemap_urls.append(loc.text)

            # Create a CSV file and write the data
            with open("sitemap_data.csv", mode="w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Serial Number", "URL", "Last Modified Date"])

                # Download URLs from each sitemap and save them in the CSV file
                serial_number = 1
                for sitemap_url in sitemap_urls:
                    urls = download_urls_from_sitemap(sitemap_url)
                    for url, formatted_lastmod in urls:
                        csv_writer.writerow([serial_number, url, formatted_lastmod])
                        serial_number += 1
        else:
            print(f"Failed to retrieve main sitemap. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to scrape and download all URLs and save them in CSV
scrape_and_download_all_urls(main_sitemap_url)
