#
# This script takes data from 'Agregado MM_Hemofilia_2019' &
#'Agregado MM_Hemofilia_2018' it first clean up the data
# It also contains the process followed in order to merge the two
# given dataframes(clean) into a single one 'hmf1'.
# The fourth part of this script processes the dataset ('df.csv')
# -obtained from the merging process- assigned to delvelop the project.
# It then, takes the data and generate some graphs with ggplot2
#
# ###	Creator: Karem Alexandra Sastoque Mendez
# ###	First Version: 			        May 6 / 2020
# ###	Date of last version:  	         / 2020
#
# Des: 	        5
# 		        1 Outputs (dataset).
# Notes:         4 parts (data cleaning 1-2, merging, analysis)
#
# 	Important changes to made:
#                -
#                - Crear una llave por año y unidad territorial
#                - Cruzar territorio con codigos DANE

#                - cuando crucemos las bases de datos podremos indagar sobre
#
#                -

# ### 1. Data Preparation

# importing modules
import pandas as pd
import numpy as np
import locale
from datetime import datetime as dt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Displaying all dataframe columns
pd.set_option('display.max_columns', None)

#Loading datasets
base_2019 = pd.read_excel("C:\Users\usuario\Desktop\KASM\Tableros HIGIA\HEMOFILIA\Agregado MM_Hemofilia_2019.xlsx")
base_2018 = pd.read_excel("C:\Users\usuario\Desktop\KASM\Tableros HIGIA\HEMOFILIA\Agregado MM_Hemofilia_2018.xlsx")

# 1. Tener un código único para año y etiqueta
# 2. Append / concat dataframes

#creating a new column as a key for year and 'etiqueta'

#def anio_column(x):
#    for df

base_2019[anio] = 2019
base_2018[anio] = 2018

#def try_concat(x, y):
#    try:
#        return x + '-' + str(y)
#    except (ValueError, TypeError):
#        return np.nan

#base_2019[k_etiqueta] = [try_concat(x, y) for x, y in zip(base_2019[Etiqueta], base_2019[anio])]

base_2019[k_filt] = base_2019.Etiqueta + '-' + base_2019.anio.map(str)
base_2018[k_filt] = base_2018.Etiqueta + '-' + base_2018.anio.map(str)

bases = [base_2018, base_2019]
df_total = pd.concat(bases)

#las sacamos una columna por cada una de las categorías una a una por demografico
# llave nacional
# llave regional
# llave departamental
# llave municipal
# llave eapb
#


for categ in df_total['Categoria'].iterrows():
    if 'Municipio' in categ:
        df_total[['k_mpio_cod', 'k_mpio_name']] = df_total['Etiqueta'].str.split("-", expand=True)
    elif 'Departamento' in categ:
        df_total['k_dpto_name'] = df_total['Etiqueta']
    elif 'Región' in categ:
        df_total['k_region'] = df_total['Etiqueta']
    elif 'Nacional' in categ:
        df_total['k_nacional'] = df_total['Indicador MM']+ '-' + df_total.anio.map(str)
    elif 'EAPB' in categ:
        df_total['k_eapb'] = df_total['Etiqueta']
    elif 'Régimen' in categ:
        df_total['k_regimen'] = df_total['Etiqueta']
    elif 'Reglón' in categ:
        



for col in list(df_total):
    for x in df_total.iterrows():
        if 'Municipio' in x:
            new =  data[k_[x]].str.split(" ", n = 1, expand = True)
            df_total.[key_col] = df_total.loc[df_total[Etiqueta]] 'extract #before -'
