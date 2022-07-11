# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# initializing comapnay_names, comapnay_descriptions and links
company_names = []
company_descriptions = []
links = []


# Iterator all the pages and scrap data

for x in range(1, 306): #total 306 page available

    url = 'https://weworkremotely.com/remote-companies?page='
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.content, 'html.parser')
    containers = soup.find('div', class_='jobs-container').find_all('li')

    for container in containers:
        # Comapny name
        company_name = container.find('span', class_='company')
        if company_name is None:
            company_name = ''
        else:
            company_name = company_name.text

        # Company description
        company_description = container.find('span', class_='company-title')
        if company_description is None:
            company_description = ''
        else:
            company_description = company_description.text

        # company link
        link = container.find('a', href=True)
        if link is None:
            link = ''
        else:
            company_url = 'https://weworkremotely.com'
            link = company_url + link['href']


        # append all the details to our intialized lists
        company_names.append(company_name)
        company_descriptions.append(company_description)
        links.append(link)

    # Display remaining page info
    print(f'Scraping page: {x}, Total remaiing page: {306 -x}')
    time.sleep(3)



# all details lists to dict
company_info_dict = {
        'company_name': company_names,
        'company_description' : company_descriptions,
        'link': links
    }


# Comvert dictioneries to pandas dataframe and save it
data = pd.DataFrame(company_info_dict)
data.to_csv('data/all_remote_company.csv')

print(f"Done..")