# Logs Analysis
The objective of this project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

![Screenshot](reports.png)

## Running the project!

### Configure VM & Database

**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org). We’ll need these tools to setup and manage the Virtual Machine (VM). 


**Step 2:** 
Download the database from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Then, copy the database newsdata.sql to vagrant/news

report.py  from the current foldern should be copied to vagrant/news

**Step 3:** 
Run the virtual machine!
Using the terminal, change directory to news using the command cd news,then type vagrant up to launch your virtual machine.
Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. 

Now that you have Vagrant up and running type vagrant ssh to log into your VM. Change directory to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains report.py

Type (python report.py) to run the program 
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

\dt — display tables — lists the tables that are available in the database.
\d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.

There are also the following views 

1. create view requests as 
select date(time), 
       count(*) 
from log 
group by date(time) 
order by date(time);

2. create view error as 
select date(time), 
      count(*)
 from log 
 where status = '404 NOT FOUND' 
 group by date(time) 
 order by date(time);

 3. create view requests_error as 
select requests.date, 
        round((100*error.count::numeric)/(requests.count::numeric),3) from requests, 
             error 
where requests.date=error.date;


### Project Rubric

1. Running the code displays the correct answers to each of the questions in the lab description.

2. The code works with the (unchanged) database schema from the lab description.

3. The code presents its output in clearly formatted plain text.

4. The code connects to and queries an SQL database. It does not use answers hardcoded into the application code.

5. The project code runs without any error messages or warnings from the language interpreter.

6. The code conforms to the PEP8 style recommendations.

7. When the application fetches data from multiple tables, it uses a single query with a join, rather than multiple queries.