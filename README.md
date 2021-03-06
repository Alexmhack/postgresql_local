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

We can also specify a substring to search for in our database field using special string denotion
'%a%'

SELECT * FROM flights WHERE origin LIKE '%a%';
the query above will return all flights which has the letter 'a' in their origin.

 id |  origin   | destination | duration
----+-----------+-------------+----------
  5 | Palo Alto | Sydney      |      600
  6 | Mumbai    | Delhi       |      180
  7 | Goa       | Canberra    |      300
(3 rows)

# Updating database
For updating information in rows and columns of our database we have the keyword UPDATE and 
since we won't update each and every row of our database we use WHERE to specify where we want
our update query to be applied.

UPDATE flights SET duration = 500 WHERE origin = 'Indore' AND destination = 'Kerela';

The above query makes sense if our flights duration has been increased for a particular route so
we can update the duration for all flights that follow that route.

# Deleting rows in database
DELETE is the keyword this particular query and since the deleted data cannot be restored we 
should be very careful as to what we delete and should always check first by a SELECT query that 
we are deleting the right data.

DELETE FROM flights WHERE destination = 'Canberra';

this will delete all rows that have its destination column with value 'Canberra';

# Limited fetching of data
SELECT * FROM flights LIMIT 2;

above query will return only 2 to rows from the database.

We can order our returned queryset by a particular column in our table for example in our 
flights table we can get the flights in an ascending order by their duration.

We can limit our queryset by saying give us the first 3 flights with least duration. 

# Grouping querset
Here we say to group by origin which means that all the rows from one origin will be grouped 
together and so on.

HAVING is same like WHERE but it can only be used if followed by a GROUP BY clause.

# Creating passengers table
Whenever there is more information that our project needs to store we should have a seperate 
table for it so here we don't wanna put our passengers in the flights table so we are creating
another table with passengers having unique id, name and a flight in which they will travel so
for that we are referencing our flights table id using keyword REFERENCES.

Now if we want to know where is the person with name = 'Pranav' is going then I can run a query
for getting the flight_id for the name = 'Pranav' and then search for that flight_id in the 
flights table.

# Joining tables
We can join seperate tables on the basis of foreign key by using the keyword JOIN.

Since the flight_id is referencing to the id in the flights table so this is a good factor in 
providing constraints in most cases for example if you delete a row in flights with id = 1;

DELETE FROM flights WHERE id = 1;

Above query cannot run because we have a passenger in the passengers table that has its flight_
id = 1 which will violate our passengers flight.

We can also perform an JOIN known as the LEFT JOIN which joins the left table to the right and 
what this does is get all the data we need from the left table whether or not the data has any
reference in the right table, which can give us some empty values as well.

Similarly there is RIGHT JOIN that includes all the rows from the right table even if it doesn't 
have a match in the left table.

# Nesting Queries
Nesting SQL queries can be helpful when we want to operate secondary query on a result of a query
itself, like if we want to know all the details of the flight which has more than one passenger 
on it, this query is not possible without having to run two seperate queries but nesting queries 
makes this very simple.

SELECT * FROM flights WHERE id IN 
	(SELECT flight_id FROM passengers GROUP BY fligt_id HAVING COUNT(*) > 2);

above query gets us the flights details (origin, destination, duration) if the flight has more 
than two passengers on it. Just break the query into two parts, the first says to get the 
flights details for id in result of query, second query gets us the flight_id if flight has more 
than two passengers on it, whose result is 4 so we are getting the flight details for just id = 4

# Running python to query database
Python Module for working with database that we are going to use is sqlalchemy, so create a file 
and import our modules.

With the help of sqlalchemy we can access almost every database that exists today, we are going
to access postgresql database that we have created so far. 

First we need to create an engine for our postgresql and we can import that from sqlalchemy
import create_engine, for creating engine we need to specify the path for our database which
is as follows:

engine = create_engine('postgresql://postgres:admin@localhost/postgres')

create_engine is just a function from the module and it takes in the database url, here
postgresql:// means we are telling to create an postgresql engine, postgres:admin means the
user:password for our postgresql server and since our database exists in the local computer we
tell that using the @localhost and then the name of the database inside our postgresql which is
postgres

Now we can access all the tables that are inside our database postgres which are namely flights 
and passengers at the moment, so to execute queries we can,

engine.execute("SELECT * FROM flights")

this way we can execute sql queries just like our terminal.

NOTE: the returned values from engine.execute is a iterable so we can use for loop to get all
the data and also use dot notation to get specific columns from table.

# Inserting data from files
Suppose we have a large csv file which is in the order that we want which is 

origin, destination, duration

then we can just run a for loop for the whole file and start making insertions into our file.
We have made inserting_csv_data.py in which we run make a reader from the csv module in python
for handling csv file data, that reader has the columns in the sequence so we just run a for
loop and insert data in our sql query

The sql query for inserting external data is a little different. We need to tell db that we are 
not yet entering the VALUES by placing a colon in front of the VALUE for example

VALUES (:origin, :destination, :duration)

Once we have done this, we need a python dictionary which has key as the VALUE name (origin, 
destination, duration) and dict values as the values that we want to enter into the VALUES.

Don't forget to commit the database once we have inserted our values, only after that our changes
will be reflected, We can also commit changes at last, sqlalchemy will store those changes at 
commit them all together at last.