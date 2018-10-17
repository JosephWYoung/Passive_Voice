# -*- coding: utf-8 -*-
"""
Joseph Young - 11/28/2017

[In Progress]; Uses elsapy module to scrape from Elsevier's Science Direct API
"""
from query_categories import subj_areas, comm_words
import os
import re
import pandas as pd
import pickle
import json
import requests as r
import sys
sys.path.append('R:\\JoePriceResearch\\Python\\Anaconda3\\Lib\\site-packages')

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch

## Load configuration
with open("config.json") as con_file:
    config = json.load(con_file)

## Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

# test = r.get('https://api.elsevier.com/content/article/doi/' + TEST_DOI)
# with open('test_sd.xml', 'w') as output_xml_file:
#     print(test.text, file=output_xml_file)

#subj_areas = ["AGRI","ARTS","BIOC","BUSI","CENG","CHEM","COMP","DECI","DENT",
             # "EART","ECON","ENER","ENGI","ENVI","HEAL","IMMU","MATE","MATH",
             #"MEDI","NEUR","NURS","PHAR","PHYS","PSYC","SOCI","VETE","MULT"]


#Stop-Words listed in the Sci-Dir. Expert search (deemed non-distinct)

DOI_List= []
Data_Headers = ["Subj_Area", "DOI"]

for subj in subj_areas:
    for word in comm_words:
        subj_srch = ElsSearch("{" + word + "}" + '+SUBJAREA(' + subj + ')','scidir')
        subj_srch.execute(client)
        
        for article in subj_srch.results:
            if "dc:identifier" in article:
                DOI_List.append((subj, article["dc:identifier"]))
                print (subj, ": " , article["dc:identifier"])

#output data as csv
table = pd.DataFrame(data=DOI_List, columns=Data_Headers)
table.to_csv('Article_DOIs.csv', index=False)
                
            
"""doi_doc = FullDoc(doi = TEST_DOI)
if doi_doc.read(client):
    print ("doi_doc.title: ", doi_doc.title)
    doi_doc.write()
    print(doi_doc.data['originalText'])
else:
    print ("Read document failed.")
"""
