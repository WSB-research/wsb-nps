# WSB Research - NPORT Processing Service (NPS)

https://wsb-nps.herokuapp.com/

## Setup

### Install:

- Python 3.8.1 https://www.python.org/downloads/release/python-381/
- pip https://pip.pypa.io/en/stable/installing/
- PostgreSQL 10.12 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- pgAdmin4 https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.19/windows/

### Setup PostgreSQL

1. Launch pgAdmin4, navigate to the browser based UI (for me it was http://127.0.0.1:19217/browser/) 
2. Connect to your local PostgreSQL server and create a new Login/User called `dev` with password `password`
3. Create a Database called `NPS`, and set the owner to be the `dev` account you just created

### Install Required Packages/Libraries

- Run: `pip install -r requirements.txt` in the root of the project 

## Python Scraper 

### Running

*Note: You will need to have the database setup by running `python manage.py migrate` from the api folder.*

From the python_scraper folder run: `scrapy crawl sec_nport_p`

### Config Options

In `python_scraper/python_scraper/settings.py` you can adjust how fast the spider requests pages and other spider
settings.

## API

### Running

Currently uses the Postgres database setup earlier. 

Make sure you have a `dbsettings.json` file created in the root api folder (right next to `manage.py`) with the following contents: 

```
{
    "DB_NAME": "NPS",
    "DB_USER": "dev",
    "DB_PASSWORD": "password",
    "DB_HOST": "localhost",
    "DB_PORT": "5432"
}
```

You will need your own local settings file to overwrite some settings that are local specific. To use this run the 
following from the api folder (you might want to put the export command in a bashrc/bash_profile or you will need
to run it in every new terminal session):
```
cp api/settings_local.py.sample api/settings_local.py
export DJANGO_SETTINGS_MODULE=api.settings_local 
```

To build the frontend, open a new terminal and run (to build for production you would run `yarn build`):
```
cd assets
yarn watch
```

From the api folder:

```
python manage.py migrate
python manage.py runserver
```

Server is now running on `localhost:8000`, the frontend is served at the root and there are readable docs for the api
generated at /api/.
