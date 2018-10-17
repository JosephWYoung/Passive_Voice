# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.path.append(r'R:\JoePriceResearch\Python\Anaconda3\Lib\site-packages')

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json


## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

## Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']



doi_doc = FullDoc(doi = '10.1016/S1525-1578(10)60571-5')
if doi_doc.read(client):
    print ("doi_doc.title: ", doi_doc.title)
    doi_doc.write()   
else:
    print ("Read document failed.")
