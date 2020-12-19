---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Pyspark con Google Colab"
subtitle: "Usando pyspark en google colab"
summary: "Configuracion de Google Colab para usar pyspark"
authors: ["joserzapata"]
tags: ["Python","Pyspark","Colab", "Data-Science" ,"Jupyter-notebook"]
categories: ["Data-Science"]
date: 2020-03-09T23:00:43-05:00
lastmod: 2020-03-09T23:00:43-05:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

# PySpark en Google Colab Automatico

1. Instalacion Marzo/2020
2. Intalacion Automatica
   1. Instalacion Java
   2. Instalacion de Spark
   3. Ejemplo de Uso de pyspark

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="joserzapata" data-color="#328cc1" data-emoji="" data-font="Cookie" data-text="Invítame a un Café" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script><br>

Abrir en Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Pyspark_Colab_es.ipynb)
   
# Instalacion Rapida Marzo/ 2020
De forma General para usar pyspark en Colab Marzo/2020 seria con los siguientes comandos en una celda en Colab:

Instalar Java
```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
```
```python
import os # libreria de manejo del sistema operativo
os.system("wget -q https://www-us.apache.org/dist/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz")
os.system("tar xf /spark-2.4.5-bin-hadoop2.7.tgz")
```
instalar pyspark
```
!pip install -q pyspark
```

```python
# Variables de Entorno
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{ver_spark}-bin-hadoop2.7"
```
```python
# Cargar Pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Test_spark").master("local[*]").getOrCreate()
spark
```
Pero cuando salga una nueva version de spark sera necesario actualizar los
links de descarga, ya que siempre borran las versiones 2.x.x cuando sale una nueva.

Lo mejor es configurar automaticamente para que descargue la version que sea
mayor que 2.3.4 que es la anterior y menor que spark 3.0.0 que aun se encuentra en desarrollo

Para esto el siguiente codigo detecta la version actual de spark, la descarga, la descomprime y luego realiza la instalacion de spark en google colab.

# Instalacion Automatica
## Instalacion de Java
Google Colaboratory funciona en un ambiente linux, por lo tanto se pueden usar comandos shell de linux antecedidos del caracter '!'

```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
```
## Instalacion de Spark

Obtener automaticamente la ultima version de spark de 

```python
from bs4 import BeautifulSoup
import requests
```


```python
#Obtener las versiones de spark la pagina web
url = 'https://downloads.apache.org/spark/' 
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
```

```python
# leer la pagina web y obtener las versiones de spark disponibles
link_files = []
for link in soup.find_all('a'):
  link_files.append(link.get('href'))
spark_link = [x for x in link_files if 'spark' in x]  
print(spark_link)
```

  ['spark-2.3.4/', 'spark-2.4.5/', 'spark-3.0.0-preview2/']


La version a usar seran las superiores a spark-2.3.4  y menores a spark-3.0.0

obtener la version y eliminar el caracter '/' del final


```python
ver_spark = spark_link[1][:-1] # obtener la version y eliminar el caracter '/' del final
print(ver_spark)
```

    spark-2.4.5

```python
import os # libreria de manejo del sistema operativo
#instalar automaticamente la version deseadda de spark
link = "https://www-us.apache.org/dist/spark/"
os.system(f"wget -q {link}{ver_spark}/{ver_spark}-bin-hadoop2.7.tgz")
os.system(f"tar xf {ver_spark}-bin-hadoop2.7.tgz")

# instalar pyspark
!pip install -q pyspark
```

    |████████████████████████████████| 217.8MB 63kB/s 
    |████████████████████████████████| 204kB 53.8MB/s 
    Building wheel for pyspark (setup.py) ... done


## Definir variables de entorno

```
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{ver_spark}-bin-hadoop2.7"
```

## Cargar pyspark en el sistema

```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Test_spark").master("local[*]").getOrCreate()
spark
```

<div>
<p><b>SparkSession - in-memory</b></p>

<div>
  <p><b>SparkContext</b></p>

  <p><a href="http://cf857c0401dc:4040">Spark UI</a></p>

  <dl>
      <dt>Version</dt>
        <dd><code>v2.4.5</code></dd>
      <dt>Master</dt>
        <dd><code>local[*]</code></dd>
      <dt>AppName</dt>
        <dd><code>pyspark-shell</code></dd>
  </dl>
</div>

</div>




# Ejemplo de Uso de pyspark

Leer archivo de prueba


```
archivo = './sample_data/california_housing_train.csv'
df_spark = spark.read.csv(archivo, inferSchema=True, header=True)

# imprimir tipo de archivo
print(type(df_spark))
```

    <class 'pyspark.sql.dataframe.DataFrame'>


¿Numero de registros en el dataframe?


```
df_spark.count()
```




    17000



Estructura del dataframe


```
df_spark.printSchema()
```

    root
     |-- longitude: double (nullable = true)
     |-- latitude: double (nullable = true)
     |-- housing_median_age: double (nullable = true)
     |-- total_rooms: double (nullable = true)
     |-- total_bedrooms: double (nullable = true)
     |-- population: double (nullable = true)
     |-- households: double (nullable = true)
     |-- median_income: double (nullable = true)
     |-- median_house_value: double (nullable = true)
    


¿Nombre de las Columnas de dataframe?


```
df_spark.columns
```

    ['longitude',
     'latitude',
     'housing_median_age',
     'total_rooms',
     'total_bedrooms',
     'population',
     'households',
     'median_income',
     'median_house_value']



Ver los primeros 20 registros del dataframe


```
df_spark.show()
```

    +---------+--------+------------------+-----------+--------------+----------+----------+-------------+------------------+
    |longitude|latitude|housing_median_age|total_rooms|total_bedrooms|population|households|median_income|median_house_value|
    +---------+--------+------------------+-----------+--------------+----------+----------+-------------+------------------+
    |  -114.31|   34.19|              15.0|     5612.0|        1283.0|    1015.0|     472.0|       1.4936|           66900.0|
    |  -114.47|    34.4|              19.0|     7650.0|        1901.0|    1129.0|     463.0|         1.82|           80100.0|
    |  -114.56|   33.69|              17.0|      720.0|         174.0|     333.0|     117.0|       1.6509|           85700.0|
    |  -114.57|   33.64|              14.0|     1501.0|         337.0|     515.0|     226.0|       3.1917|           73400.0|
    |  -114.57|   33.57|              20.0|     1454.0|         326.0|     624.0|     262.0|        1.925|           65500.0|
    |  -114.58|   33.63|              29.0|     1387.0|         236.0|     671.0|     239.0|       3.3438|           74000.0|
    |  -114.58|   33.61|              25.0|     2907.0|         680.0|    1841.0|     633.0|       2.6768|           82400.0|
    |  -114.59|   34.83|              41.0|      812.0|         168.0|     375.0|     158.0|       1.7083|           48500.0|
    |  -114.59|   33.61|              34.0|     4789.0|        1175.0|    3134.0|    1056.0|       2.1782|           58400.0|
    |   -114.6|   34.83|              46.0|     1497.0|         309.0|     787.0|     271.0|       2.1908|           48100.0|
    |   -114.6|   33.62|              16.0|     3741.0|         801.0|    2434.0|     824.0|       2.6797|           86500.0|
    |   -114.6|    33.6|              21.0|     1988.0|         483.0|    1182.0|     437.0|        1.625|           62000.0|
    |  -114.61|   34.84|              48.0|     1291.0|         248.0|     580.0|     211.0|       2.1571|           48600.0|
    |  -114.61|   34.83|              31.0|     2478.0|         464.0|    1346.0|     479.0|        3.212|           70400.0|
    |  -114.63|   32.76|              15.0|     1448.0|         378.0|     949.0|     300.0|       0.8585|           45000.0|
    |  -114.65|   34.89|              17.0|     2556.0|         587.0|    1005.0|     401.0|       1.6991|           69100.0|
    |  -114.65|    33.6|              28.0|     1678.0|         322.0|     666.0|     256.0|       2.9653|           94900.0|
    |  -114.65|   32.79|              21.0|       44.0|          33.0|      64.0|      27.0|       0.8571|           25000.0|
    |  -114.66|   32.74|              17.0|     1388.0|         386.0|     775.0|     320.0|       1.2049|           44000.0|
    |  -114.67|   33.92|              17.0|       97.0|          24.0|      29.0|      15.0|       1.2656|           27500.0|
    +---------+--------+------------------+-----------+--------------+----------+----------+-------------+------------------+
    only showing top 20 rows
    


## Descricipcion Estadistica del dataframe

```python
df_spark.describe().toPandas().transpose()
```
||0|1|2|3|4|
|--- |--- |--- |--- |--- |--- |
|summary|count|mean|stddev|min|max|
|longitude|17000|-119.56210823529375|2.0051664084260357|-124.35|-114.31|
|latitude|17000|35.6252247058827|2.1373397946570867|32.54|41.95|
|housing_median_age|17000|28.58935294117647|12.586936981660406|1.0|52.0|
|total_rooms|17000|2643.664411764706|2179.947071452777|2.0|37937.0|
|total_bedrooms|17000|539.4108235294118|421.4994515798648|1.0|6445.0|
|population|17000|1429.5739411764705|1147.852959159527|3.0|35682.0|
|households|17000|501.2219411764706|384.5208408559016|1.0|6082.0|
|median_income|17000|3.883578100000021|1.9081565183791036|0.4999|15.0001|
|median_house_value|17000|207300.91235294117|115983.76438720895|14999.0|500001.0|

Descripcion estadistica de una sola columna ('median_house_value')

```python
df_spark.describe(['median_house_value']).show()
```

    +-------+------------------+
    |summary|median_house_value|
    +-------+------------------+
    |  count|             17000|
    |   mean|207300.91235294117|
    | stddev|115983.76438720895|
    |    min|           14999.0|
    |    max|          500001.0|
    +-------+------------------+
    
De esta forma se puede instalar automaticamente spark en google colab y hacer uno de el de forma gratis.

En la version gratis solo se cuenta con una CPU si se quiere aumentar la capacidad de procesamiento es necesario pagar.
