---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Visualizacion Datos Coronavirus (COVID19) Mundial con Plotly"
subtitle: ""
summary: "Visualizaciones con Python y Plotly de los datos mundiales del corona virus COVID19"
authors: ["joserzapata"]
tags: ["Python", "Data-Science" ,"Jupyter-notebook"]
categories: ["Data-Science"]
date: 2020-03-17T17:03:57-05:00
lastmod: 2020-05-29T17:03:57-05:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
markup: blackfriday
---

  |   |  
---|---|---
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoseRZapata/JoseRZapata.github.io/master?filepath=Jupyter_Notebook/Covid19_Visualizacion_es.ipynb) | [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)

***

He visto en las redes sociales varias visualizaciones de los datos del COVID 19 y queria realizarlos en Python para tener la actualizacion de las graficas actualizadas cada dia, y ademas practicar el uso de [plotly](https://plotly.com/) para visualizacion interactiva.

Principalmente los datos que se tienen es del numero de personas contegiadas y personas muertas quiero visualizar los datos de personas recuperadas y casos activos.

**Pueden interactuar con las graficas con el mouse y las Graficas se actualizaran
diariamente con los nuevos datos!**

Informacion extraida de 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE

https://github.com/CSSEGISandData/COVID-19

**Actualizaciones:**

- 27/May/2020 Se Agregar los datos de las personas recuperadas y se calculan los casos Activos
- 29/May/2020 Se agrega Bar chart race
- 25/Sep/2020 Mapa Mundial de Confirmados por Pais con choropleth


{{% toc %}}

***

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

Para subir las graficas interactivas de plotly a chart studio
```python
#chart-studio api
username = '' # your username
api_key = '' # your api api_key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
import chart_studio.plotly as py
```

## Importar datos

```python
confirmed = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
death = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recovered = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
```

## Datos CSSEGISandData/COVID-19

Descripcion de los datos en ingles

**Province/State:** China - province name; US/Canada/Australia/ - city name, state/province name; Others - name of the event (e.g., "Diamond Princess" cruise ship); other countries - blank.

**Country/Region:** country/region name conforming to WHO (will be updated).

**Last Update:** MM/DD/YYYY HH:mm (24 hour format, in UTC).

**Confirmed:** the number of confirmed cases. For Hubei Province: from Feb 13 (GMT +8), we report both clinically diagnosed and lab-confirmed cases. For lab-confirmed cases only (Before Feb 17), please refer to who_covid_19_situation_reports. For Italy, diagnosis standard might be changed since Feb 27 to "slow the growth of new case numbers."

**Deaths:** the number of deaths.

**Recovered:** the number of recovered cases.

### Eliminar Ubicacion
Se va realizar un analisis general de los datos y No se van a tomar los datos geograficos de *latitud*, *longitud* y los datos de *Province/State* estan incompletos.

Solo se realizara un analisis por pais entonces se eliminaran las columnas mencionadas anteriormente


```python
confirmed = confirmed.drop(columns=['Lat', 'Long','Province/State'])
death = death.drop(columns=['Lat', 'Long','Province/State'])
recovered  = recovered.drop(columns=['Lat', 'Long','Province/State'])
```
### Casos Activos
Se calcula a partir del número de personas confirmadas - muertos - recuperados

```python
active =confirmed.copy()
active.iloc[:,1:] = active.iloc[:,1:] - death.iloc[:,1:] - recovered.iloc[:,1:]
```

### Consolidar datos

```python
confirmed_group = confirmed.groupby(by='Country/Region').aggregate(np.sum).T
confirmed_group.index.name = 'date'
confirmed_group =  confirmed_group.reset_index()
```

```python
recovered_group = recovered.groupby(by='Country/Region').aggregate(np.sum).T
recovered_group.index.name = 'date'
recovered_group =  recovered_group.reset_index()
```
```python
active_group = active.groupby(by='Country/Region').aggregate(np.sum).T
active_group.index.name = 'date'
active_group =  active_group.reset_index()
```
```python
death_group = death.groupby(by='Country/Region').aggregate(np.sum).T
death_group.index.name = 'date'
death_group =  death_group.reset_index()
```

```python
confirmed_melt = confirmed_group.melt(id_vars="date").copy()
confirmed_melt.rename(columns = {'value':'Confirmados', 'date':'Fecha'}, inplace = True)

death_melt = death_group.melt(id_vars="date")
death_melt.rename(columns = {'value':'Muertos', 'date':'Fecha'}, inplace = True)
```


### Datos Mundiales


```python
# Numero de Casos confirmados por dia en el mundo
column_names = ["Fecha", "Confirmados", "Recuperados","Muertos"]
world = pd.DataFrame(columns = column_names)
world['Fecha'] = confirmed_group['date'].copy()
world['Confirmados'] = confirmed_group.iloc[:,1:].sum(1)
world['Muertos'] = death_group.iloc[:,1:].sum(1)
world['Recuperados'] = recovered_group.iloc[:,1:].sum(1)
world['Activos'] = active_group.iloc[:,1:].sum(1)
```


# Covid19 en el Mundo
## Evolucion Animada de Casos Activos por Pais
La gráfica animada de la evolución temporal de los casos activos por país, la he creado con la libreria [Pandas alive](https://github.com/JackMcKew/pandas_alive) y [Bar Chart Race](https://github.com/dexplo/bar_chart_race).

{{< youtube ogd7ZifCDQU>}}

```python
import pandas_alive
active_evol = active_group.set_index('date')
active_evol.index = pd.to_datetime(active_evol.index)
active_evol.plot_animated(filename='evolucion_casos_activos.mp4', n_bars=8,n_visible=8,
                          title='Evolución en el tiempo de Casos Activos COVID-19 por pais \n https://joserzapata.github.io/',
                          perpendicular_bar_func='mean', dpi=300,
                          period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
                          period_fmt='%B %d, %Y',
                          period_summary_func=lambda v: {'x': .99, 'y': .18,
                                      's': f'Total Activos: {v.nlargest(8).sum():,.0f}',
                                      'ha': 'right', 'size': 9, 'family': 'Courier New'})
```
## Visualizacion con Plotly

## Valores Mundiales de Casos Confirmados, Activos, Recuperados y Muertos
<iframe width="100%" height="450" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/2362.embed?link=false"></iframe>

```python
temp = pd.DataFrame(world.iloc[-1,:]).T
tm = temp.melt(id_vars="Fecha", value_vars=[ "Confirmados","Activos","Recuperados","Muertos"])
fig = px.bar(tm, x="variable" , y="value", color= 'variable', text='value',
             color_discrete_sequence=["teal","navy","green", "coral"],
             height=500, width=600,
             title= f'Total de Casos Mundiales de COVID 19 - {str(world.iloc[-1,0])}')
fig.update_traces(textposition='outside')#poner los valores de las barras fuera
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": ""}} #Esconder nombre eje x
                  )
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_general', auto_open=False)
fig.show()
```
## Mapa Mundial de Confirmados por Pais
Mover el Mouse sobre el mapa para ver la informacion de cada pais
<iframe width="100%" height="500" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/2364.embed?link=false"></iframe>

```python
confirmed_melt['Fecha'] = pd.to_datetime(confirmed_melt['Fecha'])
confirmed_melt['Fecha'] = confirmed_melt['Fecha'].dt.strftime('%m/%d/%Y')

max_Fecha = confirmed_melt['Fecha'].max()
conf_max = confirmed_melt[confirmed_melt['Fecha']== max_Fecha]
conf_max.dropna(inplace=True) #eliminar filas con valores faltantes

fig = px.choropleth(conf_max, locations="Country/Region", locationmode='country names', 
                     color=np.log10(conf_max["Confirmados"]), hover_name="Country/Region", 
                     hover_data = ["Confirmados"],
                     projection="natural earth", width=900,
                     color_continuous_scale = px.colors.sequential.Jet,        
                     title='Mapa de Confirmados COVID 19 por Pais')
fig.update(layout_coloraxis_showscale=False)
#py.plot(fig, filename = 'mapa_confirmados_pais', auto_open=False)
fig.show()

```
## Confirmados vs Muertos por pais

<iframe width="100%" height="500" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/289.embed?link=false"></iframe>

```python
death_melt['Fecha'] = pd.to_datetime(death_melt['Fecha'])
death_melt['Fecha'] = death_melt['Fecha'].dt.strftime('%m/%d/%Y')

max_Fecha = death_melt['Fecha'].max()
death_max = death_melt[death_melt['Fecha']== max_Fecha].copy()
death_max.dropna(inplace=True) #eliminar filas con valores faltantes

fig = px.scatter(full_melt_max.sort_values('Muertos', ascending=False).iloc[:15, :], 
                 x='Confirmados', y='Muertos', color='Country/Region', size='Confirmados', height=500,
                 text='Country/Region', log_x=True, log_y=True, title= f'Muertos vs Confirmados - {max_Fecha} - (15 Paises)')
fig.update_traces(textposition='top center')
fig.layout.update(showlegend = False)
#py.plot(fig, filename = 'scatter_muertos_confirmados', auto_open=False)
fig.show()
```

## Progresion Mundial en el Tiempo de Confirmados y Muertos
<iframe width="100%" height="600" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/3.embed?link=false"></iframe>

```python
world_melt = world.melt(id_vars='Fecha', value_vars= list(world.columns)[1:], var_name=None)

fig = px.line(world_melt, x="Fecha", y= 'value',
              color='variable',  color_discrete_sequence=["teal","green","coral", "navy"],
              title=f'Total de Casos en el tiempo de COVID 19 - {world.iloc[-1,0]}')
for n in list(world.columns)[1:]:
  fig.add_annotation(x=world.iloc[-1,0], y=world.loc[world.index[-1],n],
                     text=n, xref="x",yref="y",
                     showarrow=True, ax=-50, ay=-20)
# Indicador de numero total de confirmados
fig.add_indicator( title= {'text':'Confirmados', 'font':{'color':'teal'}},
                  value = world['Confirmados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Confirmados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.25], 'y': [0.15, .4]})
#Indicador numero total de Activos
fig.add_indicator(title={'text':'Activos', 'font':{'color':'navy'}},
                  value = world['Activos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Activos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.25], 'y': [0.6, .85]})
#Indicador numero total de Recuperados
fig.add_indicator(title={'text':'Recuperados', 'font':{'color':'green'}},
                  value = world['Recuperados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Recuperados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.25, 0.50], 'y': [0.6, .85]}) 
#Indicador numero total de muertos
fig.add_indicator(title={'text':'Muertos', 'font':{'color':'coral'}}, 
                  value = world['Muertos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Muertos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.25, 0.5], 'y': [0.15, .4]})  
fig.layout.update(showlegend = False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_serie', auto_open=False)
fig.show()
```

## Total Casos Confirmados de COVID 19 por Pais
<iframe width="100%" height="600" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/5.embed?link=false"></iframe>

```python
df1 = confirmed_group.copy()
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
#py.plot(fig, filename = 'total_casos_no_china', auto_open=False)
fig.show()
```

## Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados)
<iframe width="100%" height="600" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/7.embed?link=false"></iframe>

```python
df2 = confirmed_group.drop(columns= mas_infectados).copy()
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
#py.plot(fig, filename = 'total_casos_no_8_infectados', auto_open=False)
fig.show()
```

## Animacion del Mapa de Evolucion Temporal del Codiv 19
Mover el Mouse sobre el mapa para ver la informacion de cada pais. Presionar el boton de play para ver la animacion.

<iframe width="100%" height="600" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/54.embed?link=false"></iframe>

```python
confirmed_melt['Fecha'] = pd.to_datetime(confirmed_melt['Fecha'])
confirmed_melt['Fecha'] = confirmed_melt['Fecha'].dt.strftime('%m/%d/%Y')
confirmed_melt['size'] = confirmed_melt['Confirmados'].pow(0.3)
confirmed_melt.dropna(inplace=True) #eliminar filas con valores faltantes

fig = px.scatter_geo(confirmed_melt, locations="Country/Region", locationmode='country names', 
                     color="Confirmados", size='size', hover_name="Country/Region", 
                     range_color= [0, max(confirmed_melt['Confirmados'])+2], 
                     projection="natural earth", animation_frame="Fecha", 
                     title='Contagiados COVID 19 en el Tiempo')
fig.update(layout_coloraxis_showscale=False)
#py.plot(fig, filename = 'mapa_evolucion_temporal', auto_open=False)
fig.show()
```
# Covid 19 en Colombia

## Numero de Casos COVID 19 en Colombia

<iframe width="100%" height="600" frameborder="0" scrolling="no" src="//plotly.com/~joser.zapata/9.embed?link=false"></iframe>

```python
column_names = ["Fecha", "Confirmados", "Recuperados","Muertos", "Activos"]
colombia = pd.DataFrame(columns = column_names)
colombia['Fecha'] = confirmed_group['Fecha']
colombia['Confirmados'] = confirmed_group['Colombia']
colombia['Muertos'] = death_group['Colombia']
colombia['Recuperados'] = recovered_group['Colombia']
colombia['Activos'] = active_group['Colombia']
df_melt3 = colombia.melt(id_vars='Fecha', value_vars= list(colombia.columns)[1:], var_name=None)
fig = px.line(df_melt3, x='Fecha' , y='value', color='variable',
              color_discrete_sequence=["teal","green","coral", "navy"],
              title=f'Corona virus (COVID 19) en Colombia - {colombia.iloc[-1,0]}')
# Indicador de numero total de confirmados
fig.add_indicator( title= {'text':'Confirmados', 'font':{'color':'teal'}},
                  value = colombia['Confirmados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Confirmados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.25], 'y': [0.15, .4]})
#Indicador numero total de Activos
fig.add_indicator(title={'text':'Activos', 'font':{'color':'navy'}},
                  value = colombia['Activos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Activos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.25], 'y': [0.6, .85]})
#Indicador numero total de Recuperados
fig.add_indicator(title={'text':'Recuperados', 'font':{'color':'green'}},
                  value = colombia['Recuperados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Recuperados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.25, 0.50], 'y': [0.6, .85]}) 
#Indicador numero total de muertos
fig.add_indicator(title={'text':'Muertos', 'font':{'color':'coral'}}, 
                  value = colombia['Muertos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Muertos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.25, 0.5], 'y': [0.15, .4]})
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": "Fecha"}})
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'Colombia_general', auto_open=False)
fig.show()
```
# Actualizacion de las Graficas cada 24 Horas
Las graficas creadas con plotly son enviadas a chart-studio y cargadas en la pagina web mediante
el tag *iframe* de html.
Las gráficas se actualizan cada 24 horas usando [Github Actions](https://github.com/features/actions)

# Codigo Fuente Jupyter notebook

 Google Colaboratory | My binder  | NBviewver  
---|---|---
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoseRZapata/JoseRZapata.github.io/master?filepath=Jupyter_Notebook/Covid19_Visualizacion_es.ipynb) | [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)

# Refencias
Fuentes de datos, visualizaciones y análisis de datos.

- https://github.com/CSSEGISandData/COVID-19
- https://www.kaggle.com/imdevskp/covid-19-analysis-viz-prediction-comparisons
- https://junye0798.com/post/build-a-dashboard-to-track-the-spread-of-coronavirus-using-dash/
- https://github.com/Perishleaf/data-visualisation-scripts/tree/master/dash-2019-coronavirus
- https://medium.com/tomas-pueyo/coronavirus-por-qu%C3%A9-debemos-actuar-ya-93079c61e200
- https://github.com/features/actions
