from bs4 import BeautifulSoup 
import urllib
import re
import csv
import lxml.html as lh
from tabulate import tabulate
import json
import requests
import argparse
import logging
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Not Required
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

try:

    statelst=[]
    source = urllib.request.urlopen("https://www.mohfw.gov.in/").read()
    soup = BeautifulSoup(source,"html.parser")
    container = soup.find("div",class_ = "content newtab")
    
    for item in container:
        tb = container.find('table', class_='table table-striped table-dark')
    
    #tb = container.find_all('table', class_='table table-striped table-dark')
    #tb = soup.find('table', class_='table table-striped table-dark')
        for item in tb.find_all("tr"):
            _content = item.find_all("td")
            state=[]
            for _fdata in _content:         
                state.append(_fdata.text)
            statelst.append(state)

        statelst = [value[1:] for value in statelst if len(value) == 6]  
    #cur_data = {x[1]: {current_time: x[1:]} for x in statelst if len(x) == 5 }
        statedict = {x[1]: {x[0]: x[1:]} for x in statelst if len(x) == 5 }
    
    # Saving Data to Json Format
    #with open('data.json', 'w') as fp:
    #    json.dump(statedict, fp)
    
    # Create a dataframe
    dtstate = pd.DataFrame(statelst,columns =["states","total_Cases","foreign_national","cured","total_deaths"])
    #dtstate.info()
    
    # EXplotary Data Analysiswith open("copy.txt", "w") as file:
    file.write("Your text goes here")
    #dtstate["total_Cases"].hist()
    plt.bar(dtstate["states"],dtstate["total_Cases"])
    
    
    
except:
    logging.exception('oops, corono script failed.')
