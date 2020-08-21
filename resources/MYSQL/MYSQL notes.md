## MYSQL Notes:

### Create / Open / Delete Database: 
	CREATE DATABASE dbNameYouWant

	CREATE DATABASE dbNameYouWant CHARACTER SET utf8

	USE dbNameYouWant

	DROP DATABASE dbNameYouWant

	ALTER DATABASE dbNameYouWant CHARACTER SET utf8



### Backup Database to SQL File
	$ mysqldump -u Username -p dbNameYouWant > databasename_backup.sql
##


###Restore from backup SQL File	
	$ mysql -u root -p databaseName < c:/databasename_backup.sql
	
	in powershell use cmd or: 
	>> &cmd /c "mysql -u root -p databaseName < c:/databasename_backup.sql"
	
	if you get binary-mode error, open sql file in notepad and save encoding to UTF-8

##

###Browsing

	SHOW DATABASES
	SHOW TABLES
	SHOW FIELDS FROM table / DESCRIBE table / DESC table
	SHOW CREATE TABLE table
	SHOW PROCESSLIST
	KILL process_number
##

### Create Table:
	CREATE TABLE books (
    book_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    title VARCHAR(100),
    author_fname VARCHAR(100),
    author_lname VARCHAR(100),
    released_year INT,
    stock_quantity INT,
    pages INT);


	CREATE TABLE table (
	field1 type1, 
	field2 type2, 
	..., 
	PRIMARY KEY (field1, field2))
##

<br>

### Inserting into Table
	INSERT INTO table1 (field1, field2, ...) VALUES (value1, value2, ...);

	INSERT INTO books 
	(title, author_fname, author_lname, released_year, stock_quantity, pages)
	VALUES ('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
	       ('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
	       ('American Gods', 'Neil', 'Gaiman', 2001, 12, 465);

##
### Update Table
	UPDATE table_name
	SET column1 = value1, column2 = value2, ...
	WHERE condition;

	UPDATE Customers
	SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
	WHERE CustomerID = 1;

##
### Delete Table:
	DROP TABLE table

	DROP TABLE IF EXISTS table

	DROP TABLE table1, table2, ...
##

### Modify Table

###### ALTER TABLE - ADD Column
	ALTER TABLE Customers
	ADD Email varchar(255);

###### ALTER TABLE - DROP COLUMN
	ALTER TABLE Customers
	DROP COLUMN Email;

###### ALTER TABLE - ALTER/MODIFY COLUMN
	ALTER TABLE table_name
	MODIFY COLUMN column_name datatype;
##


