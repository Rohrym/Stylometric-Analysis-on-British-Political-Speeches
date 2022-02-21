# Stylometric Analysis on British Political Speeches
An exploratory research project focussing on extracting and analysing speeches from British political leaders, chief among them Winston Churchill.
This project aims to determine to which political party the speeches of Winston Churchill circulated from 1939 to 1940 come closer. 
Once the data were defined by focusing on two different archives, the [Britishpoliticalspeech.org](http://britishpoliticalspeech.org/) archive and the [International Churchill Society](https://winstonchurchill.org/), it used the scraping technique to extract data. 
Then, the three levels of stylometric analysis were used to provide answers to our research question, determining where exactly in the political spectrum of the British Parliament Churchill’s Speeches fell during the relevant time. 
The whole process we have documented in a Juypiter Books format which can be found using this [link.](https://paschalisag.github.io/jupy_book_churchill/html_code/political_party_stylometric_analysis-Copy1.html)

This file constitutes a guide of the repository containing all the relevant information for the existing holdings of the Project. 

The first main folder titled 'Analysis' contains two Juypiter Notebooks. One used to do some initial exploratory analysis and another to conduct the stylometric Analysis of the collected texts. The first Notebook makes use of the 'metadata.csv' file and the second makes use of the TXT files. All are found in the third folder. 

The second main folder ‘JupyterBookChurchill’ forms the basis of the Juypiter Books website. Due to some issues with hosting the Juypiter Book from this repository we have opted to host from a different repository which can be found [here.](https://github.com/PaschalisAg/jupy_book_churchill)
The contents of the repo and this folder should be identical. This folder contains eight holdings in total:
- Within this folder is stored the ‘build’ folder, which contains the ‘html’ and ‘jupyter_execute’, which contain information on how the Jupyter Book (JB) was constructed.
- It also contains the ‘_config.yml’, the code describing how interactive is the book. 
- The ‘_toc.yml’ demonstrates the table of contents, meaning what the JB is shown. 
- In addition, there is the logo of the Book in a PNG file format titled ‘ChurchillSticker1.png’. 
- Another folder within the ‘JupyterBookChurchill’ folder is the ‘html_code’ which contains two folders in total, the first called ‘images_formulas’ containing images and the second called ‘speeches’ containing all the political speeches in .txt files. In addition, the ‘html_code’ contains a CSV and a TXT file with scrapers and a copy of the stylometric analysis.
- Finally, within the ‘JupyterBookChurchill’ folder are also stored the information on the introduction of JB in a markdown shell (‘intro.md’) and two auto-generated files, the ‘refererences.bib’ and the requirements in .txt format.

The third main folder titled ‘Metadata and Texts’ is the data based on which the Juypiter Book is generated and contains a zipped (compressed) file with the whole set of texts and a CSV file with all the metadata. Most TXT files and the CSV file have been scraped, however TXT files for Winston Churchill's speeches (speeches 355 to 364) have been manually added. The selected variables of the dataset are the following: 'id', which was generated to uniquely identify every tuple, the 'speaker', the full name of each politician, accompanied by the First, (optional) Middle and (a set of) Surname(s), 'party', indicating the MPs, Parliamentarians / Political groups / formations, 'location', the place where each speech took place, 'date', the exact day/month/year the speech was delivered, 'name speech', a generated title and lastly the 'speech'.

The fourth main folder, titled as ‘Scrapers’, contains anew Juypiter Notebooks which scraped the Britishpoliticalspeech archive for respectively speech's metadata (CSV scraper) and the texts themselves (most importantly the TXT scraper).

Finally, the repository contains a few more files, the ‘mynewbook’, which is an auto-generated file, a Creative Commons Attribution 4.0 International Public License and the Data Management Plan using the ‘Science Europe Template’.
