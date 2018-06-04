# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 12:40:06 2018

@author: avatash.rathore
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np 


Dataset = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')

print(Dataset.head())

Dataset.columns=["age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","race","sex","capital_gain","capital_loss","hours_per_week","native_country","Salary-Slab"]


print(Dataset.head())
print('='*34)
print('1. Create an sqlalchemy engine using a sample from the data set')
import sqlalchemy
import sqlite3

from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqladb', echo=False)

Dataset.to_sql('sqladb', engine, if_exists='replace')
connection = sqlite3.connect("sqladb")
cmd = connection.cursor()

print('2.Write two basic update queries')
cmd.execute('UPDATE sqladb SET Capital_gain = "10",Capital_loss="01" WHERE age >50 ')
print(pd.read_sql_query('SELECT * FROM sqladb where age >50' , connection).head())
cmd.execute('UPDATE sqladb SET workclass = "State-gov" WHERE workclass=" Local-gov" ')
print(pd.read_sql_query('SELECT * FROM sqladb where workclass="State-gov"' , connection).head())


print('3.Write two delete queries')
cmd.execute('Delete from sqladb WHERE education_num ="4" and age < 20 ')
print(pd.read_sql_query('SELECT * FROM sqladb where education_num ="4" and age < 20' , connection).head())
cmd.execute('Delete from  sqladb WHERE education like "%#%" ')
print(pd.read_sql_query('SELECT * FROM sqladb where workclass="State-gov"' , connection).head())


print('4. Write Two Filter Queries')
print(pd.read_sql_query("SELECT distinct(workclass)  FROM sqladb where workclass like '%-%' ", connection))
print(pd.read_sql_query("SELECT * FROM sqladb where education_num in ('13','9')", connection))


print('5: Write two function queries')
def Insert_single_row(DBname, new_data):
    v = ',?' * (len(new_data)-1) 
    query = "INSERT INTO "+ DBname +" VALUES (?"+ v +");"
    cmd.execute(query,list(new_data))
    
Insert_single_row('sqladb',('32557', '50','Private', '384675', 'HS#grad', '9', 'Divorced', 'Executive', 'Not-in-family', 'White', 'INHUMAN', '0', '0', '40', 'United-States', '>=50K'))
print(pd.read_sql_query("Select * from sqladb where education like '%#%'", connection))
                        
                        
def distribution(Column):
   K =pd.read_sql_query("Select "+ Column+",Count(*) as Frequency from sqladb group by "+ Column+"", connection)
   return K                         
             
print(distribution('education')) 

print(distribution('sex')) 
print(distribution('relationship')) 
print(distribution('race')) 
          