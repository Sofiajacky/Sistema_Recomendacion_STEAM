## FUNCIONES DE UTILIDAD PARA EL EDA
#---------------------------------------------------------------------------------------------------------
# Importaciones necesarias:
import pandas as pd
from textblob import TextBlob
import re

#---------------------------------------------------------------------------------------------------------

# La función "tipo_datos" hace un análisis de los tipos de datos y la presencia de valores nulos en un DataFrame y devuelve un resumen en forma de DataFrame que incluye esta información para cada columna del DataFrame original.
def tipo_datos(df):
    # Se crea un diccionario vacío para almacenar la información de resumen sobre los tipos de datos y valores nulos en cada columna del DataFrame.
    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": [], "nulos": []}
    
    # Itera sobre cada columna en el DataFrame.
    for columna in df.columns:
        # Calcula el porcentaje de valores no nulos en la columna actual.
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Agrega los datos necesarios al diccionario
        mi_dict["nombre_campo"].append(columna) 
        mi_dict["tipo_datos"].append(df[columna].dtype)  # Utiliza df[columna].dtype para obtener el tipo de dato de la columna.
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100 - porcentaje_no_nulos, 2))  # Corrección en el cálculo del porcentaje de nulos.
        mi_dict["nulos"].append(df[columna].isnull().sum())
    
    # Crea un DataFrame a partir del diccionario generado.
    df_info = pd.DataFrame(mi_dict)
        
    return df_info


#------------------------------------------------------------------------------------------------------------

# La función "resumen_porcentajes" cuenta la cantidad de True/False luego calcula el porcentaje.
def resumen_porcentajes(df, columna):

    # Cuanta la cantidad de True/False luego calcula el porcentaje
    counts = df[columna].value_counts()
    percentages = round(100 * counts / len(df),2)
    # Crea un dataframe con el resumen
    df_results = pd.DataFrame({
        "Cantidad": counts,
        "Porcentaje": percentages
    })
    return df_results

#------------------------------------------------------------------------------------------------------------

