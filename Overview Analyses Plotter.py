from pandas import DataFrame, read_csv
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import numpy as np
import re
matplotlib.style.use('ggplot')

Location = r'Ref data.csv'
df = pd.read_csv(Location)

## Filter to only the references
Refs = df[df.Reference == 'YES']

## NAME THE COLUMNS CORRECTLY
Refs.columns = ['File', 'Date of test', 'Scientist', 'CL', 'CW', 'Mobility', 'SDev', 'On/Off', 
 'VTO', 'VTH', 'Yield', 'Temp_Fish', 'Temp_Cal','Hum_Fish', 'Hum_Cal','Reference', 'Cap']


## Filter to exlude any not featuring humidity (calibrated)
Refs = Refs[Refs.Hum_Cal != '-']
Refs = Refs[Refs.Temp_Cal != '{T}']
## Filter to be only 40 and 5 um channels (do on widths as more exact thus easier)
Refs = Refs[Refs['CW'].isin([1005, 1115])]
Refs = Refs.round({'Cap': 9})
Refs = Refs.drop(['Temp_Fish','Hum_Fish','Reference','File'], axis=1)
Refs['L'] = Refs['CW']
Refs['L'] = Refs['L'].map({1005: 40, 1115: 5})

Refs['Mobility'] = Refs['Mobility'].astype('float')
Refs['Hum_Cal'] = Refs['Hum_Cal'].astype('float')
Refs['Temp_Cal'] = Refs['Temp_Cal'].astype('float')
Refs['VTO'] = Refs['VTO'].astype('float')
colors = np.where(Refs.Cap > 7E-9, 'r', 'g')

import seaborn as sns
g = sns.FacetGrid(Refs, row = "L", col = "Cap")
g.map(plt.scatter, "Mobility","VTO")

import seaborn as sns
g = sns.FacetGrid(Refs, row = "L", col = "Cap")
g.map(plt.scatter, "Mobility","Hum_Cal")

import seaborn as sns
g = sns.FacetGrid(Refs, row = "L", col = "Cap")
g.map(plt.scatter, "Mobility","Temp_Cal")

