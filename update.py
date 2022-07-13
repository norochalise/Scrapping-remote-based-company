# import libraries
from operator import index
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


remote_company_100 = pd.read_csv('data/100_remote_company.csv')
links = remote_company_100.link.to_list()



hqs = []
urls = []

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    containers = soup.find('div', class_='company-card')
    hq = containers.find("span")

    # Scrap headquarter
    if hq is None:
        hq = ''
    else:
        hq = hq.text
  

    # Scrap company url
    url = containers.find('a', href=True)
    if url is None:
        url = ''
    else:
        url = url['href']


    # append hqs and urls
    hqs.append(hq)
    urls.append(url)


# dict for hqs and urls
dict_info = {
    "Headquarter" : hqs,
    "Company_url" : urls
}


# dict to dataframe convert and merge of original csv file
df = pd.DataFrame(dict_info)
df_concate = pd.concat([remote_company_100, df], axis=1)

# reorder columns
df_concate = df_concate[['company_name', 'Headquarter',  'job_count', 'Company_url', 'link', 'company_description']]

# clean job_count column
df_concate['job_count'] = df_concate['job_count'].str.extract('(\d+)')

# save updated csv file to the data folder
df_concate.to_csv('data/updated_100_remote_company.csv', index=False)
