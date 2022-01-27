#!/usr/bin/env python
# coding: utf-8

# # Basic Britishpoliticalspeech.org Scraper (TXT)
# 
# This python based scraper will scrape British political speeches from political leaders in the UK from Britishpoliticalspeech.org. When fully run the scraper will output a directory with txt files of all the individual speeches held. These could be used for specific textual analyses.

# In[1]:


import sys
import csv
import requests
import re
import os
from bs4 import BeautifulSoup


# In[2]:


def load_page(url):
    with requests.get(url) as f:
        page = f.text
    return page


# ## Locate the speeches

# In[11]:


def get_speech(url):
    speech_page = BeautifulSoup(load_page(url), 'lxml')                  
    interesting_html = (speech_page.find(class_='speech-content').text.strip()
        .replace('\xa0\n', '').replace('\n','').replace('\x85','').replace('\u2011',''))
    skip_check = 'Owing to a copyright issue this speech has been removed.'
    if not interesting_html or skip_check in interesting_html: # or not speaker_html or not location_html don't really care about not finding these
        #print('Skipped - No information available for {}'.format(url), file=sys.stderr)
        return {}
    return {'speech' : interesting_html}


# In[12]:


def get_speech_data(url):
    speech_page = BeautifulSoup(load_page(url), 'lxml')       
    if not speech_page:                                            
        print('Something went wrong!', file=sys.stderr)
        sys.exit()
    data = []
    #for count, row in enumerate(speech_page.find_all('tr')[2:]):
    for row in speech_page.find_all('tr')[2:]:
        speech = row.find_all('td')[3]
        link = row.find('a').get('href')
        data.append({
            'link': 'http://britishpoliticalspeech.org/' + link
        })
    return data


# ## Scraping the Data

# In[13]:


index_url = 'http://britishpoliticalspeech.org/speech-archive.htm'         # Contains a list of speeches
list_speech_data = get_speech_data(index_url)                      # Get speeches with metadata
list_rows_to_remove = []
#print (" - - - - - " + str(len(list_speech_data)))

for count, row in enumerate(list_speech_data):
    #print('Scraping info on {}.'.format(row['name speech'])) # Might be useful for debugging
    url = row['link']
    speech_info = get_speech(url)                    # Get the speech, if available
    if speech_info == {}:
        list_rows_to_remove.append(count)
    else:    
        for key, value in speech_info.items():
            row[key] = value                              # Add the new data to our dictionary
    #print('Scraped info on {}.'.format(row['name speech']) + '\t from {}.'.format(row['speakers']))

for d_elem in reversed(list_rows_to_remove): # Delete list rows in reverse to avoid errors
    #print("Speech missing - Deleted: " + str(d_elem))
    del list_speech_data[d_elem]

#print (" - - - - - " + str(len(list_speech_data)))


# In[14]:


path = "speeches/"
# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:  
    # Create a new directory because it does not exist 
    os.makedirs(path)
    print("The new directory is created!")

# Write the speeches in txt files with the id as file name
number = 1
for row in list_speech_data:
    filename = f'political_speech_{number}.txt'
    #filename = row['id']
    #print(filename)
    file1 = open(path + filename,"w")
    number += 1
    file1.writelines(row['speech'])
    file1.close() #to change file access modes    

