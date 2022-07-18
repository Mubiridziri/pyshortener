## PyShortener

My 1st Project on Python after PHP Experience (Symfony)

## Run App

```bash
python3 manage.py runserver
```

## Migrations 

```bash
python3 manage.py migrate
```

## Create database
Log In to PSQL CLI
```
CREATE DATABASE pyshortener;
```

## Create admin user

```bash
python3 manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user(username, email, password)
user.save()
exit()
```