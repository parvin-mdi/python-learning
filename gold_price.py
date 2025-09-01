import requests
from bs4 import BeautifulSoup
import convert_numbers
# import csv 
# import sched, time
# import datatime

kia_gold_url = 'https://kia-gallery.com/fa'
orel_gold_url = 'https://orelgallery.com'
tgju_site_url = 'https://www.tgju.org'

kia_gold_response = requests.get(kia_gold_url)
orel_gold_response = requests.get(orel_gold_url)
tgju_site_response = requests.get(tgju_site_url)

kia_gold_soup = BeautifulSoup(kia_gold_response.text, 'html.parser')
orel_gold_soup = BeautifulSoup(orel_gold_response.text, 'html.parser')
tgju_site_soup = BeautifulSoup(tgju_site_response.text, 'html.parser')

get_kia_gold_tags = kia_gold_soup.find_all('ul')
get_orel_gold_tags = orel_gold_soup.find_all('small')
get_tgju_site_tags = tgju_site_soup.find_all('span', class_='info-price')

kia_gold_data = []
for tag in get_kia_gold_tags:
    kia_gold_data.append(tag.get_text(strip=True)[12:21])
kia_gold_price = convert_numbers.persian_to_english(kia_gold_data[1])

orel_gold_data = []
for tag in get_orel_gold_tags:
    orel_gold_data.append(tag.get_text(strip=True))
orel_gold_price = convert_numbers.persian_to_english((orel_gold_data[0])[26:36])

tgju_site_data = []
for tag in get_tgju_site_tags:
    tgju_site_data.append(tag.get_text(strip=True))
tgju_site_price = tgju_site_data[3]

print(f"kia gold price {kia_gold_price}")
print(f"orel gold price {orel_gold_price}")
print(f"tgju site price {tgju_site_price}")