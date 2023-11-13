# Contexto
En este apartado se especifican las acciones necesarias a llevar a cabo para ejecutar de manera satisfactoria el proyecto de backend guardians of the globe. La ejecución de este proyecto esta directamente ligada con el proyecto  [frontend guardians of the globe](https://github.com/jaagualimpia/frontend-guardians-of-the-globe.git)

# Prerequisitos
- La maquina en la cual se quiera ejecutar el proyecto necesita de los siguientes elementos. 
-- docker y docker compose
-- git 
-- Python 3.10.0 en adelante 
-- postgreSQL (en caso de no tener docker y docker compose)

# Paso a paso
 1. Primero se debe instalar el proyecto en la maquina haciendo uso de git clone 
 2. Posteriormente es necesario que se ejecute el comando `docker compose docker-compose.yml`
 3. De ahí crearemos el entorno virtual en el cual instalaremos las librerías necesarias para el correcto funcionamiento del proyecto haciendo uso de los siguientes comandos:

		Usando CMD:
			`py -m venv venv`
			`venv\Scripts\activate.bat` 

		Usando powershell:
			`python -m venv venv`
			`venv\Scripts\activate`
			
		Usando bash:
			`python3 -m venv venv`
			`source venv/bin/activate`

4. En este punto se debería de haber ejecutado de manera satisfactoria el entorno virtual, ahora dentro de este ejecutaremos el siguiente comando `pip install -r requirements.txt`  
5. A partir de este momento podremos ejecutar nuestro proyecto, pero antes necesitamos construir las relaciones de la base de datos, para esto usaremos el comando: `py manage.py makemigrations` y `py manage.py migrate`
7. Ahora ejecutaremos el archivo yml con la configuración de la imagen de la base de datos que vamos a utilizar, ejecutamos entonces: `docker compose up docker-compose.yml`
8. Cuando ya se haya lanzado nuestro servicio de manera correcta ingresaremos 