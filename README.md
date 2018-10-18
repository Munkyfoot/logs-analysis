# Project: Logs Analysis

This logs analysis tool queries the [news database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to find useful information about user trends and site errors.

### Requirements
* Python >= 2.7
    * psycopg2
* PostgreSQL
* [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Included Files
* analyze.py - *The main python program. Contains methods which format and output results retreived from the database.*
* db.py - *Supporting script for connecting to and querying from database.*
* analysis.txt - *Output of analysis saved in plain text.*

### How To Use
* Download/install all requirements
    * Install python, the psycopg2 python module, and postgresql
    * Unzip 'newsdata.zip' and place extracted 'newsdata.sql' into the same directory as 'analyze.py'
* Create 'news' database and import from 'newsdata.sql'
    1. Open a terminal and cd into the directory containing 'newsdata.sql'
    2. Run 'psql'
    3. In psql run 'create database news;'
    4. Run '\q' to exit psql
    5. Run 'psql news -f newsdata.sql' to populate the database
* Run 'analyze.py'

### Output
This program returns the following three pieces of information and saves it to 'analysis.txt':
* The top 3 articles ranked by views
* All authors ranked by views
* Days on which requests errors comprised more than 1% of HTTP requests order by date

### Database Structure
* articles
    * author (integer) - *Foreign key which refers to 'id' in 'authors' table*
    * title (text) - *Title of the article*
    * slug (text) - *Unique HTML friendly title*
    * lead (text) - *One-line summary of article*
    * body (text) - *Full article contents*
    * time (timestamp with time zone) - *Time article was posted*
    * id (integer) - *Primary key*

* authors
    * name (text) - *Author's name*
    * bio (text) - *Biography for the author*
    * id (integer) - *Primary key*

* log
    * path (text) - *Path to article*
    * ip (inet) - *Public IP address of user*
    * method (text) - *HTTP request method*
    * status (text) - *HTTP status*
    * time (timestamp with time zone) - *Time article was accessed by user*
    * id (integer) - *Primary key*