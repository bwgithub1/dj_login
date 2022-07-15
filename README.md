# Simple Django Login and Registration

An example of Django project with basic user functionality.

## Functionality

- Log in
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Create an account
- Log out
- Profile activation via email
- Reset password
- Remind a username
- Resend an activation code
- Change password
- Change email
- Change profile
usi
## Installing

chech if git is installed on local. Open CMD and type: git --version
Download git: https://git-scm.com/downloads

### Clone the project

```
git clone https://github.com/bwgithub1/dj_login.git
cd dj_login.git
```

### Install dependencies & activate virtualenv

```
pip install pipenv  

pipenv install  (if it does not work, try: python -m pipenv install)
pipenv shell	(if it does not work, try: python -m pipenv ishell)

(Some times, Django needs to install: python -m pip install Django)
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `source/app/conf/development/settings.py` if you want to develop the project.

2. Edit `source/app/conf/production/settings.py` if you want to run the project in production.

### Apply migrations

```
python source/manage.py migrate
```

### Collect static files (only on a production server)

```
python source/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```
python source/manage.py runserver

first: create super user (for example: admin/superuser)
http://localhost:8000/admin  
then create user for the web on the admin page

Access the web 
http://localhost:8000/
```
