# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:23:53 2020

@author: PVS
"""
###
### S1_Q.py
###
import mysql.connector, sys
from   datetime          import  datetime

def esc(code):
    '''
    f-strings are string literals that have an f at the beginning and curly braces containing expressions
    that will be replaced with their values.
    
    Most common ANSI escape sequences take the following form:
    \033[{}m or 0

    We use the Code for non-printable escape character is \033
    m is the character code in either upper case or lower case character
    0 is one or more numbers separated with ;
    Explanation for the expression that will be replaced by their values
    
    Select Graphic Rendition (SGR) parameters sets display attributes arranged in the same sequence separated by semicolons
    to establish GRAPHIC RENDITION COMBINATION MODE (GRCM) .
    
     Code  Meaning
     ----  --------
     30    Black color
     31    Red color
     32    Green color

      1    Bold or increased intensity
      2    Decreased intensity
      4    Underline
      
    https://en.wikipedia.org/wiki/ANSI_escape_code  
    http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf

    '''
    return f'\033[{code}m'
    
def  bold_text(text, color = 'R'):
      '''
      This function converts the given text into bold and underlined text in the given color
      '''
      if color == 'B':
         cd = '30;1;4'
      elif color == 'R':
         cd = '31;1;4'
      elif  color == 'G':
         cd =  '32;1;4'
         
      return esc(cd)+ text + esc(0)
folder_name = r'D:\GL_DSE_Interview\Skill_Assessment_CSI'
sys.path.insert(0, folder_name) 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from db_Class  import  Employee

error = None
emp              =    Employee("localhost","testUser", "A4min@123","employees" )
connection       =    emp.db_connection()
cursor           =    connection.cursor()

file_name_out  =  'SQL_Test: <<S1>> at ' + str(current_time) + ".txt"

f   =  open("SQL_test_log_SET1.txt", "w")

f.write(file_name_out)
f.write("\n== SET 1 ==\n")

###
f.write("\nA) Query involving a single database table\n")

###
### Q1
###

sql_query1          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE SEX = 'M';"""
cursor.execute(sql_query1)
results_M_count     =  cursor.fetchone()

try: 
    f.write("\nQ1) Give the count of male employees\n")     
    f.write("\n\nAnswer\n\n") 
    f.write(sql_query1)
    M_count         =  "\n\nMale employees count : " + str(results_M_count[0]) 
    print(M_count)
    f.write(M_count)
    Explain_txt1    =  "\n\nThe WHERE clause is used to compare the given value with the field value available in the database table."
    f.write(Explain_txt1)
    Explain_txt2    =  "\n\nThe COUNT() function returns the number of records returned by a SELECT query.\n\n"
    f.write(Explain_txt2)
except:
    print("\nError")

###
### Q2
###
sql_query2          =  """SELECT COUNT(*) FROM EMPLOYEE WHERE DOJ  < DATE_SUB(NOW(), INTERVAL 10 YEAR);"""
cursor.execute(sql_query2)
results_10y_count   =  cursor.fetchone()

try: 
    f.write("\n\nQ2) Give the count of employees who joined 10 years ago (i.e. experience in the company is 10 years or more) \n") 
    f.write("\n\nAnswer\n\n")    
    f.write(sql_query2)    
    count_10y       =  "\n\nCount of Employees who joined 10 years ago : " + str(results_10y_count[0]) 
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
try:
    f.write("\n\nQ3) Give the name of the manager who joined last, i.e. later than all other managers")    
    f.write("\n\nAnswer\n\n") 
    f.write(sql_query) 
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
f.write("\n\nAnswer\n\n") 
f.write(sql_query) 

for r in results_sal:
    
    print('\n\nCount of Employees drawing more salary department-wise : {}'.format(str(r[0])))
  
    try: 
        Salary_more      =  "\n\nCount of employees drawing more salary than average : " + str(r[0]) + " Dept ID : " + \
                          r[1] + " Name : " + r[2]
        f.write(Salary_more)

    except:
        print("\nError") 

explain_query    = '\n\nThe GROUP BY command is used to group the result set (used with aggregate functions: COUNT, MAX, MIN, SUM, AVG)'
f.write(explain_query)

###
### Q5
###

sql_select_noleave1      =  """SELECT COUNT(*) """
sql_select_noleave2      =  """FROM   EMPLOYEE A """
sql_select_noleave3      =  """WHERE A.EMP_ID NOT IN (SELECT B.EMP_ID FROM leaves B);"""

sql_query                =  sql_select_noleave1 + sql_select_noleave2 + sql_select_noleave3
cursor.execute(sql_query)
results_noleave          =  cursor.fetchall()
print(bold_text(sql_query))

print('\nCount of Employees who did not avail any leave : {}'.format(str(results_noleave[0][0])))

try:

    f.write("\n\nQ5) Give the count of employees who did not take any leave")    
    f.write("\n\nAnswer\n\n") 
    f.write(sql_query) 
    noleave_count = "\n\nCount of employees who did not avail any leave: {}".format(str(results_noleave[0][0]))
    f.write(noleave_count)
except:
    print("\nError")  

    
# disconnect from server
cursor.close() 
f.close()

