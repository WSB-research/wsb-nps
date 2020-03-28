release: python ./api/manage.py migrate
web: gunicorn --chdir ./api api.wsgi:application
