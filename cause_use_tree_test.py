# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:51:40 2020

@author: Tsai Jessica
"""

from ema_workbench.connectors import vensim
from ema_workbench.connectors import vensimDLLwrapper as venDLL

def creat_var_list(var):
    """ 整理 get_varattrib 函式所產出的因子list """
    varlist = []
    for i in range(len(var)):
        subvar = var[i]
        if i == 0:
            subvar = subvar[2:]
        varlist.append(subvar)

    if len(varlist[0]) == 0:
        varlist = []
        return varlist
    else:
        return varlist


def check_var(varList, var):
    check = False
    for i in range(len(varList)):
        if var == varList[i]:
            check = True

    return check

vensim.load_model(r"C://Users//Tsai Jessica//NTU//sdlab//SDGs_tools//class1_water1.vpm")

factor = "outflow"
attrib = 4  # 4：cause variable, 5：use variable


varList = []
tempVarList = []
resultList = []

tempVarList = creat_var_list(venDLL.get_varattrib(factor, attrib))
for i in range(len(tempVarList)):
    varList.append(tempVarList[i])

resultList.append(len(tempVarList))

while len(tempVarList) != 0:
        tempList = creat_var_list(venDLL.get_varattrib(tempVarList[0], attrib))
        
        resultList.append(len(tempList))
        for i in range(len(tempList)):
            if check_var(varList, tempList[0]) == False:
                tempVarList.append(tempList[i])
                varList.append(tempList[i])
        
        tempVarList.pop(0)
        
            

print(varList)
print(resultList)