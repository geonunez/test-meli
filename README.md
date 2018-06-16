Geonunez - Test Meli
====================
## Nota
Este proyecto es para aplicar a una vacante de trabajo. Algunos aspectos son tomadas por sentado.

### Dominio de prueba
La aplicación fue preparada y desplegada en la plataforma heroku. La misma se encuentra disponible temporalmente en el dominio:

[https://geonunez-test-meli.herokuapp.com](https://geonunez-test-meli.herokuapp.com)

**Importante:** El plan gratuito de Heroku suspende el nodo si el mismo deja de recibir peticiones por 15 minutos, por lo que tu primer llamado puede tardar un poco en ser atentido mientras la plataforma reanuda el nodo.

### Tecnologías
- Python 3.6.5
- Django
- Django Rest

### ¿Cómo instalar?
1. Clonar este repositorio y entrar en la carpeta del proyecto clonado.
2. Crear el virtualenv:
```sh
$ virtualenv -p python3 env
```
3. Activar virtualenv:
```sh
$ source env/bin/activate
```
4. Instalar dependencias:
```sh
$ pip install -r requirements.txt
```
5. Correr migraciones de la base de datos:
```sh
$ python manage.py migrate
```
6. Crear tabla para el cache de la app:
```sh
$ python manage.py createcachetable
```
### ¿Cómo correr las pruebas?
```sh
$ python manage.py test
```
### ¿Cómo ejecutar?
```sh
python manage.py runserver
```

### Endpoints
- **[POST] api/v1/mutant**
Permite verificar si una secuencia de ADN pertenece o no a un mutante.
*Ejemplo:*
```sh
$ curl -X POST \
  http[s]://[dominio]/api/v1/mutant \
  -H 'Content-Type: application/json' \
  -d '{
	"dna": ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}'
```
- **[GET] api/v1/stats**
Muestra estadísticas sobre los humanos y mutantes analizados.
*Ejemplo:*
```sh
curl -X GET \
  http[s]://[dominio]/api/v1/stats
```

### API Doc
La aplicación cuenta con swagger el cual permite visualizar y probar los distintos endpoints.

Para acceder puede dirigirse a la URL **http[s]://[dominio]/api/doc**
