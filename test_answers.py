# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:47:21 2020

@author: PVS
"""

import   os
import   pandas  as  pd


folder_name     =   r'D:\GL_DSE_Interview\2020-11-06-Interview'
file_name       =   'test_answers1.csv'

os.chdir(folder_name)
os.listdir('D://GL_DSE_Interview/2020-11-06-Interview')

df                  =    pd.read_csv(file_name, encoding= 'unicode_escape')
print('\nColumns {}'.format(df.columns))

print(df.head())

print(df['Q1'])
