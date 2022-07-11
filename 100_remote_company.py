# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Url of scrapping site
url = 'https://weworkremotely.com/top-remote-companies'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
containers = soup.find('div', class_='jobs-container').find_all('li')


# Intialized lists for company details
company_names = []
job_counts = []
links = []
company_descriptions = []


# Iterate all the company details

for container in containers:

    # company name append
    company_name = container.find('span', class_='company')
    if company_name is None:
        company_name = ''
    else:
        company_name = company_name.text

    # Job counts
    job_count = container.find('span', class_='job-count')
    if job_count is None:
        job_count = ''
    else:
        job_count = job_count.text

    #  company descriptions 
    company_description = container.find('span', class_='company-title')
    if company_description is None:
        company_description = ''
    else:
        company_description = company_description.text

    # link of company
    link = container.find('a', href=True)
    if link is None:
        link = ''
    else:
        company_url = 'https://weworkremotely.com'
        link = company_url + link['href']


    # Append campany details for each lists
    company_names.append(company_name)
    job_counts.append(job_count)
    company_descriptions.append(company_description)
    links.append(link)



# List to dictionery
company_info_dict = {
        'company_name': company_names,
        'job_count': job_counts,
        'company_description' : company_descriptions,
        'link' : links
    }


# Dict to dataframe convert and save to the csv file
data = pd.DataFrame(company_info_dict)
data.to_csv('data/100_remote_company.csv')

print('Done')