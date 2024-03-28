******PROJECT-1*******
DATABASE-SYSTEMS-CSE-5330

Student_Name1 - Akshu Nikunjkumar Patel(1002072333)
Student_Name2 - Divya Darshi(1002090905)

The project describes about how to insert and delete record by executing query in mysql.

##There are mainly three operations that have the ability to change the state of relations, these modifications are given below:

Insert –
To insert new tuples in a relation in the database.
Delete –
To delete some of the existing relation on the database.
Update (Modify) –
To make changes in the value of some existing tuples.

##Inserting the records that violate integrity constraints. 
There are three types of violation.
1. Entity integrity constraint - On inserting NULL values to any part of the primary key of a new tuple in the relation can cause violation of the Entity integrity constraint.
	For instance: Column 'gameId' cannot be null(The null value is not allowed in the primary key(s))

2. Domain constraint - Domain constraint gets violated only when a given value to the attribute does not appear in the corresponding domain or in case it is not of the appropriate datatype.
	For instance: Data too long for column 'visitorTeamAbbr' at row 1

3. Key constraint - On inserting a value in the new tuple of a relation which is already existing in another tuple of the same relation, can cause violation of Key Constraints.
	For instance: Duplicate entry '29550' for key 'players.PRIMARY'

   Referential integrity - On inserting a value in the foreign key of relation 1, for which there is no corresponding value in the Primary key which is referred to in relation 2, in such case Referential integrity is violated.
	For instance: Cannot add or update a child row: a foreign key constraint fails (`axp2333`.`scouting`, CONSTRAINT `scouting_ibfk_1` FOREIGN KEY (`gameId`, `playId`) REFERENCES `plays` (`gameId`, `playId`))

##Deletion operation

On deleting the tuples in the relation, it may cause only violation of Referential integrity constraints.

Referential integrity constraint - It causes violation only if the tuple in relation 1 is deleted which is referenced by foreign key from other tuples of table 2 in the database, if such deletion takes place then the values in the tuple of the foreign key in table 2 will become empty, which will eventually violate Referential Integrity constraint.
	For instance: Cannot delete or update a parent row: a foreign key constraint fails (`axp2333`.`scouting`, CONSTRAINT `scouting_ibfk_1` FOREIGN KEY (`gameId`, `playId`) REFERENCES `plays` (`gameId`, `playId`))


##Project decription

step1: Insert command in mysql that violate the integrity constraints.
	The query that violates this contraint are of four types as mentioned above.

step2: Insert new records that do not violate any integrity constraint by repeating the above insert commands. This will perform the correct query.
	The query for resolving the issue for integrity contraint is to check each value before inserting into the table.

step3: Delete the record that violate the referetial integrity constraint.
	The query for resolving the referential integrity constraint is of three types: RESTICT, CASCADE, SET NULL or SET DEFAULT.

step4: Create Spool file.
      Syntax- tee filename.txt
              <<Logging to file...>>
              source db.sql
	      notee;


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