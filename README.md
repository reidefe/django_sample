# SAMPLE DJANGO SALES SITE 

## SQLITE is the default BD engine, however configuration for PostgreSQL has put in place and psycopg2 is included in the piplock
## Settings.py in sp folder contains the ready postgres configuration

## Pipenv install of depencies and create virtual enviroment for development
```
pipenv install
```
## Makingmigrations needed to establish the database

```
Python3 manage.py makemigrations
```
## Migrate the database

```
Python3 manage.py migrate
```


## Running the program

```
Python3 manage.py runserver
```

