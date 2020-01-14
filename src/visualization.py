#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:47:51 2019

@author: pal00007
"""

from gmplot import *
import os
import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
#%%
data_folder = "/home/pal00007/Documents/big_data/CSCI5751/data"


#https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/
gmap = gmplot.GoogleMapPlotter(37.428, -130.145, 4)
gmap.apikey = '..' #removing the api key 



with open(os.path.join(data_folder,"business_latlong_json.json")) as location_data:
    data = json.load(location_data)
    
#%%


colors = ['r', 'g', 'b']
keys = ['Food', 'Automotive', 'Home Services']
data_3cat = { key: data[key] for key in keys}

for i, key in enumerate(data_3cat):
    locations = data_3cat[key]
    locations_tofloat = [list(map(float, i)) for i in locations]
    
    #extracting data only for USA
    locations_usa = [[i, j] for [i,j] in locations_tofloat if 19 <= i <=64 and -162 <= j <= -70 ]
    
    locations_usa = np.array(locations_usa)
    latitude = locations_usa[:,0]
    longitude = locations_usa[:,1]
    
    gmap.scatter( latitude[:20], longitude[:20], color = colors[i] ,  size = 40)


gmap.draw(os.path.join(data_folder,"map.html"))

#%%
#Attempt using GeoPandas
#data = {'latitude': latitude[: 100], 'longitude': longitude[:100]}
#pd_data = pd.DataFrame.from_dict(data)
#gdf = geopandas.GeoDataFrame(pd_data, geometry= geopandas.points_from_xy(pd_data.longitude, pd_data.latitude))
#
#world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
#ax = world[world.continent == 'North America'].plot(color = 'white', edgecolor = 'black')
## We can now plot our ``GeoDataFrame``.
#gdf.plot(ax=ax, color='red', figsize= (8,8))
#
#plt.show()