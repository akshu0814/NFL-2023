******PROJECT-1*******
DATABASE-SYSTEMS-CSE-5330

Student_Name1 - Akshu Nikunjkumar Patel(1002072333)
Student_Name2 - Divya Darshi(1002090905)

*****PROJECT DESCRIPTION*******
Step1-: Connect with Pulse Secure VPN.

Step2-: To login to the omega account we have to run (ssh axp2333@omega.uta.edu) command on Command Prompt and type NetID password.
        
Step3-: Open MySQL by using the username=axp2333 and Password = bUc@Nyix6t5h

Step4-: Create the tables in Mysql. 
   Syntax- Create Table table_name(column1 datatype, column2 datatype, ......);


Step5-:  Create Spool file.
      Syntax- tee filename.txt
              <<Logging to file...>>
              source db.sql
	      notee;


****DETAILED INSTRUCTIONS TO EXECUTE THE CODE****
## PROGRAMMING LANGUAGE - PYTHON

Step1-: Write source code in python language. Then Save the Source code on your computer.

Step2-: Connect with Pulse Secure VPN and Log on to the omega.

Step3-: Run the code on you command prompt using python filename.py

Step4-: Execute select query in mysql database and table will be created.



## PYTHON SCRIPT DETAILS

 1) Python scripts start by importing the libraries: 'mysql.connector' for connecting to the MySQL database, 'csv' for reading the CSV file.
 2) Then, it connects to the MySQL database using the mysql.connector.connect() method, passing in the username, password, host, and database name. It also creates a cursor object to
     interact with the database.
 3) It specifies the path to the CSV file and opens it using the open() function. It then creates a csv.reader object to read the contents of the CSV file.
 4) It skips the first row of the CSV file (which is assumed to be the header row) using the next() function.
 5) loops over each row in the CSV file using a for loop, and for each row, it constructs an SQL query using a formatted string. 
 6) After that execute the query using the cursor object's execute() method, passing in the query and values.
 7) After all the rows have been inserted into the database, the script commits the changes using the cnx.commit() method, and closes the cursor and connection using the cursor.close()
    and cnx.close() methods.