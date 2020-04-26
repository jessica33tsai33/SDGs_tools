# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:44:11 2019

@author: JUNG
"""

import pandas as pd
import numpy as np
from openpyxl import load_workbook
import pdfplumber


pdf_f = "Japan_DB_Colour_V3.0.pdf" 
pdf = pdfplumber.open(pdf_f)
p0 = pdf.pages[0]
df0 = p0.extract_tables()

print("pdf has been read")


for table in df0:
    df = pd.DataFrame(table[1:], columns=table[0])

print("table has been read")



df.to_csv('Japan_DB_Colour_V3.0.csv')

pdf.close()


