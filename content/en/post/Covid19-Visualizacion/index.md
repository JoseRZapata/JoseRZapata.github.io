---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Visualizacion Datos Coronavirus (COVID19) Mundial"
subtitle: ""
summary: "Visualizaciones con Python y Plotly de los datos mundiales del corona virus COVID19"
authors: ["Jose R. Zapata"]
tags: ["Python", "Data-Science" ,"Jupyter-notebook"]
categories: ["Data-Science"]
date: 2020-03-17T17:03:57-05:00
lastmod: 2020-03-17T17:03:57-05:00
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

markup: blackfriday
---
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)

He visto en las redes sociales varias visualizaciones de los datos del COVID 19 y queria realizarlos en Python para tener la actualizacion de las graficas actualizadas cada dia, y ademas practicar el uso de [plotly](https://plot.ly/) para visualizacion interactiva.

**Pueden interactuar con las graficas con el mouse y las Graficas se actualizaran 
diariamente con los nuevos datos!**

Informacion extraida de 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE

https://github.com/CSSEGISandData/COVID-19

{{% toc %}}

# Paquetes de Python y Datos

## Paquetes de Python
```
!pip install chart_studio -q
```

```python
import pandas as pd
import plotly.express as px
import numpy as np
import chart_studio
```


```python
#chart-studio api
username = '' # your username
api_key = '' # your api api_key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
import chart_studio.plotly as py
```

## Importar datos
```python
confirmed = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
recovered = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
death = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
```

## Datos CSSEGISandData/COVID-19

Descripcion de los datos en ingles

**Province/State:** China - province name; US/Canada/Australia/ - city name, state/province name; Others - name of the event (e.g., "Diamond Princess" cruise ship); other countries - blank.

**Country/Region:** country/region name conforming to WHO (will be updated).

**Last Update:** MM/DD/YYYY HH:mm (24 hour format, in UTC).

**Confirmed:** the number of confirmed cases. For Hubei Province: from Feb 13 (GMT +8), we report both clinically diagnosed and lab-confirmed cases. For lab-confirmed cases only (Before Feb 17), please refer to who_covid_19_situation_reports. For Italy, diagnosis standard might be changed since Feb 27 to "slow the growth of new case numbers."

**Deaths:** the number of deaths.
**Recovered:** the number of recovered cases.


```python
confirmed.head()
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
      <th>Country/Region</th>
      <th>1/22/20</th>
      <th>1/23/20</th>
      <th>1/24/20</th>
      <th>1/25/20</th>
      <th>1/26/20</th>
      <th>1/27/20</th>
      <th>1/28/20</th>
      <th>1/29/20</th>
      <th>1/30/20</th>
      <th>1/31/20</th>
      <th>2/1/20</th>
      <th>2/2/20</th>
      <th>2/3/20</th>
      <th>2/4/20</th>
      <th>2/5/20</th>
      <th>2/6/20</th>
      <th>2/7/20</th>
      <th>2/8/20</th>
      <th>2/9/20</th>
      <th>2/10/20</th>
      <th>2/11/20</th>
      <th>2/12/20</th>
      <th>2/13/20</th>
      <th>2/14/20</th>
      <th>2/15/20</th>
      <th>2/16/20</th>
      <th>2/17/20</th>
      <th>2/18/20</th>
      <th>2/19/20</th>
      <th>2/20/20</th>
      <th>2/21/20</th>
      <th>2/22/20</th>
      <th>2/23/20</th>
      <th>2/24/20</th>
      <th>2/25/20</th>
      <th>2/26/20</th>
      <th>2/27/20</th>
      <th>2/28/20</th>
      <th>2/29/20</th>
      <th>3/1/20</th>
      <th>3/2/20</th>
      <th>3/3/20</th>
      <th>3/4/20</th>
      <th>3/5/20</th>
      <th>3/6/20</th>
      <th>3/7/20</th>
      <th>3/8/20</th>
      <th>3/9/20</th>
      <th>3/10/20</th>
      <th>3/11/20</th>
      <th>3/12/20</th>
      <th>3/13/20</th>
      <th>3/14/20</th>
      <th>3/15/20</th>
      <th>3/16/20</th>
      <th>3/17/20</th>
      <th>3/18/20</th>
      <th>3/19/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Thailand</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>32</td>
      <td>32</td>
      <td>32</td>
      <td>33</td>
      <td>33</td>
      <td>33</td>
      <td>33</td>
      <td>33</td>
      <td>34</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>35</td>
      <td>37</td>
      <td>40</td>
      <td>40</td>
      <td>41</td>
      <td>42</td>
      <td>42</td>
      <td>43</td>
      <td>43</td>
      <td>43</td>
      <td>47</td>
      <td>48</td>
      <td>50</td>
      <td>50</td>
      <td>50</td>
      <td>53</td>
      <td>59</td>
      <td>70</td>
      <td>75</td>
      <td>82</td>
      <td>114</td>
      <td>147</td>
      <td>177</td>
      <td>212</td>
      <td>272</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>11</td>
      <td>15</td>
      <td>20</td>
      <td>20</td>
      <td>20</td>
      <td>22</td>
      <td>22</td>
      <td>45</td>
      <td>25</td>
      <td>25</td>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>28</td>
      <td>28</td>
      <td>29</td>
      <td>43</td>
      <td>59</td>
      <td>66</td>
      <td>74</td>
      <td>84</td>
      <td>94</td>
      <td>105</td>
      <td>122</td>
      <td>147</td>
      <td>159</td>
      <td>170</td>
      <td>189</td>
      <td>214</td>
      <td>228</td>
      <td>241</td>
      <td>256</td>
      <td>274</td>
      <td>293</td>
      <td>331</td>
      <td>360</td>
      <td>420</td>
      <td>461</td>
      <td>502</td>
      <td>511</td>
      <td>581</td>
      <td>639</td>
      <td>639</td>
      <td>701</td>
      <td>773</td>
      <td>839</td>
      <td>825</td>
      <td>878</td>
      <td>889</td>
      <td>924</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Singapore</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>7</td>
      <td>10</td>
      <td>13</td>
      <td>16</td>
      <td>18</td>
      <td>18</td>
      <td>24</td>
      <td>28</td>
      <td>28</td>
      <td>30</td>
      <td>33</td>
      <td>40</td>
      <td>45</td>
      <td>47</td>
      <td>50</td>
      <td>58</td>
      <td>67</td>
      <td>72</td>
      <td>75</td>
      <td>77</td>
      <td>81</td>
      <td>84</td>
      <td>84</td>
      <td>85</td>
      <td>85</td>
      <td>89</td>
      <td>89</td>
      <td>91</td>
      <td>93</td>
      <td>93</td>
      <td>93</td>
      <td>102</td>
      <td>106</td>
      <td>108</td>
      <td>110</td>
      <td>110</td>
      <td>117</td>
      <td>130</td>
      <td>138</td>
      <td>150</td>
      <td>150</td>
      <td>160</td>
      <td>178</td>
      <td>178</td>
      <td>200</td>
      <td>212</td>
      <td>226</td>
      <td>243</td>
      <td>266</td>
      <td>313</td>
      <td>345</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nepal</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Malaysia</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>10</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>16</td>
      <td>16</td>
      <td>18</td>
      <td>18</td>
      <td>18</td>
      <td>19</td>
      <td>19</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>22</td>
      <td>23</td>
      <td>23</td>
      <td>25</td>
      <td>29</td>
      <td>29</td>
      <td>36</td>
      <td>50</td>
      <td>50</td>
      <td>83</td>
      <td>93</td>
      <td>99</td>
      <td>117</td>
      <td>129</td>
      <td>149</td>
      <td>149</td>
      <td>197</td>
      <td>238</td>
      <td>428</td>
      <td>566</td>
      <td>673</td>
      <td>790</td>
      <td>900</td>
    </tr>
  </tbody>
</table>
</div>




```python
#recovered.head()
```


```python
#death.head()
```

## Datos Generales de cada Dataframe


```python
#confirmed.info()
```


```python
#recovered.info()
```


```python
#death.info()
```

### Eliminar Ubicacion
Se va realizar un analisis general de los datos y No se van a tomar los datos geograficos de *latitud*, *longitud* y los datos de *Province/State* estan incompletos.

Solo se realizara un analisis por pais entonces se eliminaran las columnas mencionadas anteriormente



```python
confirmed = confirmed.drop(columns=['Lat', 'Long','Province/State'])
```


```python
recovered = recovered.drop(columns=['Lat', 'Long','Province/State'])
```


```python
death = death.drop(columns=['Lat', 'Long','Province/State'])
```

### Consolidar datos


```python
confirmed_group = confirmed.groupby(by='Country/Region')
confirmed_group = confirmed_group.aggregate(np.sum)
confirmed_group = confirmed_group.T
confirmed_group.index.name = 'date'
confirmed_group =  confirmed_group.reset_index()
```


```python
recovered_group = recovered.groupby(by='Country/Region')
recovered_group = recovered_group.aggregate(np.sum)
recovered_group = recovered_group.T
recovered_group.index.name = 'date'
recovered_group =  recovered_group.reset_index()
```


```python
death_group = death.groupby(by='Country/Region')
death_group = death_group.aggregate(np.sum)
death_group = death_group.T
death_group.index.name = 'date'
death_group =  death_group.reset_index()
```

### Datos Mundiales


```python
# Numero de Casos confirmados por dia en el mundo
column_names = ["Fecha", "Confirmados", "Recuperados","Muertos"]
world = pd.DataFrame(columns = column_names)
world['Fecha'] = confirmed_group['date']
world['Confirmados'] = confirmed_group.iloc[:,1:].sum(1)
world['Recuperados'] = recovered_group.iloc[:,1:].sum(1)
world['Muertos'] = death_group.iloc[:,1:].sum(1)
```


```python
#world.tail()
```

# Visualizacion con Plotly

## Valores Mundiales de Confirmados, Recuperados y Muertos

```python
temp = pd.DataFrame(world.iloc[-1,:]).T
tm = temp.melt(id_vars="Fecha", value_vars=[ "Confirmados", "Recuperados","Muertos"])
fig = px.bar(tm, x="variable" , y="value", color= 'variable',
             color_discrete_sequence=["blue", "green", "red"],
             height=400, width=600,
             title= f'Total de Casos Mundiales de COVID 19 - {str(world.iloc[-1,0])}')

# Agregar el valor de cada columna en la parte superior
for n in range(len(tm['variable'])):
  fig.add_annotation(x=tm.iloc[n,1], y=tm.iloc[n,2], text=str(tm.iloc[n,2]),
                     showarrow=True, ax=0, ay=-30)
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": ""}} #Esconder nombre eje x
                  )
# grabar grafica en chart-studio
#py.plot(fig, filename = 'total_casos_general', auto_open=True)
fig.show()
```

<iframe width="900" height="400" frameborder="0" scrolling="no" src="//plot.ly/~joser.zapata/1.embed"></iframe>


## Progresion Mundial en el Tiempo de de Confirmados, Recuperados y Muertos


```python
world_melt = world.melt(id_vars='Fecha', value_vars= list(world.columns)[1:], var_name=None)

fig = px.line(world_melt, x="Fecha", y= 'value',
              color='variable',
              title=f'Total de Casos en el tiempo de COVID 19 - {world.iloc[-1,0]}')
for n in list(world.columns)[1:]:
  fig.add_annotation(x=world.iloc[-1,0], y=world.loc[world.index[-1],n],
                     text=n,
                     showarrow=True, ax=-50, ay=-20)
fig.layout.update(showlegend = False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio
#py.plot(fig, filename = 'total_casos_serie', auto_open=True)
fig.show()
```

<iframe width="900" height="500" frameborder="0" scrolling="no" src="//plot.ly/~joser.zapata/3.embed"></iframe>


## Total Casos Confirmados de COVID 19 por Pais (Excluyendo China)


```python
df1 = confirmed_group.drop(columns=["China"])
# Cambiar el nombre de la columna
df1.rename(columns = {'date':'Fecha'}, inplace = True) 
df_melt = df1.melt(id_vars='Fecha', value_vars= list(df1.columns)[1:], var_name=None)
fig = px.line(df_melt, x='Fecha' , y='value', color='Country/Region',
              color_discrete_sequence=px.colors.qualitative.G10,
              title=f'Total Casos Confirmados de COVID 19 por Pais (Excluyendo China) - {world.iloc[-1,0]}')
# 8 paises mas infectados
fecha = df1['Fecha'].iloc[-1] #obtener la fecha del ultimo dato
paises = df1.iloc[-1,1:] #obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
mas_infectados=[]
for n in range(8):
  fig.add_annotation(x=fecha, y=paises[n], text=paises.index[n],
                     showarrow=True, ax=+30, ay=0)
  mas_infectados.append(paises.index[n])
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio
#py.plot(fig, filename = 'total_casos_no_china', auto_open=True)
fig.show()
```
<iframe width="900" height="700" frameborder="0" scrolling="no" src="//plot.ly/~joser.zapata/5.embed"></iframe>


## Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados y China)


```python
df2 = confirmed_group.drop(columns=["China"] +mas_infectados)
# Cambiar el nombre de la columna
df2.rename(columns = {'date':'Fecha'}, inplace = True) 

df_melt2 = df2.melt(id_vars='Fecha', value_vars= list(df2.columns)[1:], var_name=None)
fig = px.line(df_melt2, x='Fecha' , y='value', color='Country/Region',
              color_discrete_sequence=px.colors.qualitative.G10,
              title=f'Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados) - {world.iloc[-1,0]}')

fecha = df2['Fecha'].iloc[-1] #obtener la fecha del ultimo dato
paises = df2.iloc[-1,1:] #obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
for n in range(8):
  fig.add_annotation(x=fecha, y=paises[n], text=paises.index[n],
                     showarrow=True, ax=+30, ay=0)
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
#py.plot(fig, filename = 'total_casos_no_8_infectados', auto_open=True)
fig.show()
```

<iframe width="900" height="700" frameborder="0" scrolling="no" src="//plot.ly/~joser.zapata/7.embed"></iframe>


## Numero de Casos Confirmados en Colombia

```python
fig = px.line(confirmed_group,x='date' , y='Colombia',
              title=f'Total Casos Confirmados de COVID 19 Colombia - {world.iloc[-1,0]}')
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": "Fecha"}})
#py.plot(fig, filename = 'Colombia_general', auto_open=True)
fig.show()
```
<iframe width="900" height="400" frameborder="0" scrolling="no" src="//plot.ly/~joser.zapata/9.embed"></iframe>

# Refencias

- https://github.com/CSSEGISandData/COVID-19
- https://www.kaggle.com/imdevskp/covid-19-analysis-viz-prediction-comparisons
- https://junye0798.com/post/build-a-dashboard-to-track-the-spread-of-coronavirus-using-dash/
- https://github.com/Perishleaf/data-visualisation-scripts/tree/master/dash-2019-coronavirus
- https://medium.com/tomas-pueyo/coronavirus-por-qu%C3%A9-debemos-actuar-ya-93079c61e200