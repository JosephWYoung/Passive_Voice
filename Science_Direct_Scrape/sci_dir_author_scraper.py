# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:29:55 2018

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

my_auth = ElsAuthor(
        uri = 'https://api.elsevier.com/content/author/author_id/36515313000')
# Read author data, then write to disk
if my_auth.read(client):
    print ("my_auth.full_name: ", my_auth.full_name)
    my_auth.write()
else:
    print ("Read author failed.")