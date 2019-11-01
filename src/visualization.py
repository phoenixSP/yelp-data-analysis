#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:47:51 2019

@author: pal00007
"""

import gmplot 
import os

#%%
data_folder = "/home/pal00007/Documents/big_data/CSCI5751/data"

#%%
gmap = gmap = gmplot.GoogleMapPlotter(37.428, -130.145, 4)
gmap.draw(os.path.join(data_folder,"map.html"))

#%%
import json
with open(os.path.join(data_folder,"business_latlong_json.json")) as location_data:
    data = json.load(location_data)
    
#%%
locations = data['Food']

#%%
locations_tofloat = [list(map(float, i)) for i in locations]
locations_usa = [[i, j] for [i,j] in locations_tofloat if 25 <= i <=50 and -130 <= j <= -70 ]

#%%

