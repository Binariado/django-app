# django-app
## Start
Enlace para las pruebas de la api en [Postman](https://documenter.getpostman.com/view/10381917/TzK14uNm).

#### local Docker
```sh
cd django-app
docker-compose up --build
or
docker-compose up -d --build
```

#### local
habilitar el env
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.y runserver
```

#### Host
```sh
127.0.0.1:8000
```
