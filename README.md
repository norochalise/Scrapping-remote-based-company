# Scrapping-data-of-remote-based-company
Nowadays, remote work is more in demand than a traditional workspace. It's more popular after the pandemic. Many companies were doing their work in remote setups before the pandemic. Numerous people prefer remote work for various reasons. Relocated themself also not suitable for many reasons. So they are looking for remote job opportunities for their career growth. 

I did this projects for helps to the people who are looking remote job oppurtinties. I collected this data from [we work remotely](https://weworkeremotely.com/). For scrapping data I used Python langugue, beautiful soup, requests, and pandas python libraries. 

## Prerequisites
Install Python3 in your machine.


## Installation

  1. Open Command Line Interface
  2. Run the command ```git clone https://github.com/norochalise/Scrapping-remote-based-company.git``` to clone the repository
  3. Run the command ```cd Scrapping-remote-based-company``` to change directory
  4. For **Linux user** run command ``` python3 -m venv venv``` to create virtual environment. For **Window user** run ```python -m venv venv ```
  5. To Activate virtual environment for linux user run ```source venv/bin/activate ``` For window user run ``` .\venv\activate ```
  6. Run the command ```pip install -r requirements.txt``` to install all the dependencies

  7. Run the python desired python script. For exapmle ```python 100_remote_company.py```

  If there're any challenges while installing dependencies, run the command below to upgrade pip and try again. 

```python -m pip install --upgrade pip```

Some command can be different based on the OS so please  consider it.

**NOTE:** For more information of each files and folder please looks below section. 


## Files Info

1. ```100_remote_company.py``` For extracting top 100 remote based comapny information. After that I generate ```100_remote_company.csv``` dataset in data folder.
2. ```all_remote_company.py``` For extracting all remote company info and generate ```all_remote_company.csv``` dataset in data folder

3. ```update.py``` Gather more information about company from the 100_remote_company.csv file and do some cleaning. After that I generat and saved ```updated_100_remote_company.csv``` dataset to the data folder. 

## Author
Noro Chalise
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/norochalise/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/norochalise)
