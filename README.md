## Librerias a utilizar

- flask
- flask-sqlalchemy
- flask-migrate
- pymysql (driver para mysql)
- psycopg2 (driver para postgresql)
- python-dotenv (permite leer archivos .env)
- flask-cors

## Exportar aplicacion flask

1. Windows

```shell
> SET FLASK_APP=app.py
``` 

2. Linux o Mac

```shell
$ export FLASK_APP=app.py
```

## Comandos para generar y actualizar nuestra base de datos

1. Crear la carpeta migrations (Nota: ejecutar solo la primera vez o si eliminamos la carpeta migrations)

```shell
$ flask db init
```

2. Crear las migrations con los modelos creados en el archivo models.py

```shell
$ flask db migrate
```

3. Actualizar nuestra base de datos con las migraciones

```shell
$ flask db upgrade
```