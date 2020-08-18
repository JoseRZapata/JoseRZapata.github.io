#!/usr/bin/env python
# coding: utf-8

"""[Visualizacion del Coronavirus (COVID19) Mundial]

por: Jose R. Zapata - https://joserzapata.github.io/

https://joserzapata.github.io/post/covid19-visualizacion/

Ejemplo:
python Covid19_Update.py [chart_studio username] [chart_studio password]

He visto en las redes sociales varias visualizaciones de los datos del COVID 19 y queria realizarlos en Python para tener la actualizacion de las graficas
actualizadas cada dia, y ademas practicar el uso de [plotly](https://plotly.com/) para visualizacion interactiva.

Las Graficas se actualizaran diariamente con los nuevos datos!

Informacion extraida de 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE

https://github.com/CSSEGISandData/COVID-19

Actualizaciones:
- 25/May/2020 agregar datos de personas recuperadas
"""

import pandas as pd
import plotly.express as px
import numpy as np
import chart_studio
import sys

username = sys.argv[1] # chart studio usuario
api_key = sys.argv[2] # chart studio clave

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
import chart_studio.plotly as py

# %%
# Leer datos

# los datos de personas recuperadas no eran confiables entonces ya solo se tienen los datos de confirmados y muertos

confirmed = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
death = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recovered = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

# %% [markdown]
# ## Datos CSSEGISandData/COVID-19
#
# Descripcion de los datos
#
# **Province/State:** China - province name; US/Canada/Australia/ - city name, state/province name; Others - name of the event (e.g., "Diamond Princess" cruise ship); other countries - blank.
#
# **Country/Region:** country/region name conforming to WHO (will be updated).
#
# **Last Update:** MM/DD/YYYY HH:mm (24 hour format, in UTC).
#
# **Confirmed: **the number of confirmed cases. For Hubei Province: from Feb 13 (GMT +8), we report both clinically diagnosed and lab-confirmed cases. For lab-confirmed cases only (Before Feb 17), please refer to who_covid_19_situation_reports. For Italy, diagnosis standard might be changed since Feb 27 to "slow the growth of new case numbers."
#
# **Deaths:** the number of deaths.
# **Recovered:** the number of recovered cases.

# %%
#confirmed.head()


# %%
#death.head()

# %% [markdown]
# ## Datos Generales de cada Dataframe

# %%
#confirmed.info()


# %%
#death.info()

# %% [markdown]
# ### Eliminar Ubicacion
#
# Se va realizar un analisis general de los datos y No se van a tomar los datos geograficos de *latitud*, *longitud* y los datos de *Province/State* estan incompletos.
#
# Solo se realizara un analisis por pais entonces se eliminaran las columnas mencionadas anteriormente
#

# %%
confirmed = confirmed.drop(columns=['Lat', 'Long','Province/State'])


# %%
death = death.drop(columns=['Lat', 'Long','Province/State'])
recovered  = recovered.drop(columns=['Lat', 'Long','Province/State'])
# %%
# ### Personas Activas
active =confirmed.copy()
# Calcular el numero de casos activos
active.iloc[:,1:] = confirmed.iloc[:,1:] - death.iloc[:,1:] - recovered.iloc[:,1:]

# %% [markdown]
# ### Consolidar datos

# %%
confirmed_group = confirmed.groupby(by='Country/Region')
confirmed_group = confirmed_group.aggregate(np.sum)
confirmed_group = confirmed_group.T
confirmed_group.index.name = 'date'
confirmed_group =  confirmed_group.reset_index()


# %%
death_group = death.groupby(by='Country/Region')
death_group = death_group.aggregate(np.sum)
death_group = death_group.T
death_group.index.name = 'date'
death_group =  death_group.reset_index()
# %%
recovered_group = recovered.groupby(by='Country/Region')
recovered_group = recovered_group.aggregate(np.sum)
recovered_group = recovered_group.T
recovered_group.index.name = 'date'
recovered_group =  recovered_group.reset_index()

# %%
active_group = active.groupby(by='Country/Region')
active_group = active_group.aggregate(np.sum)
active_group = active_group.T
active_group.index.name = 'date'
active_group =  active_group.reset_index()


# %%
confirmed_melt = confirmed_group.melt(id_vars="date")
confirmed_melt.rename(columns = {'value':'Confirmados', 'date':'Fecha'}, inplace = True)


# %%
death_melt = death_group.melt(id_vars="date")
death_melt.rename(columns = {'value':'Muertos', 'date':'Fecha'}, inplace = True)

# %% [markdown]
# ### Datos Mundiales

# %%
# Numero de Casos confirmados por dia en el mundo

column_names = ["Fecha", "Confirmados", "Recuperados","Muertos"]
world = pd.DataFrame(columns = column_names)
world['Fecha'] = confirmed_group['date']
world['Confirmados'] = confirmed_group.iloc[:,1:].sum(1)
world['Muertos'] = death_group.iloc[:,1:].sum(1)
world['Recuperados'] = recovered_group.iloc[:,1:].sum(1)
world['Activos'] = active_group.iloc[:,1:].sum(1)

# %% [markdown]
# # Visualizacion con Plotly
# %% [markdown]
# ## Valores Mundiales de Confirmados y Muertos
#

# %%
temp = pd.DataFrame(world.iloc[-1,:]).T
tm = temp.melt(id_vars="Fecha", value_vars=[ "Confirmados","Activos","Recuperados","Muertos"])
fig = px.bar(tm, x="variable" , y="value", color= 'variable', text='value',
             color_discrete_sequence=["teal","navy","green", "coral"],
             height=500, width=600,
             title= f'Total de Casos Mundiales de COVID 19 - {str(world.iloc[-1,0])}')
fig.update_traces(textposition='outside')#poner los valores de las barras fuera
fig.add_annotation(x='Muertos', y=tm['value'].max(),text='https://joserzapata.github.io/', showarrow=False)
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": ""}} #Esconder nombre eje x
                  )
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_general', auto_open=False)
#fig.show()

# %% [markdown]
# ## Mapa Mundial de Confirmados por Pais

# %%
confirmed_melt['Fecha'] = pd.to_datetime(confirmed_melt['Fecha'])
confirmed_melt['Fecha'] = confirmed_melt['Fecha'].dt.strftime('%m/%d/%Y')
confirmed_melt['size'] = confirmed_melt['Confirmados'].pow(0.3)

max_Fecha = confirmed_melt['Fecha'].max()
conf_max = confirmed_melt[confirmed_melt['Fecha']== max_Fecha].copy()
conf_max.dropna(inplace=True) #eliminar filas con valores faltantes

fig = px.scatter_geo(conf_max, locations="Country/Region", locationmode='country names',
                     color="Confirmados", size='size', hover_name="Country/Region",
                     range_color= [0, max(confirmed_melt['Confirmados'])+2],
                     projection="natural earth", width=900,
                     title='Mapa de Confirmados COVID 19 por Pais')
fig.add_annotation(x=0.5, y=0,text='https://joserzapata.github.io/', showarrow=False)
fig.update(layout_coloraxis_showscale=False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'mapa_confirmados_pais', auto_open=False)
#fig.show()

# %% [markdown]
# # Confirmados vs Muertos por pais

# %%
death_melt['Fecha'] = pd.to_datetime(death_melt['Fecha'])
death_melt['Fecha'] = death_melt['Fecha'].dt.strftime('%m/%d/%Y')

max_Fecha = death_melt['Fecha'].max()
death_max = death_melt[death_melt['Fecha']== max_Fecha].copy()
death_max.dropna(inplace=True) #eliminar filas con valores faltantes

full_melt_max = pd.merge(conf_max[['Country/Region','Confirmados']],
                         death_max[['Country/Region','Muertos']],
                         on='Country/Region', how='left')

fig = px.scatter(full_melt_max.sort_values('Muertos', ascending=False).iloc[:10, :],
                 x='Confirmados', y='Muertos', color='Country/Region', size='Confirmados', height=500,width=900,
                 text='Country/Region', log_x=True, log_y=True, title= f'Muertos vs Confirmados - {max_Fecha} - (10 Paises)')
fig.update_traces(textposition='top center')
fig.layout.update(showlegend = False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'scatter_muertos_confirmados', auto_open=False)
#fig.show()

# %% [markdown]
# ## Progresion Mundial en el Tiempo del numero de casos
#

# %%
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
fig.add_annotation(x=80, y=world_melt['value'].max(),
                   text='https://joserzapata.github.io/', showarrow=False)
fig.layout.update(showlegend = False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_serie', auto_open=False)
#fig.show()

# %% [markdown]
# ## Total Casos Confirmados de COVID 19 por Pais
#

# %%
#df1 = confirmed_group.drop(columns=["China"])
df1 = confirmed_group
# Cambiar el nombre de la columna
df1.rename(columns = {'date':'Fecha'}, inplace = True)
if api_key:
    # se toman la serie de tiempo cada 2 dias, por que las graficas
    # grandes no se pueden subir a chart-studio con subscripcion gratuita
    df1 = df1.iloc[::-2].iloc[::-1]

df_melt = df1.melt(id_vars='Fecha', value_vars= list(df1.columns)[1:], var_name=None)
fig = px.line(df_melt, x='Fecha' , y='value', color='Country/Region',
              color_discrete_sequence=px.colors.qualitative.G10, width=900,
              title=f'Total Casos Confirmados de COVID 19 por Pais - {world.iloc[-1,0]}')
# 8 paises mas infectados
fecha = df1['Fecha'].iloc[-1] #obtener la fecha del ultimo dato
paises = df1.iloc[-1,1:] #obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
mas_infectados=[]
for n in range(8):
  fig.add_annotation(x=fecha, y=paises[n], text=paises.index[n],
                     showarrow=True, ax=+30, xref="x",yref="y")
  mas_infectados.append(paises.index[n])
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
fig.add_annotation(x=60, y=df_melt['value'].max(),
                   text='https://joserzapata.github.io/', showarrow=False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_no_china', auto_open=False)
#fig.show()

# %% [markdown]
# ## Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados)

# %%
df2 = confirmed_group.drop(columns=mas_infectados)
# Cambiar el nombre de la columna
df2.rename(columns = {'date':'Fecha'}, inplace = True)
if api_key:
    # se toman la serie de tiempo cada 2 dias, por que las graficas
    # grandes no se pueden subir a chart-studio con subscripcion gratuita
    df2 = df2.iloc[::-2].iloc[::-1]

df_melt2 = df2.melt(id_vars='Fecha', value_vars= list(df2.columns)[1:], var_name=None)
fig = px.line(df_melt2, x='Fecha' , y='value', color='Country/Region',
              color_discrete_sequence=px.colors.qualitative.G10, width=900,
              title=f'Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados) - {world.iloc[-1,0]}')

fecha = df2['Fecha'].iloc[-1] #obtener la fecha del ultimo dato
paises = df2.iloc[-1,1:] #obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
for n in range(8):
  fig.add_annotation(x=fecha, y=paises[n], text=paises.index[n],
                     showarrow=True, ax=+30,xref="x", yref="y")
fig.add_annotation(x=60, y=df_melt2['value'].max(),
                   text='https://joserzapata.github.io/', showarrow=False)
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'total_casos_no_8_infectados', auto_open=False)
#fig.show()

# %% [markdown]
# # Animacion del Mapa de Evolucion Temporal del Codiv 19

# %%
if api_key:
    # se toman la serie de tiempo cada 4 dias, por que las graficas
    # grandes no se pueden subir a chart-studio con subscripcion gratuita
    confirmed_melt = confirmed_group.iloc[::-4].iloc[::-1].melt(id_vars="Fecha")
    confirmed_melt.rename(columns = {'value':'Confirmados', 'date':'Fecha'}, inplace = True)

confirmed_melt['Fecha'] = pd.to_datetime(confirmed_melt['Fecha'])
confirmed_melt['Fecha'] = confirmed_melt['Fecha'].dt.strftime('%m/%d/%Y')
confirmed_melt['size'] = confirmed_melt['Confirmados'].pow(0.3)
confirmed_melt.dropna(inplace=True) #eliminar filas con valores faltantes


fig = px.scatter_geo(confirmed_melt, locations="Country/Region", locationmode='country names',
                     color="Confirmados", size='size', hover_name="Country/Region",
                     range_color= [0, max(confirmed_melt['Confirmados'])+2],
                     projection="natural earth", animation_frame="Fecha", width=900,
                     title='Contagiados COVID 19 en el Tiempo')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(x=0.5, y=-0.1,text='https://joserzapata.github.io/', showarrow=False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'mapa_evolucion_temporal', auto_open=False)
#fig.show()

# %% [markdown]
# ## Numero de Casos COVID 19 en Colombia

# %%
column_names = ["Fecha", "Confirmados", "Recuperados","Muertos", "Activos"]
colombia = pd.DataFrame(columns = column_names)
colombia['Fecha'] = confirmed_group['date']
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
fig.add_annotation(x=80, y=df_melt3['value'].max(),
                   text='https://joserzapata.github.io/', showarrow=False)
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": "Fecha"}})
# grabar grafica en chart-studio si se proporciona el api-key
if api_key: py.plot(fig, filename = 'Colombia_general', auto_open=False)
#fig.show()

# %% [markdown]
# # Codigo Fuente Jupyter notebook
# ## Ejecutar en Google Colaboratory
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)
#
# ## Ejecutar en MyBinder
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoseRZapata/JoseRZapata.github.io/master?filepath=Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)
#
# ## Leer en nbviewer
# [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/JoseRZapata/JoseRZapata.github.io/blob/master/Jupyter_Notebook/Covid19_Visualizacion_es.ipynb)
# %% [markdown]
# # Refencias
# Fuentes de datos, visualizaciones y analisis de datos.
#
# - https://github.com/CSSEGISandData/COVID-19
# - https://www.kaggle.com/imdevskp/covid-19-analysis-viz-prediction-comparisons
# - https://junye0798.com/post/build-a-dashboard-to-track-the-spread-of-coronavirus-using-dash/
# - https://github.com/Perishleaf/data-visualisation-scripts/tree/master/dash-2019-coronavirus
# - https://medium.com/tomas-pueyo/coronavirus-por-qu%C3%A9-debemos-actuar-ya-93079c61e200


print("Graficas actualizadas \U0001f600")
print("https://joserzapata.github.io/")
