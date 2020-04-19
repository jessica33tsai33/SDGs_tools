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
    """ 確認因子有無重複 """
    check = False
    for i in range(len(varList)):
        if var == varList[i]:
            check = True

    return check

def creatVariableTree(model, factor, attrib):
    """
    建立因子的 cause/use tree list
    attrib - 4：cause variable, 5：use variable
    """
    vensim.load_model(model)
    varList = []  # 最終因子List
    tempVarList = []  # 暫存因子List
    resultList = []  # 子因子個數List
    tempList = []  # 每個因子的關係子因子List
    tempVarList = creat_var_list(venDLL.get_varattrib(factor, attrib))
    varList += tempVarList

    resultList.append(len(tempVarList))

    while len(tempVarList) != 0:
        tempList = creat_var_list(venDLL.get_varattrib(tempVarList[0], attrib))
        resultList.append(len(tempList))
        for i in range(len(tempList)):
            if check_var(varList, tempList[i]) == True:    
                varList.append(tempList[i])

            else:
                tempVarList.append(tempList[i])
                varList.append(tempList[i])

        tempVarList.pop(0)
    
    return (varList, resultList)


factor = '"16.b"'
attrib = 4  # 4：cause variable, 5：use variable


model = "C://Users//Tsai Jessica//NTU//sdlab//SDGs_tools//SDGs linkage_SDG 1_3.vpm"
a = creatVariableTree(model, factor, attrib)

print(a[0])
print(a[1])

print(len(a[0]))
print(sum(a[1]))