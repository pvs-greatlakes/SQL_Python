# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:08:56 2020

@author: PVS
"""

###
### Set 1
###
import mysql.connector, sys
from   datetime          import  datetime

folder_name = r'D:\GL_DSE_Interview\Skill_Assessment_CSI'
sys.path.insert(0, folder_name) 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from db_Class  import  Employee

error = None
emp              =    Employee("localhost","testUser", "A4min@123","employees" )
connection       =    emp.db_connection()
cursor           =    connection.cursor()

file_name_out  =  'SQL_Test at ' + str(current_time) + ".txt"

f   =  open("SQL_test_log_SET3.txt", "w")

f.write(file_name_out)
f.write("\n== SET 3 ==\n")

###
f.write("\nA) Query involving a single database table\n")

###
### Q1
###

f.write("\nQ1) Give the count of employees having income between 20000 AND 40000\n") 

sql_query1          =  """SELECT COUNT(*) FROM employee WHERE INCOME BETWEEN 20000 AND 40000;"""
cursor.execute(sql_query1)
results_INC_count     =  cursor.fetchone()

try: 
    INC_count         =  "\nFemale employees count : " + str(results_INC_count[0]) 
    print(INC_count)
    f.write(INC_count)
    Explain_txt1    =  "\nThe WHERE clause is used to compare the given value with the field value available in the database table."
    f.write(Explain_txt1)
    Explain_txt2    =  "\nThe COUNT() function returns the number of records returned by a SELECT query.\n\n"
    f.write(Explain_txt2)
except:
    print("\nError")

###
### Q2
###

f.write("\n\nQ2) Give the count of employees who will attain 60 years from 5 years from now \n") 

sql_query2          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE AGE < 60 AND AGE + 5  > 60;"""
cursor.execute(sql_query2)
results_5y_count   =  cursor.fetchone()

try: 
    count_5y       =  "\nCount of Employees who will attain 60 years from 5 years from now : " + str(results_5y_count[0]) 
    f.write(count_5y)
except:
    print("\nError")
    

### =====================================================================================================================================

###
### Q3
###

sql_select_old1        =  """SELECT FIRST_NAME, LAST_NAME, CONVERT(AGE, CHAR) AS AGE """
sql_select_old2        =  """FROM EMPLOYEE """
sql_select_old_female3 =  """WHERE AGE = ALL(SELECT MAX(AGE) FROM EMPLOYEE WHERE SEX = 'M') AND SEX = 'F';"""
 
sql_select_old_female  = sql_select_old1 + "\n" + sql_select_old2 + "\n" + sql_select_old_female3
             
cursor.execute(sql_select_old_female)
        
results_F            =  cursor.fetchone()
print('\nOldest Male : {}'.format(results_F))

try: 
    
    f.write("\n\nQ3) Select the Oldest Female employee")
    F_name              =  "\nFemale employee name : " + results_F[0] + " " + results_F[1] + " Age : " + results_F[2]
    f.write(F_name )
except:
    print("\nError")   

f.write("\n\n\nB) Query involving two database tables")
    
###
### Q4
###

sql_select_sal1      =  """SELECT COUNT(*), A.DEPT_ID, B.DEPT_NAME """
sql_select_sal2      =  """FROM   EMPLOYEE A, DEPARTMENT B """
sql_select_sal3      =  """WHERE INCOME < 20000 and a.DEPT_ID = b.DEPT_ID GROUP by DEPT_ID;"""

sql_query            =  sql_select_sal1 + sql_select_sal2 + sql_select_sal3
cursor.execute(sql_query)
results_sal          =  cursor.fetchall()

f.write("\n\nQ4) Give the count, department ID and department name of the employees drawing Less than 2000")

for r in results_sal:
    
    print('\nCount of Employees drawing less than 20000 as income department-wise : {}'.format(str(r[0])))
  
    try: 
        Salary_less      =  "\n\nCount of employees drawing less than 20k as income : " + str(r[0]) + " Dept ID : " + \
                          r[1] + " Name : " + r[2]
        f.write(Salary_less)
    except:
        print("\nError") 


    
# disconnect from server
cursor.close() 
f.close()   
