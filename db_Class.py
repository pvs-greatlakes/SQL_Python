# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:22:25 2020

@author: P.V.SUBRAMANIAN
"""
import mysql.connector
from   mysql.connector  import Error, errorcode
import random
import string

class Employee:
      """
      In this Class object, we establish the data base connection, create MySQL tables and insert the 
      records for the following tables
      a. EMPLOYEE
      """
    
      import mysql.connector
      from   mysql.connector  import Error, errorcode
      import random
      import string
    
      def  __init__(self, host, user, pwd, db):
           self.host     =   host
           self.db       =   db
           self.user     =   user
           self.pwd      =   pwd
           
      def db_connection(self):
          
    
           self.connection =  mysql.connector.connect(host  =  self.host,
                                              database =  self.db,
                                              user     =  self.user,
                                              password =  self.pwd)
           
           return  self.connection
       
      def db_create_table(self):
          
#           emp     =  Employee(self)
#           # prepare a cursor object using cursor() method
#           cursor = emp.db_connection(self)
#                
           # Drop table if it already exist using execute() method.
           connection  =   self.connection
           cursor      =   connection.cursor()
           cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
                
           # Create table as per requirement
           sql = """CREATE TABLE EMPLOYEE (
                    EMP_ID            CHAR(6) NOT NULL,
                    DEPT_ID          CHAR(4) NOT NULL,
                    FIRST_NAME  CHAR(20) NOT NULL,
                    LAST_NAME  CHAR(20),
                    AGE INT,  
                    SEX CHAR(1),
                    INCOME FLOAT,
                    DOJ DATETIME)"""
                
           cursor.execute(sql)    

           cursor.execute("DROP TABLE IF EXISTS DEPARTMENT")
           
           sql_dept = """CREATE TABLE DEPARTMENT(
                        DEPT_ID          CHAR(4) NOT NULL,
                        DEPT_NAME  CHAR(20),
                        EMP_ID            CHAR(6) NOT NULL)"""
           cursor.execute(sql_dept)    
           

      def insertVariblesIntoTable(self, EMPID, DEPTID, FN, LN, AGE, SEX, INCOME, DOJ):
           connection  =   self.connection                   
           try:
                cursor = connection.cursor()
               
                mySql_insert_query    = """INSERT INTO employee (EMP_ID, DEPT_ID, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME, DOJ)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        
                recordTuple = (EMPID, DEPTID, FN, LN, AGE, SEX, INCOME, DOJ)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into Employee table")
                connection.commit()
                print("Record inserted successfully into Employee table")
    
        
           except mysql.connector as error:
                print("Failed to insert into MySQL table %s " % error)
      def insertVariblesIntoTable2(self, DEPTID, DEPTNAME, EMPID):
          
           connection  =   self.connection                   
           try:
                cursor = connection.cursor()
               
                mySql_insert_query    = """INSERT INTO department (DEPT_ID, DEPT_NAME,EMP_ID)
                                         VALUES (%s, %s, %s) """    
                recordTuple           = (DEPTID, DEPTNAME, EMPID)  
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into Department table")
                
                cursor = connection.cursor()
   
        
           except mysql.connector as error:
                print("Failed to insert into MySQL table %s " % error)                
                
                

###
### End of class
###