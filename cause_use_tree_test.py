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


vensim.load_model(r"C://Users//Tsai Jessica//NTU//sdlab//SDGs_tools//class1_water1.vpm")

factor = "outflow"
cause = 4
use = 5
resultList = []

a = creat_var_list(venDLL.get_varattrib(factor, cause))
resultList.append(a)

print(len(a))

stop = False
i = 0

while stop == False:
    if len(a) == 0:
        stop = True
    else:
        factor = a[i]
        #resultList.append(creat_var_list(venDLL.get_varattrib(factor, cause)))