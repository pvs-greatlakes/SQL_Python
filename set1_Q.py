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

f   =  open("SQL_test_log_SET1.txt", "w")

f.write(file_name_out)
f.write("\n== SET 1 ==\n")

###
f.write("\nA) Query involving a single database table\n")

###
### Q1
###

f.write("\nQ1) Give the count of male employees\n") 

sql_query1          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE SEX = 'M';"""
cursor.execute(sql_query1)
results_M_count     =  cursor.fetchone()

try: 
    M_count         =  "\nMale employees count : " + str(results_M_count[0]) 
    print(M_count)
    f.write(M_count)
    Explain_txt1    =  "\nThe WHERE clause is used to compare the given value with the field value available in the database table."
    f.write(Explain_txt1)
    Explain_txt2    =  "\nThe COUNT() function returns the number of records returned by a SELECT query.\n\n"
    f.write(Explain_txt2)
except:
    print("\nError")

###
### Q2
###

f.write("\n\nQ2) Give the count of employees who joined 10 years ago (i.e. experience in the company is 10 years or more) \n") 

sql_query2          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE DOJ  < DATE_SUB(NOW(), INTERVAL 10 YEAR);"""
cursor.execute(sql_query2)
results_10y_count   =  cursor.fetchone()

try: 
    count_10y       =  "\nCount of Employees who joined 10 years ago : " + str(results_10y_count[0]) 
    f.write(count_10y)
    Explain_txt1    =  "\n\nThe DATE_SUB() function subtracts a time / date interval from a date and then returns the date."
    f.write(Explain_txt1)
except:
    print("\nError")
    

### =====================================================================================================================================

f.write("\n\n\nB) Query involving two database tables")

###
### Q3
###

sql_select_y1      =  """SELECT CONCAT(A.FIRST_NAME, " ", A.LAST_NAME) AS NAME """
sql_select_y2      =  """FROM   EMPLOYEE A, DEPARTMENT B """
sql_select_y3      =  """WHERE  A.EMP_ID = B.EMP_ID AND A.DOJ = ALL(SELECT MAX(DOJ) FROM employee);"""

sql_query          =  sql_select_y1 + sql_select_y2 + sql_select_y3
cursor.execute(sql_query)
results_yM         =  cursor.fetchone()

print('\nManager who joined last : {}'.format(results_yM[0]))

f.write("\n\nQ3) Give the name of the manager who joined last, i.e. later than all other managers")

try: 
    M_last         =  "\n\nManager who joined last : " + results_yM[0]
    f.write(M_last )
except:
    print("\nError") 
    
###
### Q4
###

sql_select_sal1      =  """SELECT COUNT(*), A.DEPT_ID, B.DEPT_NAME """
sql_select_sal2      =  """FROM   EMPLOYEE A, DEPARTMENT B """
sql_select_sal3      =  """WHERE INCOME > ALL(SELECT avg(income) FROM employee) and a.DEPT_ID = b.DEPT_ID GROUP by DEPT_ID;"""

sql_query            =  sql_select_sal1 + sql_select_sal2 + sql_select_sal3
cursor.execute(sql_query)
results_sal          =  cursor.fetchall()

f.write("\n\nQ4) Give the count, department ID and department name of the employees drawing more than the average salary")

for r in results_sal:
    
    print('\nCount of Employees drawing more salary department-wise : {}'.format(str(r[0])))
  
    try: 
        Salary_more      =  "\n\nCount of employees drawing more salary than average : " + str(r[0]) + " Dept ID : " + \
                          r[1] + " Name : " + r[2]
        f.write(Salary_more)
    except:
        print("\nError") 


    
# disconnect from server
cursor.close() 
f.close()   
