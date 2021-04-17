
---
# Title, summary, and page position.
linktitle: 3. Pandas
summary: Libreria de Manipulación y análisis de datos estructurados
weight: 30
icon: buromobelexperte
icon_pack: fab

# Page metadata.
title: PANDAS - Manipulacion de Datos con Python
date: "2021-04-17T00:00:00Z"
type: book  # Do not modify
---
Por [Jose R. Zapata](https://joserzapata.github.io/)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="joserzapata" data-color="#328cc1" data-emoji="" data-font="Cookie" data-text="Invítame a un Café" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script><br>

Pandas es una herramienta de manipulación de datos de alto nivel desarrollada por [Wes McKinney](http://wesmckinney.com/). Es construido sobre Numpy y permite el análisis de datos que cuenta con las estructuras de datos que necesitamos para limpiar los datos en bruto y que sean aptos para el análisis (por ejemplo, tablas). Como Pandas permite realizar tareas importantes, como alinear datos para su comparación, fusionar conjuntos de datos, gestión de datos perdidos, etc., se ha convertido en una librería muy importante para procesar datos a alto nivel en Python (es decir, estadísticas ). Pandas fue diseñada originalmente para gestionar datos financieros, y como alternativo al uso de hojas de cálculo (es decir, Microsoft Excel).

Los principales tipos de datos que pueden representarse con pandas son:

- Datos tabulares con columnas de tipo heterogéneo con etiquetas en columnas y filas.
- Series temporales

Pandas proporciona herramientas que permiten:

- leer y escribir datos en diferentes formatos: CSV, JSON, Excel, bases SQL y formato HDF5
- seleccionar y filtrar de manera sencilla tablas de datos en función de posición, valor o etiquetas
- fusionar y unir datos
- transformar datos aplicando funciones tanto en global como por ventanas
- manipulación de series temporales
- hacer gráficas

En pandas existen tres tipos básicos de objetos todos ellos basados a su vez en Numpy:

- Series (listas, 1D)
- DataFrame (tablas, 2D)


Por lo tanto, Pandas nos proporciona las estructuras de datos y funciones necesarias para el análisis de datos.


## Instalar Pandas
Pandas ya esta preinstalado si se usa Google Collaboratory, si va realizar una instalacion en su computador
### PIP
```
pip install pandas
```
### Conda
Si instalo Anaconda, pandas ya viene preinstalado
```
conda install pandas
```

## Importando Pandas
La libreria Pandas se importa de la siguiente manera


```python
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy
```

## Series
Una serie es el primer tipo de datos de pandas y es muy similar a una matriz NumPy (de hecho está construida sobre el objeto de matriz NumPy). Lo que diferencia un arreglo NumPy de una serie, es que una serie puede tener etiquetas en los ejes, lo que significa que puede ser indexada por una etiqueta, en lugar de solo una ubicación numérica. Tampoco necesita contener datos numéricos, puede contener cualquier Objeto de Python arbitrario.

### Creando una Serie

Puede convertir una lista, una matriz numpy o un diccionario en una serie, usando el metodo pd.Series:


```python
# Crear diferentes tipos de datos
labels = ['a','b','c'] # lista de eetiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
d = {'a':10,'b':20,'c':30} # Creacion de un diccionario
```

#### Desde Listas


```python
# Convertir una lista en series usando el metodo pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
pd.Series(data=my_list)
```




    0    10
    1    20
    2    30
    dtype: int64




```python
# Convertir una lista en series usando el metodo pd.Series
# se puede ingresar el nombre de las posiciones
pd.Series(data=my_list,index=labels)
```




    a    10
    b    20
    c    30
    dtype: int64




```python
# No es necesario ingresar la palabra de 'data =''  en el argumento
pd.Series(my_list,labels)
```




    a    10
    b    20
    c    30
    dtype: int64



#### Desde Arreglos NumPy


```python
# Convertir un arreglo en series usando el metodo pd.Series
pd.Series(arr)
```




    0    10
    1    20
    2    30
    dtype: int64




```python
# Convertir un arreglo en series indicando tambien los valores del index
pd.Series(arr,labels)
```




    a    10
    b    20
    c    30
    dtype: int64



#### Desde un Diccionario


```python
# Convertir un diccionario en series usando el metodo pd.Series
# Como el diccionario ya tiene clave entonces se le asigna como valor de la posicion
pd.Series(d)
```




    a    10
    b    20
    c    30
    dtype: int64



### Datos en una Series

Una serie de pandas puede contener una variedad de tipos de objetos:


```python
# Creando una serie basado solo en una lista de letras
pd.Series(data=labels)
```




    0    a
    1    b
    2    c
    dtype: object



### Indexacion

La clave para usar una serie es entender su índice. Pandas hace uso de estos nombres o números de índice al permitir búsquedas rápidas de información (funciona como una tabla hash o diccionario).

Veamos algunos ejemplos de cómo obtener información de una serie. Vamos a crear dos series, ser1 y ser2:


```python
# Creacion de una serie con sus labels o indices
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   
```


```python
ser1
```




    USA        1
    Germany    2
    USSR       3
    Japan      4
    dtype: int64




```python
# Creacion de una serie con sus labels o indices
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   
```


```python
ser2
```




    USA        1
    Germany    2
    Italy      5
    Japan      4
    dtype: int64




```python
# La busqueda en una serie es igual como en un diccionario
ser1['USA']
```




    1




```python
# La busqueda en una serie es igual como en un diccionario
ser2['Germany']
```




    2



Las operaciones también se realizan según el índice:


```python
# Observe los resultados de los paises que solo estan en una serie y no en las dos
ser1 + ser2
```




    Germany    4.0
    Italy      NaN
    Japan      8.0
    USA        2.0
    USSR       NaN
    dtype: float64



## DataFrames

Los *DataFrames* son la estructura mas importante en pandas y están directamente inspirados en el lenguaje de programación R. Se puede pensar en un DataFrame como un conjunto de *Series* reunidas que comparten el mismo índice.
En los *DataFrame* tenemos la opción de especificar tanto el index (el nombre de las filas) como columns (el nombre de las columnas).


```python
# Importar la funcion de NumPy para crear arreglos de numeros enteros
from numpy.random import randn
np.random.seed(101) # Inicializar el generador aleatorio
```


```python
# Forma rapida de crear una lista de python desde strings
'A B C D E'.split()
```




    ['A', 'B', 'C', 'D', 'E']




```python
# Crear un dataframe con numeros aleatorios de 4 Columnas y 5 Filas
# Crear listas rapidamente usando la funcion split 'A B C D E'.split()
# Esto evita tener que escribir repetidamente las comas

df = pd.DataFrame(randn(5,4),
                  index='A B C D E'.split(),
                  columns='W X Y Z'.split())
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



### Descripcion general del dataframe
#### Numero de Filas y Columnas


```python
df.shape # retorna un Tuple asi: (filas, col)
```




    (5, 4)



#### Informacion General de los datos


```python
# Informacion general de los datos de cada cloumna
# Indica el numero de filas del dataset
# Muestra el numero de datos No Nulos por columna (valores validos)
# Tipo de dato de cada columna
# Tamaño total del dataset
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 5 entries, A to E
    Data columns (total 4 columns):
    W    5 non-null float64
    X    5 non-null float64
    Y    5 non-null float64
    Z    5 non-null float64
    dtypes: float64(4)
    memory usage: 200.0+ bytes



```python
# Tipos de datos que existen en las columnas del dataframe
df.dtypes
```




    W    float64
    X    float64
    Y    float64
    Z    float64
    dtype: object



#### Resumen de estadistica descriptiva General
el metodo `.describe()` de los dataframes presenta un resumen de la estadistica descriptiva general de las columnas numericas del dataframe, presenta la informacion de:
- Promedio (mean)
- Desviacion estandard (std)
- Valor minimo
- Valor maximo
- Cuartiles (25%, 50% y 75%)


```python
df.describe() # No muestra la informacion de las columnas categoricas
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.343858</td>
      <td>0.453764</td>
      <td>0.452287</td>
      <td>0.431871</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.681131</td>
      <td>1.061385</td>
      <td>1.454516</td>
      <td>0.594708</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.018168</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.188695</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.190794</td>
      <td>0.628133</td>
      <td>0.528813</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.651118</td>
      <td>0.740122</td>
      <td>0.907969</td>
      <td>0.683509</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.706850</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.955057</td>
    </tr>
  </tbody>
</table>
</div>



#### Ver Primeros elementos del dataframe


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



#### Ver Ultimos elementos del dataframe


```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



### Seleccion y Indexacion

Existen diversos métodos para tomar datos de un DataFrame


```python
# Regresara todos los datos de la columna W
df['W']
```




    A    2.706850
    B    0.651118
    C   -2.018168
    D    0.188695
    E    0.190794
    Name: W, dtype: float64




```python
# Seleccionar dos o mas columnas
# Pasar una lista con los nombres de las columnas

df[['W','Z']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Seleccionar dos o mas columnas
# Pasar una lista con los nombres de las columnas
# Puedo indicar el orden de las columnas

df[['X','W','Z']] 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>W</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.628133</td>
      <td>2.706850</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.319318</td>
      <td>0.651118</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.740122</td>
      <td>-2.018168</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.758872</td>
      <td>0.188695</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>1.978757</td>
      <td>0.190794</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



Las columnas de un DataFrame Columns son solo Series


```python
type(df['W']) # Tipos de datos
```




    pandas.core.series.Series



#### Creando una Nueva Columna


```python
# Nueva columna igual a la suma de otras dos
# operacion vectorizada
df['new'] = df['W'] + df['Y']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
      <td>3.614819</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
      <td>-0.196959</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
      <td>-1.489355</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
      <td>-0.744542</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
      <td>2.796762</td>
    </tr>
  </tbody>
</table>
</div>



#### Eliminando Columnas


```python
df.drop('new',axis=1) # axis = 0 elimina filas(index) axis = 1 elimina columnas
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# No se aplica a el dataframe a menos que se especifique.
# Como se ve la operacion pasada no quedo grabada
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
      <td>3.614819</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
      <td>-0.196959</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
      <td>-1.489355</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
      <td>-0.744542</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
      <td>2.796762</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Para que quede grabado se puede hacer de dos formas
# df = df.drop('new',axis=1) # Forma 1
df.drop('new', axis=1, inplace=True) # Forma 2
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



También se puede sacar filas de esta manera:


```python
df.drop('E',axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Otra manera de borrar las columnas es
del df['X'] # Esta funcion es INPLACE
df 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



#### Obtener los nombres de las columnas y los indices (index):


```python
df.columns # nombres de las columnas
```




    Index(['W', 'Y', 'Z'], dtype='object')




```python
df.index # nombres de los indices
```




    Index(['A', 'B', 'C', 'D', 'E'], dtype='object')



#### Seleccionando Filas y Columnas

las dos formas de seleccion principal son:
* `DataFrame.loc[etiqueta_fila, etiqueta_columna]`  <- por etiquetas
* `DataFrame.iloc[indice_fila, indice_columna]` <- por indices


```python
# la funcion loc busca por medio de los nombres de los indices y columnas
df.loc['A'] # se selecciona todos los valores de la fila 'A'
```




    W    2.706850
    Y    0.907969
    Z    0.503826
    Name: A, dtype: float64



O basado en la posicion (index) en vez de usar la etiqueta


```python
df.iloc[2] # Se seleccionan los valores de la fila con indice 2
# recordar que los index empiezan en cero
```




    W   -2.018168
    Y    0.528813
    Z   -0.589001
    Name: C, dtype: float64



#### Seleccionar un subconjunto de filas y columnas


```python
# Mediante etiquetas
# se selecciona el elemento que esta en la fila=B Col=Y
df.loc['B','Y'] # con etiquetas
```




    -0.8480769834036315




```python
# Mediante etiquetas
# se selecciona un subconjunto de datos que estan entre
# filas = A, B   Cols= W, Y
df.loc[['A','B'],['W','Y']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[['B','A'],['Y','W']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Y</th>
      <th>W</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>B</th>
      <td>-0.848077</td>
      <td>0.651118</td>
    </tr>
    <tr>
      <th>A</th>
      <td>0.907969</td>
      <td>2.706850</td>
    </tr>
  </tbody>
</table>
</div>



### Seleccion Condicional o Filtros

Una característica importante de pandas es la selección condicional usando la notación de corchetes, muy similar a NumPy:


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Devuelve un dataframe con booleans
# segun si se cumple o no la condicion
df>0
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>B</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>C</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>D</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>E</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Esta operacion solo mostrara los valores del dataframe que cumplen la condicion
# los que no cumplen devuelve el valor NaN
df[df>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>NaN</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>NaN</td>
      <td>0.528813</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>NaN</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# seleccionar todas las filas donde el valor
# que esta en la columna 'W' sea mayor que cero
df[df['W']>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de la columna 'Y'
df[df['W']>0]['Y']
```




    A    0.907969
    B   -0.848077
    D   -0.933237
    E    2.605967
    Name: Y, dtype: float64




```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de las columna 'Y' y 'X'
df[df['W']>0][['Y','Z']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



Para dos condiciones, se usa los booleanos de esta forma

- `|` en vez de `or` 
- `&` en vez de `and`
- `~` en vez de `not`

Por amor a Dios, recuerde usar paréntesis:


```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y tambien donde 'Y' sea mayor que 0.5
df[(df['W']>0) & (df['Y'] > 0.5)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



#### `.query()` Busqueda condicional

Los terminos de busqueda condicional o filtros se entregan al metodo como tipo 'string'


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# seleccionar todas las filas donde el valor
# que esta en la columna 'W' sea mayor que cero

#df[df['W']>0]
df.query('W>0')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de la columna 'Y'

#df[df['W']>0]['Y']
df.query('W>0')['Y']
```




    A    0.907969
    B   -0.848077
    D   -0.933237
    E    2.605967
    Name: Y, dtype: float64




```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de las columna 'Y' y 'X'

#df[df['W']>0][['Y','Z']]
df.query('W>0')[['Y','Z']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



Para dos condiciones, puede usar | = `or` y & = `and` con paréntesis:


```python
# Seleccionar las filas donde 'W' sea mayor que cero
# y tambien donde 'Y' sea mayor que 0.5

#df[(df['W']>0) & (df['Y'] > 0.5)]
df.query('W>0 and Y>0.5')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



### Cambio de columna de Indexacion

Analicemos algunas características más de la indexación, incluido el restablecimiento del índice o el establecimiento de parametros.


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reinicializar el indice a su valor por defecto 0,1...n index
df = df.reset_index()
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
newind = 'CA NY WY OR CO'.split() # crear una lista con strings
newind
```




    ['CA', 'NY', 'WY', 'OR', 'CO']




```python
# Agregar la lista creaada en el paso anterior al dataframe
df['States'] = newind
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
      <th>States</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
      <td>CA</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
      <td>NY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
      <td>WY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
      <td>OR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
      <td>CO</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Redefinir la columna states como el indice
df.set_index('States')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
    <tr>
      <th>States</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CA</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>NY</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>WY</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>OR</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>CO</th>
      <td>E</td>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>




```python
# por que no queda establecido el indice?
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
      <th>States</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
      <td>CA</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
      <td>NY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
      <td>WY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
      <td>OR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
      <td>CO</td>
    </tr>
  </tbody>
</table>
</div>




```python
# para establecer el indice debe ser una funcion inplace
df.set_index('States',inplace=True)
#df = df.set_index('States') # otra forma de hacerlo
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>W</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
    <tr>
      <th>States</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CA</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>NY</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>WY</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>OR</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>CO</th>
      <td>E</td>
      <td>0.190794</td>
      <td>2.605967</td>
      <td>0.683509</td>
    </tr>
  </tbody>
</table>
</div>



---
## Groupby (Agrupacion por filas)

El método groupby le permite agrupar filas de datos y llamar a funciones agregadas


```python
import pandas as pd
# Crear dataframe desde un diccionario
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
data
```




    {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
     'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
     'Sales': [200, 120, 340, 124, 243, 350]}




```python
#conversion del diccionario a dataframe
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Company</th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>Sam</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GOOG</td>
      <td>Charlie</td>
      <td>120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>Amy</td>
      <td>340</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSFT</td>
      <td>Vanessa</td>
      <td>124</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FB</td>
      <td>Carl</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FB</td>
      <td>Sarah</td>
      <td>350</td>
    </tr>
  </tbody>
</table>
</div>



**Se puede usar el método `.groupby()` para agrupar filas en función de un nombre de columna. Por ejemplo, vamos a agruparnos a partir de la Compañía. Esto creará un objeto `DataFrameGroupBy`:**


```python
#agrupar por Company
df.groupby('Company')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f059acb5128>



Se puede grabar este objeto en una nueva variable:


```python
by_comp = df.groupby("Company")
```

utilizar los métodos agregados del objeto:


```python
# Promedio de ventas por company
by_comp.mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>296.5</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>160.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>232.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# agrupar por compañia y calcular el promedio por cada una
df.groupby('Company').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>296.5</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>160.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>232.0</td>
    </tr>
  </tbody>
</table>
</div>



Más ejemplos de métodos agregados:


```python
# agrupar por compañia y calcular la desviacion estandard
by_comp.std()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>75.660426</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>56.568542</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>152.735065</td>
    </tr>
  </tbody>
</table>
</div>




```python
# agrupar por compañia y calcular el minimo
by_comp.min()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>Carl</td>
      <td>243</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>Charlie</td>
      <td>120</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>Amy</td>
      <td>124</td>
    </tr>
  </tbody>
</table>
</div>




```python
# agrupar por compañia y calcular el maximo
by_comp.max()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>Sarah</td>
      <td>350</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>Sam</td>
      <td>200</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>Vanessa</td>
      <td>340</td>
    </tr>
  </tbody>
</table>
</div>




```python
# agrupar por compañia y sumar los elementos que hay excluyendo los NaN
by_comp.count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Una de las funciones mas usadas para descripcion estadistica de un dataframe
# Genera estadísticas descriptivas que resumen la tendencia central, la dispersión y la forma de la distribución de un conjunto de datos, excluyendo los valores `` NaN``.
# by_comp.describe(include = 'all') # incluir todo
by_comp.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead tr th {
        text-align: left;
    }
    
    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">Sales</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>FB</th>
      <td>2.0</td>
      <td>296.5</td>
      <td>75.660426</td>
      <td>243.0</td>
      <td>269.75</td>
      <td>296.5</td>
      <td>323.25</td>
      <td>350.0</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>2.0</td>
      <td>160.0</td>
      <td>56.568542</td>
      <td>120.0</td>
      <td>140.00</td>
      <td>160.0</td>
      <td>180.00</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>2.0</td>
      <td>232.0</td>
      <td>152.735065</td>
      <td>124.0</td>
      <td>178.00</td>
      <td>232.0</td>
      <td>286.00</td>
      <td>340.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Una de las funciones mas usadas para descripcion estadistica de un dataframe
# Genera estadísticas descriptivas que resumen la tendencia central, la dispersión y la forma de la distribución de un conjunto de datos, excluyendo los valores `` NaN``.
# Transponer la descripcion
by_comp.describe().transpose()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Company</th>
      <th>FB</th>
      <th>GOOG</th>
      <th>MSFT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">Sales</th>
      <th>count</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>296.500000</td>
      <td>160.000000</td>
      <td>232.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>75.660426</td>
      <td>56.568542</td>
      <td>152.735065</td>
    </tr>
    <tr>
      <th>min</th>
      <td>243.000000</td>
      <td>120.000000</td>
      <td>124.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>269.750000</td>
      <td>140.000000</td>
      <td>178.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>296.500000</td>
      <td>160.000000</td>
      <td>232.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>323.250000</td>
      <td>180.000000</td>
      <td>286.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>350.000000</td>
      <td>200.000000</td>
      <td>340.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Descripcion estadistica de los datos de la copmañia GOOG
by_comp.describe().transpose()['GOOG']
```




    Sales  count      2.000000
           mean     160.000000
           std       56.568542
           min      120.000000
           25%      140.000000
           50%      160.000000
           75%      180.000000
           max      200.000000
    Name: GOOG, dtype: float64



## Pivot Tables

La funcionlidad "Pivot_table" es muy utilizada y popular en las conocidas "hojas de cálculo" tipo, OpenOffice, LibreOffice, Excel, Lotus, etc. Esta funcionalidad nos permite agrupar, ordenar, calcular datos y manejar datos de una forma muy similar a la que se hace con las hojas de cálculo.
[mas informacion](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html)

La principal función del "Pivot_table" son las agrupaciones de datos a las que se les suelen aplicar funciones matemáticas como sumatorios, promedios, etc


```python
import seaborn as sns # importar la libreria seaborn
# cargar dataset del titanic
titanic = sns.load_dataset('titanic')
titanic.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



Haciendo el Pivot table a mano para obtener el promedio de personas que sobrevivieron por genero


```python
# 1. Agrupar por genero
# 2. Obtener los sobrevivientes
# 3. Calcular el promedio
titanic.groupby('sex')[['survived']].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.742038</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.188908</td>
    </tr>
  </tbody>
</table>
</div>



promedio de cuantos sobrevivieron por genero divididos por clase


```python
# 1. Agrupar por genero y clase
# 2. Obtener los sobrevivientes
# 3. Calcular el promedio
# 4. Poner el resultado como una tabla (.unstack)
titanic.groupby(['sex', 'class'])['survived'].mean().unstack()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
    </tr>
  </tbody>
</table>
</div>



Usando Pivot tables


```python
titanic.pivot_table('survived', index='sex', columns='class')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic.pivot_table('survived', index='sex', columns='class', margins=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>class</th>
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
      <th>All</th>
    </tr>
    <tr>
      <th>sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>0.968085</td>
      <td>0.921053</td>
      <td>0.500000</td>
      <td>0.742038</td>
    </tr>
    <tr>
      <th>male</th>
      <td>0.368852</td>
      <td>0.157407</td>
      <td>0.135447</td>
      <td>0.188908</td>
    </tr>
    <tr>
      <th>All</th>
      <td>0.629630</td>
      <td>0.472826</td>
      <td>0.242363</td>
      <td>0.383838</td>
    </tr>
  </tbody>
</table>
</div>



Otro ejemplo mas simple:


```python
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>one</td>
      <td>y</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>x</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bar</td>
      <td>one</td>
      <td>x</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>one</td>
      <td>y</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# pivot tables
df.pivot_table(values='D',index=['A', 'B'],columns=['C'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>x</th>
      <th>y</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>two</th>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



---
## Concatenar, Fusionar y Unir (Concatenating, Merging, Joining)

Hay 3 formas principales de combinar DataFrames: concatenar, fusionar y unir.


```python
# DataFrames de ejemplo para concatenacion
import pandas as pd
```


```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
```


```python
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
```


```python
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>



### Concatenacion (Concatenation)

La concatenación básicamente combina DataFrames. Tenga en cuenta que las dimensiones deben coincidir a lo largo del eje con el que se está concatenando. 

la concatenacion se hace con dataframes de diferentes indices

Puede usar `.concat()` y pasar una lista de DataFrames para concatenar juntos:


```python
# Concatenar cada dateframe verticalmente, ya que coinciden los nombres de las columnas
pd.concat([df1,df2,df3])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#concatenar dataframe horizontalmente, como no coinciden los index observar lo que ocurre
pd.concat([df1,df2,df3],axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>



### Fusion (Merging)

La función `merge()` le permite fusionar DataFrames juntos utilizando una lógica similar a la combinación de Tablas SQL. Por ejemplo:


```python
# DataFrames de ejemplo para merging
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    
```


```python
left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# how='inner' utilice la intersección de las claves de ambos marcos, similar a una combinación interna de SQL; 
# las keys son comunes
pd.merge(left,right,how='inner',on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



#### Un ejemplo mas complicado:
- Natural join: para mantener solo las filas que coinciden con los marcos de datos, especifique el argumento how = 'inner'.
- Full outer join: para mantener todas las filas de ambos dataframe, especifique how = 'OUTER'.
- Left outer join: para incluir todas las filas de su dataframe x y solo aquellas de y que coincidan, especifique how=‘left’.
- Right outer join: para incluir todas las filas de su dataframe y y solo aquellas de x que coincidan, especifique how=‘right’.

![](http://www.datasciencemadesimple.com/wp-content/uploads/2017/09/join-or-merge-in-python-pandas-1.png)


```python
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
```


```python
left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# fusionando comparando las mismas claves que tengan comunes
pd.merge(left, right, on=['key1', 'key2'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# fusionando totalmente las dos tablas con las claves
pd.merge(left, right, how='outer', on=['key1', 'key2'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# fusionando usando las claves de la tabla right
pd.merge(left, right, how='right', on=['key1', 'key2'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# fusionando usando las claves de la tabla left
pd.merge(left, right, how='left', on=['key1', 'key2'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Unir (Joining)

Unir (join) es un método conveniente para combinar las columnas de dos DataFrames potencialmente indexados de forma diferente en un solo DataFrame.
Join hace uniones de índices sobre índices o de índices sobre columnas


```python
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
```


```python
left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# unir el dataframe 'right' a el dataframe 'left'
left.join(right)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# unir el dataframe 'left' a el dataframe 'right'
right.join(left)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>C0</td>
      <td>D0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>C2</td>
      <td>D2</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# unir el dataframe 'left' a el dataframe 'rigth'
#how = outer
left.join(right, how='outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



## Datos Categoricos
- La busqueda en datos categoricos es mucho mas rapida
- Ocupan Menos memoria que si los datos estan como string
- Se pueden tener datos categoricos Ordinales

Mas informacion de datos categoricos:

https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html

### Creacion


```python
# Creacion de una serie de datos categoricos
cate = pd.Series(["manzana", "banano", "corozo", "manzana","pera"], dtype="category")
cate
```




    0    manzana
    1     banano
    2     corozo
    3    manzana
    4       pera
    dtype: category
    Categories (4, object): [banano, corozo, manzana, pera]




```python
cate.dtypes
```




    CategoricalDtype(categories=['banano', 'corozo', 'manzana', 'pera'], ordered=False)




```python
cate.describe()
```




    count           5
    unique          4
    top       manzana
    freq            2
    dtype: object




```python
# Creando primero los datos y luego convirtiendolos en categoricos
df_cate = pd.DataFrame({"Fruta":["manzana", "banano", "corozo", "manzana","pera"]})
df_cate
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Fruta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>manzana</td>
    </tr>
    <tr>
      <th>1</th>
      <td>banano</td>
    </tr>
    <tr>
      <th>2</th>
      <td>corozo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>manzana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pera</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Observar los tipos de datos en el data frame
df_cate.dtypes
```




    Fruta    object
    dtype: object




```python
df_cate["Fruta2"] = df_cate["Fruta"].astype('category')
df_cate
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Fruta</th>
      <th>Fruta2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>manzana</td>
      <td>manzana</td>
    </tr>
    <tr>
      <th>1</th>
      <td>banano</td>
      <td>banano</td>
    </tr>
    <tr>
      <th>2</th>
      <td>corozo</td>
      <td>corozo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>manzana</td>
      <td>manzana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pera</td>
      <td>pera</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Observar los tipos de datos en el dataframe
df_cate.dtypes
```




    Fruta       object
    Fruta2    category
    dtype: object




```python
# Crear los datos categoricos desde a declaracion de los datos
df_cate = pd.DataFrame({'A': list('abca'), 'B': list('bccd')}, dtype="category")
df_cate
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cate.dtypes
```




    A    category
    B    category
    dtype: object




```python
df_cate.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>top</th>
      <td>a</td>
      <td>c</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Categoricos Ordinales


```python
from pandas.api.types import CategoricalDtype
```


```python
# creacion de dataframe con datos
df_cate = pd.DataFrame({'A': list('abca'), 'B': list('bccd')})
df_cate
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cate.dtypes
```




    A    object
    B    object
    dtype: object




```python
# Definicion de los tipos de datos y que estan en orden
df_cate["A"] = df_cate["A"].astype(CategoricalDtype(['a','b','c','d'], ordered=True))
df_cate
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cate["A"]
```




    0    a
    1    b
    2    c
    3    a
    Name: A, dtype: category
    Categories (4, object): [a < b < c < d]




```python
# Los datos no tienen que ser strngs para qeu sean categoricos
s = pd.Series([1, 2, 3, 1], dtype="category")
s
```




    0    1
    1    2
    2    3
    3    1
    dtype: category
    Categories (3, int64): [1, 2, 3]




```python
s = s.cat.set_categories([2, 3, 1], ordered=True)
s
```




    0    1
    1    2
    2    3
    3    1
    dtype: category
    Categories (3, int64): [2 < 3 < 1]



---
## Datos Faltantes (Missing data)

Métodos para Manejar datos faltantes en pandas:


```python
# Declaracion de data frame con algunos datos faltantes
# NaN = Not a Number
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Detectar si Faltan datos


```python
# verificar cuales valores son NaN o nulos (Null)
df.isna()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# verificar cuales valores son na
# el metodo .isnull() es igual a .isna()
df.isnull()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Verificar si hay datos faltantes por columna
df.isnull().any()
```




    A     True
    B     True
    C    False
    dtype: bool



### Numero de datos faltantes

Calcular el numero de datos nulos que hay por columna


```python
# Numero de datos faltantes por columna
df.isnull().sum()
```




    A    1
    B    2
    C    0
    dtype: int64



### Eliminar datos Faltantes


```python
# Eliminar todas las filas que tengan datos faltantes
df.dropna(axis=0) # cuando son filas no es neceario escribir axis=0
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Eliminar todas las columnas que tengan datos faltantes
df.dropna(axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# eliminar las filas que tengas 2 o mas valores NaN
df.dropna(thresh=2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Reemplazar los datos faltantes


```python
# Llenar los datos faltantes con el dato que nos interese
df.fillna(value='FILL VALUE') # llenar los espacios con un string
                              # puede ser una palabra, numero , etc
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>FILL VALUE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FILL VALUE</td>
      <td>FILL VALUE</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Llenar los datos faltantes con el dato que nos interese
df.fillna(value=99) # llenar los espacios con un numero
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>99.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>99.0</td>
      <td>99.0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Llenar los datos faltantes con el promedio de esa columna
df['A'].fillna(value=df['A'].mean())
```




    0    1.0
    1    2.0
    2    1.5
    Name: A, dtype: float64




```python
# Llenar los datos faltantes con el promedio de cada columna
df.fillna(value=df.mean())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>5.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.5</td>
      <td>5.0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## Datos unicos (Unique Values)


```python
import pandas as pd
# crear un dataframe
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head() # solamente mostrar los primeros elementos del dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>abc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>def</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>ghi</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>xyz</td>
    </tr>
  </tbody>
</table>
</div>




```python
# valores unicos de la columna col2
df['col2'].unique()
```




    array([444, 555, 666])




```python
# Numero de valores unicos en el dataframe
df['col2'].nunique()
```




    3




```python
# contar cuanto se repiten cada uno de los valores
df['col2'].value_counts()
```




    444    2
    555    1
    666    1
    Name: col2, dtype: int64



## Datos Duplicados
Se puede borrar los registros que son exactamente iguales en todos los valores de las columnas


```python
import pandas as pd
```


```python
datos = {'name': ['James', 'Jason', 'Rogers', 'Jason'], 'age': [18, 20, 22, 20], 'job': ['Assistant', 'Manager', 'Clerk', 'Manager']}
df_dup = pd.DataFrame(datos)
df_dup
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Metodo para detectar los datos duplicados
# me sirve para ver si existen registros duplicados
df_dup.duplicated()
```




    0    False
    1    False
    2    False
    3     True
    dtype: bool




```python
# Contar cuantos datos duplicados existen
df_dup.duplicated().sum()
```




    1




```python
# Para remover los datos duplicados
df_dup.drop_duplicates()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
  </tbody>
</table>
</div>




```python
# El metodo drop_duplicates entrega el data frame sin duplicados
# Pero la funcion no es inplace, osea que el dataframe original sigue igual
df_dup
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_dup.drop_duplicates(inplace=True)
df_dup
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
  </tbody>
</table>
</div>



### Duplicados por Columna
Se pueden borrar los valores que se repitan solamente verificando la columna


```python
frame_datos = {'name': ['James', 'Jason', 'Rogers', 'Jason'], 'age': [18, 20, 22, 21], 'job': ['Assistant', 'Manager', 'Clerk', 'Employee']}
df_dup = pd.DataFrame(frame_datos)
df_dup
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jason</td>
      <td>21</td>
      <td>Employee</td>
    </tr>
  </tbody>
</table>
</div>



el valor de jason esta duplicado en la columna name


```python
# recordar que estas funciones no son inplace
df_dup.drop_duplicates(['name'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>job</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James</td>
      <td>18</td>
      <td>Assistant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>20</td>
      <td>Manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rogers</td>
      <td>22</td>
      <td>Clerk</td>
    </tr>
  </tbody>
</table>
</div>



## Outliers
Una de las formas de eliminar los aoutliers es identificando cual sera el rango en el que queremos nuestros datos y limitar los datos entre ese rango


```python
import seaborn as sns # importar la libreria seaborn
# cargar dataset del titanic
titanic = sns.load_dataset('titanic')
titanic.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
edad = titanic['age']
edad
```




    0      22.0
    1      38.0
    2      26.0
    3      35.0
    4      35.0
    5       NaN
    6      54.0
    7       2.0
    8      27.0
    9      14.0
    10      4.0
    11     58.0
    12     20.0
    13     39.0
    14     14.0
    15     55.0
    16      2.0
    17      NaN
    18     31.0
    19      NaN
    20     35.0
    21     34.0
    22     15.0
    23     28.0
    24      8.0
    25     38.0
    26      NaN
    27     19.0
    28      NaN
    29      NaN
           ... 
    861    21.0
    862    48.0
    863     NaN
    864    24.0
    865    42.0
    866    27.0
    867    31.0
    868     NaN
    869     4.0
    870    26.0
    871    47.0
    872    33.0
    873    47.0
    874    28.0
    875    15.0
    876    20.0
    877    19.0
    878     NaN
    879    56.0
    880    25.0
    881    33.0
    882    22.0
    883    28.0
    884    25.0
    885    39.0
    886    27.0
    887    19.0
    888     NaN
    889    26.0
    890    32.0
    Name: age, Length: 891, dtype: float64




```python
# Cual es la edad maxima
edad.max()
```




    80.0




```python
# Cual es la edad Minima
edad.min()
```




    0.42



Solo por hacer el ejercicio se delimitaran las edades entre 1 y 70 años

esto se puede hacer con el metodo `.clip(lower = Valor mas bajo, upper = valor mas alto)`


```python
edad = edad.clip(lower=1,upper = 70)
```


```python
edad.max()
```




    70.0




```python
edad.min()
```




    1.0



## Tablas de Contingencia (two way tables)


```python
# Crear Datos
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['infantry', 'infantry', 'cavalry', 'cavalry', 'infantry', 'infantry', 'cavalry', 'cavalry','infantry', 'infantry', 'cavalry', 'cavalry'], 
        'experience': ['veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie','veteran', 'rookie', 'veteran', 'rookie'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'experience', 'name', 'preTestScore', 'postTestScore'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>experience</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>infantry</td>
      <td>veteran</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>infantry</td>
      <td>rookie</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>cavalry</td>
      <td>veteran</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>cavalry</td>
      <td>rookie</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Tabla de contingencia por compañía y regimiento
pd.crosstab(df['regiment'], df['company'], margins=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>company</th>
      <th>cavalry</th>
      <th>infantry</th>
      <th>All</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>All</th>
      <td>6</td>
      <td>6</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Tabla de contingencia de compañia y experiencia por regimiento
pd.crosstab([df['company'], df['experience']], df['regiment'],  margins=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>Dragoons</th>
      <th>Nighthawks</th>
      <th>Scouts</th>
      <th>All</th>
    </tr>
    <tr>
      <th>company</th>
      <th>experience</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">cavalry</th>
      <th>rookie</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>veteran</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">infantry</th>
      <th>rookie</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>veteran</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## Metodos y Funciones en Pandas

Todos los metodos de los dataframe de pandas se pueden encontrar en:

http://pandas.pydata.org/pandas-docs/stable/reference/frame.html


```python
import pandas as pd
# crear un dataframe
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],
                   'col3':['mama   ','  papa','   HIJO  ','HiJa']})
df.head() # solamente mostrar los primeros elementos del dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>mama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>papa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>HIJO</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>HiJa</td>
    </tr>
  </tbody>
</table>
</div>



### Metodos Basicos Pandas

Ejemplos simples de los metodos de los dataframe de pandas

Para informacion completa de los metodos de computacion y estadisticos ver:

http://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats


```python
# Suma total de cada Columna, si es categorico no lo suma
df.sum()
```




    col1                            10
    col2                          2109
    col3    mama     papa   HIJO  HiJa
    dtype: object




```python
# Metodo en una sola columna
df['col1'].sum()
```




    10




```python
# Metodo en varias columnas
df[['col1','col2']].sum()
```




    col1      10
    col2    2109
    dtype: int64




```python
# Valor Minimo cada Columna
df.min()
```




    col1            1
    col2          444
    col3       HIJO  
    dtype: object




```python
# Valor Maximo cada Columna
df.max()
```




    col1          4
    col2        666
    col3    mama   
    dtype: object



### Metodos de Informacion General


```python
# Cargar la base de datos 'mpg' de la libreria seaborn
import seaborn as sns

# los datos se cargan en un dataframe
data = sns.load_dataset('mpg')
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 398 entries, 0 to 397
    Data columns (total 9 columns):
    mpg             398 non-null float64
    cylinders       398 non-null int64
    displacement    398 non-null float64
    horsepower      392 non-null float64
    weight          398 non-null int64
    acceleration    398 non-null float64
    model_year      398 non-null int64
    origin          398 non-null object
    name            398 non-null object
    dtypes: float64(4), int64(3), object(2)
    memory usage: 28.1+ KB



```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
      <td>usa</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
      <td>usa</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
      <td>usa</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
      <td>usa</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
      <td>usa</td>
      <td>ford torino</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.describe() # ver datos estadisticos de las columnas numericas
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>392.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>23.514573</td>
      <td>5.454774</td>
      <td>193.425879</td>
      <td>104.469388</td>
      <td>2970.424623</td>
      <td>15.568090</td>
      <td>76.010050</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.815984</td>
      <td>1.701004</td>
      <td>104.269838</td>
      <td>38.491160</td>
      <td>846.841774</td>
      <td>2.757689</td>
      <td>3.697627</td>
    </tr>
    <tr>
      <th>min</th>
      <td>9.000000</td>
      <td>3.000000</td>
      <td>68.000000</td>
      <td>46.000000</td>
      <td>1613.000000</td>
      <td>8.000000</td>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>17.500000</td>
      <td>4.000000</td>
      <td>104.250000</td>
      <td>75.000000</td>
      <td>2223.750000</td>
      <td>13.825000</td>
      <td>73.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>23.000000</td>
      <td>4.000000</td>
      <td>148.500000</td>
      <td>93.500000</td>
      <td>2803.500000</td>
      <td>15.500000</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>29.000000</td>
      <td>8.000000</td>
      <td>262.000000</td>
      <td>126.000000</td>
      <td>3608.000000</td>
      <td>17.175000</td>
      <td>79.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>46.600000</td>
      <td>8.000000</td>
      <td>455.000000</td>
      <td>230.000000</td>
      <td>5140.000000</td>
      <td>24.800000</td>
      <td>82.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.describe(include = 'all') # ver todos los datos incluidos los categoricos
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>392.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>398.000000</td>
      <td>398</td>
      <td>398</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>305</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>usa</td>
      <td>ford pinto</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>249</td>
      <td>6</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>23.514573</td>
      <td>5.454774</td>
      <td>193.425879</td>
      <td>104.469388</td>
      <td>2970.424623</td>
      <td>15.568090</td>
      <td>76.010050</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.815984</td>
      <td>1.701004</td>
      <td>104.269838</td>
      <td>38.491160</td>
      <td>846.841774</td>
      <td>2.757689</td>
      <td>3.697627</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>9.000000</td>
      <td>3.000000</td>
      <td>68.000000</td>
      <td>46.000000</td>
      <td>1613.000000</td>
      <td>8.000000</td>
      <td>70.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>17.500000</td>
      <td>4.000000</td>
      <td>104.250000</td>
      <td>75.000000</td>
      <td>2223.750000</td>
      <td>13.825000</td>
      <td>73.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>23.000000</td>
      <td>4.000000</td>
      <td>148.500000</td>
      <td>93.500000</td>
      <td>2803.500000</td>
      <td>15.500000</td>
      <td>76.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>29.000000</td>
      <td>8.000000</td>
      <td>262.000000</td>
      <td>126.000000</td>
      <td>3608.000000</td>
      <td>17.175000</td>
      <td>79.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>46.600000</td>
      <td>8.000000</td>
      <td>455.000000</td>
      <td>230.000000</td>
      <td>5140.000000</td>
      <td>24.800000</td>
      <td>82.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Descripcion de una sola columna
data['cylinders'].describe()
```




    count    398.000000
    mean       5.454774
    std        1.701004
    min        3.000000
    25%        4.000000
    50%        4.000000
    75%        8.000000
    max        8.000000
    Name: cylinders, dtype: float64




```python
data['mpg'].describe()
```




    count    398.000000
    mean      23.514573
    std        7.815984
    min        9.000000
    25%       17.500000
    50%       23.000000
    75%       29.000000
    max       46.600000
    Name: mpg, dtype: float64




```python
data['cylinders'].dtypes
```




    dtype('int64')



### Estadistica Descriptiva

Metodos de Estadistica Descriptiva, de medida central, simetria, momentos, etc. para mas informacion:
http://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats

Los calculos de las medidas estadisticas se hacen siempre en columnas, es algo predeterminado, si se quiere hacer por filas, se debe especificar dentro de los metodos el parametro axis=1.

Ejemplo:

- Calculo de la media por **columnas** (predeterminado) = `df.mean()`
- Calculo de la media por **filas** = `df.mean(axis=1)`

Esto funciona con los otros tipos de medidas estadisticas


```python
# Se tomara la columna 'mpg' para realizar los calculos
X = data['mpg']
type(X)
```




    pandas.core.series.Series



#### Medidas de centralizacion
estas funciones se aplican sobre un dataframe de pandas

##### Media


```python
# Media Aritmetica
X.mean()
```




    23.514572864321615




```python
# Media aritmetica en un dataframe
data.mean()
```




    mpg               23.514573
    cylinders          5.454774
    displacement     193.425879
    horsepower       104.469388
    weight          2970.424623
    acceleration      15.568090
    model_year        76.010050
    dtype: float64



##### Mediana


```python
# Mediana
X.median()
```




    23.0




```python
# Mediana en un dataframe
data.median()
```




    mpg               23.0
    cylinders          4.0
    displacement     148.5
    horsepower        93.5
    weight          2803.5
    acceleration      15.5
    model_year        76.0
    dtype: float64



##### Maximo y Minimo


```python
# Maximo
X.max()
```




    46.6




```python
# Maximo en un dataframe
data.max()
```




    mpg                         46.6
    cylinders                      8
    displacement                 455
    horsepower                   230
    weight                      5140
    acceleration                24.8
    model_year                    82
    origin                       usa
    name            vw rabbit custom
    dtype: object




```python
# Minimo
X.min()
```




    9.0




```python
# Minimo en un dataframe
data.min()
```




    mpg                                   9
    cylinders                             3
    displacement                         68
    horsepower                           46
    weight                             1613
    acceleration                          8
    model_year                           70
    origin                           europe
    name            amc ambassador brougham
    dtype: object



##### Moda


```python
# Moda
X.mode()
```




    0    13.0
    dtype: float64




```python
# Moda en un dataframe
data.mode()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>13.0</td>
      <td>4.0</td>
      <td>97.0</td>
      <td>150.0</td>
      <td>1985</td>
      <td>14.5</td>
      <td>73.0</td>
      <td>usa</td>
      <td>ford pinto</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2130</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



##### Cuartiles


```python
# Valores de los cuartiles
X.quantile([0, .25, .5, .75, 1])
```




    0.00     9.0
    0.25    17.5
    0.50    23.0
    0.75    29.0
    1.00    46.6
    Name: mpg, dtype: float64




```python
# Valores de los cuartiles en un dataframe
data.quantile([0, .25, .5, .75, 1])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.00</th>
      <td>9.0</td>
      <td>3.0</td>
      <td>68.00</td>
      <td>46.0</td>
      <td>1613.00</td>
      <td>8.000</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>0.25</th>
      <td>17.5</td>
      <td>4.0</td>
      <td>104.25</td>
      <td>75.0</td>
      <td>2223.75</td>
      <td>13.825</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>0.50</th>
      <td>23.0</td>
      <td>4.0</td>
      <td>148.50</td>
      <td>93.5</td>
      <td>2803.50</td>
      <td>15.500</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>0.75</th>
      <td>29.0</td>
      <td>8.0</td>
      <td>262.00</td>
      <td>126.0</td>
      <td>3608.00</td>
      <td>17.175</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>1.00</th>
      <td>46.6</td>
      <td>8.0</td>
      <td>455.00</td>
      <td>230.0</td>
      <td>5140.00</td>
      <td>24.800</td>
      <td>82.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Medidas de dispersion
##### Varianza


```python
# Varianza
X.var() #unbiased Normalized by N-1 by default.
```




    61.089610774274405




```python
# Varianza en un dataframe
data.var()
```




    mpg                 61.089611
    cylinders            2.893415
    displacement     10872.199152
    horsepower        1481.569393
    weight          717140.990526
    acceleration         7.604848
    model_year          13.672443
    dtype: float64



##### Desviacion Estandard


```python
# Desviacion tipica o desviacion estandard
X.std()
```




    7.815984312565782




```python
# Desviacion tipica o desviacion estandard en un dataframe
data.std()
```




    mpg               7.815984
    cylinders         1.701004
    displacement    104.269838
    horsepower       38.491160
    weight          846.841774
    acceleration      2.757689
    model_year        3.697627
    dtype: float64



##### Coeficiente de Variacion


```python
# Coeficiente de Variacion
X.std()/X.mean()
```




    0.3323889554645019



#### Medidas de Asimetria
##### Asimetria de Fisher (skewness)
La asimetría es la medida que indica la simetría de la distribución de una variable respecto a la media aritmética, sin necesidad de hacer la representación gráfica. Los coeficientes de asimetría indican si hay el mismo número de elementos a izquierda y derecha de la media.

Existen tres tipos de curva de distribución según su asimetría:

- **Asimetría negativa:** la cola de la distribución se alarga para valores inferiores a la media.
- **Simétrica:** hay el mismo número de elementos a izquierda y derecha de la media. En este caso, coinciden la media, la mediana y la moda. La distribución se adapta a la forma de la campana de Gauss, o distribución normal.
- **Asimetría positiva:** la cola de la distribución se alarga para valores superiores a la media.

![](http://www.universoformulas.com/imagenes/estadistica/descriptiva/tipos-asimetria.jpg)


```python
#unbiased skew, Normalized by N-1
X.skew() 
```




    0.45706634399491913




```python
#unbiased skew, Normalized by N-1 en un dataframe
data.skew()
```




    mpg             0.457066
    cylinders       0.526922
    displacement    0.719645
    horsepower      1.087326
    weight          0.531063
    acceleration    0.278777
    model_year      0.011535
    dtype: float64



##### Curtosis
Esta medida determina el grado de concentración que presentan los valores en la región central de la distribución. Por medio del Coeficiente de Curtosis, podemos identificar si existe una gran concentración de valores (Leptocúrtica), una concentración normal (Mesocúrtica) ó una baja concentración (Platicúrtica).
![](http://www.spssfree.com/curso-de-spss/curso/5-19.gif)


```python
# unbiased kurtosis over requested axis using Fisher's definition
X.kurtosis()
```




    -0.5107812652123154




```python
# unbiased kurtosis over requested axis using Fisher's definition
# en un dataframe
data.kurtosis()
```




    mpg            -0.510781
    cylinders      -1.376662
    displacement   -0.746597
    horsepower      0.696947
    weight         -0.785529
    acceleration    0.419497
    model_year     -1.181232
    dtype: float64



### Covarianza
#### Entre Series


```python
s1 = pd.Series(np.random.randn(1000))
s2 = pd.Series(np.random.randn(1000))
```


```python
s1.cov(s2)
```




    -0.028354705528775087




```python
# Numpy
np.cov(s1,s2)
```




    array([[ 1.09020966, -0.02835471],
           [-0.02835471,  1.07417272]])



#### Dataframe


```python
frame = pd.DataFrame(np.random.randn(1000, 5),columns=['a', 'b', 'c', 'd', 'e'])
frame.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.576828</td>
      <td>1.814651</td>
      <td>-0.261503</td>
      <td>-0.254697</td>
      <td>0.974428</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.030171</td>
      <td>0.605864</td>
      <td>0.079012</td>
      <td>-0.172524</td>
      <td>3.052445</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.842097</td>
      <td>-0.351725</td>
      <td>0.628591</td>
      <td>0.878268</td>
      <td>-0.055329</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.273158</td>
      <td>0.049033</td>
      <td>-0.301981</td>
      <td>0.562631</td>
      <td>-1.241831</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.305087</td>
      <td>0.474497</td>
      <td>0.648280</td>
      <td>-0.026315</td>
      <td>0.792715</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.cov()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.076575</td>
      <td>0.000666</td>
      <td>-0.039799</td>
      <td>-0.002462</td>
      <td>-0.043501</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.000666</td>
      <td>1.016370</td>
      <td>-0.015872</td>
      <td>-0.002416</td>
      <td>-0.021047</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.039799</td>
      <td>-0.015872</td>
      <td>1.036459</td>
      <td>-0.058312</td>
      <td>-0.057863</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-0.002462</td>
      <td>-0.002416</td>
      <td>-0.058312</td>
      <td>1.000640</td>
      <td>0.004340</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-0.043501</td>
      <td>-0.021047</td>
      <td>-0.057863</td>
      <td>0.004340</td>
      <td>0.952529</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Con Numpy
np.cov(frame)
```




    array([[ 0.7710721 ,  0.51639576, -0.42821644, ..., -0.23771807,
            -0.63698462,  0.44026319],
           [ 0.51639576,  1.78416315, -0.17363496, ..., -1.00370658,
            -1.14416467,  0.59572484],
           [-0.42821644, -0.17363496,  0.49727435, ...,  0.08767001,
             0.33921621, -0.06352345],
           ...,
           [-0.23771807, -1.00370658,  0.08767001, ...,  0.64880976,
             0.65597959, -0.23257827],
           [-0.63698462, -1.14416467,  0.33921621, ...,  0.65597959,
             0.90660696, -0.45814778],
           [ 0.44026319,  0.59572484, -0.06352345, ..., -0.23257827,
            -0.45814778,  0.46902464]])



### Correlacion

Metodos:
- pearson (predeterminado) 
- kendall 
- spearman



```python
#  Creacion de dataframe con datos aleatorios
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
frame.head()                     
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
      <td>-0.134841</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
      <td>0.807706</td>
      <td>0.072960</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.638787</td>
      <td>0.329646</td>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.484752</td>
      <td>-0.116773</td>
      <td>1.901755</td>
      <td>0.238127</td>
      <td>1.996652</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.993263</td>
      <td>0.196800</td>
      <td>-1.136645</td>
      <td>0.000366</td>
      <td>1.025984</td>
    </tr>
  </tbody>
</table>
</div>



#### Entre Series


```python
frame['a'].corr(frame['b']) # Pearson que es el predeterminado
```




    -0.052592953776030495




```python
frame['a'].corr(frame['b'], method='spearman') # Metodo spearman
```




    -0.04775690375690376




```python
frame['a'].corr(frame['b'], method='kendall') # Metodo Kendall
```




    -0.03213613613613614




```python
# Con Numpy se realiza el coefficiente de Pearson
# realiza la correlacion entre dos vectores
np.corrcoef(frame['a'],frame['b'])
```




    array([[ 1.        , -0.05259295],
           [-0.05259295,  1.        ]])



#### Dataframe


```python
frame.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.000000</td>
      <td>-0.052593</td>
      <td>-0.039170</td>
      <td>0.001333</td>
      <td>-0.001645</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-0.052593</td>
      <td>1.000000</td>
      <td>0.084488</td>
      <td>0.007218</td>
      <td>0.009969</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.039170</td>
      <td>0.084488</td>
      <td>1.000000</td>
      <td>0.080168</td>
      <td>0.006809</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.001333</td>
      <td>0.007218</td>
      <td>0.080168</td>
      <td>1.000000</td>
      <td>-0.039776</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-0.001645</td>
      <td>0.009969</td>
      <td>0.006809</td>
      <td>-0.039776</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# con Numpy
np.corrcoef(frame)
```




    array([[ 1.        , -0.58501996,  0.55616525, ...,  0.26806025,
            -0.35940809, -0.00452158],
           [-0.58501996,  1.        , -0.3400534 , ...,  0.11257458,
            -0.37590609, -0.58877942],
           [ 0.55616525, -0.3400534 ,  1.        , ...,  0.70442968,
             0.13326316, -0.19220235],
           ...,
           [ 0.26806025,  0.11257458,  0.70442968, ...,  1.        ,
             0.19271014, -0.79265039],
           [-0.35940809, -0.37590609,  0.13326316, ...,  0.19271014,
             1.        ,  0.14871875],
           [-0.00452158, -0.58877942, -0.19220235, ..., -0.79265039,
             0.14871875,  1.        ]])



### Funciones Agregadas
Para aplicar una o mas funciones en cada columna de los dataframe


```python
df.agg(['sum', 'min'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sum</th>
      <td>10</td>
      <td>2109</td>
      <td>mama     papa   HIJO  HiJa</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1</td>
      <td>444</td>
      <td>HIJO</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Aplicar los metodos en columnas especificas
df[['col1','col2']].agg(['sum', 'min'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sum</th>
      <td>10</td>
      <td>2109</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1</td>
      <td>444</td>
    </tr>
  </tbody>
</table>
</div>



### Aplicando Funciones a cada elemento


```python
#definicion de funcion
def times2(x):
    return x*2
```


```python
# es mas o menos lo que hace la funcion map
# aplicar la funcion times2 a cada elemento de la col1 de dataframe df
df['col1'].apply(times2)
```




    0    2
    1    4
    2    6
    3    8
    Name: col1, dtype: int64




```python
df['col3'].apply(len) #longitud de cada uno de los datos de la col3
```




    0    7
    1    6
    2    9
    3    4
    Name: col3, dtype: int64




```python
df['col1'].sum() #sumatoria total de los elementos de la col1
```




    10



### (Sorting) Ordenar un DataFrame:


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>mama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>papa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>HIJO</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>HiJa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ordenar el dataframe de menor a mayor basado en col2
df.sort_values(by='col2') #inplace=False por default
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>mama</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>HiJa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>papa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>HIJO</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='col2',ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>HIJO</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>papa</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>mama</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>HiJa</td>
    </tr>
  </tbody>
</table>
</div>



### Metodos de strings

Los metodos de los strings se pueden usar en pandas de forma vectorizada

https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#vectorized-string-methods


Los metodos vectorizados de los strings son:

https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-string-methods

**Nota: Recordar que la mayoria de los metodos NO son inplace**


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>mama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>papa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>HIJO</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>HiJa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Estos Metodos solo funcionan por columna (Series)
# se puede verificar el error
#df.str.lower()
```

Algunos ejemplos de metodos en strings en las columnas


```python
# convertir strings en minuscula
df['col3'].str.lower()
```




    0      mama   
    1         papa
    2       hijo  
    3         hija
    Name: col3, dtype: object




```python
# convertir strings en Mayuscula
df['col3'].str.upper()
```




    0      MAMA   
    1         PAPA
    2       HIJO  
    3         HIJA
    Name: col3, dtype: object




```python
# Eliminar los espacios de los strings
df['col3'].str.strip()
```




    0    mama
    1    papa
    2    HIJO
    3    HiJa
    Name: col3, dtype: object



## Transformacion de Variables
- Crear variables Dummy: convertir de categoría a númerica
- Discretización o Binning: convertir de número a categoría

### Columnas Dummy
Convertir variables categoricas a numericas


```python
# crear datos categoricos
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'sex': ['male', 'female', 'male', 'female', 'female']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'sex'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>female</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Crear un set de variables dummy para la columna sex
df_sex = pd.get_dummies(df['sex'])
df_sex
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>female</th>
      <th>male</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# unir los dos dataframes
df_new = df.join(df_sex)
df_new
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>sex</th>
      <th>female</th>
      <th>male</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>male</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>female</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>male</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>female</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>female</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Discretización o Binning

Conversion de Numerica a Categorica

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html


```python
# dividir los datos en 3 rangos iguales (categorias)

pd.cut(np.array([3.5, 2.8, 1, 5, 3, 4, 0, 4.4, 2, 3]), 3)
```




    [(3.333, 5.0], (1.667, 3.333], (-0.005, 1.667], (3.333, 5.0], (1.667, 3.333], (3.333, 5.0], (-0.005, 1.667], (3.333, 5.0], (1.667, 3.333], (1.667, 3.333]]
    Categories (3, interval[float64]): [(-0.005, 1.667] < (1.667, 3.333] < (3.333, 5.0]]




```python
# Asignar etiquetas ordenadas
pd.cut(np.array([3.5, 2.8, 1, 5, 3, 4,0, 4.4, 2, 3]),
       3, labels=["Malo", "Regular", "Bien"])
```




    [Bien, Regular, Malo, Bien, Regular, Bien, Malo, Bien, Regular, Regular]
    Categories (3, object): [Malo < Regular < Bien]




```python
pd.cut(np.array([2, 4 , 10 , 35 , 25 , 60 , 23, 14]),
       3, labels=["Niño", "Adolescente", "Adulto"])
```




    [Niño, Niño, Niño, Adolescente, Adolescente, Adulto, Adolescente, Niño]
    Categories (3, object): [Niño < Adolescente < Adulto]



---
## Leer y guardar Datos (Data Input and Output)

Pandas puede leer una variedad de tipos de archivos usando sus métodos `pd.read_` [mas informacion](https://pandas.pydata.org/pandas-docs/stable/io.html)
- CSV
- Excel
- Json
- Html
- SQL

### CSV File (comma-separated values)

#### CSV Input


```python
# Leer archivos separados por comas, extension .csv
df1 = pd.read_csv('./Data/supermarkets.csv')
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Name</th>
      <th>Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# dimensiones del dataframe
df1.shape
```




    (6, 7)




```python
# conocer los tipos de datos de cada columna
df1.dtypes
```




    ID            int64
    Address      object
    City         object
    State        object
    Country      object
    Name         object
    Employees     int64
    dtype: object




```python
# Tambien se puede cambiar el valor de la columna index
# definir la columna ID como el index
df1.set_index("ID",inplace=True) # se debe especificar que sea inplace
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Name</th>
      <th>Employees</th>
    </tr>
    <tr>
      <th>ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# hare un cambio y luego lo grabare
# multiplicar cada elemento de la columna employees por 2
df1['Employees']= df1['Employees'].apply(lambda x: x*2)
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Name</th>
      <th>Employees</th>
    </tr>
    <tr>
      <th>ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>24</td>
    </tr>
    <tr>
      <th>6</th>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



#### CSV Output


```python
# Grabar el dataframe como archivo separado por comas
df1.to_csv('./Data/example_out.csv',index=False)
```

#### Archivo de texto separado por comas


```python
# Leer archivos separados por comas, extension .txt o sin extension
df1 = pd.read_csv("./Data/supermarkets-commas.txt")
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Name</th>
      <th>Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



#### Archivo de texto separado por otro caracter


```python
# este archivo los valores estan separados por ;
df1 = pd.read_csv("./Data/supermarkets-semi-colons.txt",sep=';')
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Name</th>
      <th>Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



### Excel

Pandas puede leer y escribir archivos de Excel, tenga en cuenta que esto solo importa datos. No fórmulas o imágenes, que tengan imágenes o macros pueden hacer que este método read_excel se bloquee. 

#### Excel Input


```python
# leer un archivo de excel
df2 = pd.read_excel("./Data/supermarkets.xlsx",sheet_name=0) #leer la primera hoja del archivo
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Supermarket Name</th>
      <th>Number of Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# tambien podemos cambiar la columna del index
df2.set_index('ID')
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Supermarket Name</th>
      <th>Number of Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



#### Excel Output


```python
# sumar cada elemento del data frame por 4
df2['Number of Employees'] = df2['Number of Employees'].apply(lambda x: x+4)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>Country</th>
      <th>Supermarket Name</th>
      <th>Number of Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Madeira</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>CA 94119</td>
      <td>USA</td>
      <td>Bready Shop</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>California 94114</td>
      <td>USA</td>
      <td>Super River</td>
      <td>29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Ben's Shop</td>
      <td>14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>Sanchez</td>
      <td>16</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>CA 94114</td>
      <td>USA</td>
      <td>Richvalley</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.to_excel('./Data/Excel_Sample_out.xlsx',sheet_name='Hoja1')
```

### JSON
JSON (JavaScript Object Notation - Notación de Objetos de JavaScript) es un formato ligero de intercambio de datos. Leerlo y escribirlo es simple para humanos, mientras que para las máquinas es simple interpretarlo y generarlo.
#### Json Input


```python
# los archivos pueden estar en un link de internet
df4 = pd.read_json("http://pythonhow.com/supermarkets.json")
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Address</th>
      <th>City</th>
      <th>Country</th>
      <th>Employees</th>
      <th>ID</th>
      <th>Name</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>8</td>
      <td>1</td>
      <td>Madeira</td>
      <td>CA 94114</td>
    </tr>
    <tr>
      <th>1</th>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>15</td>
      <td>2</td>
      <td>Bready Shop</td>
      <td>CA 94119</td>
    </tr>
    <tr>
      <th>2</th>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>25</td>
      <td>3</td>
      <td>Super River</td>
      <td>California 94114</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>10</td>
      <td>4</td>
      <td>Ben's Shop</td>
      <td>CA 94114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>12</td>
      <td>5</td>
      <td>Sanchez</td>
      <td>California</td>
    </tr>
    <tr>
      <th>5</th>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>20</td>
      <td>6</td>
      <td>Richvalley</td>
      <td>CA 94114</td>
    </tr>
  </tbody>
</table>
</div>



#### Json output


```python
#Para grabar
df4.to_json("./Data/Salida.json")
```

### WEKA (arff)


```python
from scipy.io import arff # libreria para importar archivos de weka
# principalmente importa datos numericos
data = arff.loadarff('./Data/yeast-train.arff')
df5 = pd.DataFrame(data[0])
df5.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Att1</th>
      <th>Att2</th>
      <th>Att3</th>
      <th>Att4</th>
      <th>Att5</th>
      <th>Att6</th>
      <th>Att7</th>
      <th>Att8</th>
      <th>Att9</th>
      <th>Att10</th>
      <th>...</th>
      <th>Class5</th>
      <th>Class6</th>
      <th>Class7</th>
      <th>Class8</th>
      <th>Class9</th>
      <th>Class10</th>
      <th>Class11</th>
      <th>Class12</th>
      <th>Class13</th>
      <th>Class14</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.093700</td>
      <td>0.139771</td>
      <td>0.062774</td>
      <td>0.007698</td>
      <td>0.083873</td>
      <td>-0.119156</td>
      <td>0.073305</td>
      <td>0.005510</td>
      <td>0.027523</td>
      <td>0.043477</td>
      <td>...</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.022711</td>
      <td>-0.050504</td>
      <td>-0.035691</td>
      <td>-0.065434</td>
      <td>-0.084316</td>
      <td>-0.378560</td>
      <td>0.038212</td>
      <td>0.085770</td>
      <td>0.182613</td>
      <td>-0.055544</td>
      <td>...</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'1'</td>
      <td>b'1'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'1'</td>
      <td>b'1'</td>
      <td>b'0'</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.090407</td>
      <td>0.021198</td>
      <td>0.208712</td>
      <td>0.102752</td>
      <td>0.119315</td>
      <td>0.041729</td>
      <td>-0.021728</td>
      <td>0.019603</td>
      <td>-0.063853</td>
      <td>-0.053756</td>
      <td>...</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'1'</td>
      <td>b'1'</td>
      <td>b'0'</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.085235</td>
      <td>0.009540</td>
      <td>-0.013228</td>
      <td>0.094063</td>
      <td>-0.013592</td>
      <td>-0.030719</td>
      <td>-0.116062</td>
      <td>-0.131674</td>
      <td>-0.165448</td>
      <td>-0.123053</td>
      <td>...</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'1'</td>
      <td>b'1'</td>
      <td>b'1'</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.088765</td>
      <td>-0.026743</td>
      <td>0.002075</td>
      <td>-0.043819</td>
      <td>-0.005465</td>
      <td>0.004306</td>
      <td>-0.055865</td>
      <td>-0.071484</td>
      <td>-0.159025</td>
      <td>-0.111348</td>
      <td>...</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
      <td>b'0'</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 117 columns</p>
</div>



### HTML

Se debe instalar `htmllib5`,`lxml` y `BeautifulSoup4`. En la terminal escriba

    conda install lxml
    conda install html5lib
    conda install BeautifulSoup4

Luego reinicie el Jupyter Notebook.
(o use pip install si no esta usando la distribucion de Anaconda)

Pandas puede leer tablas de html

La función pandas read_html leerá las tablas de una página web y devolverá una lista de objetos DataFrame:


```python
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
```


```python
data[0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Bank Name</th>
      <th>City</th>
      <th>ST</th>
      <th>CERT</th>
      <th>Acquiring Institution</th>
      <th>Closing Date</th>
      <th>Updated Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Enloe State Bank</td>
      <td>Cooper</td>
      <td>TX</td>
      <td>10716</td>
      <td>Legend Bank, N. A.</td>
      <td>May 31, 2019</td>
      <td>June 5, 2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Washington Federal Bank for Savings</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>30570</td>
      <td>Royal Savings Bank</td>
      <td>December 15, 2017</td>
      <td>February 1, 2019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>The Farmers and Merchants State Bank of Argonia</td>
      <td>Argonia</td>
      <td>KS</td>
      <td>17719</td>
      <td>Conway Bank</td>
      <td>October 13, 2017</td>
      <td>February 21, 2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fayette County Bank</td>
      <td>Saint Elmo</td>
      <td>IL</td>
      <td>1802</td>
      <td>United Fidelity Bank, fsb</td>
      <td>May 26, 2017</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Guaranty Bank, (d/b/a BestBank in Georgia &amp; Mi...</td>
      <td>Milwaukee</td>
      <td>WI</td>
      <td>30003</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>May 5, 2017</td>
      <td>March 22, 2018</td>
    </tr>
    <tr>
      <th>5</th>
      <td>First NBC Bank</td>
      <td>New Orleans</td>
      <td>LA</td>
      <td>58302</td>
      <td>Whitney Bank</td>
      <td>April 28, 2017</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Proficio Bank</td>
      <td>Cottonwood Heights</td>
      <td>UT</td>
      <td>35495</td>
      <td>Cache Valley Bank</td>
      <td>March 3, 2017</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Seaway Bank and Trust Company</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>19328</td>
      <td>State Bank of Texas</td>
      <td>January 27, 2017</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Harvest Community Bank</td>
      <td>Pennsville</td>
      <td>NJ</td>
      <td>34951</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>January 13, 2017</td>
      <td>May 18, 2017</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Allied Bank</td>
      <td>Mulberry</td>
      <td>AR</td>
      <td>91</td>
      <td>Today's Bank</td>
      <td>September 23, 2016</td>
      <td>May 13, 2019</td>
    </tr>
    <tr>
      <th>10</th>
      <td>The Woodbury Banking Company</td>
      <td>Woodbury</td>
      <td>GA</td>
      <td>11297</td>
      <td>United Bank</td>
      <td>August 19, 2016</td>
      <td>December 13, 2018</td>
    </tr>
    <tr>
      <th>11</th>
      <td>First CornerStone Bank</td>
      <td>King of Prussia</td>
      <td>PA</td>
      <td>35312</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>May 6, 2016</td>
      <td>November 13, 2018</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Trust Company Bank</td>
      <td>Memphis</td>
      <td>TN</td>
      <td>9956</td>
      <td>The Bank of Fayette County</td>
      <td>April 29, 2016</td>
      <td>September 14, 2018</td>
    </tr>
    <tr>
      <th>13</th>
      <td>North Milwaukee State Bank</td>
      <td>Milwaukee</td>
      <td>WI</td>
      <td>20364</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>March 11, 2016</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Hometown National Bank</td>
      <td>Longview</td>
      <td>WA</td>
      <td>35156</td>
      <td>Twin City Bank</td>
      <td>October 2, 2015</td>
      <td>February 19, 2018</td>
    </tr>
    <tr>
      <th>15</th>
      <td>The Bank of Georgia</td>
      <td>Peachtree City</td>
      <td>GA</td>
      <td>35259</td>
      <td>Fidelity Bank</td>
      <td>October 2, 2015</td>
      <td>July 9, 2018</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Premier Bank</td>
      <td>Denver</td>
      <td>CO</td>
      <td>34112</td>
      <td>United Fidelity Bank, fsb</td>
      <td>July 10, 2015</td>
      <td>February 20, 2018</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Edgebrook Bank</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>57772</td>
      <td>Republic Bank of Chicago</td>
      <td>May 8, 2015</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Doral Bank  En Español</td>
      <td>San Juan</td>
      <td>PR</td>
      <td>32102</td>
      <td>Banco Popular de Puerto Rico</td>
      <td>February 27, 2015</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Capitol City Bank &amp; Trust Company</td>
      <td>Atlanta</td>
      <td>GA</td>
      <td>33938</td>
      <td>First-Citizens Bank &amp; Trust Company</td>
      <td>February 13, 2015</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Highland Community Bank</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>20290</td>
      <td>United Fidelity Bank, fsb</td>
      <td>January 23, 2015</td>
      <td>November 15, 2017</td>
    </tr>
    <tr>
      <th>21</th>
      <td>First National Bank of Crestview</td>
      <td>Crestview</td>
      <td>FL</td>
      <td>17557</td>
      <td>First NBC Bank</td>
      <td>January 16, 2015</td>
      <td>November 15, 2017</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Northern Star Bank</td>
      <td>Mankato</td>
      <td>MN</td>
      <td>34983</td>
      <td>BankVista</td>
      <td>December 19, 2014</td>
      <td>January 3, 2018</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Frontier Bank, FSB D/B/A El Paseo Bank</td>
      <td>Palm Desert</td>
      <td>CA</td>
      <td>34738</td>
      <td>Bank of Southern California, N.A.</td>
      <td>November 7, 2014</td>
      <td>November 10, 2016</td>
    </tr>
    <tr>
      <th>24</th>
      <td>The National Republic Bank of Chicago</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>916</td>
      <td>State Bank of Texas</td>
      <td>October 24, 2014</td>
      <td>January 6, 2016</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NBRS Financial</td>
      <td>Rising Sun</td>
      <td>MD</td>
      <td>4862</td>
      <td>Howard Bank</td>
      <td>October 17, 2014</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>26</th>
      <td>GreenChoice Bank, fsb</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>28462</td>
      <td>Providence Bank, LLC</td>
      <td>July 25, 2014</td>
      <td>December 12, 2016</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Eastside Commercial Bank</td>
      <td>Conyers</td>
      <td>GA</td>
      <td>58125</td>
      <td>Community &amp; Southern Bank</td>
      <td>July 18, 2014</td>
      <td>October 6, 2017</td>
    </tr>
    <tr>
      <th>28</th>
      <td>The Freedom State Bank</td>
      <td>Freedom</td>
      <td>OK</td>
      <td>12483</td>
      <td>Alva State Bank &amp; Trust Company</td>
      <td>June 27, 2014</td>
      <td>February 21, 2018</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Valley Bank</td>
      <td>Fort Lauderdale</td>
      <td>FL</td>
      <td>21793</td>
      <td>Landmark Bank, National Association</td>
      <td>June 20, 2014</td>
      <td>January 29, 2019</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>526</th>
      <td>ANB Financial, NA</td>
      <td>Bentonville</td>
      <td>AR</td>
      <td>33901</td>
      <td>Pulaski Bank and Trust Company</td>
      <td>May 9, 2008</td>
      <td>February 1, 2019</td>
    </tr>
    <tr>
      <th>527</th>
      <td>Hume Bank</td>
      <td>Hume</td>
      <td>MO</td>
      <td>1971</td>
      <td>Security Bank</td>
      <td>March 7, 2008</td>
      <td>January 31, 2019</td>
    </tr>
    <tr>
      <th>528</th>
      <td>Douglass National Bank</td>
      <td>Kansas City</td>
      <td>MO</td>
      <td>24660</td>
      <td>Liberty Bank and Trust Company</td>
      <td>January 25, 2008</td>
      <td>October 26, 2012</td>
    </tr>
    <tr>
      <th>529</th>
      <td>Miami Valley Bank</td>
      <td>Lakeview</td>
      <td>OH</td>
      <td>16848</td>
      <td>The Citizens Banking Company</td>
      <td>October 4, 2007</td>
      <td>September 12, 2016</td>
    </tr>
    <tr>
      <th>530</th>
      <td>NetBank</td>
      <td>Alpharetta</td>
      <td>GA</td>
      <td>32575</td>
      <td>ING DIRECT</td>
      <td>September 28, 2007</td>
      <td>January 31, 2019</td>
    </tr>
    <tr>
      <th>531</th>
      <td>Metropolitan Savings Bank</td>
      <td>Pittsburgh</td>
      <td>PA</td>
      <td>35353</td>
      <td>Allegheny Valley Bank of Pittsburgh</td>
      <td>February 2, 2007</td>
      <td>October 27, 2010</td>
    </tr>
    <tr>
      <th>532</th>
      <td>Bank of Ephraim</td>
      <td>Ephraim</td>
      <td>UT</td>
      <td>1249</td>
      <td>Far West Bank</td>
      <td>June 25, 2004</td>
      <td>April 9, 2008</td>
    </tr>
    <tr>
      <th>533</th>
      <td>Reliance Bank</td>
      <td>White Plains</td>
      <td>NY</td>
      <td>26778</td>
      <td>Union State Bank</td>
      <td>March 19, 2004</td>
      <td>April 9, 2008</td>
    </tr>
    <tr>
      <th>534</th>
      <td>Guaranty National Bank of Tallahassee</td>
      <td>Tallahassee</td>
      <td>FL</td>
      <td>26838</td>
      <td>Hancock Bank of Florida</td>
      <td>March 12, 2004</td>
      <td>April 17, 2018</td>
    </tr>
    <tr>
      <th>535</th>
      <td>Dollar Savings Bank</td>
      <td>Newark</td>
      <td>NJ</td>
      <td>31330</td>
      <td>No Acquirer</td>
      <td>February 14, 2004</td>
      <td>April 9, 2008</td>
    </tr>
    <tr>
      <th>536</th>
      <td>Pulaski Savings Bank</td>
      <td>Philadelphia</td>
      <td>PA</td>
      <td>27203</td>
      <td>Earthstar Bank</td>
      <td>November 14, 2003</td>
      <td>October 6, 2017</td>
    </tr>
    <tr>
      <th>537</th>
      <td>First National Bank of Blanchardville</td>
      <td>Blanchardville</td>
      <td>WI</td>
      <td>11639</td>
      <td>The Park Bank</td>
      <td>May 9, 2003</td>
      <td>June 5, 2012</td>
    </tr>
    <tr>
      <th>538</th>
      <td>Southern Pacific Bank</td>
      <td>Torrance</td>
      <td>CA</td>
      <td>27094</td>
      <td>Beal Bank</td>
      <td>February 7, 2003</td>
      <td>October 20, 2008</td>
    </tr>
    <tr>
      <th>539</th>
      <td>Farmers Bank of Cheneyville</td>
      <td>Cheneyville</td>
      <td>LA</td>
      <td>16445</td>
      <td>Sabine State Bank &amp; Trust</td>
      <td>December 17, 2002</td>
      <td>October 20, 2004</td>
    </tr>
    <tr>
      <th>540</th>
      <td>Bank of Alamo</td>
      <td>Alamo</td>
      <td>TN</td>
      <td>9961</td>
      <td>No Acquirer</td>
      <td>November 8, 2002</td>
      <td>March 18, 2005</td>
    </tr>
    <tr>
      <th>541</th>
      <td>AmTrade International Bank  En Español</td>
      <td>Atlanta</td>
      <td>GA</td>
      <td>33784</td>
      <td>No Acquirer</td>
      <td>September 30, 2002</td>
      <td>September 11, 2006</td>
    </tr>
    <tr>
      <th>542</th>
      <td>Universal Federal Savings Bank</td>
      <td>Chicago</td>
      <td>IL</td>
      <td>29355</td>
      <td>Chicago Community Bank</td>
      <td>June 27, 2002</td>
      <td>October 6, 2017</td>
    </tr>
    <tr>
      <th>543</th>
      <td>Connecticut Bank of Commerce</td>
      <td>Stamford</td>
      <td>CT</td>
      <td>19183</td>
      <td>Hudson United Bank</td>
      <td>June 26, 2002</td>
      <td>February 14, 2012</td>
    </tr>
    <tr>
      <th>544</th>
      <td>New Century Bank</td>
      <td>Shelby Township</td>
      <td>MI</td>
      <td>34979</td>
      <td>No Acquirer</td>
      <td>March 28, 2002</td>
      <td>March 18, 2005</td>
    </tr>
    <tr>
      <th>545</th>
      <td>Net 1st National Bank</td>
      <td>Boca Raton</td>
      <td>FL</td>
      <td>26652</td>
      <td>Bank Leumi USA</td>
      <td>March 1, 2002</td>
      <td>April 9, 2008</td>
    </tr>
    <tr>
      <th>546</th>
      <td>NextBank, NA</td>
      <td>Phoenix</td>
      <td>AZ</td>
      <td>22314</td>
      <td>No Acquirer</td>
      <td>February 7, 2002</td>
      <td>February 5, 2015</td>
    </tr>
    <tr>
      <th>547</th>
      <td>Oakwood Deposit Bank Co.</td>
      <td>Oakwood</td>
      <td>OH</td>
      <td>8966</td>
      <td>The State Bank &amp; Trust Company</td>
      <td>February 1, 2002</td>
      <td>October 25, 2012</td>
    </tr>
    <tr>
      <th>548</th>
      <td>Bank of Sierra Blanca</td>
      <td>Sierra Blanca</td>
      <td>TX</td>
      <td>22002</td>
      <td>The Security State Bank of Pecos</td>
      <td>January 18, 2002</td>
      <td>November 6, 2003</td>
    </tr>
    <tr>
      <th>549</th>
      <td>Hamilton Bank, NA  En Español</td>
      <td>Miami</td>
      <td>FL</td>
      <td>24382</td>
      <td>Israel Discount Bank of New York</td>
      <td>January 11, 2002</td>
      <td>September 21, 2015</td>
    </tr>
    <tr>
      <th>550</th>
      <td>Sinclair National Bank</td>
      <td>Gravette</td>
      <td>AR</td>
      <td>34248</td>
      <td>Delta Trust &amp; Bank</td>
      <td>September 7, 2001</td>
      <td>October 6, 2017</td>
    </tr>
    <tr>
      <th>551</th>
      <td>Superior Bank, FSB</td>
      <td>Hinsdale</td>
      <td>IL</td>
      <td>32646</td>
      <td>Superior Federal, FSB</td>
      <td>July 27, 2001</td>
      <td>August 19, 2014</td>
    </tr>
    <tr>
      <th>552</th>
      <td>Malta National Bank</td>
      <td>Malta</td>
      <td>OH</td>
      <td>6629</td>
      <td>North Valley Bank</td>
      <td>May 3, 2001</td>
      <td>November 18, 2002</td>
    </tr>
    <tr>
      <th>553</th>
      <td>First Alliance Bank &amp; Trust Co.</td>
      <td>Manchester</td>
      <td>NH</td>
      <td>34264</td>
      <td>Southern New Hampshire Bank &amp; Trust</td>
      <td>February 2, 2001</td>
      <td>February 18, 2003</td>
    </tr>
    <tr>
      <th>554</th>
      <td>National State Bank of Metropolis</td>
      <td>Metropolis</td>
      <td>IL</td>
      <td>3815</td>
      <td>Banterra Bank of Marion</td>
      <td>December 14, 2000</td>
      <td>March 17, 2005</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Bank of Honolulu</td>
      <td>Honolulu</td>
      <td>HI</td>
      <td>21029</td>
      <td>Bank of the Orient</td>
      <td>October 13, 2000</td>
      <td>March 17, 2005</td>
    </tr>
  </tbody>
</table>
<p>556 rows × 7 columns</p>
</div>



_____
### SQL

El módulo pandas.io.sql proporciona una colección de contenedores de consultas para facilitar la recuperación de datos y reducir la dependencia de la API específica de DB. La abstracción de la base de datos es proporcionada por SQLAlchemy si está instalado. Además, necesitará una biblioteca de controladores para su base de datos. Ejemplos de tales controladores son `psycopg2` para PostgreSQL o `pymysql` para MySQL. Para SQLite esto está incluido en la biblioteca estándar de Python por defecto. Puede encontrar una descripción general de los controladores admitidos para cada lenguaje SQL en los documentos de SQLAlchemy.

Vea también algunos ejemplos de libros para algunas estrategias avanzadas.

las funciones claves son:

* read_sql_table(table_name, con[, schema, ...])	
    * Read SQL database table into a DataFrame.
* read_sql_query(sql, con[, index_col, ...])	
    * Read SQL query into a DataFrame.
* read_sql(sql, con[, index_col, ...])	
    * Read SQL query or database table into a DataFrame.
* DataFrame.to_sql(name, con[, flavor, ...])	
    * Write records stored in a DataFrame to a SQL database.


```python
# librerias para crear un proceso de sql sencillo
from sqlalchemy import create_engine
```


```python
# crear un proceso en memoria
engine = create_engine('sqlite:///:memory:')
```


```python
df4.to_sql('data', engine) # grabar el dataframe en formato sql
```


```python
sql_df = pd.read_sql('data',con=engine) # definir la conexion
```


```python
sql_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Address</th>
      <th>City</th>
      <th>Country</th>
      <th>Employees</th>
      <th>ID</th>
      <th>Name</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3666 21st St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>8</td>
      <td>1</td>
      <td>Madeira</td>
      <td>CA 94114</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>735 Dolores St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>15</td>
      <td>2</td>
      <td>Bready Shop</td>
      <td>CA 94119</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>332 Hill St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>25</td>
      <td>3</td>
      <td>Super River</td>
      <td>California 94114</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3995 23rd St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>10</td>
      <td>4</td>
      <td>Ben's Shop</td>
      <td>CA 94114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1056 Sanchez St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>12</td>
      <td>5</td>
      <td>Sanchez</td>
      <td>California</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>551 Alvarado St</td>
      <td>San Francisco</td>
      <td>USA</td>
      <td>20</td>
      <td>6</td>
      <td>Richvalley</td>
      <td>CA 94114</td>
    </tr>
  </tbody>
</table>
</div>



## Referencias
- [Web Pandas](https://pandas.pydata.org/)
- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
- [Tutoriales oficiales de Pandas](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
- [Pandas Basic cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)
- [Pandas cheat sheet](http://datacamp-community.s3.amazonaws.com/9f0f2ae1-8bd8-4302-a67b-e17f3059d9e8)
- [Pandas Importing data cheat sheet](http://datacamp-community.s3.amazonaws.com/50d31142-3de0-4159-89b9-18b718a728ef)
- [Pandas vs R, SQL SAS y otras herramientas, Comparacion de comandos](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/index.html)

**Phd. Jose R. Zapata**
- [https://joserzapata.github.io/](https://joserzapata.github.io/)
- https://twitter.com/joserzapata
