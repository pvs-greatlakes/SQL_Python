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

f   =  open("SQL_test_log_SET2.txt", "w")

f.write(file_name_out)
f.write("\n== SET 2 ==\n")

###
f.write("\nA) Query involving a single database table\n")

###
### Q1
###



sql_query1          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE SEX = 'F';"""
cursor.execute(sql_query1)
results_F_count     =  cursor.fetchone()

f.write("\nQ1) Give the count of female employees\n") 
f.write("\n\nAnwers\n\n")
f.write(sql_query1)

try: 
    F_count         =  "\nFemale employees count : " + str(results_F_count[0]) 
    print(F_count)
    f.write(F_count)
    Explain_txt1    =  "\nThe WHERE clause is used to compare the given value with the field value available in the database table."
    f.write(Explain_txt1)
    Explain_txt2    =  "\nThe COUNT() function returns the number of records returned by a SELECT query.\n\n"
    f.write(Explain_txt2)
except:
    print("\nError")

###
### Q2
###

sql_query2          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE DOJ  < DATE_SUB(NOW(), INTERVAL 5 YEAR);"""
cursor.execute(sql_query2)
results_5y_count   =  cursor.fetchone()

f.write("\n\nQ2) Give the count of employees who joined 5 years ago (i.e. experience in the company is 5 years or more) \n") 
f.write("\n\nAnwers\n\n")
f.write(sql_query2)

try: 
    count_5y       =  "\nCount of Employees who joined 5 years ago : " + str(results_5y_count[0]) 
    f.write(count_5y)
    Explain_txt1    =  "\n\nThe DATE_SUB() function subtracts a time / date interval from a date and then returns the date."
    f.write(Explain_txt1)
except:
    print("\nError")
    

### =====================================================================================================================================

###
### Q3
###

sql_select_old1      =  """SELECT FIRST_NAME, LAST_NAME, CONVERT(AGE, CHAR) AS AGE """
sql_select_old2      =  """FROM EMPLOYEE """
sql_select_old_male3 =  """WHERE AGE = ALL(SELECT MAX(AGE) FROM EMPLOYEE WHERE SEX = 'M') AND SEX = 'M';"""
 
sql_select_old_male  = sql_select_old1 + "\n" + sql_select_old2 + "\n" + sql_select_old_male3
             
cursor.execute(sql_select_old_male)
        
results_M            =  cursor.fetchone()
print('\nOldest Male : {}'.format(results_M))

try: 
    
    f.write("\n\nQ3) Select the Oldest Male employee")
    f.write("\n\nAnwers\n\n")
    f.write(sql_select_old_male)
    M_name              =  "\nMale employee name : " + results_M[0] + " " + results_M[1] + " Age : " + results_M[2]
    f.write(M_name )
except:
    print("\nError")   

f.write("\n\n\nB) Query involving two database tables")
    
###
### Q4
###

sql_select_sal1      =  """SELECT COUNT(*), A.DEPT_ID, B.DEPT_NAME """
sql_select_sal2      =  """FROM   EMPLOYEE A, DEPARTMENT B """
sql_select_sal3      =  """WHERE INCOME < ALL(SELECT avg(income) FROM employee) and a.DEPT_ID = b.DEPT_ID GROUP by DEPT_ID;"""

sql_query            =  sql_select_sal1 + sql_select_sal2 + sql_select_sal3
cursor.execute(sql_query)
results_sal          =  cursor.fetchall()

f.write("\n\nQ4) Give the count, department ID and department name of the employees drawing Less than the average salary")
f.write("\n\nAnwers\n\n")
f.write(sql_query)
    
for r in results_sal:
    
    print('\nCount of Employees drawing less salary department-wise : {}'.format(str(r[0])))
  
    try: 
        Salary_less      =  "\n\nCount of employees drawing less salary than average : " + str(r[0]) + " Dept ID : " + \
                          r[1] + " Name : " + r[2]
        f.write(Salary_less)
    except:
        print("\nError") 

###
### Q5
###

sql_select_leave1      =  """SELECT CONCAT(A.FIRST_NAME, " ", A.LAST_NAME) AS NAME, B.LEAVE_DAYS """
sql_select_leave2      =  """FROM EMPLOYEE A, LEAVES B """
sql_select_leave3      =  """WHERE A.EMP_ID = B.EMP_ID AND B.LEAVE_DAYS = ALL(SELECT MAX(LEAVE_DAYS) FROM LEAVES);"""

sql_query              =  sql_select_leave1 + sql_select_leave2 + sql_select_leave3
cursor.execute(sql_query)
results_L              =  cursor.fetchone()
print('\nEmployee who take max leave : {}'.format(results_L[0]))

try: 
    
    f.write("\n\nQ5) Give the count of employees who availed leave")
    f.write("\n\nAnwers\n\n")
    f.write(sql_query)
    Name_leave          =  "\n\nEmployee name who took max. leave : " + results_L[0]
    f.write(Name_leave)
except:
    print("\nError")   

    
# disconnect from server
cursor.close() 
f.close()   
