#!/usr/bin/env python
# coding: utf-8

# # Basic Britishpoliticalspeech.org Scraper (CSV)
# 
# This python based scraper will scrape British political speeches from political leaders in the UK from Britishpoliticalspeech.org. When fully run the scraper will output a CSV file containing basic metadata about the speeches and the speeches themselves. These could for further analysis with for instance tools from the Pandas library.

# In[1]:


import sys
import csv
import requests
import re
from bs4 import BeautifulSoup


# In[2]:


def load_page(url):
    with requests.get(url) as f:
        page = f.text
    return page


# ## Locate the Data
# 
# The MetaData is inside of the < tbody > tag. Each row is either inside a < tr class="odd" > tag or in a < tr > tag. Every attribute (Date, Party, Speaker, Title) is in a < td > tag

# In[3]:


def get_speech_data(url):
    speech_page = BeautifulSoup(load_page(url), 'lxml')       
    if not speech_page:                                            
        print('Something went wrong!', file=sys.stderr)
        sys.exit()
    data = []
    for count, row in enumerate(speech_page.find_all('tr')[2:]):
    #for row in speech_page.find_all('tr')[2:]:
        dates = row.find_all('td')[0]
        parties = row.find_all('td')[1]
        speakers = row.find_all('td')[2]
        speech = row.find_all('td')[3]
        link = row.find('a').get('href')
        data.append({
            'id' : parties.text + '_' + str(count),
            'date': dates.text,
            'speaker': speakers.text,
            'party': parties.text,
            'name speech': speech.text,
            'link': 'http://britishpoliticalspeech.org/' + link
        })
    return data


# In[4]:


def get_speech(url):
    speech_page = BeautifulSoup(load_page(url), 'lxml')                  
    interesting_html = (speech_page.find(class_='speech-content').text.strip()
        .replace('\xa0\n', '').replace('\n','').replace('\x85','').replace('\u2011',''))
    skip_check = 'Owing to a copyright issue this speech has been removed.'
    speaker_html = speech_page.find(class_='speech-speaker').text.strip().split('(', 1)[0]
    location_html = speech_page.find(class_='speech-location').text.strip()
    if 'Location: ' in location_html:
        location_html = location_html.replace('Location: ', '')
    if not interesting_html or skip_check in interesting_html: # or not speaker_html or not location_html don't really care about not finding these
        #print('Skipped - No information available for {}'.format(url), file=sys.stderr)
        return {}                                                      
    return {'speech' : interesting_html, 'speaker' : speaker_html, 'location' : location_html}


# ## Scraping the Data

# In[5]:


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


# In[6]:


with open('speech_metadata.csv', 'w', encoding='utf-8') as f:       # Open a csv file for writing
    fieldnames=['id','speaker', 'party', 'location', 'date', 'name speech',
                'speech']                                 # These are the values we want to store
    writer = csv.DictWriter(f,
                            delimiter=',',                # Common delimiter
                            quotechar='"',                # Common quote character
                            quoting=csv.QUOTE_NONNUMERIC, # Make sure that all strings are quoted
                            fieldnames=fieldnames
                            )
    writer.writeheader()                                  # Create headers in our csv file
    for row in list_speech_data:
        writer.writerow({k:v for k,v in row.items() if k in fieldnames})

