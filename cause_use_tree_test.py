# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:51:40 2020

@author: Tsai Jessica
"""

from ema_workbench.connectors import vensim
from ema_workbench.connectors import vensimDLLwrapper as venDLL

vensim.load_model(r"C://Users//Tsai Jessica//NTU//sdlab//SDGs_tools//class1_water1.vpm")

a = venDLL.get_varattrib("outflow", 5)

print(a)