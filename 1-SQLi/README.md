SQL Injection
=============

Overview
--------

### Goal ###

Use SQL Injection to get a list of all names in the database.


### What you can do ###

On the main page, you can enter a name to see if it is in the database.


### Help ###

To have a view of the database, go visit [http://localhost:5000/see]().


Getting set up
--------------

-   Run `sqlite3 prism.db < db_schema.sql` to populate the database.

-   Make sure you are in the virtual environment.

    If you are not, go one directory up and run `source venv/bin/activate`,
    then go back to this directory.

-   Run `python main.py` to launch the local web server.

-   Go on [http://localhost:5000]() to hack yourself.