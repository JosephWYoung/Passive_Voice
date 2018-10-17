# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:59:00 2018

@author: josephwy
"""
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


with open("config.json") as con_file:
    config = json.load(con_file)

## Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

doi_doc = FullDoc(doi = "10.1016/S1525-1578(10)60571-5")
if doi_doc.read(client):
    print ("doi_doc.title: ", doi_doc.title)
    doi_doc.write()
    print(doi_doc.data['originalText'])
else:
    print ("Read document failed.")