# postgresql_local
Installing PostgreSQL in our local computer and applying operations on it

PostgreSQL is the server we are going to be working with.

Just open any command prompt and enter > psql -U postgres

here the psql is the command for triggering our postgresql database and -U stands for universtal 
user postgres which was created when we installed the postgresql on our computer.

You will be prompted for a password: admin

Now you are in the postgresql database where you can run commands for creating table like so,

# Creating Tables

CREATE TABLE flights (
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
);

NOTE: ; should be at end for terminating command

Above is the command for creating a table inside the postgres database, name of our table is 
flights and inside the brackets is the columns that our table is going to have

For e.g.

id is the SERIAL that each flight is going to have automatically because we have set it to 
PRIMARY KEY through which a particular flight is going to be denoted.

origin is a character which has type VARCHAR which means it can have both integer and character 
values in it and NOT NULL says that this particular field cannot be empty while creating a flight 
which is obvious since origin of a flight cannot be empty value.

Similarly destination is varchar and mandatory not null value, if we don't pass in a value our database is going to show errors.

duration is the duration of a flight from origin to destination and this is a INTEGER value with 
is like the other two values a NOT NULL value since a flight has to have a fixed duration.

NOTE: \d is the command for getting the details of our table.

# Inserting Into Table
Inserting data into our table is just like creating except here we specify the values to be 
inserted like the code in our file insert.sql

# Selecting data from tables
To access every row and column from table just mention it with a * like

SELECT * FROM flights;

NOTE: don't forget the semicolon at the end of the command.

Basically it is very rare to get all the data stored in our database at once instead we want some
filtered data and for that we can specify what we want when executing the SELECT statement, look 
at the select.sql for more info.

# Conditional Selection
Adding * in the SELECT statement will get us all the data from each column and row whereas adding 
a WHERE clause in our SELECT statement will get us the particular rows that fulfill our condition

For e.g. : SELECT * FROM flights WHERE id = 3;
For more select command look at select.sql file

We can also use greater than and smaller than symbols to get more filtered data for e.g.
SELECT * FROM flights WHERE duration > 500;

For more specific where filtering we can use the AND keyword in the WHERE clauses, or we can use
a clause with OR to fulfill either or both of the conditions.

We can use the functions that PostgreSQL has like the AVG for getting the average of some field.

SELECT AVG(duration) FROM flights;
> 7 		means our flights table has 7 rows in total

PostgreSQL also has COUNT function for counting the number of rows the database returned from a 
query.

We can also apply the MIN function to get the minimum of any value for example we can get the 
flight details which has the minimum duration.

We can also specify the values from which we want our select query to search from,

SELECT * FROM flights WHERE origin IN ('Indore', 'New York');