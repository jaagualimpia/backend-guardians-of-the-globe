# Contexto
En este apartado se especifican las acciones necesarias a llevar a cabo para ejecutar de manera satisfactoria el proyecto de backend guardians of the globe. La ejecución de este proyecto esta directamente ligada con el proyecto  [frontend guardians of the globe](https://github.com/jaagualimpia/frontend-guardians-of-the-globe.git)

# Prerequisitos
- La maquina en la cual se quiera ejecutar el proyecto necesita de los siguientes elementos. 
1. git 
2. Python 3.10.0 en adelante 
3. postgreSQL

# Paso a paso
 1. Primero se debe instalar el proyecto en la maquina haciendo uso de git clone 
 2. Posteriormente se deberá de crear en PostgreSQL una base de datos que se llame guardians_of_the_globe con el siguiente comando en un editor de consultas sql de pgadmin o usando el shell de posgres (psql): `CREATE DATABASE guardians_of_the_globe;`
 3. De ahí crearemos el entorno virtual en el cual instalaremos las librerías necesarias para el correcto funcionamiento del proyecto haciendo uso de los siguientes comandos:

		Usando CMD:
			`py -m venv venv`
			`venv\Scripts\activate.bat` 

		Usando powershell:
			`python -m venv venv`
			`venv\Scripts\activate`

4. En este punto se debería de haber creado y entrado de manera satisfactoria el entorno virtual, ahora dentro de este ejecutaremos el siguiente comando `pip install -r requirements.txt`  
5.  Después deberemos de crear un archivo .env (a nivel de proyecto, osea donde se encuentra tambien el archivo manage.py), en el cual deberemos de definir variables de entorno que cumplan con la siguiente estructura:

	    DB_NAME=guardians_of_the_globe
	    DB_USER=<nombre_usuario>
	    DB_PASSWORD=<clave_usuario>
	    DB_ROOT_DEFAULT_PASSWORD=<clave_root_por_defecto>
				
6. A partir de este momento podremos ejecutar nuestro proyecto, pero antes necesitamos construir las relaciones de la base de datos, para esto usaremos el comando: `py manage.py makemigrations` seguido de: `py manage.py migrate`
7. Ahora para cargar los datos tomaremos el archivo del proyecto llamado scripts.sql, lo arrastraremos hasta el editor de sentencias sql de postgres y lo ejecutaremos. Con esto llenaremos las distintas relaciones que previamente fueron creadas en la base de datos, en caso de que se este usando el shell de postgreSQL se debera de ejecutar el siguiente comando: 
`\i '..\\guardians_of_the_globe_back\\script.sql'`  Es importante que se cumpla que el back slash se repita dos veces y que se utilice la ruta absoluta en donde se encuentra ubicado el archivo. 
8. Finalmente para ejecutar el programa escribiremos el siguiente comando: `py manage.py runserver 0.0.0.0:5050`