# Proyecto MLOps: Sistema de Recomendación de Videojuegos para Usuarios en Steam
¡Bienvenidos al proyecto MLOps de Machine Learning Operations (MLOps)!

## Descripción del Problema
En este proyecto, nos enfrentamos al desafío de llevar un modelo de recomendación de videojuegos exitoso al mundo real. El ciclo de vida de un proyecto de Machine Learning abarca desde la recopilación y tratamiento de datos hasta el entrenamiento y mantenimiento del modelo.

## Contexto y Rol a Desarrollar
### Contexto
Trabajamos en Steam, una plataforma multinacional de videojuegos. Nuestro objetivo es crear un sistema de recomendación de videojuegos para usuarios.

### Rol a Desarrollar
Actuamos como Data Scientist y MLOps Engineer en Steam. Comenzamos desde cero para transformar datos sin estructura en un sistema de recomendación eficiente.

## Descripción del proyecto:
### Se trabaja con los siguientes datasets:
australian_user_reviews
australian_users_items
output_steam_games

### Proceso de [ETL](Data_ETL) :Transformaciones

Desanidado: Algunas columnas están anidadas, es decir, tienen un diccionario o una lista como valores en cada fila, las desanidamos para poder realizar algunas de las consultas API.

Eliminar columnas no utilizadas:
Se eliminan las columnas que no se utilizarán:
- De output_steam_games: 'publisher','url', 'reviews_url', 'specs', 'early_access', 'tags','title'.
- De australian_user_reviews: user_url, funny, last_edited, helpful.
- De australian_users_items: user_url, playtime_2weeks, steam_id, items_count.

Análisis y tratamiento de valores nulos:
En esta parte, se analizan los valores nulos en las columnas 'title' y 'app_name', se determina la cantidad de filas sin nulos y se identifica la fila donde están los datos nulos en 'app_name'.
Eliminación de filas nulas iniciales: *Se eliminan las primeras 88.310 filas del DataFrame, ya que se ha identificado que todas ellas contienen valores nulos en todas las columnas.*

Cambio del tipo de datos:
Las fechas se cambian a datetime para luego extraer el año.

## Feature Engineering
En el dataset user_reviews se crea la columna 'sentiment_analysis' para reemplazar la de user_reviews.review, aplicando análisis de sentimiento con NLP con la escala: malo:'0', neutral:'1' y positivo:'2'. 

### Desarrollo API
Se disponibilizan los datos de la empresa usando el framework FastAPI, proponiendo las siguientes consultas: 
- Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora: def developer( desarrollador : str )
- Cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items: def userdata( User_id : str )
- Usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento: def UserForGenre( genero : str )
- Top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado: def best_developer_year( año : int )
- Desarrollador y lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo: def developer_reviews_analysis( desarrolladora : str )

### Deployment
Se usa el servicio de Render que permite que la API pueda ser consumida desde la web.

### Análisis exploratorio de los datos [EDA](EDA.ipynb)
En el Análisis Exploratorio de Datos (EDA), se realizó una serie de pasos para comprender mejor la información contenida en este dataset y poder extraer algunas primeras aproximaciones y conclusiones.


### Modelo de aprendizaje automático [MODELO](Modelo_recomendacion.ipynb) 
Se desarrolló un modelo de recomendación item-item en un entorno de aprendizaje automático. 
se seleccionó un subconjunto de datos (en este caso, para que pudiera funcionar en la API, se tuvo que reducir la matriz a un 20%). 
Se calculó una matriz de similitud del coseno para determinar la similitud entre juegos basada en características como la fecha de lanzamiento y los géneros.
se implementó una función 'recomendacion_juego_muestreado' que toma el ID de un juego y devuelve una lista de 5 juegos recomendados similares al juego ingresado.

## Requisitos
fastapi
uvicorn
pandas
sqlalchemy
scikit-learn
pyarrow
fastparquet
numpy 

## Autora
Sofía Jacky-Rosell


