# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:02:54 2020

@author: P.V.SUBRAMANIAN
Ref: https://pythonhow.com/adding-more-pages-to-the-website/

https://www.tutorialspoint.com/flask/flask_quick_guide.htm
"""
from   flask             import Flask, flash, redirect, render_template, request, url_for, session
import random
from   datetime          import  datetime
import sys, os
import random
import string
import mysql.connector

folder_name = r'D:\GL_DSE_Interview\Skill_Assessment_CSI'
sys.path.insert(0, folder_name) 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from db_Class  import  Employee

error = None
emp              =    Employee("localhost","testUser", "A4min@123","employees" )
connection       =    emp.db_connection()
emp.db_create_table()
        
### 
### Insert data 
###
        
n =  20
        
for i in range(n):
        
            FN_list = ["Arun", "Arockia", "Alex", "Amin", "Bhim", "Chandar", "Durvan", "Durvik", "Dhanis", "Yashnav", \
                       "Sheshvan", "Sowgatha", "Vijaychandra", "Vijay", "Praveen", "Arya", "Ritesh", "Piyush",\
                       "Arya","Xavier"]
            
            FN_list_Female= ["Anika", "Parvathi Devi", "Aslesha", "Aashna", "Ahalya", "Anamika",\
                             "Bianca", "Binal", "Bina", "Bagya", "Saranya", "Diana", "Disha",\
                             "Deepti", "Esha", "Estaa", "Eshika", "Firaki", "Fanha", "Gina", "Gauri",\
                             "Hasina", "Hrithika", "Isha", "Iravati"]
            DEPTNAME_list =  ['HR & Admin', 'Finance & Accounts' , 'Production', 'Sales & Marketing', 'Purchase'] 
            
            DEPTNAME      =  random.choice(DEPTNAME_list)  
            DEPTNAME      =  random.choice(DEPTNAME_list)  
            DEPT_ID       =  str(DEPTNAME_list.index(DEPTNAME)  +  1) 

            DOJ_list      =  ['1990-01-31', '1998-10-31','1997-03-31','2000-04-01','2001-04-11',\
                              '1995-07-21', '2002-05-24','2004-01-22','2008-07-01','2010-08-01',\
                              '1997-11-01', '1997-11-01','1996-09-20','2014-02-03','1993-11-03',\
                              '2010-01-11', '2009-11-09','2017-10-20','2009-10-11','2008-03-20']    
          
            DOJ           =  random.choice(DOJ_list)
            
            EMP_ID        =  str(random.randrange(1000, 9000))    
            FN            =  random.choice(FN_list)
            LN            =  random.choice(random.choice(string.ascii_uppercase))
            AGE           =  str(random.choice(list(range(21, 66))))
            SEX           =  random.choice(['M', 'F'])
            INCOME        =  str(round(float(random.random()) * 100000,0))

            
            emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN, LN, AGE, 'M', INCOME, DOJ) # Male employees

            EMP_ID        =  str(random.randrange(100, 900))    
            FN_Female     =  random.choice(FN_list_Female)    
            LN            =  random.choice(random.choice(string.ascii_uppercase))
            AGE           =  str(random.choice(list(range(21, 65))))
            SEX           =  random.choice(['M', 'F'])
            INCOME        =  str(round(float(random.random()) * 100000,0))
            
            emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN_Female, LN, AGE, 'F', INCOME, DOJ) # Female employees
            
            

###

DEPTNAME_list      =  ['HR & Admin', 'Finance & Accounts' , 'Production', 'Sales & Marketing', 'Purchase'] 
MANAGER_list       =  ['HR00', 'FA00' , 'PR00' , 'SM00', 'PU00']
NAME_list          =  ['Rosy' , 'Peter', 'Arul', 'Murugan', 'Sowmya']
LN                 =  random.choice(random.choice(string.ascii_uppercase))
SEX_list           =  ['F', 'M', 'M', 'M', 'F']
DOJ_list_Manager   =  ['2010-01-11', '2009-11-09','2017-10-20','2009-10-11','2008-03-20']  

for i in range(len(DEPTNAME_list)):
    DEPTNAME       =  DEPTNAME_list[i]  
    DEPT_ID        =  str(i +  1) 
    EMP_ID         =  MANAGER_list[i] 
    FN_MANAGER     =  NAME_list[i]
    SEX            =  SEX_list[i]
    DOJ            =  DOJ_list_Manager[i]
    
    emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN_MANAGER, LN, AGE, SEX, INCOME, DOJ)  
    emp.insertVariblesIntoTable2(DEPT_ID, DEPTNAME, EMP_ID)
           
sql_select     =  """SELECT CONVERT(count(*), CHAR) FROM EMPLOYEE"""
cursor         =  connection.cursor()
cursor.execute(sql_select)
count          =  cursor.fetchone()
        
print("\n Total Employee records inserted is %s" % count)
out_1          =  "\nTotal Employee records inserted is %s" % count

sql_select1    =  """SELECT CONVERT(count(*), CHAR) FROM DEPARTMENT"""
cursor         =  connection.cursor()
cursor.execute(sql_select1)
count          =  cursor.fetchone()
        
print("\n Total Department records inserted is %s" % count)
out_2          =  "\nTotal Department records inserted is %s" % count





file_name_out  =  'SQL_Test at ' + str(current_time) + ".txt"

f   =  open("SQL_test_log.txt", "w")

f.write(file_name_out)
f.write("\n==========\n")
f.write(out_1)

f.write("\n==========\n")
f.write(out_2)

### Q1 Select the Oldest Male employee 
        
sql_select_old1      =  """SELECT FIRST_NAME, LAST_NAME, CONVERT(AGE, CHAR) AS AGE """
sql_select_old2      =  """FROM EMPLOYEE """
sql_select_old_male3 =  """WHERE AGE = ALL(SELECT MAX(AGE) FROM EMPLOYEE WHERE SEX = 'M') AND SEX = 'M';"""
 
sql_select_old_male  = sql_select_old1 + "\n" + sql_select_old2 + "\n" + sql_select_old_male3

f.write("\n\nQ1 Select the Oldest Male employee")
f.write("\nQuery\n")    
f.write(sql_select_old_male)   
                  
print(sql_select_old_male)
cursor.execute(sql_select_old_male)
        
results_M           =  cursor.fetchone()
print('\nOldest Male : {}'.format(results_M))

try: 
    M_name              =  "\nMale employee name : " + results_M[0] + " " + results_M[1] + " Age : " + results_M[2]
    f.write(M_name )
except:
    print("\nError")    
        
# ### Q2 Select the Oldest Female employee 

sql_select_old_female3 =  """WHERE AGE = ALL(SELECT MAX(AGE) FROM EMPLOYEE WHERE SEX = 'F') AND SEX = 'F';"""

sql_select_old_female =  sql_select_old1 + "\n" + sql_select_old2 + "\n" + sql_select_old_female3

f.write("\n\nQ2 Select the Oldest Female employee")
f.write("\nQuery\n")     
f.write(sql_select_old_female) 
 
print(sql_select_old_female)                                       
cursor.execute(sql_select_old_female)
        
results_F           =  cursor.fetchone()

print('\nOldest Female : {}'.format(results_F)) 
try: 
    F_name              =  "\nFemale employee name : " + results_F[0] + " " + results_F[1] + " Age : " + results_F[2]
    f.write(F_name )
except:
    print("\nError")     


# sid  = 'GL-DSE'
                          

# disconnect from server
cursor.close() 
f.close()