#!/usr/bin/python3
import requests
import logging
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import re
from pathlib import Path

logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.info("Starting download session")

# GET DATASET URLS
req = Request("https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page")
html = urlopen(req)

soup = BeautifulSoup(html, "lxml")
all_urls = []
for link in soup.findAll('a'):
    all_urls.append(link.get('href'))

# all the data is hosted on cloudfront urls only
cloudfront_urls = [link for link in all_urls if "cloudfront" in link]



# DOWNLOAD DATASET
data_dir = "nyc_taxi_data"
# create dir if it doesn't exist
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

def download_file_from_url(url):
    filename = os.path.basename(urlparse(url).path)
    file_path = Path(f"{data_dir}/{filename}")
    logging.info(f"Started {filename} from {url}")
    resp = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(resp.content)
    logging.info(f"Finished {filename} from {url}")

# download files SEQUENTIALLY
for url in cloudfront_urls:
    download_file_from_url(url=url)