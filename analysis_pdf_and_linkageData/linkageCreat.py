# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:29:26 2020

@author: Tsai Jessica
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Japan_DB_Colour_V3.0.csv', header=None, dtype=str)

df_nafilled = df.fillna(-2)
print("null has been filled")

df_np = np.array(df_nafilled)
pair_use = np.zeros((8759, 2), dtype = object)
useValue = []  # 存 use 的數值正負關係
pair_cause = np.zeros((8759, 2), dtype = object)
causeValue = []  # 存 cause 的數值正負關係


#translate csv to SDGs pair_use, pair_cause
x = 0

for i in range(1,170):
    for j in range(1,170):
        if df_np[j,i] != -2:
            pair_use[x,1] = str(df_np[j,0])
            pair_use[x,0] = str(df_np[0,i])
            useValue.append(df_np[j,i])
            x += 1

x = 0
for i in range(1,170):
    for j in range(1,170):
        if df_np[i,j] != -2:
            pair_cause[x,0] = str(df_np[i,0])
            pair_cause[x,1] = str(df_np[0,j])
            causeValue.append(df_np[i,j])
            x += 1
#print(pair_use[166, 1])

#translate SDGs pair_use, pair_cause to SDGs list_use, list_cause
list_use = []  # 把pair的形式改成目標target放第一，後面全是他的子target，二維list
factor_list = []
list_use_value = []  #跟list_use格式一樣，但內容填目標target對子target的關係值
value_list = []
factor = pair_use[0][0]
factor_list.append(str(factor))
value_list.append(-2)

for i in range(len(pair_use)):
    if pair_use[i][0] != factor:
        factor = pair_use[i][0]
        list_use.append(factor_list)
        list_use_value.append(value_list)
        
        factor_list = []
        factor_list.append(str(factor))
        value_list = []
        value_list.append(-2)
        
    factor_list.append(str(pair_use[i][1]))
    value_list.append(useValue[i])

list_use.append(factor_list)
list_use_value.append(value_list)
#print(list_use)
print("list_use has been created")

list_cause = []
factor_list = []
list_cause_value = []  #跟list_use格式一樣，但內容填目標target對子target的關係值
value_list = []
factor = pair_cause[0][0]
factor_list.append(str(factor))
value_list.append(-2)

for i in range(len(pair_cause)):
    if pair_cause[i][0] != factor:
        factor = pair_cause[i][0]
        list_cause.append(factor_list)
        list_cause_value.append(value_list)
        
        factor_list = []
        factor_list.append(str(factor))
        value_list = []
        value_list.append(-2)

    factor_list.append(str(pair_cause[i][1]))
    value_list.append(causeValue[i])

list_cause.append(factor_list)
list_cause_value.append(value_list)
#print(list_cause)
print("list_cause has been created")

def get_varattrib(factor, attrib):
    """
    找出子因子list
    attrib - 4：cause variable, 5：use variable
    """
    index = 0
    return_list = []
    return_list_value = []
    if attrib == 4:
        for i in range(len(list_cause)):
            if factor == list_cause[i][0]:
                index = i
                break

        for i in range(1, len(list_cause[index])):
            return_list.append(list_cause[index][i])
            return_list_value.append(list_cause_value[index][i])

    if attrib == 5:
        for i in range(len(list_use)):
            if factor == list_use[i][0]:
                index = i
                break
        
        for i in range(1, len(list_use[index])):
            return_list.append(list_use[index][i])
            return_list_value.append(list_use_value[index][i])

    return (return_list, return_list_value)

"""
#start creating variable tree
factor = '1.1'
attrib = 5  # 4：cause variable, 5：use variable

a = get_varattrib(factor, attrib)

print(a[0])
print(a[1])
print(len(a[0]))
print(len(a[1]))
print(sum(a[1]))
"""