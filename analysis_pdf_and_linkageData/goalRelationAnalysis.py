# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:21:53 2020

@author: Tsai Jessica
"""

import pandas as pd
import numpy as np
import json

df = pd.read_csv('goalRelation.csv', header=None, dtype=float)

#print(df)

df_np = np.array(df)
#print(df_np)
total = []

for i in range(16):
    sub = []
    for j in range(i+1,17):
        sub.append(df_np[i+1, j+1] + df_np[j+1, i+1])
    total.append(sub)

#print(total)

sdgGoal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

Data = {}
nodes = []
links = []
for i in range(len(sdgGoal)):
    subNode = {}
    subNode['id'] = sdgGoal[i]
    subNode['group'] = sdgGoal[i]
    nodes.append(subNode)

Data["nodes"] = nodes


for i in range(len(total)):
    for j in range(len(total[i])):
        subLink = {}
        subLink['source'] = sdgGoal[i]
        subLink['target'] = sdgGoal[i+j+1]
        subLink['value'] = total[i][j]
        links.append(subLink)

Data["links"] = links

with open('goalRelation.json', 'w') as outfile:
    json.dump(Data, outfile)