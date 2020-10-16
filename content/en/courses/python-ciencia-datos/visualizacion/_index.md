---
# Title, summary, and page position.
linktitle: 4 - Visualizacion
summary: matplotlib, plotly, seaborn
weight: 4
icon: book
icon_pack: fas

# Page metadata.
title: Visualización de Datos con PYTHON
date: "2020-09-09T00:00:00Z"
type: book  # Do not modify
---

Curso Programacion Analitica

Maestria TIC Linea Ciencia de Datos

Por [Jose R. Zapata](https://joserzapata.github.io/)

    
Python cuenta con varias librerias para visualizacion las principale son:
* [matplotlib](https://matplotlib.org/) para graficas sencillas: bars, pies, lines, scatter plots, etc.

* [Seaborn](https://seaborn.pydata.org/) para visualizacion estadistica: Para crear mapas de calor o de alguna manera resumiendo los datos y aún desea mostrar la distribución de los datos.

* [Plotly](https://plot.ly/) y [Bokeh](https://bokeh.pydata.org/en/latest/) para visualizacion interactiva: Si los datos son tan complejos (o no puede ver la informacion de sus datos), utilice plotly y Bokeh para crear 
visualizaciones interactivas que permitan a los usuarios explorar los datos mismos.


## Importancia de la visualizacion
El siguiente codigo demostrara [El cuarteto de Anscombe](https://es.wikipedia.org/wiki/Cuarteto_de_Anscombe) demostracion realizada por el estadístico F. J. Anscombe. 

Estos datos que estan conformados por 4 dataset demuestra la importancia de la visualizacion de los datos para su analisis.


```python
import pandas as pd # libreria manipulacion de datos
import seaborn as sns # Libreria graficas
import numpy as np

%matplotlib inline
```


```python
anscombe = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/anscombe.csv')
anscombe
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
      <th>dataset</th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>I</td>
      <td>10.0</td>
      <td>8.04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I</td>
      <td>8.0</td>
      <td>6.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I</td>
      <td>13.0</td>
      <td>7.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>I</td>
      <td>9.0</td>
      <td>8.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>I</td>
      <td>11.0</td>
      <td>8.33</td>
    </tr>
    <tr>
      <th>5</th>
      <td>I</td>
      <td>14.0</td>
      <td>9.96</td>
    </tr>
    <tr>
      <th>6</th>
      <td>I</td>
      <td>6.0</td>
      <td>7.24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>I</td>
      <td>4.0</td>
      <td>4.26</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>12.0</td>
      <td>10.84</td>
    </tr>
    <tr>
      <th>9</th>
      <td>I</td>
      <td>7.0</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>10</th>
      <td>I</td>
      <td>5.0</td>
      <td>5.68</td>
    </tr>
    <tr>
      <th>11</th>
      <td>II</td>
      <td>10.0</td>
      <td>9.14</td>
    </tr>
    <tr>
      <th>12</th>
      <td>II</td>
      <td>8.0</td>
      <td>8.14</td>
    </tr>
    <tr>
      <th>13</th>
      <td>II</td>
      <td>13.0</td>
      <td>8.74</td>
    </tr>
    <tr>
      <th>14</th>
      <td>II</td>
      <td>9.0</td>
      <td>8.77</td>
    </tr>
    <tr>
      <th>15</th>
      <td>II</td>
      <td>11.0</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>16</th>
      <td>II</td>
      <td>14.0</td>
      <td>8.10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>II</td>
      <td>6.0</td>
      <td>6.13</td>
    </tr>
    <tr>
      <th>18</th>
      <td>II</td>
      <td>4.0</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>19</th>
      <td>II</td>
      <td>12.0</td>
      <td>9.13</td>
    </tr>
    <tr>
      <th>20</th>
      <td>II</td>
      <td>7.0</td>
      <td>7.26</td>
    </tr>
    <tr>
      <th>21</th>
      <td>II</td>
      <td>5.0</td>
      <td>4.74</td>
    </tr>
    <tr>
      <th>22</th>
      <td>III</td>
      <td>10.0</td>
      <td>7.46</td>
    </tr>
    <tr>
      <th>23</th>
      <td>III</td>
      <td>8.0</td>
      <td>6.77</td>
    </tr>
    <tr>
      <th>24</th>
      <td>III</td>
      <td>13.0</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>25</th>
      <td>III</td>
      <td>9.0</td>
      <td>7.11</td>
    </tr>
    <tr>
      <th>26</th>
      <td>III</td>
      <td>11.0</td>
      <td>7.81</td>
    </tr>
    <tr>
      <th>27</th>
      <td>III</td>
      <td>14.0</td>
      <td>8.84</td>
    </tr>
    <tr>
      <th>28</th>
      <td>III</td>
      <td>6.0</td>
      <td>6.08</td>
    </tr>
    <tr>
      <th>29</th>
      <td>III</td>
      <td>4.0</td>
      <td>5.39</td>
    </tr>
    <tr>
      <th>30</th>
      <td>III</td>
      <td>12.0</td>
      <td>8.15</td>
    </tr>
    <tr>
      <th>31</th>
      <td>III</td>
      <td>7.0</td>
      <td>6.42</td>
    </tr>
    <tr>
      <th>32</th>
      <td>III</td>
      <td>5.0</td>
      <td>5.73</td>
    </tr>
    <tr>
      <th>33</th>
      <td>IV</td>
      <td>8.0</td>
      <td>6.58</td>
    </tr>
    <tr>
      <th>34</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.76</td>
    </tr>
    <tr>
      <th>35</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.71</td>
    </tr>
    <tr>
      <th>36</th>
      <td>IV</td>
      <td>8.0</td>
      <td>8.84</td>
    </tr>
    <tr>
      <th>37</th>
      <td>IV</td>
      <td>8.0</td>
      <td>8.47</td>
    </tr>
    <tr>
      <th>38</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.04</td>
    </tr>
    <tr>
      <th>39</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>40</th>
      <td>IV</td>
      <td>19.0</td>
      <td>12.50</td>
    </tr>
    <tr>
      <th>41</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.56</td>
    </tr>
    <tr>
      <th>42</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.91</td>
    </tr>
    <tr>
      <th>43</th>
      <td>IV</td>
      <td>8.0</td>
      <td>6.89</td>
    </tr>
  </tbody>
</table>
</div>



Calcular los valores de la **media** y la **varianza** de cada dataset


```python
agg = anscombe.groupby('dataset').agg([np.mean, np.var])
agg
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
      <th colspan="2" halign="left">x</th>
      <th colspan="2" halign="left">y</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>var</th>
      <th>mean</th>
      <th>var</th>
    </tr>
    <tr>
      <th>dataset</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>I</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>4.127269</td>
    </tr>
    <tr>
      <th>II</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>4.127629</td>
    </tr>
    <tr>
      <th>III</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>7.500000</td>
      <td>4.122620</td>
    </tr>
    <tr>
      <th>IV</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>4.123249</td>
    </tr>
  </tbody>
</table>
</div>



Calcular la correlacion


```python
corr = [g.corr()['x'][1] for _, g in anscombe.groupby('dataset')]
corr
```




    [0.81642051634484, 0.8162365060002428, 0.8162867394895981, 0.8165214368885028]



Graficar los datasets, haciendo un scatterplot y una regression lineal


```python
# Grafica Usando seaborn
sns.set(style="ticks")
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe,
               col_wrap=2, ci=None, palette="muted", height=4,
               scatter_kws={"s": 50, "alpha": 1});
```


![png](./4-Visualizacion_10_0.png)


Calculo de los valores de la regresion lineal


```python
fits = [np.polyfit(g['x'], g['y'], 1) for _, g in anscombe.groupby('dataset')]
```


```python
# Almacenar los valores calculados de las regresiones lineales en un dataframe
val_reg = pd.DataFrame(fits,columns=['pendiente','intercepto'],index='I II II IV'.split())
val_reg.index.names = ['dataset']
val_reg
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
      <th>pendiente</th>
      <th>intercepto</th>
    </tr>
    <tr>
      <th>dataset</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>I</th>
      <td>0.500091</td>
      <td>3.000091</td>
    </tr>
    <tr>
      <th>II</th>
      <td>0.500000</td>
      <td>3.000909</td>
    </tr>
    <tr>
      <th>II</th>
      <td>0.499727</td>
      <td>3.002455</td>
    </tr>
    <tr>
      <th>IV</th>
      <td>0.499909</td>
      <td>3.001727</td>
    </tr>
  </tbody>
</table>
</div>



## MATPLOTLIB

Matplotlib es el "abuelo" de las librerias de visualización de datos con Python. Fue creado por [John Hunter](https://numfocus.org/programs/john-hunter-technology-fellowship). Lo creó para tratar de replicar las capacidades de graficar de MatLab en Python.

Es una excelente biblioteca de gráficos 2D y 3D para generar figuras científicas.

Algunos de los principales Pros de Matplotlib son:

* Generalmente es fácil comenzar por graficas simples
* Soporte para etiquetas personalizadas y textos
* Gran control de cada elemento en una figura
* Salida de alta calidad en muchos formatos
* Muy personalizable en general

Matplotlib le permite crear figuras reproducibles mediante programación. la página web oficial de Matplotlib:
http://matplotlib.org/

### Instalacion

Se debe instalar Matplotlib, pero si instalo Anaconda ya viene instalado,
en caso de que no lo tenga se puede instalar asi: 

`pip install matplotlib` o `conda install matplotlib`

en Jupyter notebook `!pip install matplotlib`

usar preferiblemente Conda.
    
### Importar la libreria

Importar el modulo `matplotlib.pyplot` con el nombre de `plt` (esto es un estandar en la comunidad):


```python
import matplotlib.pyplot as plt
```

Para ver las graficas directamente en este notebook se debe hacer con este comando:


```python
%matplotlib inline
```

Esa línea es solo para Jupyter notebooks, si está usando otro editor, usará: `plt.show()` al final de todos sus comandos de graficos para que aparezca la figura en otra ventana.


```python
# La mayoria de los datos son inventados para evitar los warnings por divisiones por cero
# o valores igual a infinito, entonces apagare los warnings
import warnings; warnings.simplefilter('ignore')
```

### Comandos Basicos de Matplotlib

Veamos un ejemplo muy simple usando dos arreglos numpy. También se pueden usar listas, pero lo más probable es usar arreglos Numpy o columnas de pandas (que esencialmente también se comportan como arreglos).
**Los datos que queremos graficar:**


```python
import numpy as np
x = np.linspace(0,5, 11)
y = x ** 2
```


```python
x
```




    array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ])




```python
y
```




    array([ 0.  ,  0.25,  1.  ,  2.25,  4.  ,  6.25,  9.  , 12.25, 16.  ,
           20.25, 25.  ])



Podemos crear un diagrama de líneas muy simple usando lo siguiente:


```python
# Metodo basico para graficar X vs Y
plt.plot(x, y) # se grafica una linea de color azul

plt.show() # Mostrar la grafica luego de que ya se definio todos los elementos
# plt.show() no es necesario en jupyter notebook
```


![png](./4-Visualizacion_27_0.png)


### Titulo


```python
plt.plot(x, y) # se grafica una linea de color azul
plt.title('Titulo de la grafica'); # definir el titulo de la grafica
```


![png](./4-Visualizacion_29_0.png)


### Nombres de los ejes


```python
plt.plot(x, y) # se grafica una linea de color azul
plt.xlabel('Nombre del eje X') # definir el nombre del eje X
plt.ylabel('Nombre del eje Y') # definir el nombre del eje Y
plt.title('Titulo de la grafica'); # definir el titulo de la grafica
```


![png](./4-Visualizacion_31_0.png)


### Legend

Puede usar el argumento de palabra clave **label = "texto de etiqueta"** cuando se agreguen gráficas u otros objetos a la figura, y luego usar el método **legend** sin argumentos para agregar la leyenda a la figura:


```python
plt.plot(x, y, label="x vs y") # se grafica una linea de color azul
# se pone en el atributo 'label' el textto deseado

plt.xlabel('Nombre del eje X') # definir el nombre del eje X
plt.ylabel('Nombre del eje Y') # definir el nombre del eje Y
plt.title('Titulo de la grafica') # definir el titulo de la grafica
plt.legend(); # agregar el legend al plot
```


![png](./4-Visualizacion_33_0.png)


¡Observe cómo la leyenda se superpone con parte de la grafica!

EL Metodo **legend** toma un argumento opcional de palabra clave **loc** que puede usarse para especificar en qué parte de la figura debe dibujarse la leyenda. Los valores permitidos de **loc** son códigos numéricos para los diversos lugares donde se puede dibujar la leyenda. Consulte la [página de documentación](http://matplotlib.org/users/legend_guide.html#legend-location) para obtener detalles.

### Cuadricula (Grid )


```python
plt.plot(x, y, label="x vs y") # se grafica una linea de color azul
# se pone en el atributo 'label' el textto deseado

plt.xlabel('Nombre del eje X') # definir el nombre del eje X
plt.ylabel('Nombre del eje Y') # definir el nombre del eje Y
plt.title('Titulo de la grafica') # definir el titulo de la grafica
plt.legend() # agregar el legend al plot

plt.grid(True) # poner grid en la grafica
```


![png](./4-Visualizacion_36_0.png)


### Tamaño de la Figura y DPI

Matplotlib permite especificar la relación de aspecto, el DPI y el tamaño de la figura cuando se crea el objeto Figure. Puede usar los argumentos de las palabras clave `figsize` y` dpi`. No es necesario poner las dos.
* `figsize` es una tupla del ancho y alto de la figura en pulgadas
* `dpi` es el punto por pulgada (pixel por pulgada).


```python
# se cambia el tamaño de la figura y el numero de puntos por pulgada
plt.figure(figsize=(8,4), dpi=100)

plt.plot(x, y) # se grafica una linea de color azul

plt.xlabel('Nombre del eje X') # definir el nombre del eje X
plt.ylabel('Nombre del eje Y') # definir el nombre del eje Y
plt.title('Titulo de la grafica'); # definir el titulo de la grafica

# agrego ; al final del ultimo comando para solo mostrar la grafica
# plt.show() no es necesario en jupyter notebook
```


![png](./4-Visualizacion_38_0.png)


### Parametros de las lineas: colores, ancho y tipos

Matplotlib le brinda *muchas* opciones para personalizar colores, anchos de línea y tipos de línea.

Existe la sintaxis básica que se puede consultar en:

https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

#### Colores Basicos

Con matplotlib, podemos definir los colores de las líneas y otros elementos gráficos de varias maneras. En primer lugar, podemos usar la sintaxis similar a MATLAB donde `'b'` significa azul,`'g'` significa verde, etc. También se admite la API MATLAB para seleccionar estilos de línea: donde, por ejemplo, 'b.-'significa una línea azul con puntos:


```python
# Estilo MATLAB de estilo y color de linea
plt.plot(x, x**2, 'b.-') # linea azul con puntos
plt.plot(x, x**3, 'g--'); # Linea verde discontinua
```


![png](./4-Visualizacion_42_0.png)


#### Colores usando el parametro  `color`

También podemos definir colores por sus nombres o códigos hexadecimales RGB y, opcionalmente, proporcionar un valor alpha utilizando los argumentos de palabras clave `color` y` alpha`. Alpha indica opacidad.


```python
plt.plot(x, x, color="red") # Medio transparente
plt.plot(x, x+1, color="red", alpha=0.5) # Medio transparente
plt.plot(x, x+2, color="#8B008B")        # RGB hex code
plt.plot(x, x+3, color="#F08C08");       # RGB hex code 
plt.grid(True) # poner grid en la grafica
```


![png](./4-Visualizacion_45_0.png)


#### Estilos de Lineas y marcadores

Para cambiar el ancho de línea, podemos usar el argumento de la palabra clave `linewidth` o` lw`. El estilo de línea se puede seleccionar usando los argumentos de palabras clave `linestyle` o` ls`:


```python
plt.subplots(figsize=(12,6))

plt.plot(x, x+1, color="red", linewidth=0.25)
plt.plot(x, x+2, color="red", linewidth=0.50)
plt.plot(x, x+3, color="red", linewidth=1.00)
plt.plot(x, x+4, color="red", linewidth=2.00)

# posibles opciones linestype ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
plt.plot(x, x+5, color="green", lw=3, linestyle='-')
plt.plot(x, x+6, color="green", lw=3, ls='-.')
plt.plot(x, x+7, color="green", lw=3, ls=':')

# lineas parametrizadas
line, = plt.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # formato: longitud de linea, longitud de espacio, ...

# posibles simbolos del marcas: marker = '+', 'o', '*', 's', ',', '.',bb '1', '2', '3', '4', ...
plt.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
plt.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
plt.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
plt.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# tamaño y color de la marca
plt.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
plt.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
plt.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
plt.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");
```


![png](./4-Visualizacion_48_0.png)


Para mas informacion:
https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

### Subplots


```python
# la funcion es plt.subplot(nrows, ncols, plot_number)

plt.subplot(1,2,1) # subplot fila=1 Col=2, grafica=1
plt.plot(x, y, 'r--') # r-- color rojo y linea discontinua
plt.subplot(1,2,2) # subplot fila=1 Col=2, grafica=2
plt.plot(y, x, 'g*-'); # para no mostrar info de la funcion
plt.tight_layout() # para que no se superpongan las graficas
```


![png](./4-Visualizacion_51_0.png)


#### Multiples subplots

Crear subplot de diferentes tamaños se puede lograr con el metodo `.subplot2grid()`
Mas informacion en el link: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot2grid.html


```python
plt.subplot2grid((3,3), (0,0), colspan=3)
plt.subplot2grid((3,3), (1,0), colspan=2)
plt.subplot2grid((3,3), (1,2), rowspan=2)
plt.subplot2grid((3,3), (2,0))
plt.subplot2grid((3,3), (2,1))
plt.tight_layout() # para que no se superpongan las graficas
```


![png](./4-Visualizacion_53_0.png)


### Rango del Plot

Podemos configurar los rangos de los ejes usando los métodos `ylim` y` xlim` en el objeto del eje, o `axis('tight')` para obtener automáticamente rangos de ejes "tightly fitted":


```python
plt.figure(figsize=(12, 4))

plt.subplot(1,3,1)
plt.plot(x, x**2, x, x**3)
plt.title("Rango por defecto de los ejes")

plt.subplot(1,3,2)
plt.plot(x, x**2, x, x**3)
plt.axis('tight')
plt.title("Ejes apretados")

plt.subplot(1,3,3)
plt.plot(x, x**2, x, x**3)
plt.ylim([0, 60])
plt.xlim([2, 5])
plt.title("ejes de rango personalizados");

plt.tight_layout() # para que no se superpongan las graficas
```


![png](./4-Visualizacion_56_0.png)


#### Escala Logaritmica


```python
plt.figure(figsize=(10,4))
      
plt.subplot(1,2,1)
plt.plot(x, x**2, x, np.exp(x))
plt.title("escala Normal")

plt.subplot(1,2,2)
plt.plot(x, x**2, x, np.exp(x))
plt.yscale("log")
plt.title("Escala Logaritmica(y)");

plt.tight_layout() # para que no se superpongan las graficas
```


![png](./4-Visualizacion_58_0.png)


### Anotaciones de texto
Anotar texto en figuras matplotlib se puede hacer usando la función `text`. Es compatible con el formato LaTeX al igual que los textos y títulos de la etiqueta del eje:


```python
# Datos para graficar
xx = np.linspace(-0.75, 1., 100)

plt.plot(xx, xx**2, xx, xx**3)
plt.title("Plot con anotaciones")

# Anotacion 1
plt.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
#Anotacion 2
plt.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");
```


![png](./4-Visualizacion_60_0.png)


---
## Matplotlib Método orientado a objetos
Lo demostrado hasta el momento es la forma basica de usar `Matplotlib`,
pero la libreria se puede usar mediante la programacion orientada a objtetos con el Matplotlib's Object Oriented API. Esto significa que se creara una instancia del objeto de figura y luego llamaremos a métodos o atributos de ese objeto.
La idea principal al utilizar el método más formal orientado a objetos es crear objetos de figura y luego simplemente invocar métodos o atributos fuera de ese objeto. Este enfoque es más agradable cuando se trata de una figura que tiene múltiples graficos en él.
Mas informacion: https://matplotlib.org/api/api_overview.html#the-object-oriented-api

Un ejemplo de matplotlib orientado a objetos:


```python
# Se crea una figura y 2 subplots
# cada subplt se accede por medio de los objetos axes

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
plt.tight_layout() # para que no se superpongan las graficas
```


![png](./4-Visualizacion_62_0.png)


---
## Tipos Especiales de Plots

Hay muchas Graficas especializadas que podemos crear, como barras, histogramas, diagramas de dispersión y mucho más. La mayoría de este tipo de tramas lo crearemos usando seaborn, una biblioteca de gráficos estadísticos para Python. Pero aquí hay algunos ejemplos de este tipo de graficos

### Scatter Plot (Dispersion)


```python
#Grafica X vs Y
# crear datos aleatorios
N = 50
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.title("Scatter plot Simple");
plt.show() # En jupyter notebook no es necesario este comando
```


![png](./4-Visualizacion_65_0.png)


Con las graficas de scatter o dispersion se pueden representar mas de 2 variables en una misma grafica, en el siguiente ejemplo se realizara la comparacion de `x vs y` el color de los puntos se representara con otra variable y el tamaño de los puntos sera otra variable


```python
# se creara otra variable que se representara con colores
colors = np.random.rand(N) # usar colores aleatorios

# se creara otra variable que se representara con el area de los puntos
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radio

plt.scatter(x, y, s=area, c=colors, alpha=0.5) # el atributo alpha es para la transparencia
plt.title("Scatter plot de representacion de 4 variables");
```


![png](./4-Visualizacion_67_0.png)


### Histograma
Un histograma es una representación gráfica de una variable en forma de barras, donde la superficie de cada barra es proporcional a la frecuencia de los valores representados. Sirven para obtener una "primera vista" general, o panorama, de la distribución de la población, o de la muestra, respecto a una característica, cuantitativa y continua 


```python
# crear datos aleatorios
from random import sample
data = sample(range(1, 1000), 100)

plt.hist(data,bins = 10) # bins el numero de divisiones del histograma
plt.title("Histograma");
```


![png](./4-Visualizacion_69_0.png)


### Boxplot
Informacion sobre el boxplot ->  https://es.wikipedia.org/wiki/Diagrama_de_caja

* Primer cuartil (Q1) como la mediana de la primera mitad de valores
* Segundo cuartil (Q2) como la propia mediana de la serie
* Tercer cuartil (Q3) como la mediana de la segunda mitad de valores.

La diferencia entre el tercer cuartil y el primero se conoce como rango intercuartíl

![Boxplot vs PDF](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boxplot_vs_PDF.svg/598px-Boxplot_vs_PDF.svg.png)

![Box-plot](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Boxplot.svg/457px-Boxplot.svg.png)


```python
#crear datos aleatorios
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# boxplot rectangular 
plt.boxplot(data,vert=True,patch_artist=True);
plt.title("Boxplot");
```


![png](./4-Visualizacion_71_0.png)


#### Diagramas de Violin

Permiten ver como es la distribucion de los datos


```python
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

# grafico de violin, se puede activar la visualizacion de la media y de la mediana
plt.violinplot(all_data, showmeans=False, showmedians=True)
plt.title('violin plot');
```


![png](./4-Visualizacion_73_0.png)


#### Diagramas de Violin vs Boxplot

Se grafiara usando programacino orientada a objetos con Matplolib la comparacion entre las graficas de violin y las de boxplot


```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

# generar datos aleatorios
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

# plot de violin
axes[0].violinplot(all_data,
                   showmeans=False,
                   showmedians=True)
axes[0].set_title('violin plot')

# plot box plot
axes[1].boxplot(all_data)
axes[1].set_title('box plot')

# agregando lineas horizontales
for ax in axes:
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(all_data))])
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')

# agragando los nombres a las divisiones del eje x (x-tick labels)
plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
         xticklabels=['x1', 'x2', 'x3', 'x4'])

fig.suptitle("Violin vs Boxplot",fontsize = 14) # titulo general de la grafica
plt.show()
```


![png](./4-Visualizacion_75_0.png)


### Diagramas de torta
No usarlos, los humanos no somos buenos discriminando angulos


```python
labels = 'Caballos', 'Cerdos', 'Perros', 'Vacas'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # solo "Saque" el 2do pedazo (ejem. 'cerdos')

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

plt.axis('equal')  #La relación de aspecto igual garantiza que el círculo sea homogeneo
plt.show()
```


![png](./4-Visualizacion_77_0.png)


### Diagramas de error


```python
# generacion de datos aleatorios
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# Graficas de error
plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.title("Diagrama de error")
plt.grid()
plt.show()
```


![png](./4-Visualizacion_79_0.png)


---
## Guardando  las figuras
Matplotlib puede generar resultados de alta calidad en varios formatos, incluidos PNG, JPG, EPS, SVG, PGF y PDF. 
Para guardar una figura en un archivo, podemos usar el método `savefig` de la clase` Figure`:

Lo primero es antes de crear una grafica definir la clase `Figure` al principio de todo la grafica, Ejemplo:

`fig = plt.figure(figsize=(10,4))
 plt.scatter(x, y)
 plt.title("Scatter plot Simple");`



```python
fig.savefig("figura.png")
```

Aquí también podemos especificar opcionalmente el DPI y elegir entre diferentes formatos de salida (PNG, JPG, EPS, SVG, PGF y PDF):


```python
fig.savefig("figura.pdf", dpi=200)
```

___
## VISUALIZACION CON PANDAS

Pandas tiene funciones incorporadas para la visualización de datos. Está construido sobre matplotlib, pero se usa el formato de pandas para un uso más fácil. Mas informacion en: https://pandas.pydata.org/pandas-docs/stable/visualization.html

Los parametros de las graficas se pueden modificar con matplotlib.

### Importar la libreria


```python
import pandas as pd
import numpy as np
%matplotlib inline
```

**Datos para graficar:**


```python
df1 = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/mpg.csv')
df1.head()
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
df2 = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')
df2.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Hojas de estilo(Style Sheets)

Matplotlib tien [Hojas de estilo](http://matplotlib.org/gallery.html#style_sheets) se pueden usar para hacer que las graficas se vean un poco mejor. Estas hojas de estilo incluyen `plot_bmh`, `plot_fivethirtyeight`, `plot_ggplot` y más. Básicamente, crean un conjunto de reglas de estilo que siguen las gráficas. Es Recomendable usarlos, pues hacen que todas las graficas tengan el mismo aspecto y se sientan más profesionales.

**Antes de usasr `plt.style.use()` las graficas se ven así:**


```python
df1['acceleration'].hist();
```


![png](./4-Visualizacion_91_0.png)


Usar el estilo ggplot


```python
import matplotlib.pyplot as plt
plt.style.use('ggplot')
```

Ahora las graficas se ven asi:


```python
df1['acceleration'].hist();
```


![png](./4-Visualizacion_95_0.png)



```python
plt.style.use('bmh')
df1['acceleration'].hist();
```


![png](./4-Visualizacion_96_0.png)



```python
plt.style.use('dark_background')
df1['acceleration'].hist();
```


![png](./4-Visualizacion_97_0.png)



```python
plt.style.use('fivethirtyeight')
df1['acceleration'].hist();
```


![png](./4-Visualizacion_98_0.png)



```python
# El estilo por defecto es
plt.style.use('classic')
df1['acceleration'].hist();
```


![png](./4-Visualizacion_99_0.png)



```python
# Seguire usando el estilo ggplot para ver los tipos de grafica de pandas
plt.style.use('ggplot')
```

## Tipos de graficas en Pandas

Hay varios tipos de plots integradas a pandas, la mayoría de estos plots sobn para estadística por naturaleza:

* df.plot.area     
* df.plot.barh     
* df.plot.density  
* df.plot.hist     
* df.plot.line     
* df.plot.scatter
* df.plot.bar      
* df.plot.box      
* df.plot.hexbin   
* df.plot.kde      
* df.plot.pie

También se puede llamar a `df.plot(kind = 'hist')` o reemplazar ese argumento kind con cualquiera de los términos clave que se muestran en la lista anterior (por ejemplo, 'box', 'barh', etc.)

### Area


```python
# Se puede hacer de las siguiente manera
#df2.plot(kind='area',alpha = 0.4)

df2.plot.area(alpha=0.4);
```


![png](./4-Visualizacion_103_0.png)


### Barplots


```python
# Visualizacion de datos
df2.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# los nombres de cada columna equivalen a un color diferente
# Solo se graficaran algunos datos
df2.iloc[2:8].plot.bar();
```


![png](./4-Visualizacion_106_0.png)



```python
df2.iloc[2:8].plot.bar(stacked=True);
```


![png](./4-Visualizacion_107_0.png)


### Histogramas


```python
df1.head()
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
df1['acceleration'].plot.hist(bins=50);
```


![png](./4-Visualizacion_110_0.png)


### Lineas


```python
# eje y = valores de la acceleracion
# eje x = valores del index
# atributo lw es el grosor de la linea
df1.plot.line(y='acceleration',figsize=(12,3),lw=1);
```


![png](./4-Visualizacion_112_0.png)


### Scatter Plots


```python
df1.plot.scatter(x='acceleration',y='mpg');
```


![png](./4-Visualizacion_114_0.png)


Se puede usar `c` para indicar el color de los valores de otra columna
Con cmap se indica el mapa de colores que se usaran. 
Para ver los colormaps existente: http://matplotlib.org/users/colormaps.html


```python
df1.plot.scatter(x='acceleration',y='mpg',c='model_year',cmap='coolwarm');
```


![png](./4-Visualizacion_116_0.png)


O se puede usar `s` para indicar el tamaño de los puntos. El parametro `s` debe ser un arreglo, no solo el nombre de una columna:


```python
df1.plot.scatter(x='acceleration',y='mpg',s=df1['horsepower']*2);
```


![png](./4-Visualizacion_118_0.png)


### BoxPlots


```python
df2.plot.box(); # Tambien se puede poner by= argumento para groupby
```


![png](./4-Visualizacion_120_0.png)


### Diagrama de Torta


```python
serie = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
serie.plot.pie(figsize=(6, 6));
```


![png](./4-Visualizacion_122_0.png)


### Hexagonal

Util para datos de 2 variables, alternativa al scatterplot:


```python
df1.plot.hexbin(x='acceleration',y='mpg',gridsize=25,cmap='Oranges');
```


![png](./4-Visualizacion_124_0.png)


### Kernel Density Estimation Plot(KDE)


```python
df1['weight'].plot.kde();
```


![png](./4-Visualizacion_126_0.png)



```python
df2.plot.density();
```


![png](./4-Visualizacion_127_0.png)


### Scatter Matrix


```python
pd.plotting.scatter_matrix(df2, figsize=(8, 8));
```


![png](./4-Visualizacion_129_0.png)


### Parametros de las graficas

Graficar con Pandas es un método de hacer graficas mucho más fácil de usar que matplotlib, equilibra la facilidad de uso con control sobre la figura. Muchas de las llamadas a gráficos también aceptan argumentos adicionales de matplotlib plt.


```python
df2.plot.density() # grafico de densidad con pandas

plt.title('Grafica de densidad de varias variables')
plt.grid(False)
plt.xticks([]);# Para eliminar los numeros del eje
```


![png](./4-Visualizacion_131_0.png)



```python
# La misma grafica pero adicionando los parametros en los argumentos
df2.plot.density(title='Grafica de densidad de varias variables',
                 grid=False,
                xticks = []);
```


![png](./4-Visualizacion_132_0.png)


## PLOTLY: Libreria de Visualizacion Interactiva

Plotly es una libreria de graficos interactivos de código abierto que admite más de 40 tipos de gráficos únicos que cubren una amplia gama de casos de uso estadísticos, financieros, geográficos, científicos y tridimensionales.

Ademas de ser interactivo y obtener los valores en cada punto de la gráfica, **se pueden mezclar datos numéricos y categóricos.**


### Instalacion Plotly

´pip install plotly==4.1.0´

´conda install -c plotly plotly=4.1.0´

### Importar Plotly express

Plotly express es un modulo para usar de forma rapida y concisa de usar la visualización interactiva de plotly

**Nota: Los datos siempre deben estar en un dataframe**


```python
import plotly.express as px
```

### Datos integrados en Plotly
Plotly viene con algunos data sets clasicos integrados para hacer pruebas:
- carshare
- election
- gapminder
- iris
- tips
- wind


Tambien se pueden encontar otros datasets clasicos de demostracion en formato .csv
en: https://github.com/mwaskom/seaborn-data


```python
tips = px.data.tips() # Importar el dataset tips
type(tips)
```




    pandas.core.frame.DataFrame




```python
print(px.data.tips.__doc__)

```

    
        Each row represents a restaurant bill.
    
        https://vincentarelbundock.github.io/Rdatasets/doc/reshape2/tips.html
    
        Returns:
            A `pandas.DataFrame` with 244 rows and the following columns: `['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']`.
        



```python
tips.head() # ver los primeros 5 registros
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.dtypes #tipos de datos en el dataframe
```




    total_bill    float64
    tip           float64
    sex            object
    smoker         object
    day            object
    time           object
    size            int64
    dtype: object




```python
tips.describe() #Resumen estadistico de los datos del data frame por columna
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Tipos de Graficas con Plotly

### Lineas


```python
px.line(tips,y='total_bill',title='Valor Total de la Cuenta')
```


        <script type="text/javascript">
        window.PlotlyConfig = {MathJaxConfig: 'local'};
        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
        if (typeof require !== 'undefined') {
        require.undef("plotly");
        define('plotly', function(require, exports, module) {
            /**
* plotly.js v1.50.1
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
* Licensed under the MIT license
*/
        });
        require(['plotly'], function(Plotly) {
            window._Plotly = Plotly;
        });
        }
        </script>




<div>


            <div id="70ceeb2c-98b4-4382-bfed-b2fc035a3227" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("70ceeb2c-98b4-4382-bfed-b2fc035a3227")) {
                    Plotly.newPlot(
                        '70ceeb2c-98b4-4382-bfed-b2fc035a3227',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{y}", "legendgroup": "", "line": {"color": "#636efa", "dash": "solid"}, "mode": "lines", "name": "", "showlegend": false, "type": "scatter", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Valor Total de la Cuenta"}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98]}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('70ceeb2c-98b4-4382-bfed-b2fc035a3227');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Barras


```python
px.bar(tips, x="sex", y="total_bill")
```


<div>


            <div id="b6d55480-a5dd-458b-873d-af754fa7e6a1" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("b6d55480-a5dd-458b-873d-af754fa7e6a1")) {
                    Plotly.newPlot(
                        'b6d55480-a5dd-458b-873d-af754fa7e6a1',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=%{x}<br>total_bill=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "textposition": "auto", "type": "bar", "x": ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female"], "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "yaxis": "y"}],
                        {"barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "sex"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('b6d55480-a5dd-458b-873d-af754fa7e6a1');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.bar(tips, x="sex", y="total_bill", color='sex')
```


<div>


            <div id="6005d3bb-4b62-493b-a36b-06db2b37cfb3" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("6005d3bb-4b62-493b-a36b-06db2b37cfb3")) {
                    Plotly.newPlot(
                        '6005d3bb-4b62-493b-a36b-06db2b37cfb3',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa"}, "name": "sex=Female", "offsetgroup": "sex=Female", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Female"], "xaxis": "x", "y": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B"}, "name": "sex=Male", "offsetgroup": "sex=Male", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male"], "xaxis": "x", "y": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "yaxis": "y"}],
                        {"barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "categoryarray": ["Female", "Male"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "sex"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('6005d3bb-4b62-493b-a36b-06db2b37cfb3');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Histograma


```python
px.histogram(tips,'total_bill',title='Histograma Valor Total de la Cuenta')
```


<div>


            <div id="f505b0f3-dcda-40f1-9b7c-de2088813fd8" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("f505b0f3-dcda-40f1-9b7c-de2088813fd8")) {
                    Plotly.newPlot(
                        'f505b0f3-dcda-40f1-9b7c-de2088813fd8',
                        [{"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x", "yaxis": "y"}],
                        {"barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Histograma Valor Total de la Cuenta"}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "total_bill"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('f505b0f3-dcda-40f1-9b7c-de2088813fd8');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.histogram(tips,'sex',title='Histograma de Generos')
```


<div>


            <div id="0c0ea066-d5cd-41e9-8334-851ab243f22b" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("0c0ea066-d5cd-41e9-8334-851ab243f22b")) {
                    Plotly.newPlot(
                        '0c0ea066-d5cd-41e9-8334-851ab243f22b',
                        [{"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female"], "xaxis": "x", "yaxis": "y"}],
                        {"barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Histograma de Generos"}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "sex"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('0c0ea066-d5cd-41e9-8334-851ab243f22b');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.histogram(tips,'day',
             category_orders= {'day': ["Thur","Fri","Sat", "Sun"]},
             title='Histograma de Dias')
```


<div>


            <div id="07165b14-b232-4c9b-9691-1785b139fd24" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("07165b14-b232-4c9b-9691-1785b139fd24")) {
                    Plotly.newPlot(
                        '07165b14-b232-4c9b-9691-1785b139fd24',
                        [{"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "xaxis": "x", "yaxis": "y"}],
                        {"barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Histograma de Dias"}, "xaxis": {"anchor": "y", "categoryarray": ["Thur", "Fri", "Sat", "Sun"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('07165b14-b232-4c9b-9691-1785b139fd24');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Boxplot


```python
px.box(tips,y='total_bill', title='Boxplot Valor Total de la Cuenta')
```


<div>


            <div id="9060b60c-57bf-41ce-b1de-9aba42a817fa" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("9060b60c-57bf-41ce-b1de-9aba42a817fa")) {
                    Plotly.newPlot(
                        '9060b60c-57bf-41ce-b1de-9aba42a817fa',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "notched": false, "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "box", "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Boxplot Valor Total de la Cuenta"}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98]}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('9060b60c-57bf-41ce-b1de-9aba42a817fa');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.box(tips,x = 'day',y='total_bill', color='day',
       title='Boxplots por dia del Valor Total de la Cuenta')
```


<div>


            <div id="34ff3511-df98-48b9-8ad7-25eded94efc2" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("34ff3511-df98-48b9-8ad7-25eded94efc2")) {
                    Plotly.newPlot(
                        '34ff3511-df98-48b9-8ad7-25eded94efc2',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Sun", "marker": {"color": "#636efa"}, "name": "day=Sun", "notched": false, "offsetgroup": "day=Sun", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.07, 23.95, 25.71, 17.31, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Sat", "marker": {"color": "#EF553B"}, "name": "day=Sat", "notched": false, "offsetgroup": "day=Sat", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 10.59, 10.63, 50.81, 15.81, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Thur", "marker": {"color": "#00cc96"}, "name": "day=Thur", "notched": false, "offsetgroup": "day=Thur", "orientation": "v", "showlegend": true, "type": "box", "x": ["Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur"], "x0": " ", "xaxis": "x", "y": [27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Fri", "marker": {"color": "#ab63fa"}, "name": "day=Fri", "notched": false, "offsetgroup": "day=Fri", "orientation": "v", "showlegend": true, "type": "box", "x": ["Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri"], "x0": " ", "xaxis": "x", "y": [28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Boxplots por dia del Valor Total de la Cuenta"}, "xaxis": {"anchor": "y", "categoryarray": ["Sun", "Sat", "Thur", "Fri"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('34ff3511-df98-48b9-8ad7-25eded94efc2');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.box(tips,x = 'day',y='total_bill', title= 'Boxplot por dia con dias en orden',
       category_orders= {'day': ["Thur","Fri","Sat", "Sun"]})
```


<div>


            <div id="939b4599-9067-4dc3-9daa-5251fe2ba031" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("939b4599-9067-4dc3-9daa-5251fe2ba031")) {
                    Plotly.newPlot(
                        '939b4599-9067-4dc3-9daa-5251fe2ba031',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "notched": false, "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Boxplot por dia con dias en orden"}, "xaxis": {"anchor": "y", "categoryarray": ["Thur", "Fri", "Sat", "Sun"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('939b4599-9067-4dc3-9daa-5251fe2ba031');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.box(tips,x = 'day',y='total_bill', color='smoker', category_orders= {'day': ["Thur","Fri","Sat", "Sun"]})
```


<div>


            <div id="a4fe26b8-5ba8-4f9c-9606-66769f2035d2" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("a4fe26b8-5ba8-4f9c-9606-66769f2035d2")) {
                    Plotly.newPlot(
                        'a4fe26b8-5ba8-4f9c-9606-66769f2035d2',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa"}, "name": "smoker=No", "notched": false, "offsetgroup": "smoker=No", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Sat", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 26.41, 48.27, 17.59, 20.08, 16.45, 20.23, 12.02, 17.07, 14.73, 10.51, 27.2, 22.76, 17.29, 16.66, 10.07, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 22.49, 22.75, 12.46, 20.92, 18.24, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 24.52, 20.76, 31.71, 20.69, 7.56, 48.33, 15.98, 20.45, 13.28, 11.61, 10.77, 10.07, 35.83, 29.03, 17.82, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B"}, "name": "smoker=Yes", "notched": false, "offsetgroup": "smoker=Yes", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 3.07, 15.01, 26.86, 25.28, 17.92, 19.44, 32.68, 28.97, 5.75, 16.32, 40.17, 27.28, 12.03, 21.01, 11.35, 15.38, 44.3, 22.42, 15.36, 20.49, 25.21, 14.31, 16.0, 17.51, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 13.42, 16.27, 10.09, 22.12, 24.01, 15.69, 15.53, 12.6, 32.83, 27.18, 22.67], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "categoryarray": ["Thur", "Fri", "Sat", "Sun"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('a4fe26b8-5ba8-4f9c-9606-66769f2035d2');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.box(tips,x = 'day',y='total_bill', color='smoker', 
       boxmode='overlay',
       title = 'Boxplots de cuenta total por dia, fumador o no , sobrepuestos ',
       category_orders= {'day': ["Thur","Fri","Sat", "Sun"]})
```


<div>


            <div id="42cee035-17e5-4539-9b76-fc670cb4e993" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("42cee035-17e5-4539-9b76-fc670cb4e993")) {
                    Plotly.newPlot(
                        '42cee035-17e5-4539-9b76-fc670cb4e993',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa"}, "name": "smoker=No", "notched": false, "offsetgroup": "smoker=No", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Sat", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 26.41, 48.27, 17.59, 20.08, 16.45, 20.23, 12.02, 17.07, 14.73, 10.51, 27.2, 22.76, 17.29, 16.66, 10.07, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 22.49, 22.75, 12.46, 20.92, 18.24, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 24.52, 20.76, 31.71, 20.69, 7.56, 48.33, 15.98, 20.45, 13.28, 11.61, 10.77, 10.07, 35.83, 29.03, 17.82, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B"}, "name": "smoker=Yes", "notched": false, "offsetgroup": "smoker=Yes", "orientation": "v", "showlegend": true, "type": "box", "x": ["Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 3.07, 15.01, 26.86, 25.28, 17.92, 19.44, 32.68, 28.97, 5.75, 16.32, 40.17, 27.28, 12.03, 21.01, 11.35, 15.38, 44.3, 22.42, 15.36, 20.49, 25.21, 14.31, 16.0, 17.51, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 13.42, 16.27, 10.09, 22.12, 24.01, 15.69, 15.53, 12.6, 32.83, 27.18, 22.67], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "overlay", "height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Boxplots de cuenta total por dia, fumador o no , sobrepuestos "}, "xaxis": {"anchor": "y", "categoryarray": ["Thur", "Fri", "Sat", "Sun"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('42cee035-17e5-4539-9b76-fc670cb4e993');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Violin Plot


```python
px.violin(tips,y='total_bill', title='Boxplot Valor Total de la Cuenta')
```


<div>


            <div id="5f805000-5b42-4c18-94ee-195a0cf5d491" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("5f805000-5b42-4c18-94ee-195a0cf5d491")) {
                    Plotly.newPlot(
                        '5f805000-5b42-4c18-94ee-195a0cf5d491',
                        [{"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "scalegroup": "True", "showlegend": false, "type": "violin", "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "y0": " ", "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Boxplot Valor Total de la Cuenta"}, "violinmode": "group", "xaxis": {"anchor": "y", "domain": [0.0, 0.98]}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('5f805000-5b42-4c18-94ee-195a0cf5d491');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.violin(tips,x = 'day',y='total_bill', title='Violin por dia del Valor Total de la Cuenta')
```


<div>


            <div id="b4306aac-08a4-4ef8-9e57-a9c87a89a152" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("b4306aac-08a4-4ef8-9e57-a9c87a89a152")) {
                    Plotly.newPlot(
                        'b4306aac-08a4-4ef8-9e57-a9c87a89a152',
                        [{"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "scalegroup": "True", "showlegend": false, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "y0": " ", "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Violin por dia del Valor Total de la Cuenta"}, "violinmode": "group", "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('b4306aac-08a4-4ef8-9e57-a9c87a89a152');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.violin(tips,x = 'day',y='total_bill', color='day',
          title='Violin por dia del Valor Total de la Cuenta')
```


<div>


            <div id="9209898c-5e1d-4343-b06b-715171d69265" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("9209898c-5e1d-4343-b06b-715171d69265")) {
                    Plotly.newPlot(
                        '9209898c-5e1d-4343-b06b-715171d69265',
                        [{"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Sun", "marker": {"color": "#636efa"}, "name": "day=Sun", "offsetgroup": "day=Sun", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.07, 23.95, 25.71, 17.31, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Sat", "marker": {"color": "#EF553B"}, "name": "day=Sat", "offsetgroup": "day=Sat", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 10.59, 10.63, 50.81, 15.81, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Thur", "marker": {"color": "#00cc96"}, "name": "day=Thur", "offsetgroup": "day=Thur", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur"], "x0": " ", "xaxis": "x", "y": [27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "day=Fri", "marker": {"color": "#ab63fa"}, "name": "day=Fri", "offsetgroup": "day=Fri", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri"], "x0": " ", "xaxis": "x", "y": [28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09], "y0": " ", "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Violin por dia del Valor Total de la Cuenta"}, "violinmode": "group", "xaxis": {"anchor": "y", "categoryarray": ["Sun", "Sat", "Thur", "Fri"], "categoryorder": "array", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('9209898c-5e1d-4343-b06b-715171d69265');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.violin(tips,x = 'day',y='total_bill', color='sex',
          title='Violin por dia del Valor Total de la Cuenta')
```


<div>


            <div id="e1603a10-9791-438f-8aef-a02928211b9a" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("e1603a10-9791-438f-8aef-a02928211b9a")) {
                    Plotly.newPlot(
                        'e1603a10-9791-438f-8aef-a02928211b9a',
                        [{"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa"}, "name": "sex=Female", "offsetgroup": "sex=Female", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B"}, "name": "sex=Male", "offsetgroup": "sex=Male", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "y0": " ", "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Violin por dia del Valor Total de la Cuenta"}, "violinmode": "group", "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('e1603a10-9791-438f-8aef-a02928211b9a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.violin(tips,x = 'day',y='total_bill', color='sex',violinmode='overlay',
          title='Violin por dia del Valor Total de la Cuenta, Hombres y Mujeres')
```


<div>


            <div id="08aa1cd5-58d0-4d9f-8cc5-126b4f4742ce" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("08aa1cd5-58d0-4d9f-8cc5-126b4f4742ce")) {
                    Plotly.newPlot(
                        '08aa1cd5-58d0-4d9f-8cc5-126b4f4742ce',
                        [{"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa"}, "name": "sex=Female", "offsetgroup": "sex=Female", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "box": {"visible": false}, "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B"}, "name": "sex=Male", "offsetgroup": "sex=Male", "orientation": "v", "scalegroup": "True", "showlegend": true, "type": "violin", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "y0": " ", "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Violin por dia del Valor Total de la Cuenta, Hombres y Mujeres"}, "violinmode": "overlay", "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('08aa1cd5-58d0-4d9f-8cc5-126b4f4742ce');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### StripPlot


```python
px.strip(tips, x="day", y="total_bill")
```


<div>


            <div id="daf2ab16-9574-44a8-9093-2b318c080e3c" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("daf2ab16-9574-44a8-9093-2b318c080e3c")) {
                    Plotly.newPlot(
                        'daf2ab16-9574-44a8-9093-2b318c080e3c',
                        [{"alignmentgroup": "True", "boxpoints": "all", "fillcolor": "rgba(255,255,255,0)", "hoverlabel": {"namelength": 0}, "hoveron": "points", "hovertemplate": "day=%{x}<br>total_bill=%{y}", "legendgroup": "", "line": {"color": "rgba(255,255,255,0)"}, "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "pointpos": 0, "showlegend": false, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('daf2ab16-9574-44a8-9093-2b318c080e3c');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.strip(tips, x="total_bill", y="time",
         orientation="h", color="smoker")
```


<div>


            <div id="aa994c9b-0bd9-458c-8455-145a0079844f" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("aa994c9b-0bd9-458c-8455-145a0079844f")) {
                    Plotly.newPlot(
                        'aa994c9b-0bd9-458c-8455-145a0079844f',
                        [{"alignmentgroup": "True", "boxpoints": "all", "fillcolor": "rgba(255,255,255,0)", "hoverlabel": {"namelength": 0}, "hoveron": "points", "hovertemplate": "smoker=No<br>total_bill=%{x}<br>time=%{y}", "legendgroup": "smoker=No", "line": {"color": "rgba(255,255,255,0)"}, "marker": {"color": "#636efa"}, "name": "smoker=No", "offsetgroup": "smoker=No", "orientation": "h", "pointpos": 0, "showlegend": true, "type": "box", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 26.41, 48.27, 17.59, 20.08, 16.45, 20.23, 12.02, 17.07, 14.73, 10.51, 27.2, 22.76, 17.29, 16.66, 10.07, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 22.49, 22.75, 12.46, 20.92, 18.24, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 24.52, 20.76, 31.71, 20.69, 7.56, 48.33, 15.98, 20.45, 13.28, 11.61, 10.77, 10.07, 35.83, 29.03, 17.82, 18.78], "x0": " ", "xaxis": "x", "y": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Dinner", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner"], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "boxpoints": "all", "fillcolor": "rgba(255,255,255,0)", "hoverlabel": {"namelength": 0}, "hoveron": "points", "hovertemplate": "smoker=Yes<br>total_bill=%{x}<br>time=%{y}", "legendgroup": "smoker=Yes", "line": {"color": "rgba(255,255,255,0)"}, "marker": {"color": "#EF553B"}, "name": "smoker=Yes", "offsetgroup": "smoker=Yes", "orientation": "h", "pointpos": 0, "showlegend": true, "type": "box", "x": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 3.07, 15.01, 26.86, 25.28, 17.92, 19.44, 32.68, 28.97, 5.75, 16.32, 40.17, 27.28, 12.03, 21.01, 11.35, 15.38, 44.3, 22.42, 15.36, 20.49, 25.21, 14.31, 16.0, 17.51, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 13.42, 16.27, 10.09, 22.12, 24.01, 15.69, 15.53, 12.6, 32.83, 27.18, 22.67], "x0": " ", "xaxis": "x", "y": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner"], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "group", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "total_bill"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "time"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('aa994c9b-0bd9-458c-8455-145a0079844f');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.strip(tips, x="day", y="total_bill",
         color="sex", stripmode='overlay')
```


<div>


            <div id="28593578-5613-47da-8e4f-0b18bb682469" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("28593578-5613-47da-8e4f-0b18bb682469")) {
                    Plotly.newPlot(
                        '28593578-5613-47da-8e4f-0b18bb682469',
                        [{"alignmentgroup": "True", "boxpoints": "all", "fillcolor": "rgba(255,255,255,0)", "hoverlabel": {"namelength": 0}, "hoveron": "points", "hovertemplate": "sex=Female<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Female", "line": {"color": "rgba(255,255,255,0)"}, "marker": {"color": "#636efa"}, "name": "sex=Female", "offsetgroup": "sex=Female", "orientation": "v", "pointpos": 0, "showlegend": true, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Thur"], "x0": " ", "xaxis": "x", "y": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "y0": " ", "yaxis": "y"}, {"alignmentgroup": "True", "boxpoints": "all", "fillcolor": "rgba(255,255,255,0)", "hoverlabel": {"namelength": 0}, "hoveron": "points", "hovertemplate": "sex=Male<br>day=%{x}<br>total_bill=%{y}", "legendgroup": "sex=Male", "line": {"color": "rgba(255,255,255,0)"}, "marker": {"color": "#EF553B"}, "name": "sex=Male", "offsetgroup": "sex=Male", "orientation": "v", "pointpos": 0, "showlegend": true, "type": "box", "x": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat"], "x0": " ", "xaxis": "x", "y": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "y0": " ", "yaxis": "y"}],
                        {"boxmode": "overlay", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "day"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "total_bill"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('28593578-5613-47da-8e4f-0b18bb682469');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Scatterplot


```python
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year==2007")
```


```python
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")
```


<div>


            <div id="a8330366-466a-4e1f-9afa-d7a4060e6282" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("a8330366-466a-4e1f-9afa-d7a4060e6282")) {
                    Plotly.newPlot(
                        'a8330366-466a-4e1f-9afa-d7a4060e6282',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "", "showlegend": false, "type": "scatter", "x": [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.379640000001, 34435.367439999995, 36126.4927, 29796.048339999998, 1391.253792, 33692.60508, 1441.284873, 3822.1370840000004, 7446.298803, 12569.851770000001, 9065.800825, 10680.79282, 1217.032994, 430.07069160000003, 1713.7786859999999, 2042.0952399999999, 36319.235010000004, 706.016537, 1704.0637239999999, 13171.63885, 4959.1148539999995, 7006.580419, 986.1478792000001, 277.55185869999997, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000003, 6025.374752000001, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000001, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999999, 1201.637154, 3548.3308460000003, 39724.97867, 18008.94444, 36180.789189999996, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.880262000001, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.1514960000002, 10956.99112, 11977.57496, 3095.7722710000003, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999999, 2013.9773050000001, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000001, 1598.435089, 21654.83194, 1712.4721359999999, 9786.534714, 862.5407561000001, 47143.179639999995, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.0954070000003, 2602.394995, 4513.480643, 33859.74835, 37506.419069999996, 4184.548089, 28718.27684, 1107.482182, 7458.3963269999995, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.3801210000001, 33203.26128, 42951.65309, 10611.46299, 11415.805690000001, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007], "xaxis": "x", "y": [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.461999999999996, 55.321999999999996, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791000000000004, 72.235, 74.994, 71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.946999999999996, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005, 60.916000000000004, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.068999999999996, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.858999999999995, 80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556000000000004, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.516999999999996, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.486999999999995], "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "gdpPercap"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "lifeExp"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('a8330366-466a-4e1f-9afa-d7a4060e6282');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent")
```


<div>


            <div id="9797f061-95f5-43f7-b158-f36ce6008d06" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("9797f061-95f5-43f7-b158-f36ce6008d06")) {
                    Plotly.newPlot(
                        '9797f061-95f5-43f7-b158-f36ce6008d06',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Asia<br>gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Europe<br>gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Africa<br>gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Americas<br>gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Oceania<br>gdpPercap=%{x}<br>lifeExp=%{y}", "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [34435.367439999995, 25185.00911], "xaxis": "x", "y": [81.235, 80.204], "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "gdpPercap"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "lifeExp"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('9797f061-95f5-43f7-b158-f36ce6008d06');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", size="pop", color="continent", size_max=60)
```


<div>


            <div id="52a94980-ab0c-4dc9-85e2-788078d2eb74" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("52a94980-ab0c-4dc9-85e2-788078d2eb74")) {
                    Plotly.newPlot(
                        '52a94980-ab0c-4dc9-85e2-788078d2eb74',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Asia<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [31889923, 708573, 150448339, 14131858, 1318683096, 6980412, 1110396331, 223547000, 69453570, 27499638, 6426679, 127467972, 6053193, 23301725, 49044790, 2505559, 3921278, 24821286, 2874127, 47761980, 28901790, 3204897, 169270617, 91077287, 27601038, 4553009, 20378239, 19314747, 23174294, 65068149, 85262356, 4018332, 22211743], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Europe<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3600523, 8199783, 10392226, 4552198, 7322858, 4493312, 10228744, 5468120, 5238460, 61083916, 82400996, 10706290, 9956108, 301931, 4109086, 58147733, 684736, 16570613, 4627926, 38518241, 10642836, 22276056, 10150265, 5447502, 2009245, 40448191, 9031088, 7554661, 71158647, 60776238], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Africa<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [33333216, 12420476, 8078314, 1639131, 14326203, 8390505, 17696293, 4369038, 10238807, 710960, 64606759, 3800610, 18013409, 496374, 80264543, 551201, 4906585, 76511887, 1454867, 1688359, 22873338, 9947814, 1472041, 35610177, 2012649, 3193942, 6036914, 19167654, 13327079, 12031795, 3270065, 1250882, 33757175, 19951656, 2055080, 12894865, 135031164, 798094, 8860588, 199579, 12267493, 6144562, 9118773, 43997828, 42292929, 1133066, 38139640, 5701579, 10276158, 29170398, 11746035, 12311143], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Americas<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [40301927, 9119152, 190010647, 33390141, 16284741, 44227550, 4133884, 11416987, 9319622, 13755680, 6939688, 12572928, 8502814, 7483763, 2780132, 108700891, 5675356, 3242173, 6667147, 28674757, 3942491, 1056608, 301139947, 3447496, 26084662], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "continent=Oceania<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [20434176, 4115771], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [34435.367439999995, 25185.00911], "xaxis": "x", "y": [81.235, 80.204], "yaxis": "y"}],
                        {"height": 600, "legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "gdpPercap"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "lifeExp"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('52a94980-ab0c-4dc9-85e2-788078d2eb74');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
```


<div>


            <div id="c3ab73af-f32a-47e3-b74b-7ca6e2263283" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("c3ab73af-f32a-47e3-b74b-7ca6e2263283")) {
                    Plotly.newPlot(
                        'c3ab73af-f32a-47e3-b74b-7ca6e2263283',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [31889923, 708573, 150448339, 14131858, 1318683096, 6980412, 1110396331, 223547000, 69453570, 27499638, 6426679, 127467972, 6053193, 23301725, 49044790, 2505559, 3921278, 24821286, 2874127, 47761980, 28901790, 3204897, 169270617, 91077287, 27601038, 4553009, 20378239, 19314747, 23174294, 65068149, 85262356, 4018332, 22211743], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3600523, 8199783, 10392226, 4552198, 7322858, 4493312, 10228744, 5468120, 5238460, 61083916, 82400996, 10706290, 9956108, 301931, 4109086, 58147733, 684736, 16570613, 4627926, 38518241, 10642836, 22276056, 10150265, 5447502, 2009245, 40448191, 9031088, 7554661, 71158647, 60776238], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [33333216, 12420476, 8078314, 1639131, 14326203, 8390505, 17696293, 4369038, 10238807, 710960, 64606759, 3800610, 18013409, 496374, 80264543, 551201, 4906585, 76511887, 1454867, 1688359, 22873338, 9947814, 1472041, 35610177, 2012649, 3193942, 6036914, 19167654, 13327079, 12031795, 3270065, 1250882, 33757175, 19951656, 2055080, 12894865, 135031164, 798094, 8860588, 199579, 12267493, 6144562, 9118773, 43997828, 42292929, 1133066, 38139640, 5701579, 10276158, 29170398, 11746035, 12311143], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [40301927, 9119152, 190010647, 33390141, 16284741, 44227550, 4133884, 11416987, 9319622, 13755680, 6939688, 12572928, 8502814, 7483763, 2780132, 108700891, 5675356, 3242173, 6667147, 28674757, 3942491, 1056608, 301139947, 3447496, 26084662], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [20434176, 4115771], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [34435.367439999995, 25185.00911], "xaxis": "x", "y": [81.235, 80.204], "yaxis": "y"}],
                        {"height": 600, "legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "gdpPercap"}, "type": "log"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "lifeExp"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('c3ab73af-f32a-47e3-b74b-7ca6e2263283');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Regresion Lineal


```python
px.scatter(tips,x='total_bill',y='tip',trendline='ols')
```


<div>


            <div id="94c8fb6a-5533-4602-9baf-5187d7a4008a" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("94c8fb6a-5533-4602-9baf-5187d7a4008a")) {
                    Plotly.newPlot(
                        '94c8fb6a-5533-4602-9baf-5187d7a4008a',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}<br>tip=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "", "showlegend": false, "type": "scatter", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>OLS trendline</b><br>tip = 0.105025 * total_bill + 0.920270<br>R<sup>2</sup>=0.456617<br><br>total_bill=%{x}<br>tip=%{y} <b>(trend)</b>", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "lines", "name": "", "showlegend": false, "type": "scatter", "x": [3.07, 5.75, 7.25, 7.25, 7.51, 7.56, 7.74, 8.35, 8.51, 8.52, 8.58, 8.77, 9.55, 9.6, 9.68, 9.78, 9.94, 10.07, 10.07, 10.09, 10.27, 10.29, 10.33, 10.33, 10.34, 10.34, 10.51, 10.59, 10.63, 10.65, 10.77, 11.02, 11.17, 11.24, 11.35, 11.38, 11.59, 11.61, 11.69, 11.87, 12.02, 12.03, 12.16, 12.26, 12.43, 12.46, 12.48, 12.54, 12.6, 12.66, 12.69, 12.74, 12.76, 12.9, 13.0, 13.0, 13.03, 13.13, 13.16, 13.27, 13.28, 13.37, 13.39, 13.42, 13.42, 13.42, 13.51, 13.81, 13.81, 13.94, 14.0, 14.07, 14.15, 14.26, 14.31, 14.48, 14.52, 14.73, 14.78, 14.83, 15.01, 15.04, 15.06, 15.36, 15.38, 15.42, 15.48, 15.53, 15.69, 15.69, 15.77, 15.81, 15.95, 15.98, 15.98, 16.0, 16.04, 16.21, 16.27, 16.29, 16.31, 16.32, 16.4, 16.43, 16.45, 16.47, 16.49, 16.58, 16.66, 16.82, 16.93, 16.97, 16.99, 17.07, 17.26, 17.29, 17.31, 17.46, 17.47, 17.51, 17.59, 17.78, 17.81, 17.82, 17.89, 17.92, 17.92, 18.04, 18.15, 18.24, 18.26, 18.28, 18.29, 18.29, 18.35, 18.43, 18.64, 18.69, 18.71, 18.78, 19.08, 19.44, 19.49, 19.65, 19.77, 19.81, 19.82, 20.08, 20.23, 20.27, 20.29, 20.29, 20.45, 20.49, 20.53, 20.65, 20.69, 20.69, 20.76, 20.9, 20.92, 21.01, 21.01, 21.16, 21.5, 21.58, 21.7, 22.12, 22.23, 22.42, 22.49, 22.67, 22.75, 22.76, 22.82, 23.1, 23.17, 23.33, 23.68, 23.95, 24.01, 24.06, 24.08, 24.27, 24.52, 24.55, 24.59, 24.71, 25.0, 25.21, 25.28, 25.29, 25.56, 25.71, 25.89, 26.41, 26.59, 26.86, 26.88, 27.05, 27.18, 27.2, 27.28, 28.15, 28.17, 28.44, 28.55, 28.97, 29.03, 29.8, 29.85, 29.93, 30.06, 30.14, 30.4, 30.46, 31.27, 31.71, 31.85, 32.4, 32.68, 32.83, 32.9, 34.3, 34.63, 34.65, 34.81, 34.83, 35.26, 35.83, 38.01, 38.07, 38.73, 39.42, 40.17, 40.55, 41.19, 43.11, 44.3, 45.35, 48.17, 48.27, 48.33, 50.81], "xaxis": "x", "y": [1.2426948819246377, 1.5241605885147047, 1.6816973645912348, 1.6816973645912348, 1.7090037391111665, 1.7142549649803842, 1.7331593781095678, 1.7972243337140235, 1.81402825649552, 1.8150785016693636, 1.8213799727124247, 1.8413346310154517, 1.9232537545752475, 1.9285049804444652, 1.9369069418352134, 1.9474093935736487, 1.9642133163551452, 1.9778665036151113, 1.9778665036151113, 1.9799669939627984, 1.998871407091982, 2.000971897439669, 2.005172878135043, 2.005172878135043, 2.006223123308887, 2.006223123308887, 2.0240772912642266, 2.032479252654975, 2.0366802333503493, 2.038780723698036, 2.051383665784159, 2.077639795130247, 2.0933934727379, 2.1007451889548046, 2.1122978858670836, 2.115448621388614, 2.1375037700393285, 2.1396042603870153, 2.148006221777764, 2.166910634906947, 2.1826643125146004, 2.183714557688444, 2.1973677449484095, 2.2078701966868453, 2.2257243646421854, 2.228875100163716, 2.230975590511403, 2.237277061554464, 2.2435785325975255, 2.2498800036405866, 2.253030739162117, 2.258281965031335, 2.2603824553790215, 2.275085887812831, 2.285588339551267, 2.285588339551267, 2.2887390750727974, 2.2992415268112327, 2.302392262332763, 2.313944959245042, 2.3149952044188855, 2.324447410983477, 2.3265479013311645, 2.329698636852695, 2.329698636852695, 2.329698636852695, 2.3391508434172867, 2.3706581986325928, 2.3706581986325928, 2.3843113858925586, 2.39061285693562, 2.3979645731525245, 2.406366534543273, 2.417919231455552, 2.42317045732477, 2.4410246252801096, 2.4452256059754838, 2.4672807546261977, 2.4725319804954156, 2.4777832063646335, 2.496687619493817, 2.4998383550153473, 2.5019388453630347, 2.5334462005783402, 2.5355466909260276, 2.539747671621402, 2.546049142664463, 2.5513003685336804, 2.5681042913151773, 2.5681042913151773, 2.5765062527059257, 2.5807072334012995, 2.595410665835109, 2.5985614013566396, 2.5985614013566396, 2.600661891704327, 2.6048628723997007, 2.622717040355041, 2.629018511398102, 2.6311190017457893, 2.633219492093476, 2.63426973726732, 2.642671698658068, 2.645822434179599, 2.6479229245272857, 2.6500234148749726, 2.65212390522266, 2.6615761117872516, 2.669978073178, 2.6867819959594965, 2.698334692871775, 2.7025356735671493, 2.704636163914836, 2.7130381253055846, 2.732992783608612, 2.7361435191301426, 2.7382440094778295, 2.7539976870854828, 2.755047932259326, 2.7592489129547006, 2.7676508743454487, 2.7876055326484757, 2.790756268170006, 2.79180651334385, 2.7991582295607547, 2.802308965082285, 2.802308965082285, 2.8149119071684074, 2.8264646040806864, 2.835916810645278, 2.8380173009929655, 2.840117791340653, 2.841168036514496, 2.841168036514496, 2.847469507557557, 2.8558714689483056, 2.8779266175990195, 2.8831778434682374, 2.8852783338159247, 2.892630050032829, 2.9241374052481346, 2.961946231506502, 2.96719745737572, 2.984001380157216, 2.996604322243339, 3.000805302938713, 3.001855548112556, 3.029161922632488, 3.0449156002401416, 3.0491165809355154, 3.0512170712832027, 3.0512170712832027, 3.0680209940646987, 3.0722219747600734, 3.076422955455447, 3.0890258975415694, 3.093226878236944, 3.093226878236944, 3.1005785944538493, 3.115282026887658, 3.1173825172353453, 3.126834723799937, 3.126834723799937, 3.1425884014075898, 3.17829673731827, 3.1866986987090185, 3.1993016407951407, 3.2434119380965694, 3.2549646350088484, 3.274919293311876, 3.28227100952878, 3.3011754226579635, 3.309577384048712, 3.310627629222556, 3.3169291002656163, 3.3463359651332354, 3.3536876813501406, 3.3704916041316366, 3.407250185216161, 3.435606804909936, 3.441908275952997, 3.447159501822215, 3.4492599921699014, 3.469214650472929, 3.4954707798190174, 3.498621515340548, 3.5028224960359218, 3.515425438122045, 3.5458825481635072, 3.567937696814221, 3.5752894130311264, 3.5763396582049696, 3.6046962778987446, 3.6204499555063983, 3.6393543686355816, 3.693967117675445, 3.7128715308046285, 3.7412281504984044, 3.743328640846091, 3.761182808801432, 3.7748359960613973, 3.7769364864090846, 3.785338447799833, 3.87670977792422, 3.8788102682719074, 3.9071668879656825, 3.9187195848779615, 3.96282988217939, 3.9691313532224513, 4.050000231608403, 4.055251457477621, 4.063653418868369, 4.077306606128335, 4.085708567519084, 4.113014942039015, 4.1193164130820765, 4.204386272163402, 4.2505970598125185, 4.265300492246328, 4.323063976807722, 4.352470841675341, 4.368224519282994, 4.375576235499898, 4.522610559837993, 4.55726865057483, 4.5593691409225166, 4.576173063704013, 4.578273554051701, 4.623434096526973, 4.683298071436054, 4.912251519333944, 4.918552990377005, 4.9878691718506785, 5.060336088845883, 5.139104476884148, 5.179013793490202, 5.246229484616188, 5.447876557994147, 5.572855733681527, 5.683131476935098, 5.979300615958975, 5.9898030676974106, 5.996104538740471, 6.256565341853668], "yaxis": "y"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "title": {"text": "total_bill"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "tip"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('94c8fb6a-5533-4602-9baf-5187d7a4008a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Matrix Plot


```python
px.scatter_matrix(tips)
```


<div>


            <div id="641b8da8-6109-407d-99da-c51f561e6819" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("641b8da8-6109-407d-99da-c51f561e6819")) {
                    Plotly.newPlot(
                        '641b8da8-6109-407d-99da-c51f561e6819',
                        [{"dimensions": [{"axis": {"matches": true}, "label": "total_bill", "values": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78]}, {"axis": {"matches": true}, "label": "tip", "values": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0]}, {"axis": {"matches": true}, "label": "sex", "values": ["Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Female", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Male", "Male", "Female", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Male", "Female"]}, {"axis": {"matches": true}, "label": "smoker", "values": ["No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "No", "Yes", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No", "No", "No", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", "No", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No", "No"]}, {"axis": {"matches": true}, "label": "day", "values": ["Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Sun", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Thur", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Fri", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Sat", "Thur"]}, {"axis": {"matches": true}, "label": "time", "values": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner"]}, {"axis": {"matches": true}, "label": "size", "values": [2, 3, 3, 2, 4, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2, 2, 3, 3, 3, 3, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 2, 4, 2, 4, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 4, 2, 2, 4, 3, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 4, 2, 2, 2, 4, 3, 3, 2, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 2, 3, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 6, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 5, 6, 2, 2, 3, 2, 2, 2, 2, 2, 3, 4, 4, 5, 6, 4, 2, 4, 4, 2, 3, 2, 2, 3, 2, 4, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 3, 4, 2, 5, 3, 5, 3, 3, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 3, 2, 2, 2, 4, 3, 3, 4, 2, 2, 3, 4, 4, 2, 3, 2, 5, 2, 2, 4, 2, 2, 1, 3, 2, 2, 2, 4, 2, 2, 4, 3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2]}], "hoverlabel": {"namelength": 0}, "hovertemplate": "%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "", "showlegend": false, "type": "splom"}],
                        {"dragmode": "select", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('641b8da8-6109-407d-99da-c51f561e6819');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter_matrix(tips, dimensions=['total_bill','tip','size'])
```


<div>


            <div id="c7ea0109-f667-49fb-a093-322d0c6d3947" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("c7ea0109-f667-49fb-a093-322d0c6d3947")) {
                    Plotly.newPlot(
                        'c7ea0109-f667-49fb-a093-322d0c6d3947',
                        [{"dimensions": [{"axis": {"matches": true}, "label": "total_bill", "values": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78]}, {"axis": {"matches": true}, "label": "tip", "values": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0]}, {"axis": {"matches": true}, "label": "size", "values": [2, 3, 3, 2, 4, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2, 2, 3, 3, 3, 3, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 2, 4, 2, 4, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 4, 2, 2, 4, 3, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 4, 2, 2, 2, 4, 3, 3, 2, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 2, 3, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 6, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 5, 6, 2, 2, 3, 2, 2, 2, 2, 2, 3, 4, 4, 5, 6, 4, 2, 4, 4, 2, 3, 2, 2, 3, 2, 4, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 3, 4, 2, 5, 3, 5, 3, 3, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 3, 2, 2, 2, 4, 3, 3, 4, 2, 2, 3, 4, 4, 2, 3, 2, 5, 2, 2, 4, 2, 2, 1, 3, 2, 2, 2, 4, 2, 2, 4, 3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2]}], "hoverlabel": {"namelength": 0}, "hovertemplate": "%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "", "showlegend": false, "type": "splom"}],
                        {"dragmode": "select", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('c7ea0109-f667-49fb-a093-322d0c6d3947');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter_matrix(tips, dimensions=['total_bill','tip','size'], color='sex')
```


<div>


            <div id="6c0003f8-a5d4-4bb6-b8c5-f7bd4ae8a082" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("6c0003f8-a5d4-4bb6-b8c5-f7bd4ae8a082")) {
                    Plotly.newPlot(
                        '6c0003f8-a5d4-4bb6-b8c5-f7bd4ae8a082',
                        [{"dimensions": [{"axis": {"matches": true}, "label": "total_bill", "values": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78]}, {"axis": {"matches": true}, "label": "tip", "values": [1.01, 3.61, 5.0, 3.02, 1.67, 3.5, 2.75, 2.23, 3.0, 3.0, 2.45, 3.07, 2.6, 5.2, 1.5, 2.47, 1.0, 3.0, 3.14, 5.0, 2.2, 1.83, 5.17, 1.0, 4.3, 3.25, 2.5, 3.0, 2.5, 3.48, 4.08, 4.0, 1.0, 4.0, 3.5, 1.5, 1.8, 2.92, 1.68, 2.52, 4.2, 2.0, 2.0, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.75, 3.5, 5.0, 2.3, 1.5, 1.36, 1.63, 5.14, 3.75, 2.61, 2.0, 3.0, 1.61, 2.0, 4.0, 3.5, 3.5, 4.19, 5.0, 2.0, 2.01, 2.0, 2.5, 3.23, 2.23, 2.5, 6.5, 1.1, 3.09, 3.48, 3.0, 2.5, 2.0, 2.88, 4.67, 2.0, 3.0]}, {"axis": {"matches": true}, "label": "size", "values": [2, 4, 4, 2, 3, 3, 2, 2, 2, 2, 4, 3, 2, 4, 2, 2, 1, 3, 2, 2, 2, 1, 4, 2, 2, 2, 2, 2, 3, 2, 2, 2, 1, 3, 2, 2, 2, 4, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 3, 2, 5, 4, 2, 3, 2, 2, 2, 2, 3, 3, 2, 4, 2, 2, 2, 2, 3, 2, 2, 3, 2, 4, 2, 3, 2, 2, 2, 3, 2, 2]}], "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "sex=Female", "showlegend": true, "type": "splom"}, {"dimensions": [{"axis": {"matches": true}, "label": "total_bill", "values": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82]}, {"axis": {"matches": true}, "label": "tip", "values": [1.66, 3.5, 3.31, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 1.57, 3.0, 3.92, 3.71, 3.35, 4.08, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 1.45, 2.5, 3.27, 3.6, 2.0, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 1.56, 4.34, 3.51, 3.0, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.01, 2.09, 1.97, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 5.0, 2.03, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 4.73, 4.0, 1.5, 3.0, 1.5, 1.64, 4.06, 4.29, 3.76, 3.0, 4.0, 2.55, 5.07, 2.31, 2.5, 2.0, 1.48, 2.18, 1.5, 2.0, 6.7, 5.0, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.0, 2.0, 3.5, 2.5, 2.0, 3.48, 2.24, 4.5, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 2.0, 4.0, 1.5, 2.56, 2.02, 4.0, 1.44, 2.0, 2.0, 4.0, 4.0, 3.41, 3.0, 2.03, 2.0, 5.16, 9.0, 3.0, 1.5, 1.44, 2.2, 1.92, 1.58, 3.0, 2.72, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 5.92, 2.0, 1.75]}, {"axis": {"matches": true}, "label": "size", "values": [3, 3, 2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 3, 3, 2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 3, 3, 3, 3, 3, 2, 2, 2, 4, 2, 2, 4, 3, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 3, 3, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 4, 2, 2, 2, 2, 3, 2, 2, 6, 5, 2, 2, 2, 2, 3, 4, 4, 6, 4, 4, 2, 2, 3, 2, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 3, 4, 2, 5, 5, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 3, 4, 2, 3, 4, 4, 5, 2, 2, 2, 1, 2, 4, 2, 4, 3, 2, 2, 2, 2, 2, 2, 3, 2, 2]}], "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>%{xaxis.title.text}=%{x}<br>%{yaxis.title.text}=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "name": "sex=Male", "showlegend": true, "type": "splom"}],
                        {"dragmode": "select", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('6c0003f8-a5d4-4bb6-b8c5-f7bd4ae8a082');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### HeatMap


```python
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Matriz de correlacion de los datos
tips.corr()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
      <td>0.598315</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
      <td>0.489299</td>
    </tr>
    <tr>
      <th>size</th>
      <td>0.598315</td>
      <td>0.489299</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Este grafico usa plotly de forma diferente
import plotly.figure_factory as ff

correlation = tips.corr().values # obtener los numeros de la correlacion
names = list(tips.corr().columns.values) # obtener los nombres de las columnas
transposed_corr = correlation[::-1] # es necesario transponer la matriz
```


```python
ff.create_annotated_heatmap(transposed_corr, x = names,y = names[::-1], colorscale='Viridis')
```


<div>


            <div id="b8d85490-9be5-439b-a95f-916c17d5d573" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("b8d85490-9be5-439b-a95f-916c17d5d573")) {
                    Plotly.newPlot(
                        'b8d85490-9be5-439b-a95f-916c17d5d573',
                        [{"colorscale": [[0.0, "#440154"], [0.1111111111111111, "#482878"], [0.2222222222222222, "#3e4989"], [0.3333333333333333, "#31688e"], [0.4444444444444444, "#26828e"], [0.5555555555555556, "#1f9e89"], [0.6666666666666666, "#35b779"], [0.7777777777777778, "#6ece58"], [0.8888888888888888, "#b5de2b"], [1.0, "#fde725"]], "reversescale": false, "showscale": false, "type": "heatmap", "x": ["total_bill", "tip", "size"], "y": ["size", "tip", "total_bill"], "z": [[0.5983151309049025, 0.48929877523035775, 1.0], [0.6757341092113642, 1.0, 0.48929877523035775], [1.0, 0.6757341092113642, 0.5983151309049025]]}],
                        {"annotations": [{"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.5983151309049025", "x": "total_bill", "xref": "x", "y": "size", "yref": "y"}, {"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.48929877523035775", "x": "tip", "xref": "x", "y": "size", "yref": "y"}, {"font": {"color": "#000000"}, "showarrow": false, "text": "1.0", "x": "size", "xref": "x", "y": "size", "yref": "y"}, {"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.6757341092113642", "x": "total_bill", "xref": "x", "y": "tip", "yref": "y"}, {"font": {"color": "#000000"}, "showarrow": false, "text": "1.0", "x": "tip", "xref": "x", "y": "tip", "yref": "y"}, {"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.48929877523035775", "x": "size", "xref": "x", "y": "tip", "yref": "y"}, {"font": {"color": "#000000"}, "showarrow": false, "text": "1.0", "x": "total_bill", "xref": "x", "y": "total_bill", "yref": "y"}, {"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.6757341092113642", "x": "tip", "xref": "x", "y": "total_bill", "yref": "y"}, {"font": {"color": "#FFFFFF"}, "showarrow": false, "text": "0.5983151309049025", "x": "size", "xref": "x", "y": "total_bill", "yref": "y"}], "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"dtick": 1, "gridcolor": "rgb(0, 0, 0)", "side": "top", "ticks": ""}, "yaxis": {"dtick": 1, "ticks": "", "ticksuffix": "  "}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('b8d85490-9be5-439b-a95f-916c17d5d573');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


## Animaciones con  Plotly


```python
px.scatter(gapminder, x="gdpPercap", y="lifeExp",
           animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
```


<div>


            <div id="53d845cb-b495-4874-9d46-2075a1cc372c" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("53d845cb-b495-4874-9d46-2075a1cc372c")) {
                    Plotly.newPlot(
                        '53d845cb-b495-4874-9d46-2075a1cc372c',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [8425333, 120447, 46886859, 4693836, 556263527, 2125900, 372000000, 82052000, 17272000, 5441766, 1620914, 86459025, 607914, 8865488, 20947571, 160000, 1439529, 6748378, 800663, 20092996, 9182536, 507833, 41346560, 22438691, 4005677, 1127000, 7982342, 3661549, 8550362, 21289402, 26246839, 1030585, 4963829], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [779.4453145, 9867.084765000001, 684.2441716, 368.46928560000003, 400.44861099999997, 3054.421209, 546.5657493, 749.6816546, 3035.326002, 4129.766056, 4086.522128, 3216.956347, 1546.907807, 1088.277758, 1030.592226, 108382.3529, 4834.804067, 1831.132894, 786.5668575, 331.0, 545.8657228999999, 1828.230307, 684.5971437999999, 1272.880995, 6459.5548229999995, 2315.138227, 1083.53203, 1643.485354, 1206.947913, 757.7974177, 605.0664917, 1515.5923289999998, 781.7175761], "xaxis": "x", "y": [28.801, 50.93899999999999, 37.484, 39.417, 44.0, 60.96, 37.373000000000005, 37.468, 44.869, 45.32, 65.39, 63.03, 43.158, 50.056000000000004, 47.453, 55.565, 55.928000000000004, 48.463, 42.244, 36.319, 36.157, 37.578, 43.43600000000001, 47.751999999999995, 39.875, 60.396, 57.593, 45.883, 58.5, 50.848, 40.412, 43.16, 32.548], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1282697, 6927772, 8730405, 2791000, 7274900, 3882229, 9125183, 4334000, 4090500, 42459667, 69145952, 7733250, 9504000, 147962, 2952156, 47666000, 413834, 10381988, 3327728, 25730551, 8526050, 16630000, 6860147, 3558137, 1489518, 28549870, 7124673, 4815000, 22235677, 50430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [1601.056136, 6137.076492, 8343.105126999999, 973.5331947999999, 2444.2866480000002, 3119.23652, 6876.14025, 9692.385245, 6424.519071, 7029.809327, 7144.114393000001, 3530.690067, 5263.6738159999995, 7267.688428, 5210.280328, 4931.404154999999, 2647.585601, 8941.571858, 10095.42172, 4029.3296990000003, 3068.319867, 3144.613186, 3581.4594479999996, 5074.659104, 4215.041741, 3834.0347420000003, 8527.844662000001, 14734.23275, 1969.1009800000002, 9979.508487000001], "xaxis": "x", "y": [55.23, 66.8, 68.0, 53.82, 59.6, 61.21, 66.87, 70.78, 66.55, 67.41, 67.5, 65.86, 64.03, 72.49, 66.91, 65.94, 59.163999999999994, 72.13, 72.67, 61.31, 59.82, 61.05, 57.996, 64.36, 65.57, 64.94, 71.86, 69.62, 43.585, 69.18], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [9279525, 4232095, 1738315, 442308, 4469979, 2445618, 5009067, 1291695, 2682462, 153936, 14100005, 854885, 2977019, 63149, 22223309, 216964, 1438760, 20860941, 420702, 284320, 5581001, 2664249, 580653, 6464046, 748747, 863308, 1019729, 4762912, 2917802, 3838168, 1022556, 516556, 9939217, 6446316, 485831, 3379468, 33119096, 257700, 2534927, 60011, 2755589, 2143249, 2526994, 14264935, 8504667, 290243, 8322925, 1219113, 3647735, 5824797, 2672000, 3080907], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [2449.008185, 3520.610273, 1062.7522, 851.2411407, 543.2552413, 339.29645869999996, 1172.667655, 1071.310713, 1178.665927, 1102.990936, 780.5423257, 2125.621418, 1388.594732, 2669.529475, 1418.822445, 375.6431231, 328.94055710000004, 362.1462796, 4293.476475, 485.2306591, 911.2989371, 510.19649230000005, 299.850319, 853.5409189999999, 298.8462121, 575.5729961000001, 2387.54806, 1443.011715, 369.1650802, 452.3369807, 743.1159097, 1967.955707, 1688.20357, 468.5260381, 2423.780443, 761.879376, 1077.281856, 2718.885295, 493.32387520000003, 879.5835855, 1450.356983, 879.7877358, 1135.749842, 4725.295531000001, 1615.991129, 1148.376626, 716.6500721, 859.8086567, 1468.475631, 734.753484, 1147.388831, 406.8841148], "xaxis": "x", "y": [43.077, 30.015, 38.223, 47.622, 31.975, 39.031, 38.523, 35.463, 38.092, 40.715, 39.143, 42.111000000000004, 40.477, 34.812, 41.893, 34.482, 35.928000000000004, 34.078, 37.003, 30.0, 43.148999999999994, 33.609, 32.5, 42.27, 42.138000000000005, 38.48, 42.723, 36.681, 36.256, 33.685, 40.543, 50.986000000000004, 42.873000000000005, 31.285999999999998, 41.725, 37.444, 36.324, 52.724, 40.0, 46.471000000000004, 37.278, 30.331, 32.978, 45.00899999999999, 38.635, 41.407, 41.215, 38.596, 44.6, 39.978, 42.038000000000004, 48.451], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [17876956, 2883315, 56602560, 14785584, 6377619, 12350771, 926317, 6007797, 2491346, 3548753, 2042865, 3146381, 3201488, 1517453, 1426095, 30144317, 1165790, 940080, 1555876, 8025700, 2227000, 662850, 157553000, 2252965, 5439568], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [5911.315053, 2677.3263469999997, 2108.944355, 11367.16112, 3939.9787890000002, 2144.115096, 2627.0094710000003, 5586.53878, 1397.7171369999999, 3522.110717, 3048.3029, 2428.2377690000003, 1840.366939, 2194.926204, 2898.5308809999997, 3478.125529, 3112.363948, 2480.380334, 1952.3087010000002, 3758.523437, 3081.959785, 3023.271928, 13990.482080000002, 5716.766744, 7689.799761], "xaxis": "x", "y": [62.485, 40.414, 50.917, 68.75, 54.745, 50.643, 57.206, 59.42100000000001, 45.928000000000004, 48.357, 45.262, 42.023, 37.579, 41.912, 58.53, 50.788999999999994, 42.31399999999999, 55.191, 62.648999999999994, 43.902, 64.28, 59.1, 68.44, 66.071, 55.088], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [8691212, 1994794], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [10039.595640000001, 10556.575659999999], "xaxis": "x", "y": [69.12, 69.39], "yaxis": "y"}],
                        {"height": 600, "legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "sliders": [{"active": 0, "currentvalue": {"prefix": "year="}, "len": 0.9, "pad": {"b": 10, "t": 60}, "steps": [{"args": [["1952"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1952", "method": "animate"}, {"args": [["1957"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1957", "method": "animate"}, {"args": [["1962"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1962", "method": "animate"}, {"args": [["1967"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1967", "method": "animate"}, {"args": [["1972"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1972", "method": "animate"}, {"args": [["1977"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1977", "method": "animate"}, {"args": [["1982"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1982", "method": "animate"}, {"args": [["1987"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1987", "method": "animate"}, {"args": [["1992"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1992", "method": "animate"}, {"args": [["1997"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1997", "method": "animate"}, {"args": [["2002"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "2002", "method": "animate"}, {"args": [["2007"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "2007", "method": "animate"}], "x": 0.1, "xanchor": "left", "y": 0, "yanchor": "top"}], "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "updatemenus": [{"buttons": [{"args": [null, {"frame": {"duration": 500, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 500, "easing": "linear"}}], "label": "&#9654;", "method": "animate"}, {"args": [[null], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "&#9724;", "method": "animate"}], "direction": "left", "pad": {"r": 10, "t": 70}, "showactive": false, "type": "buttons", "x": 0.1, "xanchor": "right", "y": 0, "yanchor": "top"}], "xaxis": {"anchor": "y", "domain": [0.0, 0.98], "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "range": [25, 90], "title": {"text": "lifeExp"}}},
                        {"responsive": true}
                    ).then(function(){
                            Plotly.addFrames('53d845cb-b495-4874-9d46-2075a1cc372c', [{"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [8425333, 120447, 46886859, 4693836, 556263527, 2125900, 372000000, 82052000, 17272000, 5441766, 1620914, 86459025, 607914, 8865488, 20947571, 160000, 1439529, 6748378, 800663, 20092996, 9182536, 507833, 41346560, 22438691, 4005677, 1127000, 7982342, 3661549, 8550362, 21289402, 26246839, 1030585, 4963829], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [779.4453145, 9867.084765000001, 684.2441716, 368.46928560000003, 400.44861099999997, 3054.421209, 546.5657493, 749.6816546, 3035.326002, 4129.766056, 4086.522128, 3216.956347, 1546.907807, 1088.277758, 1030.592226, 108382.3529, 4834.804067, 1831.132894, 786.5668575, 331.0, 545.8657228999999, 1828.230307, 684.5971437999999, 1272.880995, 6459.5548229999995, 2315.138227, 1083.53203, 1643.485354, 1206.947913, 757.7974177, 605.0664917, 1515.5923289999998, 781.7175761], "xaxis": "x", "y": [28.801, 50.93899999999999, 37.484, 39.417, 44.0, 60.96, 37.373000000000005, 37.468, 44.869, 45.32, 65.39, 63.03, 43.158, 50.056000000000004, 47.453, 55.565, 55.928000000000004, 48.463, 42.244, 36.319, 36.157, 37.578, 43.43600000000001, 47.751999999999995, 39.875, 60.396, 57.593, 45.883, 58.5, 50.848, 40.412, 43.16, 32.548], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1282697, 6927772, 8730405, 2791000, 7274900, 3882229, 9125183, 4334000, 4090500, 42459667, 69145952, 7733250, 9504000, 147962, 2952156, 47666000, 413834, 10381988, 3327728, 25730551, 8526050, 16630000, 6860147, 3558137, 1489518, 28549870, 7124673, 4815000, 22235677, 50430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [1601.056136, 6137.076492, 8343.105126999999, 973.5331947999999, 2444.2866480000002, 3119.23652, 6876.14025, 9692.385245, 6424.519071, 7029.809327, 7144.114393000001, 3530.690067, 5263.6738159999995, 7267.688428, 5210.280328, 4931.404154999999, 2647.585601, 8941.571858, 10095.42172, 4029.3296990000003, 3068.319867, 3144.613186, 3581.4594479999996, 5074.659104, 4215.041741, 3834.0347420000003, 8527.844662000001, 14734.23275, 1969.1009800000002, 9979.508487000001], "xaxis": "x", "y": [55.23, 66.8, 68.0, 53.82, 59.6, 61.21, 66.87, 70.78, 66.55, 67.41, 67.5, 65.86, 64.03, 72.49, 66.91, 65.94, 59.163999999999994, 72.13, 72.67, 61.31, 59.82, 61.05, 57.996, 64.36, 65.57, 64.94, 71.86, 69.62, 43.585, 69.18], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [9279525, 4232095, 1738315, 442308, 4469979, 2445618, 5009067, 1291695, 2682462, 153936, 14100005, 854885, 2977019, 63149, 22223309, 216964, 1438760, 20860941, 420702, 284320, 5581001, 2664249, 580653, 6464046, 748747, 863308, 1019729, 4762912, 2917802, 3838168, 1022556, 516556, 9939217, 6446316, 485831, 3379468, 33119096, 257700, 2534927, 60011, 2755589, 2143249, 2526994, 14264935, 8504667, 290243, 8322925, 1219113, 3647735, 5824797, 2672000, 3080907], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [2449.008185, 3520.610273, 1062.7522, 851.2411407, 543.2552413, 339.29645869999996, 1172.667655, 1071.310713, 1178.665927, 1102.990936, 780.5423257, 2125.621418, 1388.594732, 2669.529475, 1418.822445, 375.6431231, 328.94055710000004, 362.1462796, 4293.476475, 485.2306591, 911.2989371, 510.19649230000005, 299.850319, 853.5409189999999, 298.8462121, 575.5729961000001, 2387.54806, 1443.011715, 369.1650802, 452.3369807, 743.1159097, 1967.955707, 1688.20357, 468.5260381, 2423.780443, 761.879376, 1077.281856, 2718.885295, 493.32387520000003, 879.5835855, 1450.356983, 879.7877358, 1135.749842, 4725.295531000001, 1615.991129, 1148.376626, 716.6500721, 859.8086567, 1468.475631, 734.753484, 1147.388831, 406.8841148], "xaxis": "x", "y": [43.077, 30.015, 38.223, 47.622, 31.975, 39.031, 38.523, 35.463, 38.092, 40.715, 39.143, 42.111000000000004, 40.477, 34.812, 41.893, 34.482, 35.928000000000004, 34.078, 37.003, 30.0, 43.148999999999994, 33.609, 32.5, 42.27, 42.138000000000005, 38.48, 42.723, 36.681, 36.256, 33.685, 40.543, 50.986000000000004, 42.873000000000005, 31.285999999999998, 41.725, 37.444, 36.324, 52.724, 40.0, 46.471000000000004, 37.278, 30.331, 32.978, 45.00899999999999, 38.635, 41.407, 41.215, 38.596, 44.6, 39.978, 42.038000000000004, 48.451], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [17876956, 2883315, 56602560, 14785584, 6377619, 12350771, 926317, 6007797, 2491346, 3548753, 2042865, 3146381, 3201488, 1517453, 1426095, 30144317, 1165790, 940080, 1555876, 8025700, 2227000, 662850, 157553000, 2252965, 5439568], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [5911.315053, 2677.3263469999997, 2108.944355, 11367.16112, 3939.9787890000002, 2144.115096, 2627.0094710000003, 5586.53878, 1397.7171369999999, 3522.110717, 3048.3029, 2428.2377690000003, 1840.366939, 2194.926204, 2898.5308809999997, 3478.125529, 3112.363948, 2480.380334, 1952.3087010000002, 3758.523437, 3081.959785, 3023.271928, 13990.482080000002, 5716.766744, 7689.799761], "xaxis": "x", "y": [62.485, 40.414, 50.917, 68.75, 54.745, 50.643, 57.206, 59.42100000000001, 45.928000000000004, 48.357, 45.262, 42.023, 37.579, 41.912, 58.53, 50.788999999999994, 42.31399999999999, 55.191, 62.648999999999994, 43.902, 64.28, 59.1, 68.44, 66.071, 55.088], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [8691212, 1994794], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [10039.595640000001, 10556.575659999999], "xaxis": "x", "y": [69.12, 69.39], "yaxis": "y", "type": "scatter"}], "name": "1952"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [9240934, 138655, 51365468, 5322536, 637408000, 2736300, 409000000, 90124000, 19792000, 6248643, 1944401, 91563009, 746559, 9411381, 22611552, 212846, 1647412, 7739235, 882134, 21731844, 9682338, 561977, 46679944, 26072194, 4419650, 1445929, 9128546, 4149908, 10164215, 25041917, 28998543, 1070439, 5498090], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [820.8530296, 11635.79945, 661.6374577, 434.0383364, 575.9870009, 3629.076457, 590.061996, 858.9002707000001, 3290.257643, 6229.333562, 5385.278451, 4317.694365, 1886.080591, 1571.134655, 1487.593537, 113523.1329, 6089.786934000001, 1810.0669920000003, 912.6626085, 350.0, 597.9363557999999, 2242.746551, 747.0835292, 1547.9448439999999, 8157.591248000001, 2843.104409, 1072.546602, 2117.234893, 1507.86129, 793.5774147999999, 676.2854477999999, 1827.0677420000002, 804.8304547], "xaxis": "x", "y": [30.331999999999997, 53.832, 39.348, 41.36600000000001, 50.54896, 64.75, 40.249, 39.918, 47.181000000000004, 48.437, 67.84, 65.5, 45.669, 54.081, 52.681000000000004, 58.033, 59.489, 52.102, 45.248000000000005, 41.905, 37.686, 40.08, 45.556999999999995, 51.333999999999996, 42.868, 63.178999999999995, 61.456, 48.284, 62.4, 53.63, 42.887, 45.67100000000001, 33.97], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1476505, 6965860, 8989111, 3076000, 7651254, 3991242, 9513758, 4487831, 4324000, 44310863, 71019069, 8096218, 9839000, 165110, 2878220, 49182000, 442829, 11026383, 3491938, 28235346, 8817650, 17829327, 7271135, 3844277, 1533070, 29841614, 7363802, 5126000, 25670939, 51430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [1942.2842440000002, 8842.59803, 9714.960623, 1353.989176, 3008.670727, 4338.231617, 8256.343918, 11099.65935, 7545.415386, 8662.834898000001, 10187.82665, 4916.299889, 6040.180011, 9244.001412, 5599.077872, 6248.656232, 3682.259903, 11276.193440000001, 11653.97304, 4734.253019, 3774.571743, 3943.370225, 4981.090891, 6093.2629799999995, 5862.276629, 4564.80241, 9911.878226, 17909.48973, 2218.754257, 11283.17795], "xaxis": "x", "y": [59.28, 67.48, 69.24, 58.45, 66.61, 64.77, 69.03, 71.81, 67.49, 68.93, 69.1, 67.86, 66.41, 73.47, 68.9, 67.81, 61.448, 72.99, 73.44, 65.77, 61.51, 64.1, 61.685, 67.45, 67.85, 66.66, 72.49, 70.56, 48.07899999999999, 70.42], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [10270856, 4561361, 1925173, 474639, 4713416, 2667518, 5359923, 1392284, 2894855, 170928, 15577932, 940458, 3300000, 71851, 25009741, 232922, 1542611, 22815614, 434904, 323150, 6391288, 2876726, 601095, 7454779, 813338, 975950, 1201578, 5181679, 3221238, 4241884, 1076852, 609816, 11406350, 7038035, 548080, 3692184, 37173340, 308700, 2822082, 61325, 3054547, 2295678, 2780415, 16151549, 9753392, 326741, 9452826, 1357445, 3950849, 6675501, 3016000, 3646340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [3013.976023, 3827.9404649999997, 959.6010805, 918.2325348999999, 617.1834647999999, 379.56462810000005, 1313.048099, 1190.844328, 1308.495577, 1211.1485480000001, 905.8602302999999, 2315.056572, 1500.895925, 2864.9690760000003, 1458.915272, 426.0964081, 344.16188589999996, 378.90416319999997, 4976.198099, 520.9267111, 1043.5615369999998, 576.2670245, 431.7904566000001, 944.4383152, 335.99711510000003, 620.9699901, 3448.284395, 1589.20275, 416.36980639999996, 490.3821867, 846.1202613, 2034.037981, 1642.002314, 495.5868333000001, 2621.448058, 835.5234025000001, 1100.5925630000002, 2769.451844, 540.2893982999999, 860.7369026, 1567.653006, 1004.484437, 1258.1474130000001, 5487.104219, 1770.3370739999998, 1244.708364, 698.5356073, 925.9083201999999, 1395.232468, 774.3710692000001, 1311.956766, 518.7642681], "xaxis": "x", "y": [45.685, 31.999000000000002, 40.358000000000004, 49.618, 34.906, 40.533, 40.428000000000004, 37.464, 39.881, 42.46, 40.652, 45.053000000000004, 42.468999999999994, 37.328, 44.443999999999996, 35.983000000000004, 38.047, 36.667, 38.999, 32.065, 44.778999999999996, 34.558, 33.489000000000004, 44.68600000000001, 45.047, 39.486, 45.288999999999994, 38.865, 37.207, 35.306999999999995, 42.338, 58.089, 45.423, 33.779, 45.226000000000006, 38.598, 37.802, 55.09, 41.5, 48.945, 39.329, 31.57, 34.977, 47.985, 39.624, 43.424, 42.974, 41.208, 47.1, 42.571000000000005, 44.077, 50.468999999999994], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [19610538, 3211738, 65551171, 17010154, 7048426, 14485993, 1112300, 6640752, 2923186, 4058385, 2355805, 3640876, 3507701, 1770390, 1535090, 35015548, 1358828, 1063506, 1770902, 9146100, 2260000, 764900, 171984000, 2424959, 6702668], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [6856.856212000001, 2127.686326, 2487.365989, 12489.95006, 4315.6227229999995, 2323.805581, 2990.010802, 6092.174359000001, 1544.402995, 3780.5466509999997, 3421.523218, 2617.155967, 1726.887882, 2220.487682, 4756.525781, 4131.546641, 3457.415947, 2961.800905, 2046.1547059999998, 4245.256697999999, 3907.1561890000003, 4100.3934, 14847.12712, 6150.772969, 9802.466526], "xaxis": "x", "y": [64.399, 41.89, 53.285, 69.96, 56.074, 55.118, 60.026, 62.325, 49.828, 51.356, 48.57, 44.141999999999996, 40.696, 44.665, 62.61, 55.19, 45.431999999999995, 59.201, 63.196000000000005, 46.263000000000005, 68.54, 61.8, 69.49, 67.044, 57.907], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [9712569, 2229407], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [10949.64959, 12247.39532], "xaxis": "x", "y": [70.33, 70.26], "yaxis": "y", "type": "scatter"}], "name": "1957"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [10267083, 171863, 56839289, 6083619, 665770000, 3305200, 454000000, 99028000, 22874000, 7240260, 2310904, 95831757, 933559, 10917494, 26420307, 358266, 1886848, 8906385, 1010280, 23634436, 10332057, 628164, 53100671, 30325264, 4943029, 1750200, 10421936, 4834621, 11918938, 29263397, 33796140, 1133134, 6120081], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [853.1007099999999, 12753.27514, 686.3415537999999, 496.9136476, 487.6740183, 4692.648271999999, 658.3471509, 849.2897700999999, 4187.329802, 8341.737815, 7105.630706, 6576.649461, 2348.009158, 1621.693598, 1536.3443869999999, 95458.11176, 5714.560611, 2036.8849440000001, 1056.353958, 388.0, 652.3968593, 2924.638113, 803.3427418, 1649.5521529999999, 11626.41975, 3674.735572, 1074.4719599999999, 2193.037133, 1822.879028, 1002.1991720000001, 772.0491602000001, 2198.9563120000003, 825.6232006], "xaxis": "x", "y": [31.997, 56.923, 41.216, 43.415, 44.50136, 67.65, 43.605, 42.518, 49.325, 51.457, 69.39, 68.73, 48.126000000000005, 56.656000000000006, 55.292, 60.47, 62.093999999999994, 55.736999999999995, 48.251000000000005, 45.108000000000004, 39.393, 43.165, 47.67, 54.757, 45.913999999999994, 65.798, 62.192, 50.305, 65.2, 56.06100000000001, 45.363, 48.126999999999995, 35.18], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1728137, 7129864, 9218400, 3349000, 8012946, 4076557, 9620282, 4646899, 4491443, 47124000, 73739117, 8448233, 10063000, 182053, 2830000, 50843200, 474528, 11805689, 3638919, 30329617, 9019800, 18680721, 7616060, 4237384, 1582962, 31158061, 7561588, 5666000, 29788695, 53292000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2312.888958, 10750.721109999999, 10991.20676, 1709.683679, 4254.337839, 5477.890018, 10136.86713, 13583.31351, 9371.842561, 10560.48553, 12902.46291, 6017.190732999999, 7550.359877, 10350.15906, 6631.597314, 8243.58234, 4649.593785, 12790.849559999999, 13450.40151, 5338.752143, 4727.954889, 4734.9975859999995, 6289.629157, 7481.1075980000005, 7402.303395, 5693.843879, 12329.441920000001, 20431.0927, 2322.8699079999997, 12477.17707], "xaxis": "x", "y": [64.82, 69.54, 70.25, 61.93, 69.51, 67.13, 69.9, 72.35, 68.75, 70.51, 70.3, 69.51, 67.96, 73.68, 70.29, 69.24, 63.728, 73.23, 73.47, 67.64, 64.39, 66.8, 64.531, 70.33, 69.15, 69.69, 73.37, 71.32, 52.098, 70.76], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [11000948, 4826015, 2151895, 512764, 4919632, 2961915, 5793633, 1523478, 3150417, 191689, 17486434, 1047924, 3832408, 89898, 28173309, 249220, 1666618, 25145372, 455661, 374020, 7355248, 3140003, 627820, 8678557, 893143, 1112796, 1441863, 5703324, 3628608, 4690372, 1146757, 701016, 13056604, 7788944, 621392, 4076008, 41871351, 358900, 3051242, 65345, 3430243, 2467895, 3080153, 18356657, 11183227, 370006, 10863958, 1528098, 4286552, 7688797, 3421000, 4277736], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [2550.81688, 4269.276742, 949.4990641, 983.6539764, 722.5120206, 355.2032273, 1399.607441, 1193.068753, 1389.817618, 1406.648278, 896.3146335000001, 2464.783157, 1728.8694280000002, 3020.989263, 1693.335853, 582.8419713999999, 380.99584330000005, 419.4564161, 6631.4592219999995, 599.650276, 1190.0411179999999, 686.3736739, 522.0343725, 896.9663732, 411.80062660000004, 634.1951625, 6757.0308159999995, 1643.38711, 427.90108560000004, 496.17434280000003, 1055.8960359999999, 2529.0674870000003, 1566.353493, 556.6863539, 3173.215595, 997.7661127, 1150.9274779999998, 3173.72334, 597.4730727000001, 1071.551119, 1654.988723, 1116.6398769999998, 1369.488336, 5768.729717, 1959.593767, 1856.182125, 722.0038073, 1067.5348099999999, 1660.30321, 767.2717397999999, 1452.725766, 527.2721818], "xaxis": "x", "y": [48.303000000000004, 34.0, 42.618, 51.52, 37.814, 42.045, 42.643, 39.475, 41.716, 44.467, 42.122, 48.435, 44.93, 39.693000000000005, 46.992, 37.485, 40.158, 40.059, 40.489000000000004, 33.896, 46.452, 35.753, 34.488, 47.949, 47.747, 40.501999999999995, 47.808, 40.848, 38.41, 36.936, 44.248000000000005, 60.246, 47.924, 36.161, 48.386, 39.486999999999995, 39.36, 57.666000000000004, 43.0, 51.893, 41.45399999999999, 32.766999999999996, 36.981, 49.951, 40.87, 44.992, 44.246, 43.922, 49.57899999999999, 45.343999999999994, 46.023, 52.358000000000004], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [21283783, 3593918, 76039390, 18985849, 7961258, 17009885, 1345187, 7254373, 3453434, 4681707, 2747687, 4208858, 3880130, 2090162, 1665128, 41121485, 1590597, 1215725, 2009813, 10516500, 2448046, 887498, 186538000, 2598466, 8143375], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [7133.166023000001, 2180.972546, 3336.585802, 13462.48555, 4519.094331, 2492.351109, 3460.937025, 5180.75591, 1662.137359, 4086.114078, 3776.8036270000002, 2750.364446, 1796.589032, 2291.1568350000002, 5246.107524, 4581.609385, 3634.364406, 3536.540301, 2148.027146, 4957.037982, 5108.34463, 4997.5239710000005, 16173.145859999999, 5603.357717, 8422.974165000001], "xaxis": "x", "y": [65.142, 43.428000000000004, 55.665, 71.3, 57.924, 57.863, 62.842, 65.24600000000001, 53.458999999999996, 54.64, 52.306999999999995, 46.95399999999999, 43.59, 48.041000000000004, 65.61, 58.299, 48.632, 61.817, 64.361, 49.096000000000004, 69.62, 64.9, 70.21, 68.253, 60.77], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [10794968, 2488550], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [12217.226859999999, 13175.678], "xaxis": "x", "y": [70.93, 71.24], "yaxis": "y", "type": "scatter"}], "name": "1962"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [11537966, 202182, 62821884, 6960067, 754550000, 3722800, 506000000, 109343000, 26538000, 8519282, 2693585, 100825279, 1255058, 12617009, 30131000, 575003, 2186894, 10154878, 1149500, 25870271, 11261690, 714775, 60641899, 35356600, 5618198, 1977600, 11737396, 5680812, 13648692, 34024249, 39463910, 1142636, 6740785], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [836.1971382, 14804.6727, 721.1860862000001, 523.4323142, 612.7056934, 6197.962814, 700.7706107000001, 762.4317721, 5906.731804999999, 8931.459811, 8393.741404, 9847.788606999999, 2741.796252, 2143.540609, 2029.2281420000002, 80894.88326, 6006.983042, 2277.742396, 1226.04113, 349.0, 676.4422254, 4720.942687, 942.4082588, 1814.12743, 16903.04886, 4977.41854, 1135.514326, 1881.923632, 2643.8586809999997, 1295.46066, 637.1232887, 2649.7150070000002, 862.4421463], "xaxis": "x", "y": [34.02, 59.923, 43.453, 45.415, 58.381119999999996, 70.0, 47.193000000000005, 45.964, 52.468999999999994, 54.458999999999996, 70.75, 71.43, 51.629, 59.942, 57.716, 64.624, 63.87, 59.371, 51.253, 49.379, 41.472, 46.988, 49.8, 56.393, 49.901, 67.946, 64.266, 53.655, 67.5, 58.285, 47.838, 51.631, 36.984], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1984060, 7376998, 9556500, 3585000, 8310226, 4174366, 9835109, 4838800, 4605744, 49569000, 76368453, 8716441, 10223422, 198676, 2900100, 52667100, 501035, 12596822, 3786019, 31785378, 9103000, 19284814, 7971222, 4442238, 1646912, 32850275, 7867931, 6063000, 33411317, 54959000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2760.196931, 12834.6024, 13149.04119, 2172.3524230000003, 5577.0028, 6960.297861, 11399.44489, 15937.21123, 10921.63626, 12999.91766, 14745.62561, 8513.097016, 9326.64467, 13319.89568, 7655.568963, 10022.40131, 5907.850937, 15363.25136, 16361.87647, 6557.152776, 6361.517993, 6470.866545, 7991.707066, 8412.902397, 9405.489397, 7993.512294, 15258.29697, 22966.14432, 2826.3563870000003, 14142.85089], "xaxis": "x", "y": [66.22, 70.14, 70.94, 64.79, 70.42, 68.5, 70.38, 72.96, 69.83, 71.55, 70.8, 71.0, 69.5, 73.73, 71.08, 71.06, 67.178, 73.82, 74.08, 69.61, 66.6, 66.8, 66.914, 70.98, 69.18, 71.44, 74.16, 72.77, 54.336000000000006, 71.36], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [12760499, 5247469, 2427334, 553541, 5127935, 3330989, 6335506, 1733638, 3495967, 217378, 19941073, 1179760, 4744870, 127617, 31681188, 259864, 1820319, 27860297, 489004, 439593, 8490213, 3451418, 601287, 10191512, 996380, 1279406, 1759224, 6334556, 4147252, 5212416, 1230542, 789309, 14770296, 8680909, 706640, 4534062, 47287752, 414024, 3451079, 70787, 3965841, 2662190, 3428839, 20997321, 12716129, 420690, 12607312, 1735550, 4786986, 8900294, 3900000, 4995432], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [3246.991771, 5522.776375, 1035.831411, 1214.709294, 794.8265597, 412.97751360000007, 1508.453148, 1136.056615, 1196.810565, 1876.029643, 861.5932424, 2677.9396420000003, 2052.0504730000002, 3020.0505129999997, 1814.880728, 915.5960025, 468.7949699, 516.1186438, 8358.761987, 734.7829124, 1125.69716, 708.7595409, 715.5806402000001, 1056.736457, 498.63902649999994, 713.6036482999999, 18772.75169, 1634.047282, 495.5147806, 545.0098873, 1421.145193, 2475.387562, 1711.04477, 566.6691539, 3793.694753, 1054.384891, 1014.5141039999999, 4021.1757390000002, 510.9637142, 1384.840593, 1612.404632, 1206.043465, 1284.7331800000002, 7114.477970999999, 1687.997641, 2613.1016649999997, 848.2186575, 1477.59676, 1932.3601670000003, 908.9185217, 1777.0773179999999, 569.7950712], "xaxis": "x", "y": [51.407, 35.985, 44.885, 53.298, 40.696999999999996, 43.548, 44.799, 41.478, 43.601000000000006, 46.472, 44.056000000000004, 52.04, 47.35, 42.074, 49.293, 38.986999999999995, 42.18899999999999, 42.115, 44.598, 35.857, 48.071999999999996, 37.196999999999996, 35.492, 50.653999999999996, 48.492, 41.536, 50.227, 42.881, 39.486999999999995, 38.486999999999995, 46.288999999999994, 61.556999999999995, 50.335, 38.113, 51.159, 40.118, 41.04, 60.542, 44.1, 54.425, 43.563, 34.113, 38.977, 51.927, 42.858000000000004, 46.633, 45.757, 46.769, 52.053000000000004, 48.051, 47.768, 53.995], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [22934225, 4040665, 88049823, 20819767, 8858908, 19764027, 1588717, 8139332, 4049146, 5432424, 3232927, 4690773, 4318137, 2500689, 1861096, 47995559, 1865490, 1405486, 2287985, 12132200, 2648961, 960155, 198712000, 2748579, 9709552], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8052.953020999999, 2586.886053, 3429.864357, 16076.58803, 5106.654313, 2678.729839, 4161.727834, 5690.268015, 1653.7230029999998, 4579.074215, 4358.595393, 3242.5311469999997, 1452.057666, 2538.269358, 6124.703450999999, 5754.733883, 4643.393534000001, 4421.009084, 2299.376311, 5788.09333, 6929.277714, 5621.368472, 19530.365569999998, 5444.61962, 9541.474188], "xaxis": "x", "y": [65.634, 45.032, 57.632, 72.13, 60.523, 59.963, 65.42399999999999, 68.29, 56.751000000000005, 56.678000000000004, 55.855, 50.016000000000005, 46.243, 50.924, 67.51, 60.11, 51.88399999999999, 64.071, 64.95100000000001, 51.445, 71.1, 65.4, 70.76, 68.468, 63.479], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [11872264, 2728150], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [14526.12465, 14463.918930000002], "xaxis": "x", "y": [71.1, 71.52], "yaxis": "y", "type": "scatter"}], "name": "1967"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [13079460, 230800, 70759295, 7450606, 862030000, 4115700, 567000000, 121282000, 30614000, 10061506, 3095893, 107188273, 1613551, 14781241, 33505000, 841934, 2680018, 11441462, 1320500, 28466390, 12412593, 829050, 69325921, 40850141, 6472756, 2152400, 13016733, 6701172, 15226039, 39276153, 44655014, 1089572, 7407075], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [739.9811057999999, 18268.65839, 630.2336265, 421.6240257, 676.9000921, 8315.928145, 724.032527, 1111.107907, 9613.818607, 9576.037596, 12786.93223, 14778.78636, 2110.856309, 3701.6215030000003, 3030.87665, 109347.867, 7486.384341, 2849.09478, 1421.741975, 357.0, 674.7881296, 10618.03855, 1049.938981, 1989.3740699999998, 24837.42865, 8597.756202, 1213.39553, 2571.423014, 4062.523897, 1524.3589359999999, 699.5016441, 3133.4092769999997, 1265.047031], "xaxis": "x", "y": [36.088, 63.3, 45.251999999999995, 40.317, 63.118880000000004, 72.0, 50.651, 49.203, 55.233999999999995, 56.95, 71.63, 73.42, 56.528, 63.983000000000004, 62.611999999999995, 67.712, 65.421, 63.01, 53.754, 53.07, 43.971000000000004, 52.143, 51.928999999999995, 58.065, 53.886, 69.521, 65.042, 57.29600000000001, 69.39, 60.405, 50.254, 56.532, 39.848], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2263554, 7544201, 9709100, 3819000, 8576200, 4225310, 9862158, 4991596, 4639657, 51732000, 78717088, 8888628, 10394091, 209275, 3024400, 54365564, 527678, 13329874, 3933004, 33039545, 8970450, 20662648, 8313288, 4593433, 1694510, 34513161, 8122293, 6401400, 37492953, 56079000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3313.422188, 16661.6256, 16672.14356, 2860.16975, 6597.494398, 9164.090127, 13108.4536, 18866.20721, 14358.8759, 16107.19171, 18016.180269999997, 12724.82957, 10168.65611, 15798.063619999999, 9530.772895999999, 12269.27378, 7778.414017, 18794.74567, 18965.05551, 8006.506993000001, 9022.247417, 8011.414401999999, 10522.067490000001, 9674.167626, 12383.4862, 10638.75131, 17832.02464, 27195.113039999997, 3450.69638, 15895.116409999999], "xaxis": "x", "y": [67.69, 70.63, 71.44, 67.45, 70.9, 69.61, 70.29, 73.47, 70.87, 72.38, 71.0, 72.34, 69.76, 74.46, 71.28, 72.19, 70.63600000000001, 73.75, 74.34, 70.85, 69.26, 69.21, 68.7, 70.35, 69.82, 73.06, 74.72, 73.78, 57.005, 72.01], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [14760787, 5894858, 2761407, 619351, 5433886, 3529983, 7021028, 1927260, 3899068, 250027, 23007669, 1340458, 6071696, 178848, 34807417, 277603, 2260187, 30770372, 537977, 517101, 9354120, 3811387, 625361, 12044785, 1116779, 1482628, 2183877, 7082430, 4730997, 5828158, 1332786, 851334, 16660670, 9809596, 821782, 5060262, 53740085, 461633, 3992121, 76595, 4588696, 2879013, 3840161, 23935810, 14597019, 480105, 14706593, 2056351, 5303507, 10190285, 4506497, 5861135], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4182.663766, 5473.288004999999, 1085.796879, 2263.6111140000003, 854.7359763000001, 464.0995039, 1684.1465280000002, 1070.013275, 1104.103987, 1937.577675, 904.8960685000001, 3213.152683, 2378.201111, 3694.2123520000005, 2024.0081469999998, 672.4122571, 514.3242081999999, 566.2439442000001, 11401.948409999999, 756.0868363, 1178.223708, 741.6662307, 820.2245876000001, 1222.359968, 496.58159220000005, 803.0054535, 21011.497209999998, 1748.562982, 584.6219709, 581.3688761, 1586.851781, 2575.4841579999998, 1930.194975, 724.9178037, 3746.080948, 954.2092363, 1698.3888379999999, 5047.658563, 590.5806637999999, 1532.985254, 1597.712056, 1353.759762, 1254.576127, 7765.962636, 1659.652775, 3364.836625, 915.9850592, 1649.660188, 2753.2859940000003, 950.735869, 1773.498265, 799.3621757999999], "xaxis": "x", "y": [54.518, 37.928000000000004, 47.013999999999996, 56.023999999999994, 43.591, 44.056999999999995, 47.049, 43.457, 45.568999999999996, 48.943999999999996, 45.989, 54.907, 49.801, 44.36600000000001, 51.137, 40.516, 44.141999999999996, 43.515, 48.69, 38.308, 49.875, 38.842, 36.486, 53.559, 49.766999999999996, 42.614, 52.773, 44.851000000000006, 41.766000000000005, 39.977, 48.437, 62.943999999999996, 52.861999999999995, 40.328, 53.867, 40.546, 42.821000000000005, 64.274, 44.6, 56.48, 45.815, 35.4, 40.973, 53.696000000000005, 45.083, 49.552, 47.62, 49.75899999999999, 55.602, 51.016000000000005, 50.107, 55.635], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [24779799, 4565872, 100840058, 22284500, 9717524, 22542890, 1834796, 8831348, 4671329, 6298651, 3790903, 5149581, 4698301, 2965146, 1997616, 55984294, 2182908, 1616384, 2614104, 13954700, 2847132, 975199, 209896000, 2829526, 11515649], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9443.038526, 2980.331339, 4985.711467, 18970.57086, 5494.024437, 3264.660041, 5118.146939, 5305.445256, 2189.874499, 5280.99471, 4520.246008, 4031.4082710000002, 1654.456946, 2529.842345, 7433.889293000001, 6809.406690000001, 4688.593267, 5364.2496630000005, 2523.337977, 5937.827283, 9123.041742, 6619.551418999999, 21806.03594, 5703.408898, 10505.25966], "xaxis": "x", "y": [67.065, 46.714, 59.504, 72.88, 63.441, 61.623000000000005, 67.84899999999999, 70.723, 59.631, 58.79600000000001, 58.207, 53.738, 48.042, 53.88399999999999, 69.0, 62.361000000000004, 55.151, 66.21600000000001, 65.815, 55.448, 72.16, 65.9, 71.34, 68.673, 65.712], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [13177000, 2929100], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [16788.62948, 16046.03728], "xaxis": "x", "y": [71.93, 71.89], "yaxis": "y", "type": "scatter"}], "name": "1972"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [14880372, 297410, 80428306, 6978607, 943455000, 4583700, 634000000, 136725000, 35480679, 11882916, 3495918, 113872473, 1937652, 16325320, 36436000, 1140357, 3115787, 12845381, 1528000, 31528087, 13933198, 1004533, 78152686, 46850962, 8128505, 2325300, 14116836, 7932503, 16785196, 44148285, 50533506, 1261091, 8403990], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [786.11336, 19340.10196, 659.8772322000001, 524.9721831999999, 741.2374699, 11186.14125, 813.3373230000001, 1382.702056, 11888.59508, 14688.235069999999, 13306.619209999999, 16610.37701, 2852.351568, 4106.301249, 4657.22102, 59265.477139999995, 8659.696836, 3827.9215710000003, 1647.511665, 371.0, 694.1124398, 11848.343920000001, 1175.921193, 2373.204287, 34167.7626, 11210.08948, 1348.775651, 3195.484582, 5596.519826, 1961.2246350000003, 713.5371196000001, 3682.8314939999996, 1829.765177], "xaxis": "x", "y": [38.438, 65.593, 46.923, 31.22, 63.96736, 73.6, 54.208, 52.702, 57.702, 60.413000000000004, 73.06, 75.38, 61.13399999999999, 67.15899999999999, 64.766, 69.343, 66.09899999999999, 65.256, 55.49100000000001, 56.059, 46.748000000000005, 57.367, 54.043, 60.06, 58.69, 70.795, 65.949, 61.195, 70.59, 62.494, 55.763999999999996, 60.765, 44.175], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2509048, 7568430, 9821800, 4086000, 8797022, 4318673, 10161915, 5088419, 4738902, 53165019, 78160773, 9308479, 10637171, 221823, 3271900, 56059245, 560073, 13852989, 4043205, 34621254, 9662600, 21658597, 8686367, 4827803, 1746919, 36439000, 8251648, 6316424, 42404033, 56179000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3533.0039100000004, 19749.4223, 19117.97448, 3528.481305, 7612.240438, 11305.38517, 14800.160619999999, 20422.9015, 15605.422830000001, 18292.635140000002, 20512.92123, 14195.524280000001, 11674.837370000001, 19654.96247, 11150.98113, 14255.98475, 9595.929904999999, 21209.0592, 23311.34939, 9508.141454, 10172.48572, 9356.39724, 12980.66956, 10922.664040000001, 15277.030169999998, 13236.92117, 18855.72521, 26982.29052, 4269.122326, 17428.74846], "xaxis": "x", "y": [68.93, 72.17, 72.8, 69.86, 70.81, 70.64, 70.71, 74.69, 72.52, 73.83, 72.5, 73.68, 69.95, 76.11, 72.03, 73.48, 73.066, 75.24, 75.37, 70.67, 70.41, 69.46, 70.3, 70.45, 70.97, 74.39, 75.44, 75.39, 59.507, 72.76], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [17152804, 6162675, 3168267, 781472, 5889574, 3834415, 7959865, 2167533, 4388260, 304739, 26480870, 1536769, 7459574, 228694, 38783863, 192675, 2512642, 34617799, 706367, 608274, 10538093, 4227026, 745228, 14500404, 1251524, 1703617, 2721783, 8007166, 5637246, 6491649, 1456688, 913025, 18396941, 11127868, 977026, 5682086, 62209173, 492095, 4657072, 86796, 5260855, 3140897, 4353666, 27129932, 17104986, 551425, 17129565, 2308582, 6005061, 11457758, 5216550, 6642107], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4910.4167560000005, 3008.647355, 1029.161251, 3214.857818, 743.3870368, 556.1032651, 1783.432873, 1109.374338, 1133.98495, 1172.603047, 795.757282, 3259.178978, 2517.736547, 3081.7610219999997, 2785.493582, 958.5668124, 505.7538077, 556.8083834, 21745.57328, 884.7552507000001, 993.2239571, 874.6858642999999, 764.7259627999999, 1267.613204, 745.3695408, 640.3224382999999, 21951.21176, 1544.228586, 663.2236766, 686.3952693, 1497.492223, 3710.9829630000004, 2370.619976, 502.31973339999996, 3876.4859579999998, 808.8970727999999, 1981.9518059999998, 4319.804067, 670.0806011, 1737.561657, 1561.769116, 1348.285159, 1450.9925130000001, 8028.651439, 2202.9884230000002, 3781.410618, 962.4922932, 1532.776998, 3120.876811, 843.7331372000001, 1588.688299, 685.5876821], "xaxis": "x", "y": [58.013999999999996, 39.483000000000004, 49.19, 59.318999999999996, 46.137, 45.91, 49.355, 46.775, 47.383, 50.93899999999999, 47.803999999999995, 55.625, 52.373999999999995, 46.519, 53.318999999999996, 42.023999999999994, 44.535, 44.51, 52.79, 41.842, 51.756, 40.762, 37.465, 56.155, 52.208, 43.763999999999996, 57.442, 46.881, 43.766999999999996, 41.714, 50.852, 64.93, 55.73, 42.495, 56.437, 41.291000000000004, 44.513999999999996, 67.064, 45.0, 58.55, 48.879, 36.788000000000004, 41.974, 55.527, 47.8, 52.537, 49.919, 52.887, 59.836999999999996, 50.35, 51.386, 57.674], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [26983828, 5079716, 114313951, 23796400, 10599793, 25094412, 2108457, 9537988, 5302800, 7278866, 4282586, 5703430, 4908554, 3055235, 2156814, 63759976, 2554598, 1839782, 2984494, 15990099, 3080828, 1039009, 220239000, 2873520, 13503563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [10079.026740000001, 3548.097832, 6660.118654, 22090.88306, 4756.763836, 3815.80787, 5926.876967, 6380.494965999999, 2681.9889, 6679.62326, 5138.922374, 4879.992748, 1874.2989309999998, 3203.208066, 6650.195573, 7674.929108, 5486.371089, 5351.912144, 3248.373311, 6281.290854999999, 9770.524921, 7899.554209000001, 24072.63213, 6504.339663000001, 13143.95095], "xaxis": "x", "y": [68.48100000000001, 50.023, 61.489, 74.21, 67.05199999999999, 63.836999999999996, 70.75, 72.649, 61.788000000000004, 61.31, 56.696000000000005, 56.028999999999996, 49.923, 57.402, 70.11, 65.032, 57.47, 68.681, 66.35300000000001, 58.446999999999996, 73.44, 68.3, 73.38, 69.48100000000001, 67.456], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [14074100, 3164900], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [18334.197509999998, 16233.7177], "xaxis": "x", "y": [73.49, 72.22], "yaxis": "y", "type": "scatter"}], "name": "1977"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [12881816, 377967, 93074406, 7272485, 1000281000, 5264500, 708000000, 153343000, 43072751, 14173318, 3858421, 118454974, 2347031, 17647518, 39326000, 1497494, 3086876, 14441916, 1756032, 34680442, 15796314, 1301048, 91462088, 53456774, 11254672, 2651869, 15410151, 9410494, 18501390, 48827160, 56142181, 1425876, 9657618], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [978.0114388000001, 19211.14731, 676.9818656, 624.4754784, 962.4213804999999, 14560.530509999999, 855.7235377000001, 1516.872988, 7608.334602, 14517.90711, 15367.0292, 19384.10571, 4161.415959, 4106.525293, 5622.942464, 31354.03573, 7640.519520999999, 4920.355951, 2000.603139, 424.0, 718.3730947, 12954.791009999999, 1443.429832, 2603.273765, 33693.17525, 15169.161119999999, 1648.0797890000001, 3761.8377149999997, 7426.354773999999, 2393.219781, 707.2357863, 4336.032082, 1977.5570100000002], "xaxis": "x", "y": [39.854, 69.05199999999999, 50.00899999999999, 50.957, 65.525, 75.45, 56.596000000000004, 56.159, 59.62, 62.038000000000004, 74.45, 77.11, 63.739, 69.1, 67.123, 71.309, 66.983, 68.0, 57.489, 58.056000000000004, 49.593999999999994, 62.728, 56.158, 62.082, 63.012, 71.76, 68.757, 64.59, 72.16, 64.597, 58.816, 64.406, 49.113], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2780097, 7574613, 9856303, 4172693, 8892098, 4413368, 10303704, 5117810, 4826933, 54433565, 78335266, 9786480, 10705535, 233997, 3480000, 56535636, 562548, 14310401, 4114787, 36227381, 9859650, 22356726, 9032824, 5048043, 1861252, 37983310, 8325260, 6468126, 47328791, 56339704], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3630.880722, 21597.083619999998, 20979.84589, 4126.613157, 8224.191647, 13221.82184, 15377.22855, 21688.04048, 18533.15761, 20293.89746, 22031.532740000002, 15268.420890000001, 12545.99066, 23269.6075, 12618.321409999999, 16537.4835, 11222.58762, 21399.46046, 26298.635309999998, 8451.531004, 11753.84291, 9605.314053, 15181.0927, 11348.54585, 17866.72175, 13926.169969999999, 20667.38125, 28397.715119999997, 4241.356344, 18232.42452], "xaxis": "x", "y": [70.42, 73.18, 73.93, 70.69, 71.08, 70.46, 70.96, 74.63, 74.55, 74.89, 73.8, 75.24, 69.39, 76.99, 73.1, 74.98, 74.101, 76.05, 75.97, 71.32, 72.77, 69.66, 70.16199999999999, 70.8, 71.063, 76.3, 76.42, 76.21, 61.036, 74.04], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [20033753, 7016384, 3641603, 970347, 6634596, 4580410, 9250831, 2476971, 4875118, 348643, 30646495, 1774735, 9025951, 305991, 45681811, 285483, 2637297, 38111756, 753874, 715523, 11400338, 4710497, 825987, 17661452, 1411807, 1956875, 3344074, 9171477, 6502825, 6998256, 1622136, 992040, 20198730, 12587223, 1099010, 6437188, 73039376, 517810, 5507565, 98593, 6147783, 3464522, 5828892, 31140029, 20367053, 649901, 19844382, 2644765, 6734098, 12939400, 6100407, 7636524], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5745.160213, 2756.953672, 1277.897616, 4551.14215, 807.1985855, 559.6032309999999, 2367.983282, 956.7529906999999, 797.9081006, 1267.100083, 673.7478181, 4879.507522, 2602.710169, 2879.4680670000002, 3503.729636, 927.8253427000001, 524.8758493, 577.8607471, 15113.36194, 835.8096107999999, 876.032569, 857.2503577, 838.1239671, 1348.225791, 797.2631074, 572.1995694, 17364.275380000003, 1302.878658, 632.8039209, 618.0140640999999, 1481.150189, 3688.037739, 2702.620356, 462.2114149, 4191.100511, 909.7221354000001, 1576.97375, 5267.219353, 881.5706467, 1890.2181170000001, 1518.479984, 1465.010784, 1176.807031, 8568.266228, 1895.544073, 3895.384018, 874.2426069, 1344.577953, 3560.2331740000004, 682.2662267999999, 1408.678565, 788.8550411], "xaxis": "x", "y": [61.368, 39.942, 50.903999999999996, 61.483999999999995, 48.122, 47.471000000000004, 52.961000000000006, 48.295, 49.516999999999996, 52.933, 47.784, 56.695, 53.983000000000004, 48.812, 56.006, 43.662, 43.89, 44.916000000000004, 56.56399999999999, 45.58, 53.744, 42.891000000000005, 39.327, 58.766000000000005, 55.078, 44.852, 62.155, 48.968999999999994, 45.641999999999996, 43.916000000000004, 53.599, 66.711, 59.65, 42.795, 58.968, 42.598, 45.826, 69.885, 46.218, 60.351000000000006, 52.379, 38.445, 42.955, 58.161, 50.338, 55.56100000000001, 50.608000000000004, 55.471000000000004, 64.048, 49.849, 51.821000000000005, 60.363], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [29341374, 5642224, 128962939, 25201900, 11487112, 27764644, 2424367, 9789224, 5968349, 8365850, 4474873, 6395630, 5198399, 3669448, 2298309, 71640904, 2979423, 2036305, 3366439, 18125129, 3279001, 1116479, 232187835, 2953997, 15620766], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8997.897412, 3156.510452, 7030.835878, 22898.79214, 5095.665738000001, 4397.575659, 5262.734751, 7316.9181069999995, 2861.092386, 7213.7912670000005, 4098.344175, 4820.49479, 2011.1595489999997, 3121.7607940000003, 6068.05135, 9611.147541, 3470.3381560000003, 7009.601598, 4258.5036039999995, 6434.501797, 10330.98915, 9119.528607, 25009.55914, 6920.223051000001, 11152.410109999999], "xaxis": "x", "y": [69.942, 53.858999999999995, 63.336000000000006, 75.76, 70.565, 66.653, 73.45, 73.717, 63.727, 64.342, 56.604, 58.137, 51.461000000000006, 60.909, 71.21, 67.405, 59.298, 70.472, 66.874, 61.406000000000006, 73.75, 68.832, 74.65, 70.805, 68.557], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [15184200, 3210650], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [19477.009280000002, 17632.4104], "xaxis": "x", "y": [74.74, 73.84], "yaxis": "y", "type": "scatter"}], "name": "1982"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [13867957, 454612, 103764241, 8371791, 1084035000, 5584510, 788000000, 169276000, 51889696, 16543189, 4203148, 122091325, 2820042, 19067554, 41622000, 1891487, 3089353, 16331785, 2015133, 38028578, 17917180, 1593882, 105186881, 60017788, 14619745, 2794552, 16495304, 11242847, 19757799, 52910342, 62826491, 1691210, 11219340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [852.3959447999999, 18524.02406, 751.9794035, 683.8955732000001, 1378.904018, 20038.472690000002, 976.5126756000001, 1748.356961, 6642.881371, 11643.57268, 17122.47986, 22375.941890000002, 4448.679912, 4106.4923149999995, 8533.088805, 28118.42998, 5377.091329, 5249.802653, 2338.008304, 385.0, 775.6324501, 18115.223130000002, 1704.686583, 2189.634995, 21198.26136, 18861.53081, 1876.766827, 3116.774285, 11054.56175, 2982.653773, 820.7994449, 5107.197384, 1971.741538], "xaxis": "x", "y": [40.821999999999996, 70.75, 52.818999999999996, 53.913999999999994, 67.274, 76.2, 58.553000000000004, 60.137, 63.04, 65.044, 75.6, 78.67, 65.869, 70.64699999999999, 69.81, 74.17399999999999, 67.926, 69.5, 60.222, 58.339, 52.537, 67.734, 58.245, 64.15100000000001, 66.295, 73.56, 69.01100000000001, 66.97399999999999, 73.4, 66.084, 62.82, 67.046, 52.922], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3075321, 7578903, 9870200, 4338977, 8971958, 4484310, 10311597, 5127024, 4931729, 55630100, 77718298, 9974490, 10612740, 244676, 3539900, 56729703, 569473, 14665278, 4186147, 37740710, 9915289, 22686371, 9230783, 5199318, 1945870, 38880702, 8421403, 6649942, 52881328, 56981620], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3738.9327350000003, 23687.82607, 22525.56308, 4314.114757, 8239.854824, 13822.58394, 16310.4434, 25116.17581, 21141.01223, 22066.44214, 24639.18566, 16120.528390000001, 12986.47998, 26923.206280000002, 13872.86652, 19207.234819999998, 11732.51017, 23651.32361, 31540.9748, 9082.351172, 13039.30876, 9696.273295, 15870.878509999999, 12037.26758, 18678.53492, 15764.98313, 23586.92927, 30281.704589999998, 5089.043686, 21664.787669999998], "xaxis": "x", "y": [72.0, 74.94, 75.35, 71.14, 71.34, 71.52, 71.58, 74.8, 74.83, 76.34, 74.847, 76.67, 69.58, 77.23, 74.36, 76.42, 74.865, 76.83, 75.89, 70.98, 74.06, 69.53, 71.218, 71.08, 72.25, 76.9, 77.19, 77.41, 63.108000000000004, 75.007], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [23254956, 7874230, 4243788, 1151184, 7586551, 5126023, 10780667, 2840009, 5498955, 395114, 35481645, 2064095, 10761098, 311025, 52799062, 341244, 2915959, 42999530, 880397, 848406, 14168101, 5650262, 927524, 21198082, 1599200, 2269414, 3799845, 10568642, 7824747, 7634008, 1841240, 1042663, 22987397, 12891952, 1278184, 7332638, 81551520, 562035, 6349365, 110812, 7171347, 3868905, 6921858, 35933379, 24725960, 779348, 23040630, 3154264, 7724976, 15283050, 7272406, 9216418], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5681.358539, 2430.208311, 1225.85601, 6205.88385, 912.0631417000001, 621.8188188999999, 2602.664206, 844.8763504000001, 952.3861289999999, 1315.980812, 672.774812, 4201.194936999999, 2156.9560690000003, 2880.102568, 3885.4607100000003, 966.8968149, 521.1341333, 573.7413142000001, 11864.408440000001, 611.6588611000001, 847.0061135, 805.5724717999999, 736.4153921, 1361.936856, 773.9932140999999, 506.1138573, 11770.5898, 1155.4419480000001, 635.5173633999999, 684.1715576, 1421.603576, 4783.586903, 2755.046991, 389.87618460000004, 3693.7313369999997, 668.3000228, 1385.029563, 5303.377488, 847.991217, 1516.525457, 1441.72072, 1294.4477880000002, 1093.244963, 7825.823398, 1507.819159, 3984.8398119999997, 831.8220794, 1202.201361, 3810.419296, 617.7244065, 1213.315116, 706.1573059], "xaxis": "x", "y": [65.79899999999999, 39.906, 52.336999999999996, 63.622, 49.556999999999995, 48.211000000000006, 54.985, 50.485, 51.051, 54.926, 47.412, 57.47, 54.655, 50.04, 59.797, 45.663999999999994, 46.453, 46.684, 60.19, 49.265, 55.729, 45.552, 41.245, 59.339, 57.18, 46.027, 66.234, 49.35, 47.457, 46.364, 56.145, 68.74, 62.677, 42.861000000000004, 60.835, 44.555, 46.886, 71.913, 44.02, 61.728, 55.769, 40.006, 44.501000000000005, 60.833999999999996, 51.744, 57.678000000000004, 51.535, 56.941, 66.89399999999999, 51.50899999999999, 50.821000000000005, 62.351000000000006], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [31620918, 6156369, 142938076, 26549700, 12463354, 30964245, 2799811, 10239839, 6655297, 9545158, 4842194, 7326406, 5756203, 4372203, 2326606, 80122492, 3344353, 2253639, 3886512, 20195924, 3444468, 1191336, 242803533, 3045153, 17910182], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9139.671389, 2753.6914899999997, 7807.095818000001, 26626.515030000002, 5547.063754, 4903.2191, 5629.915318, 7532.924762999999, 2899.842175, 6481.776993, 4140.442097, 4246.485974, 1823.015995, 3023.0966989999997, 6351.237495, 8688.156003, 2955.984375, 7034.779161, 3998.875695, 6360.9434439999995, 12281.34191, 7388.597823, 29884.350410000003, 7452.398969, 9883.584648], "xaxis": "x", "y": [70.774, 57.251000000000005, 65.205, 76.86, 72.492, 67.768, 74.752, 74.17399999999999, 66.046, 67.23100000000001, 63.153999999999996, 60.782, 53.636, 64.492, 71.77, 69.498, 62.008, 71.523, 67.378, 64.134, 74.63, 69.582, 75.02, 71.918, 70.19], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [16257249, 3317166], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [21888.889030000002, 19007.19129], "xaxis": "x", "y": [76.32, 74.32], "yaxis": "y", "type": "scatter"}], "name": "1987"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [16317921, 529491, 113704579, 10150094, 1164970000, 5829696, 872000000, 184816000, 60397973, 17861905, 4936550, 124329269, 3867409, 20711375, 43805450, 1418095, 3219994, 18319502, 2312802, 40546538, 20326209, 1915208, 120065004, 67185766, 16945857, 3235865, 17587060, 13219062, 20686918, 56667095, 69940728, 2104779, 13367997], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [649.3413952000001, 19035.579169999997, 837.8101642999999, 682.3031755, 1655.784158, 24757.60301, 1164.406809, 2383.140898, 7235.653187999999, 3745.6406869999996, 18051.52254, 26824.895109999998, 3431.5936469999997, 3726.063507, 12104.27872, 34932.91959, 6890.806854, 7277.912802, 1785.402016, 347.0, 897.7403604, 18616.70691, 1971.8294640000001, 2279.3240170000004, 24841.617769999997, 24769.8912, 2153.7392219999997, 3340.542768, 15215.6579, 4616.8965450000005, 989.0231487, 6017.654756, 1879.496673], "xaxis": "x", "y": [41.674, 72.601, 56.018, 55.803000000000004, 68.69, 77.601, 60.223, 62.681000000000004, 65.742, 59.461000000000006, 76.93, 79.36, 68.015, 69.97800000000001, 72.244, 75.19, 69.292, 70.693, 61.271, 59.32, 55.727, 71.197, 60.838, 66.458, 68.768, 75.788, 70.37899999999999, 69.249, 74.26, 67.298, 67.66199999999999, 69.718, 55.599], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3326498, 7914969, 10045622, 4256013, 8658506, 4494013, 10315702, 5171393, 5041039, 57374179, 80597764, 10325429, 10348684, 259012, 3557761, 56840847, 621621, 15174244, 4286357, 38370697, 9927680, 22797027, 9826397, 5302888, 1999210, 39549438, 8718867, 6995447, 58179144, 57866349], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2497.4379010000002, 27042.01868, 25575.57069, 2546.781445, 6302.6234380000005, 8447.794873, 14297.021219999999, 26406.73985, 20647.16499, 24703.79615, 26505.30317, 17541.49634, 10535.62855, 25144.39201, 17558.81555, 22013.64486, 7003.339037000001, 26790.94961, 33965.66115, 7738.881247, 16207.266630000002, 6598.409903, 9325.068238, 9498.467723, 14214.71681, 18603.06452, 23880.01683, 31871.5303, 5678.348271, 22705.09254], "xaxis": "x", "y": [71.581, 76.04, 76.46, 72.178, 71.19, 72.527, 72.4, 75.33, 75.7, 77.46, 76.07, 77.03, 69.17, 78.77, 75.467, 77.44, 75.435, 77.42, 77.32, 70.99, 74.86, 69.36, 71.65899999999999, 71.38, 73.64, 77.57, 78.16, 78.03, 66.146, 76.42], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [26298373, 8735988, 4981671, 1342614, 8878303, 5809236, 12467171, 3265124, 6429417, 454429, 41672143, 2409073, 12772596, 384156, 59402198, 387838, 3668440, 52088559, 985739, 1025384, 16278738, 6990574, 1050938, 25020539, 1803195, 1912974, 4364501, 12210395, 10014249, 8416215, 2119465, 1096202, 25798239, 13160731, 1554253, 8392818, 93364244, 622191, 7290203, 125911, 8307920, 4260884, 6099799, 39964159, 28227588, 962344, 26605473, 3747553, 8523077, 18252190, 8381163, 10704340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5023.216647, 2627.8456850000002, 1191.207681, 7954.111645, 931.7527731, 631.6998778, 1793.1632780000002, 747.9055252, 1058.0643, 1246.90737, 457.7191807, 4016.239529, 1648.073791, 2377.1561920000004, 3794.755195, 1132.055034, 582.8585102000001, 421.3534653, 13522.157519999999, 665.6244126, 925.0601539999999, 794.3484384, 745.5398706, 1341.9217210000002, 977.4862724999999, 636.6229191000001, 9640.138501000001, 1040.6761900000001, 563.2000145, 739.014375, 1361.369784, 6058.2538460000005, 2948.047252, 410.89682389999996, 3804.537999, 581.182725, 1619.848217, 6101.2558229999995, 737.0685949, 1428.777814, 1367.899369, 1068.696278, 926.9602964, 7225.0692579999995, 1492.197043, 3553.0224, 825.682454, 1034.298904, 4332.720164, 644.1707968999999, 1210.884633, 693.4207856], "xaxis": "x", "y": [67.744, 40.647, 53.919, 62.745, 50.26, 44.736000000000004, 54.31399999999999, 49.396, 51.724, 57.93899999999999, 45.548, 56.433, 52.044, 51.604, 63.674, 47.545, 49.99100000000001, 48.091, 61.36600000000001, 52.644, 57.501000000000005, 48.576, 43.266000000000005, 59.285, 59.685, 40.802, 68.755, 52.214, 49.42, 48.388000000000005, 58.333, 69.745, 65.393, 44.284, 61.998999999999995, 47.391000000000005, 47.472, 73.615, 23.599, 62.742, 58.196000000000005, 38.333, 39.658, 61.888000000000005, 53.556000000000004, 58.474, 50.44, 58.06100000000001, 70.001, 48.825, 46.1, 60.376999999999995], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [33958947, 6893451, 155975974, 28523502, 13572994, 34202721, 3173216, 10723260, 7351181, 10748394, 5274649, 8486949, 6326682, 5077347, 2378618, 88111030, 4017939, 2484997, 4483945, 22430449, 3585176, 1183669, 256894189, 3149262, 20265563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9308.41871, 2961.699694, 6950.283020999999, 26342.88426, 7596.125964, 5444.648617, 6160.416317, 5592.843963, 3044.214214, 7103.702595000001, 4444.2317, 4439.4508399999995, 1456.309517, 3081.694603, 7404.923685, 9472.384295, 2170.151724, 6618.74305, 4196.411078, 4446.380924, 14641.587109999999, 7370.990932, 32003.93224, 8137.004775, 10733.926309999999], "xaxis": "x", "y": [71.868, 59.957, 67.057, 77.95, 74.126, 68.421, 75.71300000000001, 74.414, 68.457, 69.613, 66.798, 63.373000000000005, 55.089, 66.399, 71.766, 71.455, 65.843, 72.462, 68.225, 66.458, 73.911, 69.862, 76.09, 72.752, 71.15], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [17481977, 3437674], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [23424.76683, 18363.324940000002], "xaxis": "x", "y": [77.56, 76.33], "yaxis": "y", "type": "scatter"}], "name": "1992"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [22227415, 598561, 123315288, 11782962, 1230075000, 6495918, 959000000, 199278000, 63327987, 20775703, 5531387, 125956499, 4526235, 21585105, 46173816, 1765345, 3430388, 20476091, 2494803, 43247867, 23001113, 2283635, 135564834, 75012988, 21229759, 3802309, 18698655, 15081016, 21628605, 60216677, 76048996, 2826046, 15826497], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [635.341351, 20292.01679, 972.7700352, 734.28517, 2289.234136, 28377.632189999997, 1458.817442, 3119.335603, 8263.590301, 3076.239795, 20896.60924, 28816.58499, 3645.379572, 1690.756814, 15993.52796, 40300.61996, 8754.96385, 10132.90964, 1902.2521, 415.0, 1010.892138, 19702.055809999998, 2049.3505210000003, 2536.534925, 20586.69019, 33519.4766, 2664.477257, 4014.238972, 20206.82098, 5852.625497, 1385.896769, 7110.667619, 2117.484526], "xaxis": "x", "y": [41.763000000000005, 73.925, 59.412, 56.534, 70.426, 80.0, 61.765, 66.041, 68.042, 58.81100000000001, 78.26899999999999, 80.69, 69.77199999999999, 67.727, 74.64699999999999, 76.156, 70.265, 71.938, 63.625, 60.328, 59.426, 72.499, 61.818000000000005, 68.564, 70.533, 77.158, 70.457, 71.527, 75.25, 67.521, 70.672, 71.096, 58.02], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3428038, 8069876, 10199787, 3607000, 8066057, 4444595, 10300707, 5283663, 5134406, 58623428, 82011073, 10502372, 10244684, 271192, 3667233, 57479469, 692651, 15604464, 4405672, 38654957, 10156415, 22562458, 10336594, 5383010, 2011612, 39855442, 8897619, 7193761, 63047647, 58808266], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3193.054604, 29095.920660000003, 27561.196630000002, 4766.355904, 5970.38876, 9875.604515, 16048.51424, 29804.34567, 23723.9502, 25889.78487, 27788.88416, 18747.69814, 11712.7768, 28061.099660000003, 24521.94713, 24675.02446, 6465.613349, 30246.13063, 41283.16433, 10159.58368, 17641.03156, 7346.547556999999, 7914.320304000001, 12126.23065, 17161.10735, 20445.29896, 25266.59499, 32135.323010000004, 6601.429915, 26074.53136], "xaxis": "x", "y": [72.95, 77.51, 77.53, 73.244, 70.32, 73.68, 74.01, 76.11, 77.13, 78.64, 77.34, 77.869, 71.04, 78.95, 76.122, 78.82, 75.445, 78.03, 78.32, 72.75, 75.97, 69.72, 72.232, 72.71, 75.13, 78.77, 79.39, 79.37, 68.835, 77.218], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [29072015, 9875024, 6066080, 1536536, 10352843, 6121610, 14195809, 3696513, 7562011, 527982, 47798986, 2800947, 14625967, 417908, 66134291, 439971, 4058319, 59861301, 1126189, 1235767, 18418288, 8048834, 1193708, 28263827, 1982823, 2200725, 4759670, 14165114, 10419991, 9384984, 2444741, 1149818, 28529501, 16603334, 1774766, 9666252, 106207839, 684810, 7212583, 145608, 9535314, 4578212, 6633514, 42835005, 32160729, 1054486, 30686889, 4320890, 9231669, 21210254, 9417789, 11404948], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4797.295051, 2277.140884, 1232.975292, 8647.142313, 946.2949617999999, 463.1151478, 1694.337469, 740.5063317, 1004.9613529999999, 1173.618235, 312.188423, 3484.1643759999997, 1786.265407, 1895.016984, 4173.181797, 2814.480755, 913.4707900000001, 515.8894013, 14722.841880000002, 653.7301704, 1005.2458119999999, 869.4497667999999, 796.6644681, 1360.4850210000002, 1186.147994, 609.1739508, 9467.446056, 986.2958956, 692.2758102999999, 790.2579846, 1483.1361359999999, 7425.705295000001, 2982.101858, 472.34607710000006, 3899.52426, 580.3052092, 1624.941275, 6071.941411, 589.9445051, 1339.076036, 1392.368347, 574.6481576, 930.5964284, 7479.188244, 1632.2107640000002, 3876.7684600000002, 789.1862231, 982.2869242999999, 4876.798614, 816.559081, 1071.353818, 792.4499602999999], "xaxis": "x", "y": [69.152, 40.963, 54.777, 52.556000000000004, 50.324, 45.326, 52.199, 46.066, 51.573, 60.66, 42.586999999999996, 52.961999999999996, 47.99100000000001, 53.157, 67.217, 48.245, 53.378, 49.402, 60.461000000000006, 55.861000000000004, 58.556000000000004, 51.455, 44.873000000000005, 54.407, 55.558, 42.221000000000004, 71.555, 54.978, 47.495, 49.903, 60.43, 70.736, 67.66, 46.343999999999994, 58.909, 51.313, 47.464, 74.77199999999999, 36.086999999999996, 63.306000000000004, 60.187, 39.897, 43.795, 60.236000000000004, 55.373000000000005, 54.288999999999994, 48.466, 58.39, 71.973, 44.578, 40.238, 46.809], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [36203463, 7693188, 168546719, 30305843, 14599929, 37657830, 3518107, 10983007, 7992357, 11911819, 5783439, 9803875, 6913545, 5867957, 2531311, 95895146, 4609572, 2734531, 5154123, 24748122, 3759430, 1138101, 272911760, 3262838, 22374398], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [10967.28195, 3326.143191, 7957.980823999999, 28954.92589, 10118.053179999999, 6117.3617460000005, 6677.045314, 5431.990415, 3614.101285, 7429.455876999999, 5154.825496, 4684.313807, 1341.7269310000001, 3160.454906, 7121.924704000001, 9767.29753, 2253.023004, 7113.692252, 4247.400261, 5838.347657, 16999.4333, 8792.573126000001, 35767.43303, 9230.240708, 10165.49518], "xaxis": "x", "y": [73.275, 62.05, 69.388, 78.61, 75.816, 70.313, 77.26, 76.15100000000001, 69.957, 72.312, 69.535, 66.322, 56.67100000000001, 67.65899999999999, 72.262, 73.67, 68.426, 73.738, 69.4, 68.38600000000001, 74.917, 69.465, 76.81, 74.223, 72.146], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [18565243, 3676187], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [26997.936569999998, 21050.41377], "xaxis": "x", "y": [78.83, 77.55], "yaxis": "y", "type": "scatter"}], "name": "1997"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [25268405, 656397, 135656790, 12926707, 1280400000, 6762476, 1034172547, 211060000, 66907826, 24001816, 6029529, 127065841, 5307470, 22215365, 47969150, 2111561, 3677780, 22662365, 2674234, 45598081, 25873917, 2713462, 153403524, 82995088, 24501530, 4197776, 19576783, 17155814, 22454239, 62806748, 80908147, 3389578, 18701257], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [726.7340548, 23403.559269999998, 1136.3904300000002, 896.2260152999999, 3119.280896, 30209.015160000003, 1746.769454, 2873.91287, 9240.761975, 4390.717312, 21905.59514, 28604.5919, 3844.9171939999997, 1646.758151, 19233.98818, 35110.10566, 9313.93883, 10206.97794, 2140.7393230000002, 611.0, 1057.206311, 19774.83687, 2092.712441, 2650.921068, 19014.54118, 36023.1054, 3015.3788329999998, 4090.9253310000004, 23235.42329, 5913.187529, 1764.456677, 4515.487575, 2234.820827], "xaxis": "x", "y": [42.129, 74.795, 62.013000000000005, 56.751999999999995, 72.028, 81.495, 62.879, 68.58800000000001, 69.45100000000001, 57.04600000000001, 79.696, 82.0, 71.263, 66.66199999999999, 77.045, 76.904, 71.028, 73.044, 65.033, 59.908, 61.34, 74.193, 63.61, 70.303, 71.626, 78.77, 70.815, 73.053, 76.99, 68.564, 73.017, 72.37, 60.308], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3508512, 8148312, 10311970, 4165416, 7661799, 4481020, 10256295, 5374693, 5193039, 59925035, 82350671, 10603863, 10083313, 288030, 3879155, 57926999, 720230, 16122830, 4535591, 38625976, 10433867, 22404337, 10111559, 5410052, 2011497, 40152517, 8954175, 7361757, 67308928, 59912431], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [4604.211737, 32417.607689999997, 30485.88375, 6018.975239, 7696.777725, 11628.38895, 17596.210219999997, 32166.500060000002, 28204.59057, 28926.032339999998, 30035.80198, 22514.2548, 14843.93556, 31163.201960000002, 34077.04939, 27968.098169999997, 6557.194282, 33724.75778, 44683.97525, 12002.23908, 19970.90787, 7885.360081, 7236.075251, 13638.778369999998, 20660.01936, 24835.47166, 29341.630930000003, 34480.95771, 6508.085718, 29478.99919], "xaxis": "x", "y": [75.65100000000001, 78.98, 78.32, 74.09, 72.14, 74.876, 75.51, 77.18, 78.37, 79.59, 78.67, 78.256, 72.59, 80.5, 77.783, 80.24, 73.98100000000001, 78.53, 79.05, 74.67, 77.29, 71.322, 73.21300000000001, 73.8, 76.66, 79.78, 80.04, 80.62, 70.845, 78.471], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [31287142, 10866106, 7026113, 1630347, 12251209, 7021078, 15929988, 4048013, 8835739, 614382, 55379852, 3328795, 16252726, 447416, 73312559, 495627, 4414865, 67946797, 1299304, 1457766, 20550751, 8807818, 1332459, 31386842, 2046772, 2814651, 5368585, 16473477, 11824495, 10580176, 2828858, 1200206, 31167783, 18473780, 1972153, 11140655, 119901274, 743981, 7852401, 170372, 10870037, 5359092, 7753310, 44433622, 37090298, 1130269, 34593779, 4977378, 9770575, 24739869, 10595811, 11926563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5288.040382, 2773.287312, 1372.877931, 11003.60508, 1037.645221, 446.4035126, 1934.0114489999999, 738.6906068, 1156.18186, 1075.811558, 241.16587650000002, 3484.06197, 1648.800823, 1908.2608670000002, 4754.604414, 7703.4959, 765.3500015, 530.0535319, 12521.71392, 660.5855997, 1111.9845779999998, 945.5835837000001, 575.7047176, 1287.514732, 1275.184575, 531.4823679, 9534.677467, 894.6370822, 665.4231186000001, 951.4097517999999, 1579.0195429999999, 9021.815894, 3258.495584, 633.6179466, 4072.3247509999997, 601.0745012, 1615.2863949999999, 6316.1652, 785.6537647999999, 1353.09239, 1519.635262, 699.4897129999999, 882.0818218000001, 7710.946444, 1993.398314, 4128.116943, 899.0742111, 886.2205765000001, 5722.895654999999, 927.7210018, 1071.6139380000002, 672.0386227000001], "xaxis": "x", "y": [70.994, 41.003, 54.406000000000006, 46.63399999999999, 50.65, 47.36, 49.856, 43.308, 50.525, 62.974, 44.966, 52.97, 46.832, 53.373000000000005, 69.806, 49.348, 55.24, 50.725, 56.761, 58.041000000000004, 58.453, 53.676, 45.504, 50.992, 44.593, 43.753, 72.737, 57.286, 45.00899999999999, 51.818000000000005, 62.247, 71.954, 69.615, 44.026, 51.479, 54.496, 46.608000000000004, 75.744, 43.413000000000004, 64.337, 61.6, 41.012, 45.93600000000001, 53.365, 56.369, 43.869, 49.651, 57.56100000000001, 73.042, 47.813, 39.193000000000005, 39.989000000000004], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [38331121, 8445134, 179914212, 31902268, 15497046, 41008227, 3834934, 11226999, 8650322, 12921234, 6353681, 11178650, 7607651, 6677328, 2664659, 102479927, 5146848, 2990875, 5884491, 26769436, 3859606, 1101832, 287675526, 3363085, 24287670], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8797.640716, 3413.26269, 8131.212843000001, 33328.96507, 10778.78385, 5755.259962, 7723.447195000001, 6340.646683, 4563.808154, 5773.0445119999995, 5351.568665999999, 4858.347495, 1270.364932, 3099.72866, 6994.774861, 10742.44053, 2474.548819, 7356.031934000001, 3783.674243, 5909.020073, 18855.606180000002, 11460.60023, 39097.09955, 7727.002004000001, 8605.047831], "xaxis": "x", "y": [74.34, 63.883, 71.006, 79.77, 77.86, 71.682, 78.123, 77.158, 70.847, 74.173, 70.734, 68.97800000000001, 58.137, 68.565, 72.047, 74.902, 70.836, 74.712, 70.755, 69.906, 77.778, 68.976, 77.31, 75.307, 72.766], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [19546792, 3908037], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [30687.75473, 23189.80135], "xaxis": "x", "y": [80.37, 79.11], "yaxis": "y", "type": "scatter"}], "name": "2002"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [31889923, 708573, 150448339, 14131858, 1318683096, 6980412, 1110396331, 223547000, 69453570, 27499638, 6426679, 127467972, 6053193, 23301725, 49044790, 2505559, 3921278, 24821286, 2874127, 47761980, 28901790, 3204897, 169270617, 91077287, 27601038, 4553009, 20378239, 19314747, 23174294, 65068149, 85262356, 4018332, 22211743], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3600523, 8199783, 10392226, 4552198, 7322858, 4493312, 10228744, 5468120, 5238460, 61083916, 82400996, 10706290, 9956108, 301931, 4109086, 58147733, 684736, 16570613, 4627926, 38518241, 10642836, 22276056, 10150265, 5447502, 2009245, 40448191, 9031088, 7554661, 71158647, 60776238], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [33333216, 12420476, 8078314, 1639131, 14326203, 8390505, 17696293, 4369038, 10238807, 710960, 64606759, 3800610, 18013409, 496374, 80264543, 551201, 4906585, 76511887, 1454867, 1688359, 22873338, 9947814, 1472041, 35610177, 2012649, 3193942, 6036914, 19167654, 13327079, 12031795, 3270065, 1250882, 33757175, 19951656, 2055080, 12894865, 135031164, 798094, 8860588, 199579, 12267493, 6144562, 9118773, 43997828, 42292929, 1133066, 38139640, 5701579, 10276158, 29170398, 11746035, 12311143], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [40301927, 9119152, 190010647, 33390141, 16284741, 44227550, 4133884, 11416987, 9319622, 13755680, 6939688, 12572928, 8502814, 7483763, 2780132, 108700891, 5675356, 3242173, 6667147, 28674757, 3942491, 1056608, 301139947, 3447496, 26084662], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [20434176, 4115771], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [34435.367439999995, 25185.00911], "xaxis": "x", "y": [81.235, 80.204], "yaxis": "y", "type": "scatter"}], "name": "2007"}]);
                        }).then(function(){

var gd = document.getElementById('53d845cb-b495-4874-9d46-2075a1cc372c');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


## Division de Columnas y filas por Categorias (Facet)


```python
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", size="pop",
           color="continent",
           hover_name="country",
           size_max=60, facet_col='continent',
           log_x=True)
```


<div>


            <div id="8603926a-154b-47df-91dd-38aec919300e" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("8603926a-154b-47df-91dd-38aec919300e")) {
                    Plotly.newPlot(
                        '8603926a-154b-47df-91dd-38aec919300e',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [31889923, 708573, 150448339, 14131858, 1318683096, 6980412, 1110396331, 223547000, 69453570, 27499638, 6426679, 127467972, 6053193, 23301725, 49044790, 2505559, 3921278, 24821286, 2874127, 47761980, 28901790, 3204897, 169270617, 91077287, 27601038, 4553009, 20378239, 19314747, 23174294, 65068149, 85262356, 4018332, 22211743], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3600523, 8199783, 10392226, 4552198, 7322858, 4493312, 10228744, 5468120, 5238460, 61083916, 82400996, 10706290, 9956108, 301931, 4109086, 58147733, 684736, 16570613, 4627926, 38518241, 10642836, 22276056, 10150265, 5447502, 2009245, 40448191, 9031088, 7554661, 71158647, 60776238], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x2", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [33333216, 12420476, 8078314, 1639131, 14326203, 8390505, 17696293, 4369038, 10238807, 710960, 64606759, 3800610, 18013409, 496374, 80264543, 551201, 4906585, 76511887, 1454867, 1688359, 22873338, 9947814, 1472041, 35610177, 2012649, 3193942, 6036914, 19167654, 13327079, 12031795, 3270065, 1250882, 33757175, 19951656, 2055080, 12894865, 135031164, 798094, 8860588, 199579, 12267493, 6144562, 9118773, 43997828, 42292929, 1133066, 38139640, 5701579, 10276158, 29170398, 11746035, 12311143], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x3", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [40301927, 9119152, 190010647, 33390141, 16284741, 44227550, 4133884, 11416987, 9319622, 13755680, 6939688, 12572928, 8502814, 7483763, 2780132, 108700891, 5675356, 3242173, 6667147, 28674757, 3942491, 1056608, 301139947, 3447496, 26084662], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x4", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y4"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [20434176, 4115771], "sizemode": "area", "sizeref": 366300.86, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [34435.367439999995, 25185.00911], "xaxis": "x5", "y": [81.235, 80.204], "yaxis": "y5"}],
                        {"annotations": [{"font": {}, "showarrow": false, "text": "continent=Asia", "x": 0.09000000000000001, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Europe", "x": 0.29000000000000004, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Africa", "x": 0.49000000000000005, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Americas", "x": 0.6900000000000002, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Oceania", "x": 0.8900000000000001, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}], "height": 600, "legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.18000000000000002], "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis2": {"anchor": "y2", "domain": [0.2, 0.38], "matches": "x", "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis3": {"anchor": "y3", "domain": [0.4, 0.5800000000000001], "matches": "x", "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis4": {"anchor": "y4", "domain": [0.6000000000000001, 0.7800000000000001], "matches": "x", "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis5": {"anchor": "y5", "domain": [0.8, 0.9800000000000001], "matches": "x", "title": {"text": "gdpPercap"}, "type": "log"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "lifeExp"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis5": {"anchor": "x5", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('8603926a-154b-47df-91dd-38aec919300e');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(gapminder, x="gdpPercap", y="lifeExp",
           animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", 
           facet_col="continent",
           log_x=True, size_max=45, range_x=[100, 100000], range_y=[25, 90])
```


<div>


            <div id="712b2a58-acb5-4423-ba56-a10fca39f2f9" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("712b2a58-acb5-4423-ba56-a10fca39f2f9")) {
                    Plotly.newPlot(
                        '712b2a58-acb5-4423-ba56-a10fca39f2f9',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [8425333, 120447, 46886859, 4693836, 556263527, 2125900, 372000000, 82052000, 17272000, 5441766, 1620914, 86459025, 607914, 8865488, 20947571, 160000, 1439529, 6748378, 800663, 20092996, 9182536, 507833, 41346560, 22438691, 4005677, 1127000, 7982342, 3661549, 8550362, 21289402, 26246839, 1030585, 4963829], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "type": "scatter", "x": [779.4453145, 9867.084765000001, 684.2441716, 368.46928560000003, 400.44861099999997, 3054.421209, 546.5657493, 749.6816546, 3035.326002, 4129.766056, 4086.522128, 3216.956347, 1546.907807, 1088.277758, 1030.592226, 108382.3529, 4834.804067, 1831.132894, 786.5668575, 331.0, 545.8657228999999, 1828.230307, 684.5971437999999, 1272.880995, 6459.5548229999995, 2315.138227, 1083.53203, 1643.485354, 1206.947913, 757.7974177, 605.0664917, 1515.5923289999998, 781.7175761], "xaxis": "x", "y": [28.801, 50.93899999999999, 37.484, 39.417, 44.0, 60.96, 37.373000000000005, 37.468, 44.869, 45.32, 65.39, 63.03, 43.158, 50.056000000000004, 47.453, 55.565, 55.928000000000004, 48.463, 42.244, 36.319, 36.157, 37.578, 43.43600000000001, 47.751999999999995, 39.875, 60.396, 57.593, 45.883, 58.5, 50.848, 40.412, 43.16, 32.548], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1282697, 6927772, 8730405, 2791000, 7274900, 3882229, 9125183, 4334000, 4090500, 42459667, 69145952, 7733250, 9504000, 147962, 2952156, 47666000, 413834, 10381988, 3327728, 25730551, 8526050, 16630000, 6860147, 3558137, 1489518, 28549870, 7124673, 4815000, 22235677, 50430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "type": "scatter", "x": [1601.056136, 6137.076492, 8343.105126999999, 973.5331947999999, 2444.2866480000002, 3119.23652, 6876.14025, 9692.385245, 6424.519071, 7029.809327, 7144.114393000001, 3530.690067, 5263.6738159999995, 7267.688428, 5210.280328, 4931.404154999999, 2647.585601, 8941.571858, 10095.42172, 4029.3296990000003, 3068.319867, 3144.613186, 3581.4594479999996, 5074.659104, 4215.041741, 3834.0347420000003, 8527.844662000001, 14734.23275, 1969.1009800000002, 9979.508487000001], "xaxis": "x2", "y": [55.23, 66.8, 68.0, 53.82, 59.6, 61.21, 66.87, 70.78, 66.55, 67.41, 67.5, 65.86, 64.03, 72.49, 66.91, 65.94, 59.163999999999994, 72.13, 72.67, 61.31, 59.82, 61.05, 57.996, 64.36, 65.57, 64.94, 71.86, 69.62, 43.585, 69.18], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [9279525, 4232095, 1738315, 442308, 4469979, 2445618, 5009067, 1291695, 2682462, 153936, 14100005, 854885, 2977019, 63149, 22223309, 216964, 1438760, 20860941, 420702, 284320, 5581001, 2664249, 580653, 6464046, 748747, 863308, 1019729, 4762912, 2917802, 3838168, 1022556, 516556, 9939217, 6446316, 485831, 3379468, 33119096, 257700, 2534927, 60011, 2755589, 2143249, 2526994, 14264935, 8504667, 290243, 8322925, 1219113, 3647735, 5824797, 2672000, 3080907], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "type": "scatter", "x": [2449.008185, 3520.610273, 1062.7522, 851.2411407, 543.2552413, 339.29645869999996, 1172.667655, 1071.310713, 1178.665927, 1102.990936, 780.5423257, 2125.621418, 1388.594732, 2669.529475, 1418.822445, 375.6431231, 328.94055710000004, 362.1462796, 4293.476475, 485.2306591, 911.2989371, 510.19649230000005, 299.850319, 853.5409189999999, 298.8462121, 575.5729961000001, 2387.54806, 1443.011715, 369.1650802, 452.3369807, 743.1159097, 1967.955707, 1688.20357, 468.5260381, 2423.780443, 761.879376, 1077.281856, 2718.885295, 493.32387520000003, 879.5835855, 1450.356983, 879.7877358, 1135.749842, 4725.295531000001, 1615.991129, 1148.376626, 716.6500721, 859.8086567, 1468.475631, 734.753484, 1147.388831, 406.8841148], "xaxis": "x3", "y": [43.077, 30.015, 38.223, 47.622, 31.975, 39.031, 38.523, 35.463, 38.092, 40.715, 39.143, 42.111000000000004, 40.477, 34.812, 41.893, 34.482, 35.928000000000004, 34.078, 37.003, 30.0, 43.148999999999994, 33.609, 32.5, 42.27, 42.138000000000005, 38.48, 42.723, 36.681, 36.256, 33.685, 40.543, 50.986000000000004, 42.873000000000005, 31.285999999999998, 41.725, 37.444, 36.324, 52.724, 40.0, 46.471000000000004, 37.278, 30.331, 32.978, 45.00899999999999, 38.635, 41.407, 41.215, 38.596, 44.6, 39.978, 42.038000000000004, 48.451], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [17876956, 2883315, 56602560, 14785584, 6377619, 12350771, 926317, 6007797, 2491346, 3548753, 2042865, 3146381, 3201488, 1517453, 1426095, 30144317, 1165790, 940080, 1555876, 8025700, 2227000, 662850, 157553000, 2252965, 5439568], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "type": "scatter", "x": [5911.315053, 2677.3263469999997, 2108.944355, 11367.16112, 3939.9787890000002, 2144.115096, 2627.0094710000003, 5586.53878, 1397.7171369999999, 3522.110717, 3048.3029, 2428.2377690000003, 1840.366939, 2194.926204, 2898.5308809999997, 3478.125529, 3112.363948, 2480.380334, 1952.3087010000002, 3758.523437, 3081.959785, 3023.271928, 13990.482080000002, 5716.766744, 7689.799761], "xaxis": "x4", "y": [62.485, 40.414, 50.917, 68.75, 54.745, 50.643, 57.206, 59.42100000000001, 45.928000000000004, 48.357, 45.262, 42.023, 37.579, 41.912, 58.53, 50.788999999999994, 42.31399999999999, 55.191, 62.648999999999994, 43.902, 64.28, 59.1, 68.44, 66.071, 55.088], "yaxis": "y4"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [8691212, 1994794], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "type": "scatter", "x": [10039.595640000001, 10556.575659999999], "xaxis": "x5", "y": [69.12, 69.39], "yaxis": "y5"}],
                        {"annotations": [{"font": {}, "showarrow": false, "text": "continent=Asia", "x": 0.09000000000000001, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Europe", "x": 0.29000000000000004, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Africa", "x": 0.49000000000000005, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Americas", "x": 0.6900000000000002, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "continent=Oceania", "x": 0.8900000000000001, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}], "height": 600, "legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "sliders": [{"active": 0, "currentvalue": {"prefix": "year="}, "len": 0.9, "pad": {"b": 10, "t": 60}, "steps": [{"args": [["1952"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1952", "method": "animate"}, {"args": [["1957"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1957", "method": "animate"}, {"args": [["1962"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1962", "method": "animate"}, {"args": [["1967"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1967", "method": "animate"}, {"args": [["1972"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1972", "method": "animate"}, {"args": [["1977"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1977", "method": "animate"}, {"args": [["1982"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1982", "method": "animate"}, {"args": [["1987"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1987", "method": "animate"}, {"args": [["1992"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1992", "method": "animate"}, {"args": [["1997"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "1997", "method": "animate"}, {"args": [["2002"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "2002", "method": "animate"}, {"args": [["2007"], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "2007", "method": "animate"}], "x": 0.1, "xanchor": "left", "y": 0, "yanchor": "top"}], "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "updatemenus": [{"buttons": [{"args": [null, {"frame": {"duration": 500, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 500, "easing": "linear"}}], "label": "&#9654;", "method": "animate"}, {"args": [[null], {"frame": {"duration": 0, "redraw": false}, "fromcurrent": true, "mode": "immediate", "transition": {"duration": 0, "easing": "linear"}}], "label": "&#9724;", "method": "animate"}], "direction": "left", "pad": {"r": 10, "t": 70}, "showactive": false, "type": "buttons", "x": 0.1, "xanchor": "right", "y": 0, "yanchor": "top"}], "xaxis": {"anchor": "y", "domain": [0.0, 0.18000000000000002], "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis2": {"anchor": "y2", "domain": [0.2, 0.38], "matches": "x", "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis3": {"anchor": "y3", "domain": [0.4, 0.5800000000000001], "matches": "x", "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis4": {"anchor": "y4", "domain": [0.6000000000000001, 0.7800000000000001], "matches": "x", "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "xaxis5": {"anchor": "y5", "domain": [0.8, 0.9800000000000001], "matches": "x", "range": [2.0, 5.0], "title": {"text": "gdpPercap"}, "type": "log"}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "range": [25, 90], "title": {"text": "lifeExp"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}, "yaxis5": {"anchor": "x5", "domain": [0.0, 1.0], "matches": "y", "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){
                            Plotly.addFrames('712b2a58-acb5-4423-ba56-a10fca39f2f9', [{"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [8425333, 120447, 46886859, 4693836, 556263527, 2125900, 372000000, 82052000, 17272000, 5441766, 1620914, 86459025, 607914, 8865488, 20947571, 160000, 1439529, 6748378, 800663, 20092996, 9182536, 507833, 41346560, 22438691, 4005677, 1127000, 7982342, 3661549, 8550362, 21289402, 26246839, 1030585, 4963829], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [779.4453145, 9867.084765000001, 684.2441716, 368.46928560000003, 400.44861099999997, 3054.421209, 546.5657493, 749.6816546, 3035.326002, 4129.766056, 4086.522128, 3216.956347, 1546.907807, 1088.277758, 1030.592226, 108382.3529, 4834.804067, 1831.132894, 786.5668575, 331.0, 545.8657228999999, 1828.230307, 684.5971437999999, 1272.880995, 6459.5548229999995, 2315.138227, 1083.53203, 1643.485354, 1206.947913, 757.7974177, 605.0664917, 1515.5923289999998, 781.7175761], "xaxis": "x", "y": [28.801, 50.93899999999999, 37.484, 39.417, 44.0, 60.96, 37.373000000000005, 37.468, 44.869, 45.32, 65.39, 63.03, 43.158, 50.056000000000004, 47.453, 55.565, 55.928000000000004, 48.463, 42.244, 36.319, 36.157, 37.578, 43.43600000000001, 47.751999999999995, 39.875, 60.396, 57.593, 45.883, 58.5, 50.848, 40.412, 43.16, 32.548], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1282697, 6927772, 8730405, 2791000, 7274900, 3882229, 9125183, 4334000, 4090500, 42459667, 69145952, 7733250, 9504000, 147962, 2952156, 47666000, 413834, 10381988, 3327728, 25730551, 8526050, 16630000, 6860147, 3558137, 1489518, 28549870, 7124673, 4815000, 22235677, 50430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [1601.056136, 6137.076492, 8343.105126999999, 973.5331947999999, 2444.2866480000002, 3119.23652, 6876.14025, 9692.385245, 6424.519071, 7029.809327, 7144.114393000001, 3530.690067, 5263.6738159999995, 7267.688428, 5210.280328, 4931.404154999999, 2647.585601, 8941.571858, 10095.42172, 4029.3296990000003, 3068.319867, 3144.613186, 3581.4594479999996, 5074.659104, 4215.041741, 3834.0347420000003, 8527.844662000001, 14734.23275, 1969.1009800000002, 9979.508487000001], "xaxis": "x2", "y": [55.23, 66.8, 68.0, 53.82, 59.6, 61.21, 66.87, 70.78, 66.55, 67.41, 67.5, 65.86, 64.03, 72.49, 66.91, 65.94, 59.163999999999994, 72.13, 72.67, 61.31, 59.82, 61.05, 57.996, 64.36, 65.57, 64.94, 71.86, 69.62, 43.585, 69.18], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [9279525, 4232095, 1738315, 442308, 4469979, 2445618, 5009067, 1291695, 2682462, 153936, 14100005, 854885, 2977019, 63149, 22223309, 216964, 1438760, 20860941, 420702, 284320, 5581001, 2664249, 580653, 6464046, 748747, 863308, 1019729, 4762912, 2917802, 3838168, 1022556, 516556, 9939217, 6446316, 485831, 3379468, 33119096, 257700, 2534927, 60011, 2755589, 2143249, 2526994, 14264935, 8504667, 290243, 8322925, 1219113, 3647735, 5824797, 2672000, 3080907], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [2449.008185, 3520.610273, 1062.7522, 851.2411407, 543.2552413, 339.29645869999996, 1172.667655, 1071.310713, 1178.665927, 1102.990936, 780.5423257, 2125.621418, 1388.594732, 2669.529475, 1418.822445, 375.6431231, 328.94055710000004, 362.1462796, 4293.476475, 485.2306591, 911.2989371, 510.19649230000005, 299.850319, 853.5409189999999, 298.8462121, 575.5729961000001, 2387.54806, 1443.011715, 369.1650802, 452.3369807, 743.1159097, 1967.955707, 1688.20357, 468.5260381, 2423.780443, 761.879376, 1077.281856, 2718.885295, 493.32387520000003, 879.5835855, 1450.356983, 879.7877358, 1135.749842, 4725.295531000001, 1615.991129, 1148.376626, 716.6500721, 859.8086567, 1468.475631, 734.753484, 1147.388831, 406.8841148], "xaxis": "x3", "y": [43.077, 30.015, 38.223, 47.622, 31.975, 39.031, 38.523, 35.463, 38.092, 40.715, 39.143, 42.111000000000004, 40.477, 34.812, 41.893, 34.482, 35.928000000000004, 34.078, 37.003, 30.0, 43.148999999999994, 33.609, 32.5, 42.27, 42.138000000000005, 38.48, 42.723, 36.681, 36.256, 33.685, 40.543, 50.986000000000004, 42.873000000000005, 31.285999999999998, 41.725, 37.444, 36.324, 52.724, 40.0, 46.471000000000004, 37.278, 30.331, 32.978, 45.00899999999999, 38.635, 41.407, 41.215, 38.596, 44.6, 39.978, 42.038000000000004, 48.451], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [17876956, 2883315, 56602560, 14785584, 6377619, 12350771, 926317, 6007797, 2491346, 3548753, 2042865, 3146381, 3201488, 1517453, 1426095, 30144317, 1165790, 940080, 1555876, 8025700, 2227000, 662850, 157553000, 2252965, 5439568], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [5911.315053, 2677.3263469999997, 2108.944355, 11367.16112, 3939.9787890000002, 2144.115096, 2627.0094710000003, 5586.53878, 1397.7171369999999, 3522.110717, 3048.3029, 2428.2377690000003, 1840.366939, 2194.926204, 2898.5308809999997, 3478.125529, 3112.363948, 2480.380334, 1952.3087010000002, 3758.523437, 3081.959785, 3023.271928, 13990.482080000002, 5716.766744, 7689.799761], "xaxis": "x4", "y": [62.485, 40.414, 50.917, 68.75, 54.745, 50.643, 57.206, 59.42100000000001, 45.928000000000004, 48.357, 45.262, 42.023, 37.579, 41.912, 58.53, 50.788999999999994, 42.31399999999999, 55.191, 62.648999999999994, 43.902, 64.28, 59.1, 68.44, 66.071, 55.088], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1952<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [8691212, 1994794], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [10039.595640000001, 10556.575659999999], "xaxis": "x5", "y": [69.12, 69.39], "yaxis": "y5", "type": "scatter"}], "name": "1952"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [9240934, 138655, 51365468, 5322536, 637408000, 2736300, 409000000, 90124000, 19792000, 6248643, 1944401, 91563009, 746559, 9411381, 22611552, 212846, 1647412, 7739235, 882134, 21731844, 9682338, 561977, 46679944, 26072194, 4419650, 1445929, 9128546, 4149908, 10164215, 25041917, 28998543, 1070439, 5498090], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [820.8530296, 11635.79945, 661.6374577, 434.0383364, 575.9870009, 3629.076457, 590.061996, 858.9002707000001, 3290.257643, 6229.333562, 5385.278451, 4317.694365, 1886.080591, 1571.134655, 1487.593537, 113523.1329, 6089.786934000001, 1810.0669920000003, 912.6626085, 350.0, 597.9363557999999, 2242.746551, 747.0835292, 1547.9448439999999, 8157.591248000001, 2843.104409, 1072.546602, 2117.234893, 1507.86129, 793.5774147999999, 676.2854477999999, 1827.0677420000002, 804.8304547], "xaxis": "x", "y": [30.331999999999997, 53.832, 39.348, 41.36600000000001, 50.54896, 64.75, 40.249, 39.918, 47.181000000000004, 48.437, 67.84, 65.5, 45.669, 54.081, 52.681000000000004, 58.033, 59.489, 52.102, 45.248000000000005, 41.905, 37.686, 40.08, 45.556999999999995, 51.333999999999996, 42.868, 63.178999999999995, 61.456, 48.284, 62.4, 53.63, 42.887, 45.67100000000001, 33.97], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1476505, 6965860, 8989111, 3076000, 7651254, 3991242, 9513758, 4487831, 4324000, 44310863, 71019069, 8096218, 9839000, 165110, 2878220, 49182000, 442829, 11026383, 3491938, 28235346, 8817650, 17829327, 7271135, 3844277, 1533070, 29841614, 7363802, 5126000, 25670939, 51430000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [1942.2842440000002, 8842.59803, 9714.960623, 1353.989176, 3008.670727, 4338.231617, 8256.343918, 11099.65935, 7545.415386, 8662.834898000001, 10187.82665, 4916.299889, 6040.180011, 9244.001412, 5599.077872, 6248.656232, 3682.259903, 11276.193440000001, 11653.97304, 4734.253019, 3774.571743, 3943.370225, 4981.090891, 6093.2629799999995, 5862.276629, 4564.80241, 9911.878226, 17909.48973, 2218.754257, 11283.17795], "xaxis": "x2", "y": [59.28, 67.48, 69.24, 58.45, 66.61, 64.77, 69.03, 71.81, 67.49, 68.93, 69.1, 67.86, 66.41, 73.47, 68.9, 67.81, 61.448, 72.99, 73.44, 65.77, 61.51, 64.1, 61.685, 67.45, 67.85, 66.66, 72.49, 70.56, 48.07899999999999, 70.42], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [10270856, 4561361, 1925173, 474639, 4713416, 2667518, 5359923, 1392284, 2894855, 170928, 15577932, 940458, 3300000, 71851, 25009741, 232922, 1542611, 22815614, 434904, 323150, 6391288, 2876726, 601095, 7454779, 813338, 975950, 1201578, 5181679, 3221238, 4241884, 1076852, 609816, 11406350, 7038035, 548080, 3692184, 37173340, 308700, 2822082, 61325, 3054547, 2295678, 2780415, 16151549, 9753392, 326741, 9452826, 1357445, 3950849, 6675501, 3016000, 3646340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [3013.976023, 3827.9404649999997, 959.6010805, 918.2325348999999, 617.1834647999999, 379.56462810000005, 1313.048099, 1190.844328, 1308.495577, 1211.1485480000001, 905.8602302999999, 2315.056572, 1500.895925, 2864.9690760000003, 1458.915272, 426.0964081, 344.16188589999996, 378.90416319999997, 4976.198099, 520.9267111, 1043.5615369999998, 576.2670245, 431.7904566000001, 944.4383152, 335.99711510000003, 620.9699901, 3448.284395, 1589.20275, 416.36980639999996, 490.3821867, 846.1202613, 2034.037981, 1642.002314, 495.5868333000001, 2621.448058, 835.5234025000001, 1100.5925630000002, 2769.451844, 540.2893982999999, 860.7369026, 1567.653006, 1004.484437, 1258.1474130000001, 5487.104219, 1770.3370739999998, 1244.708364, 698.5356073, 925.9083201999999, 1395.232468, 774.3710692000001, 1311.956766, 518.7642681], "xaxis": "x3", "y": [45.685, 31.999000000000002, 40.358000000000004, 49.618, 34.906, 40.533, 40.428000000000004, 37.464, 39.881, 42.46, 40.652, 45.053000000000004, 42.468999999999994, 37.328, 44.443999999999996, 35.983000000000004, 38.047, 36.667, 38.999, 32.065, 44.778999999999996, 34.558, 33.489000000000004, 44.68600000000001, 45.047, 39.486, 45.288999999999994, 38.865, 37.207, 35.306999999999995, 42.338, 58.089, 45.423, 33.779, 45.226000000000006, 38.598, 37.802, 55.09, 41.5, 48.945, 39.329, 31.57, 34.977, 47.985, 39.624, 43.424, 42.974, 41.208, 47.1, 42.571000000000005, 44.077, 50.468999999999994], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [19610538, 3211738, 65551171, 17010154, 7048426, 14485993, 1112300, 6640752, 2923186, 4058385, 2355805, 3640876, 3507701, 1770390, 1535090, 35015548, 1358828, 1063506, 1770902, 9146100, 2260000, 764900, 171984000, 2424959, 6702668], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [6856.856212000001, 2127.686326, 2487.365989, 12489.95006, 4315.6227229999995, 2323.805581, 2990.010802, 6092.174359000001, 1544.402995, 3780.5466509999997, 3421.523218, 2617.155967, 1726.887882, 2220.487682, 4756.525781, 4131.546641, 3457.415947, 2961.800905, 2046.1547059999998, 4245.256697999999, 3907.1561890000003, 4100.3934, 14847.12712, 6150.772969, 9802.466526], "xaxis": "x4", "y": [64.399, 41.89, 53.285, 69.96, 56.074, 55.118, 60.026, 62.325, 49.828, 51.356, 48.57, 44.141999999999996, 40.696, 44.665, 62.61, 55.19, 45.431999999999995, 59.201, 63.196000000000005, 46.263000000000005, 68.54, 61.8, 69.49, 67.044, 57.907], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1957<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [9712569, 2229407], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [10949.64959, 12247.39532], "xaxis": "x5", "y": [70.33, 70.26], "yaxis": "y5", "type": "scatter"}], "name": "1957"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [10267083, 171863, 56839289, 6083619, 665770000, 3305200, 454000000, 99028000, 22874000, 7240260, 2310904, 95831757, 933559, 10917494, 26420307, 358266, 1886848, 8906385, 1010280, 23634436, 10332057, 628164, 53100671, 30325264, 4943029, 1750200, 10421936, 4834621, 11918938, 29263397, 33796140, 1133134, 6120081], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [853.1007099999999, 12753.27514, 686.3415537999999, 496.9136476, 487.6740183, 4692.648271999999, 658.3471509, 849.2897700999999, 4187.329802, 8341.737815, 7105.630706, 6576.649461, 2348.009158, 1621.693598, 1536.3443869999999, 95458.11176, 5714.560611, 2036.8849440000001, 1056.353958, 388.0, 652.3968593, 2924.638113, 803.3427418, 1649.5521529999999, 11626.41975, 3674.735572, 1074.4719599999999, 2193.037133, 1822.879028, 1002.1991720000001, 772.0491602000001, 2198.9563120000003, 825.6232006], "xaxis": "x", "y": [31.997, 56.923, 41.216, 43.415, 44.50136, 67.65, 43.605, 42.518, 49.325, 51.457, 69.39, 68.73, 48.126000000000005, 56.656000000000006, 55.292, 60.47, 62.093999999999994, 55.736999999999995, 48.251000000000005, 45.108000000000004, 39.393, 43.165, 47.67, 54.757, 45.913999999999994, 65.798, 62.192, 50.305, 65.2, 56.06100000000001, 45.363, 48.126999999999995, 35.18], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1728137, 7129864, 9218400, 3349000, 8012946, 4076557, 9620282, 4646899, 4491443, 47124000, 73739117, 8448233, 10063000, 182053, 2830000, 50843200, 474528, 11805689, 3638919, 30329617, 9019800, 18680721, 7616060, 4237384, 1582962, 31158061, 7561588, 5666000, 29788695, 53292000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2312.888958, 10750.721109999999, 10991.20676, 1709.683679, 4254.337839, 5477.890018, 10136.86713, 13583.31351, 9371.842561, 10560.48553, 12902.46291, 6017.190732999999, 7550.359877, 10350.15906, 6631.597314, 8243.58234, 4649.593785, 12790.849559999999, 13450.40151, 5338.752143, 4727.954889, 4734.9975859999995, 6289.629157, 7481.1075980000005, 7402.303395, 5693.843879, 12329.441920000001, 20431.0927, 2322.8699079999997, 12477.17707], "xaxis": "x2", "y": [64.82, 69.54, 70.25, 61.93, 69.51, 67.13, 69.9, 72.35, 68.75, 70.51, 70.3, 69.51, 67.96, 73.68, 70.29, 69.24, 63.728, 73.23, 73.47, 67.64, 64.39, 66.8, 64.531, 70.33, 69.15, 69.69, 73.37, 71.32, 52.098, 70.76], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [11000948, 4826015, 2151895, 512764, 4919632, 2961915, 5793633, 1523478, 3150417, 191689, 17486434, 1047924, 3832408, 89898, 28173309, 249220, 1666618, 25145372, 455661, 374020, 7355248, 3140003, 627820, 8678557, 893143, 1112796, 1441863, 5703324, 3628608, 4690372, 1146757, 701016, 13056604, 7788944, 621392, 4076008, 41871351, 358900, 3051242, 65345, 3430243, 2467895, 3080153, 18356657, 11183227, 370006, 10863958, 1528098, 4286552, 7688797, 3421000, 4277736], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [2550.81688, 4269.276742, 949.4990641, 983.6539764, 722.5120206, 355.2032273, 1399.607441, 1193.068753, 1389.817618, 1406.648278, 896.3146335000001, 2464.783157, 1728.8694280000002, 3020.989263, 1693.335853, 582.8419713999999, 380.99584330000005, 419.4564161, 6631.4592219999995, 599.650276, 1190.0411179999999, 686.3736739, 522.0343725, 896.9663732, 411.80062660000004, 634.1951625, 6757.0308159999995, 1643.38711, 427.90108560000004, 496.17434280000003, 1055.8960359999999, 2529.0674870000003, 1566.353493, 556.6863539, 3173.215595, 997.7661127, 1150.9274779999998, 3173.72334, 597.4730727000001, 1071.551119, 1654.988723, 1116.6398769999998, 1369.488336, 5768.729717, 1959.593767, 1856.182125, 722.0038073, 1067.5348099999999, 1660.30321, 767.2717397999999, 1452.725766, 527.2721818], "xaxis": "x3", "y": [48.303000000000004, 34.0, 42.618, 51.52, 37.814, 42.045, 42.643, 39.475, 41.716, 44.467, 42.122, 48.435, 44.93, 39.693000000000005, 46.992, 37.485, 40.158, 40.059, 40.489000000000004, 33.896, 46.452, 35.753, 34.488, 47.949, 47.747, 40.501999999999995, 47.808, 40.848, 38.41, 36.936, 44.248000000000005, 60.246, 47.924, 36.161, 48.386, 39.486999999999995, 39.36, 57.666000000000004, 43.0, 51.893, 41.45399999999999, 32.766999999999996, 36.981, 49.951, 40.87, 44.992, 44.246, 43.922, 49.57899999999999, 45.343999999999994, 46.023, 52.358000000000004], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [21283783, 3593918, 76039390, 18985849, 7961258, 17009885, 1345187, 7254373, 3453434, 4681707, 2747687, 4208858, 3880130, 2090162, 1665128, 41121485, 1590597, 1215725, 2009813, 10516500, 2448046, 887498, 186538000, 2598466, 8143375], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [7133.166023000001, 2180.972546, 3336.585802, 13462.48555, 4519.094331, 2492.351109, 3460.937025, 5180.75591, 1662.137359, 4086.114078, 3776.8036270000002, 2750.364446, 1796.589032, 2291.1568350000002, 5246.107524, 4581.609385, 3634.364406, 3536.540301, 2148.027146, 4957.037982, 5108.34463, 4997.5239710000005, 16173.145859999999, 5603.357717, 8422.974165000001], "xaxis": "x4", "y": [65.142, 43.428000000000004, 55.665, 71.3, 57.924, 57.863, 62.842, 65.24600000000001, 53.458999999999996, 54.64, 52.306999999999995, 46.95399999999999, 43.59, 48.041000000000004, 65.61, 58.299, 48.632, 61.817, 64.361, 49.096000000000004, 69.62, 64.9, 70.21, 68.253, 60.77], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1962<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [10794968, 2488550], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [12217.226859999999, 13175.678], "xaxis": "x5", "y": [70.93, 71.24], "yaxis": "y5", "type": "scatter"}], "name": "1962"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [11537966, 202182, 62821884, 6960067, 754550000, 3722800, 506000000, 109343000, 26538000, 8519282, 2693585, 100825279, 1255058, 12617009, 30131000, 575003, 2186894, 10154878, 1149500, 25870271, 11261690, 714775, 60641899, 35356600, 5618198, 1977600, 11737396, 5680812, 13648692, 34024249, 39463910, 1142636, 6740785], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [836.1971382, 14804.6727, 721.1860862000001, 523.4323142, 612.7056934, 6197.962814, 700.7706107000001, 762.4317721, 5906.731804999999, 8931.459811, 8393.741404, 9847.788606999999, 2741.796252, 2143.540609, 2029.2281420000002, 80894.88326, 6006.983042, 2277.742396, 1226.04113, 349.0, 676.4422254, 4720.942687, 942.4082588, 1814.12743, 16903.04886, 4977.41854, 1135.514326, 1881.923632, 2643.8586809999997, 1295.46066, 637.1232887, 2649.7150070000002, 862.4421463], "xaxis": "x", "y": [34.02, 59.923, 43.453, 45.415, 58.381119999999996, 70.0, 47.193000000000005, 45.964, 52.468999999999994, 54.458999999999996, 70.75, 71.43, 51.629, 59.942, 57.716, 64.624, 63.87, 59.371, 51.253, 49.379, 41.472, 46.988, 49.8, 56.393, 49.901, 67.946, 64.266, 53.655, 67.5, 58.285, 47.838, 51.631, 36.984], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [1984060, 7376998, 9556500, 3585000, 8310226, 4174366, 9835109, 4838800, 4605744, 49569000, 76368453, 8716441, 10223422, 198676, 2900100, 52667100, 501035, 12596822, 3786019, 31785378, 9103000, 19284814, 7971222, 4442238, 1646912, 32850275, 7867931, 6063000, 33411317, 54959000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2760.196931, 12834.6024, 13149.04119, 2172.3524230000003, 5577.0028, 6960.297861, 11399.44489, 15937.21123, 10921.63626, 12999.91766, 14745.62561, 8513.097016, 9326.64467, 13319.89568, 7655.568963, 10022.40131, 5907.850937, 15363.25136, 16361.87647, 6557.152776, 6361.517993, 6470.866545, 7991.707066, 8412.902397, 9405.489397, 7993.512294, 15258.29697, 22966.14432, 2826.3563870000003, 14142.85089], "xaxis": "x2", "y": [66.22, 70.14, 70.94, 64.79, 70.42, 68.5, 70.38, 72.96, 69.83, 71.55, 70.8, 71.0, 69.5, 73.73, 71.08, 71.06, 67.178, 73.82, 74.08, 69.61, 66.6, 66.8, 66.914, 70.98, 69.18, 71.44, 74.16, 72.77, 54.336000000000006, 71.36], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [12760499, 5247469, 2427334, 553541, 5127935, 3330989, 6335506, 1733638, 3495967, 217378, 19941073, 1179760, 4744870, 127617, 31681188, 259864, 1820319, 27860297, 489004, 439593, 8490213, 3451418, 601287, 10191512, 996380, 1279406, 1759224, 6334556, 4147252, 5212416, 1230542, 789309, 14770296, 8680909, 706640, 4534062, 47287752, 414024, 3451079, 70787, 3965841, 2662190, 3428839, 20997321, 12716129, 420690, 12607312, 1735550, 4786986, 8900294, 3900000, 4995432], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [3246.991771, 5522.776375, 1035.831411, 1214.709294, 794.8265597, 412.97751360000007, 1508.453148, 1136.056615, 1196.810565, 1876.029643, 861.5932424, 2677.9396420000003, 2052.0504730000002, 3020.0505129999997, 1814.880728, 915.5960025, 468.7949699, 516.1186438, 8358.761987, 734.7829124, 1125.69716, 708.7595409, 715.5806402000001, 1056.736457, 498.63902649999994, 713.6036482999999, 18772.75169, 1634.047282, 495.5147806, 545.0098873, 1421.145193, 2475.387562, 1711.04477, 566.6691539, 3793.694753, 1054.384891, 1014.5141039999999, 4021.1757390000002, 510.9637142, 1384.840593, 1612.404632, 1206.043465, 1284.7331800000002, 7114.477970999999, 1687.997641, 2613.1016649999997, 848.2186575, 1477.59676, 1932.3601670000003, 908.9185217, 1777.0773179999999, 569.7950712], "xaxis": "x3", "y": [51.407, 35.985, 44.885, 53.298, 40.696999999999996, 43.548, 44.799, 41.478, 43.601000000000006, 46.472, 44.056000000000004, 52.04, 47.35, 42.074, 49.293, 38.986999999999995, 42.18899999999999, 42.115, 44.598, 35.857, 48.071999999999996, 37.196999999999996, 35.492, 50.653999999999996, 48.492, 41.536, 50.227, 42.881, 39.486999999999995, 38.486999999999995, 46.288999999999994, 61.556999999999995, 50.335, 38.113, 51.159, 40.118, 41.04, 60.542, 44.1, 54.425, 43.563, 34.113, 38.977, 51.927, 42.858000000000004, 46.633, 45.757, 46.769, 52.053000000000004, 48.051, 47.768, 53.995], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [22934225, 4040665, 88049823, 20819767, 8858908, 19764027, 1588717, 8139332, 4049146, 5432424, 3232927, 4690773, 4318137, 2500689, 1861096, 47995559, 1865490, 1405486, 2287985, 12132200, 2648961, 960155, 198712000, 2748579, 9709552], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8052.953020999999, 2586.886053, 3429.864357, 16076.58803, 5106.654313, 2678.729839, 4161.727834, 5690.268015, 1653.7230029999998, 4579.074215, 4358.595393, 3242.5311469999997, 1452.057666, 2538.269358, 6124.703450999999, 5754.733883, 4643.393534000001, 4421.009084, 2299.376311, 5788.09333, 6929.277714, 5621.368472, 19530.365569999998, 5444.61962, 9541.474188], "xaxis": "x4", "y": [65.634, 45.032, 57.632, 72.13, 60.523, 59.963, 65.42399999999999, 68.29, 56.751000000000005, 56.678000000000004, 55.855, 50.016000000000005, 46.243, 50.924, 67.51, 60.11, 51.88399999999999, 64.071, 64.95100000000001, 51.445, 71.1, 65.4, 70.76, 68.468, 63.479], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1967<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [11872264, 2728150], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [14526.12465, 14463.918930000002], "xaxis": "x5", "y": [71.1, 71.52], "yaxis": "y5", "type": "scatter"}], "name": "1967"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [13079460, 230800, 70759295, 7450606, 862030000, 4115700, 567000000, 121282000, 30614000, 10061506, 3095893, 107188273, 1613551, 14781241, 33505000, 841934, 2680018, 11441462, 1320500, 28466390, 12412593, 829050, 69325921, 40850141, 6472756, 2152400, 13016733, 6701172, 15226039, 39276153, 44655014, 1089572, 7407075], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [739.9811057999999, 18268.65839, 630.2336265, 421.6240257, 676.9000921, 8315.928145, 724.032527, 1111.107907, 9613.818607, 9576.037596, 12786.93223, 14778.78636, 2110.856309, 3701.6215030000003, 3030.87665, 109347.867, 7486.384341, 2849.09478, 1421.741975, 357.0, 674.7881296, 10618.03855, 1049.938981, 1989.3740699999998, 24837.42865, 8597.756202, 1213.39553, 2571.423014, 4062.523897, 1524.3589359999999, 699.5016441, 3133.4092769999997, 1265.047031], "xaxis": "x", "y": [36.088, 63.3, 45.251999999999995, 40.317, 63.118880000000004, 72.0, 50.651, 49.203, 55.233999999999995, 56.95, 71.63, 73.42, 56.528, 63.983000000000004, 62.611999999999995, 67.712, 65.421, 63.01, 53.754, 53.07, 43.971000000000004, 52.143, 51.928999999999995, 58.065, 53.886, 69.521, 65.042, 57.29600000000001, 69.39, 60.405, 50.254, 56.532, 39.848], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2263554, 7544201, 9709100, 3819000, 8576200, 4225310, 9862158, 4991596, 4639657, 51732000, 78717088, 8888628, 10394091, 209275, 3024400, 54365564, 527678, 13329874, 3933004, 33039545, 8970450, 20662648, 8313288, 4593433, 1694510, 34513161, 8122293, 6401400, 37492953, 56079000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3313.422188, 16661.6256, 16672.14356, 2860.16975, 6597.494398, 9164.090127, 13108.4536, 18866.20721, 14358.8759, 16107.19171, 18016.180269999997, 12724.82957, 10168.65611, 15798.063619999999, 9530.772895999999, 12269.27378, 7778.414017, 18794.74567, 18965.05551, 8006.506993000001, 9022.247417, 8011.414401999999, 10522.067490000001, 9674.167626, 12383.4862, 10638.75131, 17832.02464, 27195.113039999997, 3450.69638, 15895.116409999999], "xaxis": "x2", "y": [67.69, 70.63, 71.44, 67.45, 70.9, 69.61, 70.29, 73.47, 70.87, 72.38, 71.0, 72.34, 69.76, 74.46, 71.28, 72.19, 70.63600000000001, 73.75, 74.34, 70.85, 69.26, 69.21, 68.7, 70.35, 69.82, 73.06, 74.72, 73.78, 57.005, 72.01], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [14760787, 5894858, 2761407, 619351, 5433886, 3529983, 7021028, 1927260, 3899068, 250027, 23007669, 1340458, 6071696, 178848, 34807417, 277603, 2260187, 30770372, 537977, 517101, 9354120, 3811387, 625361, 12044785, 1116779, 1482628, 2183877, 7082430, 4730997, 5828158, 1332786, 851334, 16660670, 9809596, 821782, 5060262, 53740085, 461633, 3992121, 76595, 4588696, 2879013, 3840161, 23935810, 14597019, 480105, 14706593, 2056351, 5303507, 10190285, 4506497, 5861135], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4182.663766, 5473.288004999999, 1085.796879, 2263.6111140000003, 854.7359763000001, 464.0995039, 1684.1465280000002, 1070.013275, 1104.103987, 1937.577675, 904.8960685000001, 3213.152683, 2378.201111, 3694.2123520000005, 2024.0081469999998, 672.4122571, 514.3242081999999, 566.2439442000001, 11401.948409999999, 756.0868363, 1178.223708, 741.6662307, 820.2245876000001, 1222.359968, 496.58159220000005, 803.0054535, 21011.497209999998, 1748.562982, 584.6219709, 581.3688761, 1586.851781, 2575.4841579999998, 1930.194975, 724.9178037, 3746.080948, 954.2092363, 1698.3888379999999, 5047.658563, 590.5806637999999, 1532.985254, 1597.712056, 1353.759762, 1254.576127, 7765.962636, 1659.652775, 3364.836625, 915.9850592, 1649.660188, 2753.2859940000003, 950.735869, 1773.498265, 799.3621757999999], "xaxis": "x3", "y": [54.518, 37.928000000000004, 47.013999999999996, 56.023999999999994, 43.591, 44.056999999999995, 47.049, 43.457, 45.568999999999996, 48.943999999999996, 45.989, 54.907, 49.801, 44.36600000000001, 51.137, 40.516, 44.141999999999996, 43.515, 48.69, 38.308, 49.875, 38.842, 36.486, 53.559, 49.766999999999996, 42.614, 52.773, 44.851000000000006, 41.766000000000005, 39.977, 48.437, 62.943999999999996, 52.861999999999995, 40.328, 53.867, 40.546, 42.821000000000005, 64.274, 44.6, 56.48, 45.815, 35.4, 40.973, 53.696000000000005, 45.083, 49.552, 47.62, 49.75899999999999, 55.602, 51.016000000000005, 50.107, 55.635], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [24779799, 4565872, 100840058, 22284500, 9717524, 22542890, 1834796, 8831348, 4671329, 6298651, 3790903, 5149581, 4698301, 2965146, 1997616, 55984294, 2182908, 1616384, 2614104, 13954700, 2847132, 975199, 209896000, 2829526, 11515649], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9443.038526, 2980.331339, 4985.711467, 18970.57086, 5494.024437, 3264.660041, 5118.146939, 5305.445256, 2189.874499, 5280.99471, 4520.246008, 4031.4082710000002, 1654.456946, 2529.842345, 7433.889293000001, 6809.406690000001, 4688.593267, 5364.2496630000005, 2523.337977, 5937.827283, 9123.041742, 6619.551418999999, 21806.03594, 5703.408898, 10505.25966], "xaxis": "x4", "y": [67.065, 46.714, 59.504, 72.88, 63.441, 61.623000000000005, 67.84899999999999, 70.723, 59.631, 58.79600000000001, 58.207, 53.738, 48.042, 53.88399999999999, 69.0, 62.361000000000004, 55.151, 66.21600000000001, 65.815, 55.448, 72.16, 65.9, 71.34, 68.673, 65.712], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1972<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [13177000, 2929100], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [16788.62948, 16046.03728], "xaxis": "x5", "y": [71.93, 71.89], "yaxis": "y5", "type": "scatter"}], "name": "1972"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [14880372, 297410, 80428306, 6978607, 943455000, 4583700, 634000000, 136725000, 35480679, 11882916, 3495918, 113872473, 1937652, 16325320, 36436000, 1140357, 3115787, 12845381, 1528000, 31528087, 13933198, 1004533, 78152686, 46850962, 8128505, 2325300, 14116836, 7932503, 16785196, 44148285, 50533506, 1261091, 8403990], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [786.11336, 19340.10196, 659.8772322000001, 524.9721831999999, 741.2374699, 11186.14125, 813.3373230000001, 1382.702056, 11888.59508, 14688.235069999999, 13306.619209999999, 16610.37701, 2852.351568, 4106.301249, 4657.22102, 59265.477139999995, 8659.696836, 3827.9215710000003, 1647.511665, 371.0, 694.1124398, 11848.343920000001, 1175.921193, 2373.204287, 34167.7626, 11210.08948, 1348.775651, 3195.484582, 5596.519826, 1961.2246350000003, 713.5371196000001, 3682.8314939999996, 1829.765177], "xaxis": "x", "y": [38.438, 65.593, 46.923, 31.22, 63.96736, 73.6, 54.208, 52.702, 57.702, 60.413000000000004, 73.06, 75.38, 61.13399999999999, 67.15899999999999, 64.766, 69.343, 66.09899999999999, 65.256, 55.49100000000001, 56.059, 46.748000000000005, 57.367, 54.043, 60.06, 58.69, 70.795, 65.949, 61.195, 70.59, 62.494, 55.763999999999996, 60.765, 44.175], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2509048, 7568430, 9821800, 4086000, 8797022, 4318673, 10161915, 5088419, 4738902, 53165019, 78160773, 9308479, 10637171, 221823, 3271900, 56059245, 560073, 13852989, 4043205, 34621254, 9662600, 21658597, 8686367, 4827803, 1746919, 36439000, 8251648, 6316424, 42404033, 56179000], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3533.0039100000004, 19749.4223, 19117.97448, 3528.481305, 7612.240438, 11305.38517, 14800.160619999999, 20422.9015, 15605.422830000001, 18292.635140000002, 20512.92123, 14195.524280000001, 11674.837370000001, 19654.96247, 11150.98113, 14255.98475, 9595.929904999999, 21209.0592, 23311.34939, 9508.141454, 10172.48572, 9356.39724, 12980.66956, 10922.664040000001, 15277.030169999998, 13236.92117, 18855.72521, 26982.29052, 4269.122326, 17428.74846], "xaxis": "x2", "y": [68.93, 72.17, 72.8, 69.86, 70.81, 70.64, 70.71, 74.69, 72.52, 73.83, 72.5, 73.68, 69.95, 76.11, 72.03, 73.48, 73.066, 75.24, 75.37, 70.67, 70.41, 69.46, 70.3, 70.45, 70.97, 74.39, 75.44, 75.39, 59.507, 72.76], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [17152804, 6162675, 3168267, 781472, 5889574, 3834415, 7959865, 2167533, 4388260, 304739, 26480870, 1536769, 7459574, 228694, 38783863, 192675, 2512642, 34617799, 706367, 608274, 10538093, 4227026, 745228, 14500404, 1251524, 1703617, 2721783, 8007166, 5637246, 6491649, 1456688, 913025, 18396941, 11127868, 977026, 5682086, 62209173, 492095, 4657072, 86796, 5260855, 3140897, 4353666, 27129932, 17104986, 551425, 17129565, 2308582, 6005061, 11457758, 5216550, 6642107], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4910.4167560000005, 3008.647355, 1029.161251, 3214.857818, 743.3870368, 556.1032651, 1783.432873, 1109.374338, 1133.98495, 1172.603047, 795.757282, 3259.178978, 2517.736547, 3081.7610219999997, 2785.493582, 958.5668124, 505.7538077, 556.8083834, 21745.57328, 884.7552507000001, 993.2239571, 874.6858642999999, 764.7259627999999, 1267.613204, 745.3695408, 640.3224382999999, 21951.21176, 1544.228586, 663.2236766, 686.3952693, 1497.492223, 3710.9829630000004, 2370.619976, 502.31973339999996, 3876.4859579999998, 808.8970727999999, 1981.9518059999998, 4319.804067, 670.0806011, 1737.561657, 1561.769116, 1348.285159, 1450.9925130000001, 8028.651439, 2202.9884230000002, 3781.410618, 962.4922932, 1532.776998, 3120.876811, 843.7331372000001, 1588.688299, 685.5876821], "xaxis": "x3", "y": [58.013999999999996, 39.483000000000004, 49.19, 59.318999999999996, 46.137, 45.91, 49.355, 46.775, 47.383, 50.93899999999999, 47.803999999999995, 55.625, 52.373999999999995, 46.519, 53.318999999999996, 42.023999999999994, 44.535, 44.51, 52.79, 41.842, 51.756, 40.762, 37.465, 56.155, 52.208, 43.763999999999996, 57.442, 46.881, 43.766999999999996, 41.714, 50.852, 64.93, 55.73, 42.495, 56.437, 41.291000000000004, 44.513999999999996, 67.064, 45.0, 58.55, 48.879, 36.788000000000004, 41.974, 55.527, 47.8, 52.537, 49.919, 52.887, 59.836999999999996, 50.35, 51.386, 57.674], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [26983828, 5079716, 114313951, 23796400, 10599793, 25094412, 2108457, 9537988, 5302800, 7278866, 4282586, 5703430, 4908554, 3055235, 2156814, 63759976, 2554598, 1839782, 2984494, 15990099, 3080828, 1039009, 220239000, 2873520, 13503563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [10079.026740000001, 3548.097832, 6660.118654, 22090.88306, 4756.763836, 3815.80787, 5926.876967, 6380.494965999999, 2681.9889, 6679.62326, 5138.922374, 4879.992748, 1874.2989309999998, 3203.208066, 6650.195573, 7674.929108, 5486.371089, 5351.912144, 3248.373311, 6281.290854999999, 9770.524921, 7899.554209000001, 24072.63213, 6504.339663000001, 13143.95095], "xaxis": "x4", "y": [68.48100000000001, 50.023, 61.489, 74.21, 67.05199999999999, 63.836999999999996, 70.75, 72.649, 61.788000000000004, 61.31, 56.696000000000005, 56.028999999999996, 49.923, 57.402, 70.11, 65.032, 57.47, 68.681, 66.35300000000001, 58.446999999999996, 73.44, 68.3, 73.38, 69.48100000000001, 67.456], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1977<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [14074100, 3164900], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [18334.197509999998, 16233.7177], "xaxis": "x5", "y": [73.49, 72.22], "yaxis": "y5", "type": "scatter"}], "name": "1977"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [12881816, 377967, 93074406, 7272485, 1000281000, 5264500, 708000000, 153343000, 43072751, 14173318, 3858421, 118454974, 2347031, 17647518, 39326000, 1497494, 3086876, 14441916, 1756032, 34680442, 15796314, 1301048, 91462088, 53456774, 11254672, 2651869, 15410151, 9410494, 18501390, 48827160, 56142181, 1425876, 9657618], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [978.0114388000001, 19211.14731, 676.9818656, 624.4754784, 962.4213804999999, 14560.530509999999, 855.7235377000001, 1516.872988, 7608.334602, 14517.90711, 15367.0292, 19384.10571, 4161.415959, 4106.525293, 5622.942464, 31354.03573, 7640.519520999999, 4920.355951, 2000.603139, 424.0, 718.3730947, 12954.791009999999, 1443.429832, 2603.273765, 33693.17525, 15169.161119999999, 1648.0797890000001, 3761.8377149999997, 7426.354773999999, 2393.219781, 707.2357863, 4336.032082, 1977.5570100000002], "xaxis": "x", "y": [39.854, 69.05199999999999, 50.00899999999999, 50.957, 65.525, 75.45, 56.596000000000004, 56.159, 59.62, 62.038000000000004, 74.45, 77.11, 63.739, 69.1, 67.123, 71.309, 66.983, 68.0, 57.489, 58.056000000000004, 49.593999999999994, 62.728, 56.158, 62.082, 63.012, 71.76, 68.757, 64.59, 72.16, 64.597, 58.816, 64.406, 49.113], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [2780097, 7574613, 9856303, 4172693, 8892098, 4413368, 10303704, 5117810, 4826933, 54433565, 78335266, 9786480, 10705535, 233997, 3480000, 56535636, 562548, 14310401, 4114787, 36227381, 9859650, 22356726, 9032824, 5048043, 1861252, 37983310, 8325260, 6468126, 47328791, 56339704], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3630.880722, 21597.083619999998, 20979.84589, 4126.613157, 8224.191647, 13221.82184, 15377.22855, 21688.04048, 18533.15761, 20293.89746, 22031.532740000002, 15268.420890000001, 12545.99066, 23269.6075, 12618.321409999999, 16537.4835, 11222.58762, 21399.46046, 26298.635309999998, 8451.531004, 11753.84291, 9605.314053, 15181.0927, 11348.54585, 17866.72175, 13926.169969999999, 20667.38125, 28397.715119999997, 4241.356344, 18232.42452], "xaxis": "x2", "y": [70.42, 73.18, 73.93, 70.69, 71.08, 70.46, 70.96, 74.63, 74.55, 74.89, 73.8, 75.24, 69.39, 76.99, 73.1, 74.98, 74.101, 76.05, 75.97, 71.32, 72.77, 69.66, 70.16199999999999, 70.8, 71.063, 76.3, 76.42, 76.21, 61.036, 74.04], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [20033753, 7016384, 3641603, 970347, 6634596, 4580410, 9250831, 2476971, 4875118, 348643, 30646495, 1774735, 9025951, 305991, 45681811, 285483, 2637297, 38111756, 753874, 715523, 11400338, 4710497, 825987, 17661452, 1411807, 1956875, 3344074, 9171477, 6502825, 6998256, 1622136, 992040, 20198730, 12587223, 1099010, 6437188, 73039376, 517810, 5507565, 98593, 6147783, 3464522, 5828892, 31140029, 20367053, 649901, 19844382, 2644765, 6734098, 12939400, 6100407, 7636524], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5745.160213, 2756.953672, 1277.897616, 4551.14215, 807.1985855, 559.6032309999999, 2367.983282, 956.7529906999999, 797.9081006, 1267.100083, 673.7478181, 4879.507522, 2602.710169, 2879.4680670000002, 3503.729636, 927.8253427000001, 524.8758493, 577.8607471, 15113.36194, 835.8096107999999, 876.032569, 857.2503577, 838.1239671, 1348.225791, 797.2631074, 572.1995694, 17364.275380000003, 1302.878658, 632.8039209, 618.0140640999999, 1481.150189, 3688.037739, 2702.620356, 462.2114149, 4191.100511, 909.7221354000001, 1576.97375, 5267.219353, 881.5706467, 1890.2181170000001, 1518.479984, 1465.010784, 1176.807031, 8568.266228, 1895.544073, 3895.384018, 874.2426069, 1344.577953, 3560.2331740000004, 682.2662267999999, 1408.678565, 788.8550411], "xaxis": "x3", "y": [61.368, 39.942, 50.903999999999996, 61.483999999999995, 48.122, 47.471000000000004, 52.961000000000006, 48.295, 49.516999999999996, 52.933, 47.784, 56.695, 53.983000000000004, 48.812, 56.006, 43.662, 43.89, 44.916000000000004, 56.56399999999999, 45.58, 53.744, 42.891000000000005, 39.327, 58.766000000000005, 55.078, 44.852, 62.155, 48.968999999999994, 45.641999999999996, 43.916000000000004, 53.599, 66.711, 59.65, 42.795, 58.968, 42.598, 45.826, 69.885, 46.218, 60.351000000000006, 52.379, 38.445, 42.955, 58.161, 50.338, 55.56100000000001, 50.608000000000004, 55.471000000000004, 64.048, 49.849, 51.821000000000005, 60.363], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [29341374, 5642224, 128962939, 25201900, 11487112, 27764644, 2424367, 9789224, 5968349, 8365850, 4474873, 6395630, 5198399, 3669448, 2298309, 71640904, 2979423, 2036305, 3366439, 18125129, 3279001, 1116479, 232187835, 2953997, 15620766], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8997.897412, 3156.510452, 7030.835878, 22898.79214, 5095.665738000001, 4397.575659, 5262.734751, 7316.9181069999995, 2861.092386, 7213.7912670000005, 4098.344175, 4820.49479, 2011.1595489999997, 3121.7607940000003, 6068.05135, 9611.147541, 3470.3381560000003, 7009.601598, 4258.5036039999995, 6434.501797, 10330.98915, 9119.528607, 25009.55914, 6920.223051000001, 11152.410109999999], "xaxis": "x4", "y": [69.942, 53.858999999999995, 63.336000000000006, 75.76, 70.565, 66.653, 73.45, 73.717, 63.727, 64.342, 56.604, 58.137, 51.461000000000006, 60.909, 71.21, 67.405, 59.298, 70.472, 66.874, 61.406000000000006, 73.75, 68.832, 74.65, 70.805, 68.557], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1982<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [15184200, 3210650], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [19477.009280000002, 17632.4104], "xaxis": "x5", "y": [74.74, 73.84], "yaxis": "y5", "type": "scatter"}], "name": "1982"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [13867957, 454612, 103764241, 8371791, 1084035000, 5584510, 788000000, 169276000, 51889696, 16543189, 4203148, 122091325, 2820042, 19067554, 41622000, 1891487, 3089353, 16331785, 2015133, 38028578, 17917180, 1593882, 105186881, 60017788, 14619745, 2794552, 16495304, 11242847, 19757799, 52910342, 62826491, 1691210, 11219340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [852.3959447999999, 18524.02406, 751.9794035, 683.8955732000001, 1378.904018, 20038.472690000002, 976.5126756000001, 1748.356961, 6642.881371, 11643.57268, 17122.47986, 22375.941890000002, 4448.679912, 4106.4923149999995, 8533.088805, 28118.42998, 5377.091329, 5249.802653, 2338.008304, 385.0, 775.6324501, 18115.223130000002, 1704.686583, 2189.634995, 21198.26136, 18861.53081, 1876.766827, 3116.774285, 11054.56175, 2982.653773, 820.7994449, 5107.197384, 1971.741538], "xaxis": "x", "y": [40.821999999999996, 70.75, 52.818999999999996, 53.913999999999994, 67.274, 76.2, 58.553000000000004, 60.137, 63.04, 65.044, 75.6, 78.67, 65.869, 70.64699999999999, 69.81, 74.17399999999999, 67.926, 69.5, 60.222, 58.339, 52.537, 67.734, 58.245, 64.15100000000001, 66.295, 73.56, 69.01100000000001, 66.97399999999999, 73.4, 66.084, 62.82, 67.046, 52.922], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3075321, 7578903, 9870200, 4338977, 8971958, 4484310, 10311597, 5127024, 4931729, 55630100, 77718298, 9974490, 10612740, 244676, 3539900, 56729703, 569473, 14665278, 4186147, 37740710, 9915289, 22686371, 9230783, 5199318, 1945870, 38880702, 8421403, 6649942, 52881328, 56981620], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3738.9327350000003, 23687.82607, 22525.56308, 4314.114757, 8239.854824, 13822.58394, 16310.4434, 25116.17581, 21141.01223, 22066.44214, 24639.18566, 16120.528390000001, 12986.47998, 26923.206280000002, 13872.86652, 19207.234819999998, 11732.51017, 23651.32361, 31540.9748, 9082.351172, 13039.30876, 9696.273295, 15870.878509999999, 12037.26758, 18678.53492, 15764.98313, 23586.92927, 30281.704589999998, 5089.043686, 21664.787669999998], "xaxis": "x2", "y": [72.0, 74.94, 75.35, 71.14, 71.34, 71.52, 71.58, 74.8, 74.83, 76.34, 74.847, 76.67, 69.58, 77.23, 74.36, 76.42, 74.865, 76.83, 75.89, 70.98, 74.06, 69.53, 71.218, 71.08, 72.25, 76.9, 77.19, 77.41, 63.108000000000004, 75.007], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [23254956, 7874230, 4243788, 1151184, 7586551, 5126023, 10780667, 2840009, 5498955, 395114, 35481645, 2064095, 10761098, 311025, 52799062, 341244, 2915959, 42999530, 880397, 848406, 14168101, 5650262, 927524, 21198082, 1599200, 2269414, 3799845, 10568642, 7824747, 7634008, 1841240, 1042663, 22987397, 12891952, 1278184, 7332638, 81551520, 562035, 6349365, 110812, 7171347, 3868905, 6921858, 35933379, 24725960, 779348, 23040630, 3154264, 7724976, 15283050, 7272406, 9216418], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5681.358539, 2430.208311, 1225.85601, 6205.88385, 912.0631417000001, 621.8188188999999, 2602.664206, 844.8763504000001, 952.3861289999999, 1315.980812, 672.774812, 4201.194936999999, 2156.9560690000003, 2880.102568, 3885.4607100000003, 966.8968149, 521.1341333, 573.7413142000001, 11864.408440000001, 611.6588611000001, 847.0061135, 805.5724717999999, 736.4153921, 1361.936856, 773.9932140999999, 506.1138573, 11770.5898, 1155.4419480000001, 635.5173633999999, 684.1715576, 1421.603576, 4783.586903, 2755.046991, 389.87618460000004, 3693.7313369999997, 668.3000228, 1385.029563, 5303.377488, 847.991217, 1516.525457, 1441.72072, 1294.4477880000002, 1093.244963, 7825.823398, 1507.819159, 3984.8398119999997, 831.8220794, 1202.201361, 3810.419296, 617.7244065, 1213.315116, 706.1573059], "xaxis": "x3", "y": [65.79899999999999, 39.906, 52.336999999999996, 63.622, 49.556999999999995, 48.211000000000006, 54.985, 50.485, 51.051, 54.926, 47.412, 57.47, 54.655, 50.04, 59.797, 45.663999999999994, 46.453, 46.684, 60.19, 49.265, 55.729, 45.552, 41.245, 59.339, 57.18, 46.027, 66.234, 49.35, 47.457, 46.364, 56.145, 68.74, 62.677, 42.861000000000004, 60.835, 44.555, 46.886, 71.913, 44.02, 61.728, 55.769, 40.006, 44.501000000000005, 60.833999999999996, 51.744, 57.678000000000004, 51.535, 56.941, 66.89399999999999, 51.50899999999999, 50.821000000000005, 62.351000000000006], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [31620918, 6156369, 142938076, 26549700, 12463354, 30964245, 2799811, 10239839, 6655297, 9545158, 4842194, 7326406, 5756203, 4372203, 2326606, 80122492, 3344353, 2253639, 3886512, 20195924, 3444468, 1191336, 242803533, 3045153, 17910182], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9139.671389, 2753.6914899999997, 7807.095818000001, 26626.515030000002, 5547.063754, 4903.2191, 5629.915318, 7532.924762999999, 2899.842175, 6481.776993, 4140.442097, 4246.485974, 1823.015995, 3023.0966989999997, 6351.237495, 8688.156003, 2955.984375, 7034.779161, 3998.875695, 6360.9434439999995, 12281.34191, 7388.597823, 29884.350410000003, 7452.398969, 9883.584648], "xaxis": "x4", "y": [70.774, 57.251000000000005, 65.205, 76.86, 72.492, 67.768, 74.752, 74.17399999999999, 66.046, 67.23100000000001, 63.153999999999996, 60.782, 53.636, 64.492, 71.77, 69.498, 62.008, 71.523, 67.378, 64.134, 74.63, 69.582, 75.02, 71.918, 70.19], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1987<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [16257249, 3317166], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [21888.889030000002, 19007.19129], "xaxis": "x5", "y": [76.32, 74.32], "yaxis": "y5", "type": "scatter"}], "name": "1987"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [16317921, 529491, 113704579, 10150094, 1164970000, 5829696, 872000000, 184816000, 60397973, 17861905, 4936550, 124329269, 3867409, 20711375, 43805450, 1418095, 3219994, 18319502, 2312802, 40546538, 20326209, 1915208, 120065004, 67185766, 16945857, 3235865, 17587060, 13219062, 20686918, 56667095, 69940728, 2104779, 13367997], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [649.3413952000001, 19035.579169999997, 837.8101642999999, 682.3031755, 1655.784158, 24757.60301, 1164.406809, 2383.140898, 7235.653187999999, 3745.6406869999996, 18051.52254, 26824.895109999998, 3431.5936469999997, 3726.063507, 12104.27872, 34932.91959, 6890.806854, 7277.912802, 1785.402016, 347.0, 897.7403604, 18616.70691, 1971.8294640000001, 2279.3240170000004, 24841.617769999997, 24769.8912, 2153.7392219999997, 3340.542768, 15215.6579, 4616.8965450000005, 989.0231487, 6017.654756, 1879.496673], "xaxis": "x", "y": [41.674, 72.601, 56.018, 55.803000000000004, 68.69, 77.601, 60.223, 62.681000000000004, 65.742, 59.461000000000006, 76.93, 79.36, 68.015, 69.97800000000001, 72.244, 75.19, 69.292, 70.693, 61.271, 59.32, 55.727, 71.197, 60.838, 66.458, 68.768, 75.788, 70.37899999999999, 69.249, 74.26, 67.298, 67.66199999999999, 69.718, 55.599], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3326498, 7914969, 10045622, 4256013, 8658506, 4494013, 10315702, 5171393, 5041039, 57374179, 80597764, 10325429, 10348684, 259012, 3557761, 56840847, 621621, 15174244, 4286357, 38370697, 9927680, 22797027, 9826397, 5302888, 1999210, 39549438, 8718867, 6995447, 58179144, 57866349], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [2497.4379010000002, 27042.01868, 25575.57069, 2546.781445, 6302.6234380000005, 8447.794873, 14297.021219999999, 26406.73985, 20647.16499, 24703.79615, 26505.30317, 17541.49634, 10535.62855, 25144.39201, 17558.81555, 22013.64486, 7003.339037000001, 26790.94961, 33965.66115, 7738.881247, 16207.266630000002, 6598.409903, 9325.068238, 9498.467723, 14214.71681, 18603.06452, 23880.01683, 31871.5303, 5678.348271, 22705.09254], "xaxis": "x2", "y": [71.581, 76.04, 76.46, 72.178, 71.19, 72.527, 72.4, 75.33, 75.7, 77.46, 76.07, 77.03, 69.17, 78.77, 75.467, 77.44, 75.435, 77.42, 77.32, 70.99, 74.86, 69.36, 71.65899999999999, 71.38, 73.64, 77.57, 78.16, 78.03, 66.146, 76.42], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [26298373, 8735988, 4981671, 1342614, 8878303, 5809236, 12467171, 3265124, 6429417, 454429, 41672143, 2409073, 12772596, 384156, 59402198, 387838, 3668440, 52088559, 985739, 1025384, 16278738, 6990574, 1050938, 25020539, 1803195, 1912974, 4364501, 12210395, 10014249, 8416215, 2119465, 1096202, 25798239, 13160731, 1554253, 8392818, 93364244, 622191, 7290203, 125911, 8307920, 4260884, 6099799, 39964159, 28227588, 962344, 26605473, 3747553, 8523077, 18252190, 8381163, 10704340], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5023.216647, 2627.8456850000002, 1191.207681, 7954.111645, 931.7527731, 631.6998778, 1793.1632780000002, 747.9055252, 1058.0643, 1246.90737, 457.7191807, 4016.239529, 1648.073791, 2377.1561920000004, 3794.755195, 1132.055034, 582.8585102000001, 421.3534653, 13522.157519999999, 665.6244126, 925.0601539999999, 794.3484384, 745.5398706, 1341.9217210000002, 977.4862724999999, 636.6229191000001, 9640.138501000001, 1040.6761900000001, 563.2000145, 739.014375, 1361.369784, 6058.2538460000005, 2948.047252, 410.89682389999996, 3804.537999, 581.182725, 1619.848217, 6101.2558229999995, 737.0685949, 1428.777814, 1367.899369, 1068.696278, 926.9602964, 7225.0692579999995, 1492.197043, 3553.0224, 825.682454, 1034.298904, 4332.720164, 644.1707968999999, 1210.884633, 693.4207856], "xaxis": "x3", "y": [67.744, 40.647, 53.919, 62.745, 50.26, 44.736000000000004, 54.31399999999999, 49.396, 51.724, 57.93899999999999, 45.548, 56.433, 52.044, 51.604, 63.674, 47.545, 49.99100000000001, 48.091, 61.36600000000001, 52.644, 57.501000000000005, 48.576, 43.266000000000005, 59.285, 59.685, 40.802, 68.755, 52.214, 49.42, 48.388000000000005, 58.333, 69.745, 65.393, 44.284, 61.998999999999995, 47.391000000000005, 47.472, 73.615, 23.599, 62.742, 58.196000000000005, 38.333, 39.658, 61.888000000000005, 53.556000000000004, 58.474, 50.44, 58.06100000000001, 70.001, 48.825, 46.1, 60.376999999999995], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [33958947, 6893451, 155975974, 28523502, 13572994, 34202721, 3173216, 10723260, 7351181, 10748394, 5274649, 8486949, 6326682, 5077347, 2378618, 88111030, 4017939, 2484997, 4483945, 22430449, 3585176, 1183669, 256894189, 3149262, 20265563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [9308.41871, 2961.699694, 6950.283020999999, 26342.88426, 7596.125964, 5444.648617, 6160.416317, 5592.843963, 3044.214214, 7103.702595000001, 4444.2317, 4439.4508399999995, 1456.309517, 3081.694603, 7404.923685, 9472.384295, 2170.151724, 6618.74305, 4196.411078, 4446.380924, 14641.587109999999, 7370.990932, 32003.93224, 8137.004775, 10733.926309999999], "xaxis": "x4", "y": [71.868, 59.957, 67.057, 77.95, 74.126, 68.421, 75.71300000000001, 74.414, 68.457, 69.613, 66.798, 63.373000000000005, 55.089, 66.399, 71.766, 71.455, 65.843, 72.462, 68.225, 66.458, 73.911, 69.862, 76.09, 72.752, 71.15], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1992<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [17481977, 3437674], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [23424.76683, 18363.324940000002], "xaxis": "x5", "y": [77.56, 76.33], "yaxis": "y5", "type": "scatter"}], "name": "1992"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [22227415, 598561, 123315288, 11782962, 1230075000, 6495918, 959000000, 199278000, 63327987, 20775703, 5531387, 125956499, 4526235, 21585105, 46173816, 1765345, 3430388, 20476091, 2494803, 43247867, 23001113, 2283635, 135564834, 75012988, 21229759, 3802309, 18698655, 15081016, 21628605, 60216677, 76048996, 2826046, 15826497], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [635.341351, 20292.01679, 972.7700352, 734.28517, 2289.234136, 28377.632189999997, 1458.817442, 3119.335603, 8263.590301, 3076.239795, 20896.60924, 28816.58499, 3645.379572, 1690.756814, 15993.52796, 40300.61996, 8754.96385, 10132.90964, 1902.2521, 415.0, 1010.892138, 19702.055809999998, 2049.3505210000003, 2536.534925, 20586.69019, 33519.4766, 2664.477257, 4014.238972, 20206.82098, 5852.625497, 1385.896769, 7110.667619, 2117.484526], "xaxis": "x", "y": [41.763000000000005, 73.925, 59.412, 56.534, 70.426, 80.0, 61.765, 66.041, 68.042, 58.81100000000001, 78.26899999999999, 80.69, 69.77199999999999, 67.727, 74.64699999999999, 76.156, 70.265, 71.938, 63.625, 60.328, 59.426, 72.499, 61.818000000000005, 68.564, 70.533, 77.158, 70.457, 71.527, 75.25, 67.521, 70.672, 71.096, 58.02], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3428038, 8069876, 10199787, 3607000, 8066057, 4444595, 10300707, 5283663, 5134406, 58623428, 82011073, 10502372, 10244684, 271192, 3667233, 57479469, 692651, 15604464, 4405672, 38654957, 10156415, 22562458, 10336594, 5383010, 2011612, 39855442, 8897619, 7193761, 63047647, 58808266], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [3193.054604, 29095.920660000003, 27561.196630000002, 4766.355904, 5970.38876, 9875.604515, 16048.51424, 29804.34567, 23723.9502, 25889.78487, 27788.88416, 18747.69814, 11712.7768, 28061.099660000003, 24521.94713, 24675.02446, 6465.613349, 30246.13063, 41283.16433, 10159.58368, 17641.03156, 7346.547556999999, 7914.320304000001, 12126.23065, 17161.10735, 20445.29896, 25266.59499, 32135.323010000004, 6601.429915, 26074.53136], "xaxis": "x2", "y": [72.95, 77.51, 77.53, 73.244, 70.32, 73.68, 74.01, 76.11, 77.13, 78.64, 77.34, 77.869, 71.04, 78.95, 76.122, 78.82, 75.445, 78.03, 78.32, 72.75, 75.97, 69.72, 72.232, 72.71, 75.13, 78.77, 79.39, 79.37, 68.835, 77.218], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [29072015, 9875024, 6066080, 1536536, 10352843, 6121610, 14195809, 3696513, 7562011, 527982, 47798986, 2800947, 14625967, 417908, 66134291, 439971, 4058319, 59861301, 1126189, 1235767, 18418288, 8048834, 1193708, 28263827, 1982823, 2200725, 4759670, 14165114, 10419991, 9384984, 2444741, 1149818, 28529501, 16603334, 1774766, 9666252, 106207839, 684810, 7212583, 145608, 9535314, 4578212, 6633514, 42835005, 32160729, 1054486, 30686889, 4320890, 9231669, 21210254, 9417789, 11404948], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [4797.295051, 2277.140884, 1232.975292, 8647.142313, 946.2949617999999, 463.1151478, 1694.337469, 740.5063317, 1004.9613529999999, 1173.618235, 312.188423, 3484.1643759999997, 1786.265407, 1895.016984, 4173.181797, 2814.480755, 913.4707900000001, 515.8894013, 14722.841880000002, 653.7301704, 1005.2458119999999, 869.4497667999999, 796.6644681, 1360.4850210000002, 1186.147994, 609.1739508, 9467.446056, 986.2958956, 692.2758102999999, 790.2579846, 1483.1361359999999, 7425.705295000001, 2982.101858, 472.34607710000006, 3899.52426, 580.3052092, 1624.941275, 6071.941411, 589.9445051, 1339.076036, 1392.368347, 574.6481576, 930.5964284, 7479.188244, 1632.2107640000002, 3876.7684600000002, 789.1862231, 982.2869242999999, 4876.798614, 816.559081, 1071.353818, 792.4499602999999], "xaxis": "x3", "y": [69.152, 40.963, 54.777, 52.556000000000004, 50.324, 45.326, 52.199, 46.066, 51.573, 60.66, 42.586999999999996, 52.961999999999996, 47.99100000000001, 53.157, 67.217, 48.245, 53.378, 49.402, 60.461000000000006, 55.861000000000004, 58.556000000000004, 51.455, 44.873000000000005, 54.407, 55.558, 42.221000000000004, 71.555, 54.978, 47.495, 49.903, 60.43, 70.736, 67.66, 46.343999999999994, 58.909, 51.313, 47.464, 74.77199999999999, 36.086999999999996, 63.306000000000004, 60.187, 39.897, 43.795, 60.236000000000004, 55.373000000000005, 54.288999999999994, 48.466, 58.39, 71.973, 44.578, 40.238, 46.809], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [36203463, 7693188, 168546719, 30305843, 14599929, 37657830, 3518107, 10983007, 7992357, 11911819, 5783439, 9803875, 6913545, 5867957, 2531311, 95895146, 4609572, 2734531, 5154123, 24748122, 3759430, 1138101, 272911760, 3262838, 22374398], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [10967.28195, 3326.143191, 7957.980823999999, 28954.92589, 10118.053179999999, 6117.3617460000005, 6677.045314, 5431.990415, 3614.101285, 7429.455876999999, 5154.825496, 4684.313807, 1341.7269310000001, 3160.454906, 7121.924704000001, 9767.29753, 2253.023004, 7113.692252, 4247.400261, 5838.347657, 16999.4333, 8792.573126000001, 35767.43303, 9230.240708, 10165.49518], "xaxis": "x4", "y": [73.275, 62.05, 69.388, 78.61, 75.816, 70.313, 77.26, 76.15100000000001, 69.957, 72.312, 69.535, 66.322, 56.67100000000001, 67.65899999999999, 72.262, 73.67, 68.426, 73.738, 69.4, 68.38600000000001, 74.917, 69.465, 76.81, 74.223, 72.146], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=1997<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [18565243, 3676187], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [26997.936569999998, 21050.41377], "xaxis": "x5", "y": [78.83, 77.55], "yaxis": "y5", "type": "scatter"}], "name": "1997"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [25268405, 656397, 135656790, 12926707, 1280400000, 6762476, 1034172547, 211060000, 66907826, 24001816, 6029529, 127065841, 5307470, 22215365, 47969150, 2111561, 3677780, 22662365, 2674234, 45598081, 25873917, 2713462, 153403524, 82995088, 24501530, 4197776, 19576783, 17155814, 22454239, 62806748, 80908147, 3389578, 18701257], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [726.7340548, 23403.559269999998, 1136.3904300000002, 896.2260152999999, 3119.280896, 30209.015160000003, 1746.769454, 2873.91287, 9240.761975, 4390.717312, 21905.59514, 28604.5919, 3844.9171939999997, 1646.758151, 19233.98818, 35110.10566, 9313.93883, 10206.97794, 2140.7393230000002, 611.0, 1057.206311, 19774.83687, 2092.712441, 2650.921068, 19014.54118, 36023.1054, 3015.3788329999998, 4090.9253310000004, 23235.42329, 5913.187529, 1764.456677, 4515.487575, 2234.820827], "xaxis": "x", "y": [42.129, 74.795, 62.013000000000005, 56.751999999999995, 72.028, 81.495, 62.879, 68.58800000000001, 69.45100000000001, 57.04600000000001, 79.696, 82.0, 71.263, 66.66199999999999, 77.045, 76.904, 71.028, 73.044, 65.033, 59.908, 61.34, 74.193, 63.61, 70.303, 71.626, 78.77, 70.815, 73.053, 76.99, 68.564, 73.017, 72.37, 60.308], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3508512, 8148312, 10311970, 4165416, 7661799, 4481020, 10256295, 5374693, 5193039, 59925035, 82350671, 10603863, 10083313, 288030, 3879155, 57926999, 720230, 16122830, 4535591, 38625976, 10433867, 22404337, 10111559, 5410052, 2011497, 40152517, 8954175, 7361757, 67308928, 59912431], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [4604.211737, 32417.607689999997, 30485.88375, 6018.975239, 7696.777725, 11628.38895, 17596.210219999997, 32166.500060000002, 28204.59057, 28926.032339999998, 30035.80198, 22514.2548, 14843.93556, 31163.201960000002, 34077.04939, 27968.098169999997, 6557.194282, 33724.75778, 44683.97525, 12002.23908, 19970.90787, 7885.360081, 7236.075251, 13638.778369999998, 20660.01936, 24835.47166, 29341.630930000003, 34480.95771, 6508.085718, 29478.99919], "xaxis": "x2", "y": [75.65100000000001, 78.98, 78.32, 74.09, 72.14, 74.876, 75.51, 77.18, 78.37, 79.59, 78.67, 78.256, 72.59, 80.5, 77.783, 80.24, 73.98100000000001, 78.53, 79.05, 74.67, 77.29, 71.322, 73.21300000000001, 73.8, 76.66, 79.78, 80.04, 80.62, 70.845, 78.471], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [31287142, 10866106, 7026113, 1630347, 12251209, 7021078, 15929988, 4048013, 8835739, 614382, 55379852, 3328795, 16252726, 447416, 73312559, 495627, 4414865, 67946797, 1299304, 1457766, 20550751, 8807818, 1332459, 31386842, 2046772, 2814651, 5368585, 16473477, 11824495, 10580176, 2828858, 1200206, 31167783, 18473780, 1972153, 11140655, 119901274, 743981, 7852401, 170372, 10870037, 5359092, 7753310, 44433622, 37090298, 1130269, 34593779, 4977378, 9770575, 24739869, 10595811, 11926563], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [5288.040382, 2773.287312, 1372.877931, 11003.60508, 1037.645221, 446.4035126, 1934.0114489999999, 738.6906068, 1156.18186, 1075.811558, 241.16587650000002, 3484.06197, 1648.800823, 1908.2608670000002, 4754.604414, 7703.4959, 765.3500015, 530.0535319, 12521.71392, 660.5855997, 1111.9845779999998, 945.5835837000001, 575.7047176, 1287.514732, 1275.184575, 531.4823679, 9534.677467, 894.6370822, 665.4231186000001, 951.4097517999999, 1579.0195429999999, 9021.815894, 3258.495584, 633.6179466, 4072.3247509999997, 601.0745012, 1615.2863949999999, 6316.1652, 785.6537647999999, 1353.09239, 1519.635262, 699.4897129999999, 882.0818218000001, 7710.946444, 1993.398314, 4128.116943, 899.0742111, 886.2205765000001, 5722.895654999999, 927.7210018, 1071.6139380000002, 672.0386227000001], "xaxis": "x3", "y": [70.994, 41.003, 54.406000000000006, 46.63399999999999, 50.65, 47.36, 49.856, 43.308, 50.525, 62.974, 44.966, 52.97, 46.832, 53.373000000000005, 69.806, 49.348, 55.24, 50.725, 56.761, 58.041000000000004, 58.453, 53.676, 45.504, 50.992, 44.593, 43.753, 72.737, 57.286, 45.00899999999999, 51.818000000000005, 62.247, 71.954, 69.615, 44.026, 51.479, 54.496, 46.608000000000004, 75.744, 43.413000000000004, 64.337, 61.6, 41.012, 45.93600000000001, 53.365, 56.369, 43.869, 49.651, 57.56100000000001, 73.042, 47.813, 39.193000000000005, 39.989000000000004], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [38331121, 8445134, 179914212, 31902268, 15497046, 41008227, 3834934, 11226999, 8650322, 12921234, 6353681, 11178650, 7607651, 6677328, 2664659, 102479927, 5146848, 2990875, 5884491, 26769436, 3859606, 1101832, 287675526, 3363085, 24287670], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [8797.640716, 3413.26269, 8131.212843000001, 33328.96507, 10778.78385, 5755.259962, 7723.447195000001, 6340.646683, 4563.808154, 5773.0445119999995, 5351.568665999999, 4858.347495, 1270.364932, 3099.72866, 6994.774861, 10742.44053, 2474.548819, 7356.031934000001, 3783.674243, 5909.020073, 18855.606180000002, 11460.60023, 39097.09955, 7727.002004000001, 8605.047831], "xaxis": "x4", "y": [74.34, 63.883, 71.006, 79.77, 77.86, 71.682, 78.123, 77.158, 70.847, 74.173, 70.734, 68.97800000000001, 58.137, 68.565, 72.047, 74.902, 70.836, 74.712, 70.755, 69.906, 77.778, 68.976, 77.31, 75.307, 72.766], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=2002<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [19546792, 3908037], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [30687.75473, 23189.80135], "xaxis": "x5", "y": [80.37, 79.11], "yaxis": "y5", "type": "scatter"}], "name": "2002"}, {"data": [{"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Asia<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "ids": ["Afghanistan", "Bahrain", "Bangladesh", "Cambodia", "China", "Hong Kong, China", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Lebanon", "Malaysia", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Saudi Arabia", "Singapore", "Sri Lanka", "Syria", "Taiwan", "Thailand", "Vietnam", "West Bank and Gaza", "Yemen, Rep."], "legendgroup": "continent=Asia", "marker": {"color": "#636efa", "size": [31889923, 708573, 150448339, 14131858, 1318683096, 6980412, 1110396331, 223547000, 69453570, 27499638, 6426679, 127467972, 6053193, 23301725, 49044790, 2505559, 3921278, 24821286, 2874127, 47761980, 28901790, 3204897, 169270617, 91077287, 27601038, 4553009, 20378239, 19314747, 23174294, 65068149, 85262356, 4018332, 22211743], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Asia", "showlegend": true, "x": [974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906], "xaxis": "x", "y": [43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698], "yaxis": "y", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Europe<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "ids": ["Albania", "Austria", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Serbia", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom"], "legendgroup": "continent=Europe", "marker": {"color": "#EF553B", "size": [3600523, 8199783, 10392226, 4552198, 7322858, 4493312, 10228744, 5468120, 5238460, 61083916, 82400996, 10706290, 9956108, 301931, 4109086, 58147733, 684736, 16570613, 4627926, 38518241, 10642836, 22276056, 10150265, 5447502, 2009245, 40448191, 9031088, 7554661, 71158647, 60776238], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Europe", "showlegend": true, "x": [5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128], "xaxis": "x2", "y": [76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425], "yaxis": "y2", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Africa<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "ids": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Reunion", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"], "legendgroup": "continent=Africa", "marker": {"color": "#00cc96", "size": [33333216, 12420476, 8078314, 1639131, 14326203, 8390505, 17696293, 4369038, 10238807, 710960, 64606759, 3800610, 18013409, 496374, 80264543, 551201, 4906585, 76511887, 1454867, 1688359, 22873338, 9947814, 1472041, 35610177, 2012649, 3193942, 6036914, 19167654, 13327079, 12031795, 3270065, 1250882, 33757175, 19951656, 2055080, 12894865, 135031164, 798094, 8860588, 199579, 12267493, 6144562, 9118773, 43997828, 42292929, 1133066, 38139640, 5701579, 10276158, 29170398, 11746035, 12311143], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Africa", "showlegend": true, "x": [6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007], "xaxis": "x3", "y": [72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995], "yaxis": "y3", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Americas<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "ids": ["Argentina", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"], "legendgroup": "continent=Americas", "marker": {"color": "#ab63fa", "size": [40301927, 9119152, 190010647, 33390141, 16284741, 44227550, 4133884, 11416987, 9319622, 13755680, 6939688, 12572928, 8502814, 7483763, 2780132, 108700891, 5675356, 3242173, 6667147, 28674757, 3942491, 1056608, 301139947, 3447496, 26084662], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Americas", "showlegend": true, "x": [12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001], "xaxis": "x4", "y": [75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747], "yaxis": "y4", "type": "scatter"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "<b>%{hovertext}</b><br><br>continent=Oceania<br>year=2007<br>gdpPercap=%{x}<br>lifeExp=%{y}<br>pop=%{marker.size}", "hovertext": ["Australia", "New Zealand"], "ids": ["Australia", "New Zealand"], "legendgroup": "continent=Oceania", "marker": {"color": "#FFA15A", "size": [20434176, 4115771], "sizemode": "area", "sizeref": 651201.5288888889, "symbol": "circle"}, "mode": "markers", "name": "continent=Oceania", "showlegend": true, "x": [34435.367439999995, 25185.00911], "xaxis": "x5", "y": [81.235, 80.204], "yaxis": "y5", "type": "scatter"}], "name": "2007"}]);
                        }).then(function(){

var gd = document.getElementById('712b2a58-acb5-4423-ba56-a10fca39f2f9');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.histogram(tips,'total_bill', facet_col="time", facet_row="smoker")
```


<div>


            <div id="a6d4b7f9-385b-450b-a6c1-901bff651b0a" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("a6d4b7f9-385b-450b-a6c1-901bff651b0a")) {
                    Plotly.newPlot(
                        'a6d4b7f9-385b-450b-a6c1-901bff651b0a',
                        [{"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Dinner<br>total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 26.41, 48.27, 17.59, 20.08, 16.45, 20.23, 12.02, 17.07, 14.73, 10.51, 22.49, 22.75, 12.46, 20.92, 18.24, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 24.52, 20.76, 31.71, 20.69, 48.33, 20.45, 13.28, 11.61, 10.77, 10.07, 35.83, 29.03, 17.82, 18.78], "xaxis": "x3", "yaxis": "y3"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Lunch<br>total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": [27.2, 22.76, 17.29, 16.66, 10.07, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 7.56, 15.98], "xaxis": "x4", "yaxis": "y4"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Dinner<br>total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 3.07, 15.01, 26.86, 25.28, 17.92, 28.97, 5.75, 16.32, 40.17, 27.28, 12.03, 21.01, 11.35, 15.38, 44.3, 22.42, 15.36, 20.49, 25.21, 14.31, 17.51, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.9, 30.46, 18.15, 23.1, 15.69, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 22.12, 24.01, 15.69, 15.53, 12.6, 32.83, 27.18, 22.67], "xaxis": "x", "yaxis": "y"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Lunch<br>total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "orientation": "v", "showlegend": false, "type": "histogram", "x": [19.44, 32.68, 16.0, 19.81, 28.44, 15.48, 16.58, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 12.16, 13.42, 8.58, 13.42, 16.27, 10.09], "xaxis": "x2", "yaxis": "y2"}],
                        {"annotations": [{"font": {}, "showarrow": false, "text": "time=Dinner", "x": 0.24, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "time=Lunch", "x": 0.74, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "smoker=Yes", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.2425, "yanchor": "middle", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "smoker=No", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.7575000000000001, "yanchor": "middle", "yref": "paper"}], "barmode": "relative", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.48], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.5, 0.98], "matches": "x", "title": {"text": "total_bill"}}, "xaxis3": {"anchor": "y3", "domain": [0.0, 0.48], "matches": "x", "showticklabels": false}, "xaxis4": {"anchor": "y4", "domain": [0.5, 0.98], "matches": "x", "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.485], "title": {"text": "count"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.485], "matches": "y", "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.515, 1.0], "matches": "y", "title": {"text": "count"}}, "yaxis4": {"anchor": "x4", "domain": [0.515, 1.0], "matches": "y", "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('a6d4b7f9-385b-450b-a6c1-901bff651b0a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(tips, x="total_bill", y="tip", 
           facet_row="smoker", facet_col="time", color="sex")
```


<div>


            <div id="3e567741-942f-4edb-b828-1046f65b3e70" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("3e567741-942f-4edb-b828-1046f65b3e70")) {
                    Plotly.newPlot(
                        '3e567741-942f-4edb-b828-1046f65b3e70',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>smoker=No<br>time=Dinner<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "sex=Female", "showlegend": true, "type": "scatter", "x": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 17.07, 14.73, 22.75, 20.92, 7.25, 25.71, 17.31, 29.85, 25.0, 13.39, 16.21, 35.83, 18.78], "xaxis": "x3", "y": [1.01, 3.61, 5.0, 3.02, 1.67, 3.5, 2.75, 2.23, 3.0, 3.0, 2.45, 3.07, 2.6, 5.2, 1.5, 2.47, 3.0, 2.2, 3.25, 4.08, 1.0, 4.0, 3.5, 5.14, 3.75, 2.61, 2.0, 4.67, 3.0], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>smoker=No<br>time=Lunch<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "sex=Female", "showlegend": false, "type": "scatter", "x": [10.07, 34.83, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 15.98], "xaxis": "x4", "y": [1.83, 5.17, 1.5, 1.8, 2.92, 1.68, 2.52, 4.2, 2.0, 2.0, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.75, 3.5, 5.0, 2.3, 1.5, 1.36, 1.63, 3.0], "yaxis": "y4"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>smoker=Yes<br>time=Dinner<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "sex=Female", "showlegend": false, "type": "scatter", "x": [3.07, 26.86, 25.28, 5.75, 16.32, 11.35, 15.38, 44.3, 22.42, 14.31, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 12.76, 13.27, 28.17, 12.9, 30.14, 22.12, 27.18], "xaxis": "x", "y": [1.0, 3.14, 5.0, 1.0, 4.3, 2.5, 3.0, 2.5, 3.48, 4.0, 3.0, 1.61, 2.0, 4.0, 3.5, 3.5, 2.23, 2.5, 6.5, 1.1, 3.09, 2.88, 2.0], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>smoker=Yes<br>time=Lunch<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "sex=Female", "showlegend": false, "type": "scatter", "x": [19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 13.42, 16.27, 10.09], "xaxis": "x2", "y": [4.19, 5.0, 2.0, 2.01, 2.0, 2.5, 3.23, 3.48, 2.5, 2.0], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>smoker=No<br>time=Dinner<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "sex=Male", "showlegend": true, "type": "scatter", "x": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 48.27, 17.59, 20.08, 20.23, 12.02, 10.51, 22.49, 12.46, 18.24, 14.0, 38.07, 23.95, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 20.69, 48.33, 20.45, 13.28, 11.61, 10.77, 10.07, 29.03, 17.82], "xaxis": "x3", "y": [1.66, 3.5, 3.31, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 1.57, 3.0, 3.92, 3.71, 3.35, 4.08, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 1.45, 2.5, 3.27, 3.6, 2.0, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 1.56, 4.34, 3.51, 6.73, 2.64, 3.15, 2.01, 1.97, 1.25, 3.5, 1.5, 3.76, 3.0, 4.0, 2.55, 5.07, 2.5, 2.0, 2.74, 2.0, 2.0, 5.0, 2.0, 3.5, 2.5, 2.0, 3.48, 2.24, 4.5, 5.0, 9.0, 3.0, 2.72, 3.39, 1.47, 1.25, 5.92, 1.75], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>smoker=No<br>time=Lunch<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "sex=Male", "showlegend": false, "type": "scatter", "x": [27.2, 22.76, 17.29, 16.66, 15.98, 13.03, 18.28, 24.71, 21.16, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 34.3, 41.19, 9.78, 7.51, 7.56], "xaxis": "x4", "y": [4.0, 3.0, 2.71, 3.4, 2.03, 2.0, 4.0, 5.85, 3.0, 2.31, 2.5, 2.0, 1.48, 2.18, 1.5, 6.7, 5.0, 1.73, 2.0, 1.44], "yaxis": "y4"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>smoker=Yes<br>time=Dinner<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "sex=Male", "showlegend": false, "type": "scatter", "x": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 15.01, 17.92, 28.97, 40.17, 27.28, 12.03, 21.01, 15.36, 20.49, 25.21, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 30.46, 23.1, 15.69, 26.59, 38.73, 24.27, 30.06, 25.89, 28.15, 11.59, 7.74, 24.01, 15.69, 15.53, 12.6, 32.83, 22.67], "xaxis": "x", "y": [3.0, 1.76, 3.21, 2.0, 1.98, 3.76, 2.09, 3.08, 3.0, 4.73, 4.0, 1.5, 3.0, 1.64, 4.06, 4.29, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 2.0, 4.0, 1.5, 3.41, 3.0, 2.03, 2.0, 5.16, 3.0, 1.5, 1.44, 2.0, 3.0, 3.0, 1.0, 1.17, 2.0], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>smoker=Yes<br>time=Lunch<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "sex=Male", "showlegend": false, "type": "scatter", "x": [19.44, 32.68, 16.0, 28.44, 15.48, 16.58, 10.34, 13.51, 18.71, 20.53, 12.16, 8.58, 13.42], "xaxis": "x2", "y": [3.0, 5.0, 2.0, 2.56, 2.02, 4.0, 2.0, 2.0, 4.0, 4.0, 2.2, 1.92, 1.58], "yaxis": "y2"}],
                        {"annotations": [{"font": {}, "showarrow": false, "text": "time=Dinner", "x": 0.24, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "time=Lunch", "x": 0.74, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "smoker=Yes", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.2425, "yanchor": "middle", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "smoker=No", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.7575000000000001, "yanchor": "middle", "yref": "paper"}], "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.48], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.5, 0.98], "matches": "x", "title": {"text": "total_bill"}}, "xaxis3": {"anchor": "y3", "domain": [0.0, 0.48], "matches": "x", "showticklabels": false}, "xaxis4": {"anchor": "y4", "domain": [0.5, 0.98], "matches": "x", "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.485], "title": {"text": "tip"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.485], "matches": "y", "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.515, 1.0], "matches": "y", "title": {"text": "tip"}}, "yaxis4": {"anchor": "x4", "domain": [0.515, 1.0], "matches": "y", "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('3e567741-942f-4edb-b828-1046f65b3e70');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(tips, x="total_bill", y="tip", facet_row="time", facet_col="day", color="smoker",
          category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
```


<div>


            <div id="5b504737-66f5-49a8-9d5d-c4c6e706d50d" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("5b504737-66f5-49a8-9d5d-c4c6e706d50d")) {
                    Plotly.newPlot(
                        '5b504737-66f5-49a8-9d5d-c4c6e706d50d',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Lunch<br>day=Thur<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": true, "type": "scatter", "x": [27.2, 22.76, 17.29, 16.66, 10.07, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 7.56], "xaxis": "x5", "y": [4.0, 3.0, 2.71, 3.4, 1.83, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 1.44], "yaxis": "y5"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Lunch<br>day=Fri<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": false, "type": "scatter", "x": [15.98], "xaxis": "x6", "y": [3.0], "yaxis": "y6"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Dinner<br>day=Thur<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": false, "type": "scatter", "x": [18.78], "xaxis": "x", "y": [3.0], "yaxis": "y"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Dinner<br>day=Fri<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": false, "type": "scatter", "x": [22.49, 22.75, 12.46], "xaxis": "x2", "y": [3.5, 3.25, 1.5], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Dinner<br>day=Sat<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": false, "type": "scatter", "x": [20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 26.41, 48.27, 17.59, 20.08, 16.45, 20.23, 12.02, 17.07, 14.73, 10.51, 20.92, 18.24, 14.0, 7.25, 48.33, 20.45, 13.28, 11.61, 10.77, 10.07, 35.83, 29.03, 17.82], "xaxis": "x3", "y": [3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 1.5, 6.73, 2.64, 3.15, 2.47, 2.01, 1.97, 3.0, 2.2, 1.25, 4.08, 3.76, 3.0, 1.0, 9.0, 3.0, 2.72, 3.39, 1.47, 1.25, 4.67, 5.92, 1.75], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=No<br>time=Dinner<br>day=Sun<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=No", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "smoker=No", "showlegend": false, "type": "scatter", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.07, 23.95, 25.71, 17.31, 29.93, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 24.52, 20.76, 31.71, 20.69], "xaxis": "x4", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 4.0, 2.55, 4.0, 3.5, 5.07, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.48, 2.24, 4.5, 5.0], "yaxis": "y4"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Lunch<br>day=Thur<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "smoker=Yes", "showlegend": true, "type": "scatter", "x": [19.44, 32.68, 16.0, 19.81, 28.44, 15.48, 16.58, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47], "xaxis": "x5", "y": [3.0, 5.0, 2.0, 4.19, 2.56, 2.02, 4.0, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23], "yaxis": "y5"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Lunch<br>day=Fri<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "smoker=Yes", "showlegend": false, "type": "scatter", "x": [12.16, 13.42, 8.58, 13.42, 16.27, 10.09], "xaxis": "x6", "y": [2.2, 3.48, 1.92, 1.58, 2.5, 2.0], "yaxis": "y6"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Dinner<br>day=Fri<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "smoker=Yes", "showlegend": false, "type": "scatter", "x": [28.97, 5.75, 16.32, 40.17, 27.28, 12.03, 21.01, 11.35, 15.38], "xaxis": "x2", "y": [3.0, 1.0, 4.3, 4.73, 4.0, 1.5, 3.0, 2.5, 3.0], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Dinner<br>day=Sat<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "smoker=Yes", "showlegend": false, "type": "scatter", "x": [38.01, 11.24, 20.29, 13.81, 11.02, 18.29, 3.07, 15.01, 26.86, 25.28, 17.92, 44.3, 22.42, 15.36, 20.49, 25.21, 14.31, 10.59, 10.63, 50.81, 15.81, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 22.12, 24.01, 15.69, 15.53, 12.6, 32.83, 27.18, 22.67], "xaxis": "x3", "y": [3.0, 1.76, 3.21, 2.0, 1.98, 3.76, 1.0, 2.09, 3.14, 5.0, 3.08, 2.5, 3.48, 1.64, 4.06, 4.29, 4.0, 1.61, 2.0, 10.0, 3.16, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.88, 2.0, 3.0, 3.0, 1.0, 1.17, 2.0, 2.0], "yaxis": "y3"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "smoker=Yes<br>time=Dinner<br>day=Sun<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "smoker=Yes", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "smoker=Yes", "showlegend": false, "type": "scatter", "x": [17.51, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.9, 30.46, 18.15, 23.1, 15.69], "xaxis": "x4", "y": [3.0, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 3.5, 2.0, 3.5, 4.0, 1.5], "yaxis": "y4"}],
                        {"annotations": [{"font": {}, "showarrow": false, "text": "day=Thur", "x": 0.11499999999999999, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "day=Fri", "x": 0.365, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "day=Sat", "x": 0.615, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "day=Sun", "x": 0.865, "xanchor": "center", "xref": "paper", "y": 1.0, "yanchor": "bottom", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "time=Dinner", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.2425, "yanchor": "middle", "yref": "paper"}, {"font": {}, "showarrow": false, "text": "time=Lunch", "textangle": 90, "x": 0.98, "xanchor": "left", "xref": "paper", "y": 0.7575000000000001, "yanchor": "middle", "yref": "paper"}], "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.22999999999999998], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.24999999999999997, 0.48], "matches": "x", "title": {"text": "total_bill"}}, "xaxis3": {"anchor": "y3", "domain": [0.49999999999999994, 0.73], "matches": "x", "title": {"text": "total_bill"}}, "xaxis4": {"anchor": "y4", "domain": [0.75, 0.98], "matches": "x", "title": {"text": "total_bill"}}, "xaxis5": {"anchor": "y5", "domain": [0.0, 0.22999999999999998], "matches": "x", "showticklabels": false}, "xaxis6": {"anchor": "y6", "domain": [0.24999999999999997, 0.48], "matches": "x", "showticklabels": false}, "xaxis7": {"anchor": "y7", "domain": [0.49999999999999994, 0.73], "matches": "x", "showticklabels": false}, "xaxis8": {"anchor": "y8", "domain": [0.75, 0.98], "matches": "x", "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.485], "title": {"text": "tip"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.485], "matches": "y", "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.0, 0.485], "matches": "y", "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.0, 0.485], "matches": "y", "showticklabels": false}, "yaxis5": {"anchor": "x5", "domain": [0.515, 1.0], "matches": "y", "title": {"text": "tip"}}, "yaxis6": {"anchor": "x6", "domain": [0.515, 1.0], "matches": "y", "showticklabels": false}, "yaxis7": {"anchor": "x7", "domain": [0.515, 1.0], "matches": "y", "showticklabels": false}, "yaxis8": {"anchor": "x8", "domain": [0.515, 1.0], "matches": "y", "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('5b504737-66f5-49a8-9d5d-c4c6e706d50d');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


## Graficos en Margenes


```python
px.scatter(tips,x='total_bill',y='tip',
          marginal_x='histogram',
          marginal_y='histogram')
```


<div>


            <div id="692986a3-76d0-4b63-b922-dec909e435e9" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("692986a3-76d0-4b63-b922-dec909e435e9")) {
                    Plotly.newPlot(
                        '692986a3-76d0-4b63-b922-dec909e435e9',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}<br>tip=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "", "showlegend": false, "type": "scatter", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0], "yaxis": "y"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}<br>count=%{y}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "opacity": 0.5, "showlegend": false, "type": "histogram", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x3", "yaxis": "y3"}, {"alignmentgroup": "True", "bingroup": "y", "hoverlabel": {"namelength": 0}, "hovertemplate": "tip=%{y}<br>count=%{x}", "legendgroup": "", "marker": {"color": "#636efa"}, "name": "", "offsetgroup": "", "opacity": 0.5, "showlegend": false, "type": "histogram", "xaxis": "x2", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0], "yaxis": "y2"}],
                        {"barmode": "overlay", "height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.7215], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.7265, 0.98], "matches": "x2", "showgrid": true, "showticklabels": false}, "xaxis3": {"anchor": "y3", "domain": [0.0, 0.7215], "matches": "x", "showgrid": true, "showticklabels": false}, "xaxis4": {"anchor": "y4", "domain": [0.7265, 0.98], "matches": "x2", "showgrid": true, "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.7326], "title": {"text": "tip"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.7326], "matches": "y", "showgrid": true, "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.7426, 1.0], "matches": "y3", "showgrid": true, "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.7426, 1.0], "matches": "y3", "showgrid": true, "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('692986a3-76d0-4b63-b922-dec909e435e9');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(tips,x='total_bill',y='tip',
          marginal_x='violin',
          marginal_y ='box')
```


<div>


            <div id="8ac505b1-f76e-42d5-9b79-8ddfbf245ee0" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("8ac505b1-f76e-42d5-9b79-8ddfbf245ee0")) {
                    Plotly.newPlot(
                        '8ac505b1-f76e-42d5-9b79-8ddfbf245ee0',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}<br>tip=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "", "showlegend": false, "type": "scatter", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "total_bill=%{x}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "", "offsetgroup": "", "scalegroup": "x", "showlegend": false, "type": "violin", "x": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 35.26, 15.42, 18.43, 14.83, 21.58, 10.33, 16.29, 16.97, 20.65, 17.92, 20.29, 15.77, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 19.65, 9.55, 18.35, 15.06, 20.69, 17.78, 24.06, 16.31, 16.93, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 10.29, 34.81, 9.94, 25.56, 19.49, 38.01, 26.41, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 16.45, 3.07, 20.23, 15.01, 12.02, 17.07, 26.86, 25.28, 14.73, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 10.07, 32.68, 15.98, 34.83, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 5.75, 16.32, 22.75, 40.17, 27.28, 12.03, 21.01, 12.46, 11.35, 15.38, 44.3, 22.42, 20.92, 15.36, 20.49, 25.21, 18.24, 14.31, 14.0, 7.25, 38.07, 23.95, 25.71, 17.31, 29.93, 10.65, 12.43, 24.08, 11.69, 13.42, 14.26, 15.95, 12.48, 29.8, 8.52, 14.52, 11.38, 22.82, 19.08, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 16.0, 13.16, 17.47, 34.3, 41.19, 27.05, 16.43, 8.35, 18.64, 11.87, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 29.85, 48.17, 25.0, 13.39, 16.49, 21.5, 12.66, 16.21, 13.81, 17.51, 24.52, 20.76, 31.71, 10.59, 10.63, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 9.6, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 20.9, 30.46, 18.15, 23.1, 15.69, 19.81, 28.44, 15.48, 16.58, 7.56, 10.34, 43.11, 13.0, 13.51, 18.71, 12.74, 13.0, 16.4, 20.53, 16.47, 26.59, 38.73, 24.27, 12.76, 30.06, 25.89, 48.33, 13.27, 28.17, 12.9, 28.15, 11.59, 7.74, 30.14, 12.16, 13.42, 8.58, 15.98, 13.42, 16.27, 10.09, 20.45, 13.28, 22.12, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 35.83, 29.03, 27.18, 22.67, 17.82, 18.78], "xaxis": "x3", "yaxis": "y3"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "tip=%{y}", "legendgroup": "", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "", "notched": true, "offsetgroup": "", "showlegend": false, "type": "box", "xaxis": "x2", "y": [1.01, 1.66, 3.5, 3.31, 3.61, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 5.0, 1.57, 3.0, 3.02, 3.92, 1.67, 3.71, 3.5, 3.35, 4.08, 2.75, 2.23, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 3.0, 1.45, 2.5, 3.0, 2.45, 3.27, 3.6, 2.0, 3.07, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 2.6, 5.2, 1.56, 4.34, 3.51, 3.0, 1.5, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.47, 1.0, 2.01, 2.09, 1.97, 3.0, 3.14, 5.0, 2.2, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 1.83, 5.0, 2.03, 5.17, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 1.0, 4.3, 3.25, 4.73, 4.0, 1.5, 3.0, 1.5, 2.5, 3.0, 2.5, 3.48, 4.08, 1.64, 4.06, 4.29, 3.76, 4.0, 3.0, 1.0, 4.0, 2.55, 4.0, 3.5, 5.07, 1.5, 1.8, 2.92, 2.31, 1.68, 2.5, 2.0, 2.52, 4.2, 1.48, 2.0, 2.0, 2.18, 1.5, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.0, 2.75, 3.5, 6.7, 5.0, 5.0, 2.3, 1.5, 1.36, 1.63, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.14, 5.0, 3.75, 2.61, 2.0, 3.5, 2.5, 2.0, 2.0, 3.0, 3.48, 2.24, 4.5, 1.61, 2.0, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 4.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 3.5, 2.0, 3.5, 4.0, 1.5, 4.19, 2.56, 2.02, 4.0, 1.44, 2.0, 5.0, 2.0, 2.0, 4.0, 2.01, 2.0, 2.5, 4.0, 3.23, 3.41, 3.0, 2.03, 2.23, 2.0, 5.16, 9.0, 2.5, 6.5, 1.1, 3.0, 1.5, 1.44, 3.09, 2.2, 3.48, 1.92, 3.0, 1.58, 2.5, 2.0, 3.0, 2.72, 2.88, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 4.67, 5.92, 2.0, 2.0, 1.75, 3.0], "yaxis": "y2"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.819], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.824, 0.98], "matches": "x2", "showgrid": false, "showticklabels": false}, "xaxis3": {"anchor": "y3", "domain": [0.0, 0.819], "matches": "x", "showgrid": true, "showticklabels": false}, "xaxis4": {"anchor": "y4", "domain": [0.824, 0.98], "matches": "x2", "showgrid": false, "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.8316], "title": {"text": "tip"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.8316], "matches": "y", "showgrid": true, "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.8416, 1.0], "matches": "y3", "showgrid": false, "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.8416, 1.0], "matches": "y3", "showgrid": true, "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('8ac505b1-f76e-42d5-9b79-8ddfbf245ee0');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
px.scatter(tips,x='total_bill',y='tip',
          marginal_x='violin',
          marginal_y ='box',
          color='sex')
```


<div>


            <div id="b11ec531-5802-47d6-abc1-1d552cc2b74f" class="plotly-graph-div" style="height:600px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("b11ec531-5802-47d6-abc1-1d552cc2b74f")) {
                    Plotly.newPlot(
                        'b11ec531-5802-47d6-abc1-1d552cc2b74f',
                        [{"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "mode": "markers", "name": "sex=Female", "showlegend": true, "type": "scatter", "x": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "xaxis": "x", "y": [1.01, 3.61, 5.0, 3.02, 1.67, 3.5, 2.75, 2.23, 3.0, 3.0, 2.45, 3.07, 2.6, 5.2, 1.5, 2.47, 1.0, 3.0, 3.14, 5.0, 2.2, 1.83, 5.17, 1.0, 4.3, 3.25, 2.5, 3.0, 2.5, 3.48, 4.08, 4.0, 1.0, 4.0, 3.5, 1.5, 1.8, 2.92, 1.68, 2.52, 4.2, 2.0, 2.0, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.75, 3.5, 5.0, 2.3, 1.5, 1.36, 1.63, 5.14, 3.75, 2.61, 2.0, 3.0, 1.61, 2.0, 4.0, 3.5, 3.5, 4.19, 5.0, 2.0, 2.01, 2.0, 2.5, 3.23, 2.23, 2.5, 6.5, 1.1, 3.09, 3.48, 3.0, 2.5, 2.0, 2.88, 4.67, 2.0, 3.0], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>total_bill=%{x}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "sex=Female", "offsetgroup": "sex=Female", "scalegroup": "x", "showlegend": false, "type": "violin", "x": [16.99, 24.59, 35.26, 14.83, 10.33, 16.97, 20.29, 15.77, 19.65, 15.06, 20.69, 16.93, 10.29, 34.81, 26.41, 16.45, 3.07, 17.07, 26.86, 25.28, 14.73, 10.07, 34.83, 5.75, 16.32, 22.75, 11.35, 15.38, 44.3, 22.42, 20.92, 14.31, 7.25, 25.71, 17.31, 10.65, 12.43, 24.08, 13.42, 12.48, 29.8, 14.52, 11.38, 20.27, 11.17, 12.26, 18.26, 8.51, 10.33, 14.15, 13.16, 17.47, 27.05, 16.43, 8.35, 18.64, 11.87, 29.85, 25.0, 13.39, 16.21, 17.51, 10.59, 10.63, 9.6, 20.9, 18.15, 19.81, 43.11, 13.0, 12.74, 13.0, 16.4, 16.47, 12.76, 13.27, 28.17, 12.9, 30.14, 13.42, 15.98, 16.27, 10.09, 22.12, 35.83, 27.18, 18.78], "xaxis": "x3", "yaxis": "y3"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Female<br>tip=%{y}", "legendgroup": "sex=Female", "marker": {"color": "#636efa", "symbol": "circle"}, "name": "sex=Female", "notched": true, "offsetgroup": "sex=Female", "showlegend": false, "type": "box", "xaxis": "x2", "y": [1.01, 3.61, 5.0, 3.02, 1.67, 3.5, 2.75, 2.23, 3.0, 3.0, 2.45, 3.07, 2.6, 5.2, 1.5, 2.47, 1.0, 3.0, 3.14, 5.0, 2.2, 1.83, 5.17, 1.0, 4.3, 3.25, 2.5, 3.0, 2.5, 3.48, 4.08, 4.0, 1.0, 4.0, 3.5, 1.5, 1.8, 2.92, 1.68, 2.52, 4.2, 2.0, 2.0, 2.83, 1.5, 2.0, 3.25, 1.25, 2.0, 2.0, 2.75, 3.5, 5.0, 2.3, 1.5, 1.36, 1.63, 5.14, 3.75, 2.61, 2.0, 3.0, 1.61, 2.0, 4.0, 3.5, 3.5, 4.19, 5.0, 2.0, 2.01, 2.0, 2.5, 3.23, 2.23, 2.5, 6.5, 1.1, 3.09, 3.48, 3.0, 2.5, 2.0, 2.88, 4.67, 2.0, 3.0], "yaxis": "y2"}, {"hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>total_bill=%{x}<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "mode": "markers", "name": "sex=Male", "showlegend": true, "type": "scatter", "x": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "xaxis": "x", "y": [1.66, 3.5, 3.31, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 1.57, 3.0, 3.92, 3.71, 3.35, 4.08, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 1.45, 2.5, 3.27, 3.6, 2.0, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 1.56, 4.34, 3.51, 3.0, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.01, 2.09, 1.97, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 5.0, 2.03, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 4.73, 4.0, 1.5, 3.0, 1.5, 1.64, 4.06, 4.29, 3.76, 3.0, 4.0, 2.55, 5.07, 2.31, 2.5, 2.0, 1.48, 2.18, 1.5, 2.0, 6.7, 5.0, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.0, 2.0, 3.5, 2.5, 2.0, 3.48, 2.24, 4.5, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 2.0, 4.0, 1.5, 2.56, 2.02, 4.0, 1.44, 2.0, 2.0, 4.0, 4.0, 3.41, 3.0, 2.03, 2.0, 5.16, 9.0, 3.0, 1.5, 1.44, 2.2, 1.92, 1.58, 3.0, 2.72, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 5.92, 2.0, 1.75], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>total_bill=%{x}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "name": "sex=Male", "offsetgroup": "sex=Male", "scalegroup": "x", "showlegend": false, "type": "violin", "x": [10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58, 16.29, 20.65, 17.92, 39.42, 19.82, 17.81, 13.37, 12.69, 21.7, 9.55, 18.35, 17.78, 24.06, 16.31, 18.69, 31.27, 16.04, 17.46, 13.94, 9.68, 30.4, 18.29, 22.23, 32.4, 28.55, 18.04, 12.54, 9.94, 25.56, 19.49, 38.01, 11.24, 48.27, 20.29, 13.81, 11.02, 18.29, 17.59, 20.08, 20.23, 15.01, 12.02, 10.51, 17.92, 27.2, 22.76, 17.29, 19.44, 16.66, 32.68, 15.98, 13.03, 18.28, 24.71, 21.16, 28.97, 22.49, 40.17, 27.28, 12.03, 21.01, 12.46, 15.36, 20.49, 25.21, 18.24, 14.0, 38.07, 23.95, 29.93, 11.69, 14.26, 15.95, 8.52, 22.82, 19.08, 16.0, 34.3, 41.19, 9.78, 7.51, 14.07, 13.13, 17.26, 24.55, 19.77, 48.17, 16.49, 21.5, 12.66, 13.81, 24.52, 20.76, 31.71, 50.81, 15.81, 7.25, 31.85, 16.82, 32.9, 17.89, 14.48, 34.63, 34.65, 23.33, 45.35, 23.17, 40.55, 20.69, 30.46, 23.1, 15.69, 28.44, 15.48, 16.58, 7.56, 10.34, 13.51, 18.71, 20.53, 26.59, 38.73, 24.27, 30.06, 25.89, 48.33, 28.15, 11.59, 7.74, 12.16, 8.58, 13.42, 20.45, 13.28, 24.01, 15.69, 11.61, 10.77, 15.53, 10.07, 12.6, 32.83, 29.03, 22.67, 17.82], "xaxis": "x3", "yaxis": "y3"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "sex=Male<br>tip=%{y}", "legendgroup": "sex=Male", "marker": {"color": "#EF553B", "symbol": "circle"}, "name": "sex=Male", "notched": true, "offsetgroup": "sex=Male", "showlegend": false, "type": "box", "xaxis": "x2", "y": [1.66, 3.5, 3.31, 4.71, 2.0, 3.12, 1.96, 3.23, 1.71, 1.57, 3.0, 3.92, 3.71, 3.35, 4.08, 7.58, 3.18, 2.34, 2.0, 2.0, 4.3, 1.45, 2.5, 3.27, 3.6, 2.0, 2.31, 5.0, 2.24, 2.54, 3.06, 1.32, 5.6, 3.0, 5.0, 6.0, 2.05, 3.0, 2.5, 1.56, 4.34, 3.51, 3.0, 1.76, 6.73, 3.21, 2.0, 1.98, 3.76, 2.64, 3.15, 2.01, 2.09, 1.97, 1.25, 3.08, 4.0, 3.0, 2.71, 3.0, 3.4, 5.0, 2.03, 2.0, 4.0, 5.85, 3.0, 3.0, 3.5, 4.73, 4.0, 1.5, 3.0, 1.5, 1.64, 4.06, 4.29, 3.76, 3.0, 4.0, 2.55, 5.07, 2.31, 2.5, 2.0, 1.48, 2.18, 1.5, 2.0, 6.7, 5.0, 1.73, 2.0, 2.5, 2.0, 2.74, 2.0, 2.0, 5.0, 2.0, 3.5, 2.5, 2.0, 3.48, 2.24, 4.5, 10.0, 3.16, 5.15, 3.18, 4.0, 3.11, 2.0, 2.0, 3.55, 3.68, 5.65, 3.5, 6.5, 3.0, 5.0, 2.0, 4.0, 1.5, 2.56, 2.02, 4.0, 1.44, 2.0, 2.0, 4.0, 4.0, 3.41, 3.0, 2.03, 2.0, 5.16, 9.0, 3.0, 1.5, 1.44, 2.2, 1.92, 1.58, 3.0, 2.72, 2.0, 3.0, 3.39, 1.47, 3.0, 1.25, 1.0, 1.17, 5.92, 2.0, 1.75], "yaxis": "y2"}],
                        {"height": 600, "legend": {"tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 0.7215], "title": {"text": "total_bill"}}, "xaxis2": {"anchor": "y2", "domain": [0.7265, 0.98], "matches": "x2", "showgrid": false, "showticklabels": false}, "xaxis3": {"anchor": "y3", "domain": [0.0, 0.7215], "matches": "x", "showgrid": true, "showticklabels": false}, "xaxis4": {"anchor": "y4", "domain": [0.7265, 0.98], "matches": "x2", "showgrid": false, "showticklabels": false}, "yaxis": {"anchor": "x", "domain": [0.0, 0.7326], "title": {"text": "tip"}}, "yaxis2": {"anchor": "x2", "domain": [0.0, 0.7326], "matches": "y", "showgrid": true, "showticklabels": false}, "yaxis3": {"anchor": "x3", "domain": [0.7426, 1.0], "matches": "y3", "showgrid": false, "showticklabels": false}, "yaxis4": {"anchor": "x4", "domain": [0.7426, 1.0], "matches": "y3", "showgrid": true, "showticklabels": false}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('b11ec531-5802-47d6-abc1-1d552cc2b74f');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


## SEABORN: Libreria de visualización de datos estadísticos de Python

Seaborn complementa a Matplotlib y se dirige específicamente a la visualización de datos estadísticos, funciona muy bien con pandas.

### Instalacion Seaborn
Anaconda instala automaticamente Seaborn, en caso de no tenerlo instalarlo con el siguiente comando:

`conda install seaborn` o `pip install seaborn`.

Se recomienda la instalacion con Conda, se debe tener instalado:
numpy (>= 1.9.3), 
scipy (>= 0.14.0), 
matplotlib (>= 1.4.3), 
pandas (>= 0.15.2)

### Importar seaborn
Se importa de forma estandar de la siguiente manera:


```python
import seaborn as sns
#para graficar dentro del jupyter notebook
%matplotlib inline 
```

### Datos integrados en seaborn
Seaborn viene con algunos data sets integrados, la lista competa se puede encontrar en: https://github.com/mwaskom/seaborn-data


```python
tips = sns.load_dataset('tips') # Importar el dataset tips
type(tips)
```




    pandas.core.frame.DataFrame




```python
tips.head() # ver los primeros 5 registros
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.dtypes #tipos de datos en el dataframe
```




    total_bill     float64
    tip            float64
    sex           category
    smoker        category
    day           category
    time          category
    size             int64
    dtype: object




```python
tips.describe() #Resumen estadistico de los datos del data frame por columna
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Plots de Distribucion en Seaborn

### distplot

El distplot muestra la distribución de un conjunto univariante de observaciones.


```python
sns.distplot(tips['total_bill']);
```


![png](./4-Visualizacion_206_0.png)


Si se quiere eliminar la grafica kde y solo tener el histograma entonces:


```python
sns.distplot(tips['total_bill'],kde=False,bins=30);
```


![png](./4-Visualizacion_208_0.png)


### jointplot
jointplot() le permite básicamente emparejar dos distplots para datos bivariados. Con su elección de  que parámetro **kind** va comparar:
* “scatter” 
* “reg” 
* “resid” 
* “kde” 
* “hex”


```python
# Histogramas y scatter plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter');
```


![png](./4-Visualizacion_210_0.png)



```python
# Histogramas  y hexagonal
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex');
```


![png](./4-Visualizacion_211_0.png)



```python
#Hystogramas con kde y scatter plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg');
```


![png](./4-Visualizacion_212_0.png)


### pairplot

pairplot grafica relaciones por pares en un dataframe completo (para las columnas numéricas) y soporta un argumento de tono de color(Hue) (para columnas categóricas).


```python
#diagonal histogramas los demas son scatter plots
sns.pairplot(tips); # datos numericos
```


![png](./4-Visualizacion_214_0.png)



```python
# Datos categoricos

# Diagonal KDE y los otros plots son scatter
sns.pairplot(tips,hue='sex',palette='coolwarm'); # cambio de colormap
```


![png](./4-Visualizacion_215_0.png)


### kdeplot

kdeplots son [Gráficos de Estimación de Densidad del Núcleo](http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth).


```python
# Variable 'total bill'
sns.kdeplot(tips['total_bill']) #plot kde
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f47c6f3c860>




![png](./4-Visualizacion_217_1.png)



```python
#Variable 'tip'
sns.kdeplot(tips['tip'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f47c6964908>




![png](./4-Visualizacion_218_1.png)


## Plots para datos categoricos
* boxplot
* violinplot
* stripplot
* swarmplot
* barplot
* countplot


```python
import seaborn as sns
%matplotlib inline
```

### barplot

Es un gráfico general que le permite agregar los datos categóricos basados en alguna función, el valor predeterminado es la media:


```python
sns.barplot(x='sex',y='total_bill',data=tips);
```


![png](./4-Visualizacion_222_0.png)


Puede cambiar el objeto estimador a su propia función, que convierte un vector a escalar:


```python
import numpy as np
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std); # la desviacion estandar como estimador
```


![png](./4-Visualizacion_224_0.png)


### countplot

Esto es esencialmente lo mismo que Barplot, excepto que el estimador está contando explícitamente el número de ocurrencias. Por eso solo pasamos el valor de x:


```python
sns.countplot(x='sex',data=tips);
```


![png](./4-Visualizacion_226_0.png)


### boxplot
los boxplots (diagrama de caja) y violin plots se utilizan para mostrar la distribución de datos categóricos. Un diagrama de caja (boxplots o gráfico de caja y bigotes) muestra la distribución de datos cuantitativos de una manera que facilita las comparaciones entre variables o entre niveles de una variable categórica. El cuadro muestra los cuartiles del conjunto de datos, mientras que los bigotes se extienden para mostrar el resto de la distribución, a excepción de los puntos que se determinan como "valores atípicos" utilizando un método que es una función del rango intercuartílico.


```python
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow');
```


![png](./4-Visualizacion_228_0.png)



```python
# se pueden graficar de forma horizontal
sns.boxplot(data=tips,palette='rainbow',orient='h');
```


![png](./4-Visualizacion_229_0.png)



```python
# cambiar el color y ver varias variables (hue)
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm");
```


![png](./4-Visualizacion_230_0.png)


### violinplot
Un plot de violín juega un papel similar a un box and whisker plot (diagrama de cajas y bigotes). Muestra la distribución de datos cuantitativos a través de varios niveles de una (o más) variables categóricas de modo que esas distribuciones se puedan comparar. A diferencia de un diagrama de caja, en el que todos los componentes de la gráfica corresponden a los puntos de datos reales, la gráfica del violín presenta una estimación de la densidad del núcleo de la distribución subyacente.


```python
sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow');
```


![png](./4-Visualizacion_232_0.png)



```python
# Varias Variables
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1');
```


![png](./4-Visualizacion_233_0.png)



```python
# Varias variables
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1');
```


![png](./4-Visualizacion_234_0.png)


### stripplot
El stripplot dibujará un diagrama de dispersión donde una variable es categórica. Un stripplot se puede dibujar por sí mismo, pero también es un buen complemento de una casilla o trama de violín en los casos en que desea mostrar todas las observaciones junto con alguna representación de la distribución subyacente.


```python
sns.stripplot(x="day", y="total_bill", data=tips);
```


![png](./4-Visualizacion_236_0.png)



```python
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True);
```


![png](./4-Visualizacion_237_0.png)



```python
# Varias variables
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1');
```


![png](./4-Visualizacion_238_0.png)



```python
# Varias Variables
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',dodge=True);
```


![png](./4-Visualizacion_239_0.png)


### swarmplot
El swarmplot es similar a stripplot(), pero los puntos se ajustan (solo a lo largo del eje categórico) para que no se superpongan. Esto proporciona una mejor representación de la distribución de los valores, aunque no se ajusta a un gran número de observaciones (tanto en términos de la capacidad de mostrar todos los puntos como en términos del cálculo necesario para organizarlos).


```python
sns.swarmplot(x="day", y="total_bill", data=tips);
```


![png](./4-Visualizacion_241_0.png)



```python
sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", dodge=True);
```


![png](./4-Visualizacion_242_0.png)


### Combininando Plots Categoricos


```python
sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3);
```


![png](./4-Visualizacion_244_0.png)


## Graficas de Matrices

Los Plot de matriz permiten graficar los datos como matrices codificadas por colores y también se pueden usar para indicar clústeres dentro de los datos, algunos de los mas usados son el heatmap y el clustermap de seaborn:


```python
flights = sns.load_dataset('flights') # carga de datos
```


```python
tips = sns.load_dataset('tips') # carga de datos
```


```python
tips.head() # ver los primeros 5 elementos de la tabla
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
flights.head() # ver los primeros 5 elementos de la tabla
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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>January</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>February</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>March</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>April</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>



### Heatmap

Para que un mapa de calor funcione correctamente, los datos ya deben estar en forma de matriz, la función de sns.heatmap básicamente los colorea. Por ejemplo:


```python
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Matriz de correlacion de los datos
tips.corr()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
      <td>0.598315</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
      <td>0.489299</td>
    </tr>
    <tr>
      <th>size</th>
      <td>0.598315</td>
      <td>0.489299</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Heatmap de la matriz de correlacion
sns.heatmap(tips.corr());
```


![png](./4-Visualizacion_253_0.png)



```python
# Cambiando el mapa de colres y agregando las anotaciones a la grafica
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True);
```


![png](./4-Visualizacion_254_0.png)


O para los datos de vuelos:


```python
# Definir una pivot table
flights.pivot_table(values='passengers',index='month',columns='year')
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
      <th>year</th>
      <th>1949</th>
      <th>1950</th>
      <th>1951</th>
      <th>1952</th>
      <th>1953</th>
      <th>1954</th>
      <th>1955</th>
      <th>1956</th>
      <th>1957</th>
      <th>1958</th>
      <th>1959</th>
      <th>1960</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>January</th>
      <td>112</td>
      <td>115</td>
      <td>145</td>
      <td>171</td>
      <td>196</td>
      <td>204</td>
      <td>242</td>
      <td>284</td>
      <td>315</td>
      <td>340</td>
      <td>360</td>
      <td>417</td>
    </tr>
    <tr>
      <th>February</th>
      <td>118</td>
      <td>126</td>
      <td>150</td>
      <td>180</td>
      <td>196</td>
      <td>188</td>
      <td>233</td>
      <td>277</td>
      <td>301</td>
      <td>318</td>
      <td>342</td>
      <td>391</td>
    </tr>
    <tr>
      <th>March</th>
      <td>132</td>
      <td>141</td>
      <td>178</td>
      <td>193</td>
      <td>236</td>
      <td>235</td>
      <td>267</td>
      <td>317</td>
      <td>356</td>
      <td>362</td>
      <td>406</td>
      <td>419</td>
    </tr>
    <tr>
      <th>April</th>
      <td>129</td>
      <td>135</td>
      <td>163</td>
      <td>181</td>
      <td>235</td>
      <td>227</td>
      <td>269</td>
      <td>313</td>
      <td>348</td>
      <td>348</td>
      <td>396</td>
      <td>461</td>
    </tr>
    <tr>
      <th>May</th>
      <td>121</td>
      <td>125</td>
      <td>172</td>
      <td>183</td>
      <td>229</td>
      <td>234</td>
      <td>270</td>
      <td>318</td>
      <td>355</td>
      <td>363</td>
      <td>420</td>
      <td>472</td>
    </tr>
    <tr>
      <th>June</th>
      <td>135</td>
      <td>149</td>
      <td>178</td>
      <td>218</td>
      <td>243</td>
      <td>264</td>
      <td>315</td>
      <td>374</td>
      <td>422</td>
      <td>435</td>
      <td>472</td>
      <td>535</td>
    </tr>
    <tr>
      <th>July</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>230</td>
      <td>264</td>
      <td>302</td>
      <td>364</td>
      <td>413</td>
      <td>465</td>
      <td>491</td>
      <td>548</td>
      <td>622</td>
    </tr>
    <tr>
      <th>August</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>242</td>
      <td>272</td>
      <td>293</td>
      <td>347</td>
      <td>405</td>
      <td>467</td>
      <td>505</td>
      <td>559</td>
      <td>606</td>
    </tr>
    <tr>
      <th>September</th>
      <td>136</td>
      <td>158</td>
      <td>184</td>
      <td>209</td>
      <td>237</td>
      <td>259</td>
      <td>312</td>
      <td>355</td>
      <td>404</td>
      <td>404</td>
      <td>463</td>
      <td>508</td>
    </tr>
    <tr>
      <th>October</th>
      <td>119</td>
      <td>133</td>
      <td>162</td>
      <td>191</td>
      <td>211</td>
      <td>229</td>
      <td>274</td>
      <td>306</td>
      <td>347</td>
      <td>359</td>
      <td>407</td>
      <td>461</td>
    </tr>
    <tr>
      <th>November</th>
      <td>104</td>
      <td>114</td>
      <td>146</td>
      <td>172</td>
      <td>180</td>
      <td>203</td>
      <td>237</td>
      <td>271</td>
      <td>305</td>
      <td>310</td>
      <td>362</td>
      <td>390</td>
    </tr>
    <tr>
      <th>December</th>
      <td>118</td>
      <td>140</td>
      <td>166</td>
      <td>194</td>
      <td>201</td>
      <td>229</td>
      <td>278</td>
      <td>306</td>
      <td>336</td>
      <td>337</td>
      <td>405</td>
      <td>432</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Graficar la pivot table como un heatmap
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights);
```


![png](./4-Visualizacion_257_0.png)



```python
# Cambiando los parametros del colormap y el ancho y color de las lineas d division
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1);
```


![png](./4-Visualizacion_258_0.png)


### clustermap

El mapa de clúster utiliza la agrupación jerárquica para producir una versión agrupada del mapa de calor. Por ejemplo:


```python
# Grafica Clustermap de la tabla pivot de los vuelos
sns.clustermap(pvflights);
```


![png](./4-Visualizacion_260_0.png)


Observe ahora cómo los años y meses ya no están en orden, en su lugar se agrupan por similitud en el valor (recuento de pasajeros). Eso significa que podemos comenzar a inferir cosas de esta trama, como agosto y julio siendo similares (tiene sentido, ya que ambos son meses de viaje de verano)


```python
# Más opciones para obtener la información un poco más clara como la normalización
# Cambiar el colormap
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1);
```


![png](./4-Visualizacion_262_0.png)


## Grids
Las grids son tipos generales de plots que le permiten mapear tipos de plots en filas y columnas de una cuadrícula, esto le ayuda a crear plots similares separadas por características.


```python
# Importar librerias
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
iris = sns.load_dataset('iris') #Importar el dataset
```


```python
iris.head() #Ver los primeros 5 elementos de la tabla
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



### PairGrid

Pairgrid es un subplot grid para graficar relaciones por pares en un conjunto de datos.


```python
# solo el Grid
sns.PairGrid(iris);
```


![png](./4-Visualizacion_268_0.png)



```python
# Ahora se mapea el grid
g = sns.PairGrid(iris)
g.map(plt.scatter);
```


![png](./4-Visualizacion_269_0.png)



```python
# Mapear a arriba, abajo y diagonal
g = sns.PairGrid(iris) # crear una cuadricula
g.map_diag(plt.hist) #Histogramas en la diagonal
g.map_upper(plt.scatter) # Scatter plots en la parte superior
g.map_lower(sns.kdeplot); # Plots de densidad kde en la parte inferior
```


![png](./4-Visualizacion_270_0.png)


### pairplot

pairplot es una versión más simple de PairGrid (se usa con bastante frecuencia)


```python
# La diagonal es un histograma
# las otras graficas son scatter plots
sns.pairplot(iris);
```


![png](./4-Visualizacion_272_0.png)



```python
# la diagonal son kde de los datos categoricos
# las otars graficas son scatter plots
sns.pairplot(iris,hue='species',palette='rainbow');
```


![png](./4-Visualizacion_273_0.png)


### Facet Grid

FacetGrid es la forma general de crear grids de plots basados en dos caracteristica:


```python
tips = sns.load_dataset('tips')
```


```python
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Solo el Grid
g = sns.FacetGrid(tips, col="time", row="smoker");
```


![png](./4-Visualizacion_277_0.png)



```python
# histogramas entre las dos variables
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")
```


![png](./4-Visualizacion_278_0.png)



```python
# Scatterplots
g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Observe como los argumentos vienen despues de llamar a plt.scatter
g = g.map(plt.scatter, "total_bill", "tip").add_legend()
```


![png](./4-Visualizacion_279_0.png)


### JointGrid

JointGrid es la version general de jointplot()


```python
# Solo el grid
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
```


![png](./4-Visualizacion_281_0.png)



```python
# Grafica de regresion y histograma con kde
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)
```


![png](./4-Visualizacion_282_0.png)


## Plots de Regresion

Seaborn tiene muchas capacidades integradas para trazados de regresión, **lmplot** le permite visualizar modelos lineales, pero también le permite dividir los gráficos en función de las características, así como también colorear el tono (hue) en función de las características.


```python
#Importar librerias
import seaborn as sns
%matplotlib inline
```


```python
tips = sns.load_dataset('tips') # importar el dataset
```


```python
tips.head() # ver los primeros datos del dataset
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### lmplot()


```python
#scatter plot mas la regresion lineal
sns.lmplot(x='total_bill',y='tip',data=tips);
```


![png](./4-Visualizacion_288_0.png)



```python
#scatter plot mas la regresion lineal basado en el genero
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex');
```


![png](./4-Visualizacion_289_0.png)



```python
# Cambio de paleta de colores
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm');
```


![png](./4-Visualizacion_290_0.png)


### Usando Marcadores

Los argumentos kwargs lmplot  pasan a **regplto** que es una forma más general de lmplot(). regplot tiene un parámetro scatter_kws que se pasa a plt.scatter y puede modificar los parametros.

Mire siempre la documentacion http://matplotlib.org/api/markers_api.html


```python
# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100});
```


![png](./4-Visualizacion_292_0.png)


### Usando un Grid

Podemos agregar una separación más variable a través de columnas y filas con el uso de un grid. Simplemente indícandolo en los argumentos col o row:


```python
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex'); #hace una division por el genero
```


![png](./4-Visualizacion_294_0.png)



```python
# division por el genero y por tiempo de almuerzo o cena
sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips);
```


![png](./4-Visualizacion_295_0.png)



```python
# informacion del genero en HUE
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm');
```


![png](./4-Visualizacion_296_0.png)


### Aspecto y Tamaño

Las figuras de Seaborn se les puede ajustar su tamaño y relación de aspecto con los parámetros **height** y **aspect**:


```python
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,height=8);
```


![png](./4-Visualizacion_298_0.png)


## Referencias

* http://www.matplotlib.org
* http://matplotlib.org/gallery.html - Una gran galería que muestra varios tipos de graficos matplotlib. ¡Muy recomendable!
* [Matplotlib cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)
* http://www.loria.fr/~rougier/teaching/matplotlib - Un Buen tutorial de matplotlib.
* http://scipy-lectures.github.io/matplotlib/matplotlib.html - Otra buena referencia para matplotlib reference.
* https://medium.com/plotly/introducing-plotly-express-808df010143d
* https://plot.ly/python/plotly-express/
* http://seaborn.pydata.org/ - Documentacion Seaborn otra libreria de graficas estadisticas
* http://matplotlib.org/api/markers_api.html - documentacion de marcadores
* Lista de colormaps http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps


**Phd. Jose R. Zapata**
- [https://joserzapata.github.io/](https://joserzapata.github.io/)
- https://twitter.com/joserzapata