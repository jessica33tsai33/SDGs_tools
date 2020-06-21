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
pair_cause = np.zeros((8759, 2), dtype = object)
pair_use = np.zeros((8759, 2), dtype = object)


#translate csv to SDGs pair_use, pair_cause
x = 0

for j in range(1,170):
    for i in range(1,170):
        if df_np[i,j] != -2:
            pair_use[x,1] = str(df_np[i,0])
            pair_use[x,0] = str(df_np[0,j])
            x += 1

x = 0
for i in range(1,170):
    for j in range(1,170):
        if df_np[i,j] != -2:
            pair_cause[x,0] = df_np[i,0]
            pair_cause[x,1] = df_np[0,j]
            x += 1


#translate SDGs pair_use, pair_cause to SDGs list_use, list_cause
list_use = []
factor_list = []
factor = pair_use[0][0]
factor_list.append(str(factor))

for i in range(len(pair_use)):
    if pair_use[i][0] != factor:
        factor = pair_use[i][0]
        list_use.append(factor_list)
        factor_list = []
        factor_list.append(str(factor))
        
    factor_list.append(str(pair_use[i][1]))

list_use.append(factor_list)
#print(list_use)
print("list_use has been created")


list_cause = []
factor_list = []
factor = pair_cause[0][0]
factor_list.append(str(factor))

for i in range(len(pair_cause)):
    if pair_cause[i][0] != factor:
        factor = pair_cause[i][0]
        list_cause.append(factor_list)
        factor_list = []
        factor_list.append(str(factor))

    factor_list.append(str(pair_cause[i][1]))

list_cause.append(factor_list)
#print(list_cause)
print("list_cause has been created")


def check_var(varList, var):
    """ 確認因子有無重複 """
    check = False
    for i in range(len(varList)):
        if var == varList[i]:
            check = True

    return check


def get_varattrib(factor, attrib):
    """
    找出子因子list
    attrib - 4：cause variable, 5：use variable
    """
    index = 0
    return_list = []
    if attrib == 4:
        for i in range(len(list_cause)):
            if factor == list_cause[i][0]:
                index = i
                break

        for i in range(1, len(list_cause[index])):
            return_list.append(list_cause[index][i])


    if attrib == 5:
        for i in range(len(list_use)):
            if factor == list_use[i][0]:
                index = i
                break
        
        for i in range(1, len(list_use[index])):
            return_list.append(list_use[index][i])


    return return_list


def creatVariableTree(factor, attrib):
    """
    建立因子的 cause/use tree list
    attrib - 4：cause variable, 5：use variable
    """
    varList = []  # 最終因子List
    tempVarList = []  # 暫存因子List
    resultList = []  # 子因子個數List
    tempList = []  # 每個因子的關係子因子List
    tempVarList = get_varattrib(factor, attrib)
    varList += tempVarList

    resultList.append(len(tempVarList))

    while len(tempVarList) != 0:
        if tempVarList[0] == 0:
            resultList.append(0)
        else:
            tempList = get_varattrib(tempVarList[0], attrib)
            resultList.append(len(tempList))
            for i in range(len(tempList)):
                if check_var(varList, tempList[i]) == True:    
                    varList.append(tempList[i])
                    tempVarList.append(0)

                else:
                    tempVarList.append(tempList[i])
                    varList.append(tempList[i])

        tempVarList.pop(0)
    
    firstVarList = []
    for i in range(resultList[0]):
        firstVarList.append(varList[i])
    
    return (varList, resultList, firstVarList)


"""
#start creating variable tree
factor = '1.1'
attrib = 5  # 4：cause variable, 5：use variable

a = creatVariableTree(factor, attrib)

print(a[0])
print(a[1])
print(len(a[0]))
print(len(a[1]))
print(sum(a[1]))
"""