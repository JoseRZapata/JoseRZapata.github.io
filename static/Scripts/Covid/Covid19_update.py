#!/usr/bin/env python
# coding: utf-8

"""[Visualizacion del Coronavirus (COVID19) Mundial]

por: Jose R. Zapata - https://joserzapata.github.io/

https://joserzapata.github.io/post/covid19-visualizacion/ 

Ejemplo:
python Covid19_update.py [chart_studio username] [chart_studio password]
 
He visto en las redes sociales varias visualizaciones de los datos del COVID 19 y queria realizarlos en Python para tener la actualizacion de las graficas
actualizadas cada dia, y ademas practicar el uso de [plotly](https://plot.ly/) para visualizacion interactiva.

Las Graficas se actualizaran diariamente con los nuevos datos!

Informacion extraida de 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE
 
https://github.com/CSSEGISandData/COVID-19
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


# Leer datos

confirmed = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
death = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')


# Eliminar Ubicacion


confirmed = confirmed.drop(columns=['Lat', 'Long','Province/State'])
death = death.drop(columns=['Lat', 'Long','Province/State'])

#  Consolidar datos

confirmed_group = confirmed.groupby(by='Country/Region')
confirmed_group = confirmed_group.aggregate(np.sum)
confirmed_group = confirmed_group.T
confirmed_group.index.name = 'date'
confirmed_group =  confirmed_group.reset_index()

death_group = death.groupby(by='Country/Region')
death_group = death_group.aggregate(np.sum)
death_group = death_group.T
death_group.index.name = 'date'
death_group =  death_group.reset_index()

confirmed_melt = confirmed_group.melt(id_vars="date")
confirmed_melt.rename(columns = {'value':'Confirmados', 'date':'Fecha'}, inplace = True)


#  Datos Mundiales

# Numero de Casos confirmados por dia en el mundo

column_names = ["Fecha", "Confirmados", "Muertos"]
world = pd.DataFrame(columns = column_names)
world['Fecha'] = confirmed_group['date']
world['Confirmados'] = confirmed_group.iloc[:,1:].sum(1)
world['Muertos'] = death_group.iloc[:,1:].sum(1)

# Visualizacion con Plotly

# Valores Mundiales de Confirmados y Muertos
# 

temp = pd.DataFrame(world.iloc[-1,:]).T

tm = temp.melt(id_vars="Fecha", value_vars=[ "Confirmados","Muertos"])
fig = px.bar(tm, x="variable" , y="value", color= 'variable',
             color_discrete_sequence=["green", "blue"],
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
py.plot(fig, filename = 'total_casos_general', auto_open=False)
#fig.show()


# Mapa Mundial de Confirmados por Pais

confirmed_melt['Fecha'] = pd.to_datetime(confirmed_melt['Fecha'])
confirmed_melt['Fecha'] = confirmed_melt['Fecha'].dt.strftime('%m/%d/%Y')
confirmed_melt['size'] = confirmed_melt['Confirmados'].pow(0.3)

max_Fecha = confirmed_melt['Fecha'].max()
conf_max = confirmed_melt[confirmed_melt['Fecha']== max_Fecha].copy()
conf_max.dropna(inplace=True) #eliminar filas con valores faltantes

fig = px.scatter_geo(conf_max, locations="Country/Region", locationmode='country names', 
                     color="Confirmados", size='size', hover_name="Country/Region", 
                     range_color= [0, max(confirmed_melt['Confirmados'])+2], 
                     projection="natural earth", 
                     title='Mapa de Confirmados COVID 19 por Pais')
fig.update(layout_coloraxis_showscale=False)
py.plot(fig, filename = 'mapa_confirmados_pais', auto_open=False)
#fig.show()


# ## Progresion Mundial en el Tiempo del numero de casos

world_melt = world.melt(id_vars='Fecha', value_vars= list(world.columns)[1:], var_name=None)

fig = px.line(world_melt, x="Fecha", y= 'value',
              color='variable',
              title=f'Total de Casos en el tiempo de COVID 19 - {world.iloc[-1,0]}')
for n in list(world.columns)[1:]:
  fig.add_annotation(x=world.iloc[-1,0], y=world.loc[world.index[-1],n],
                     text=n,
                     showarrow=True, ax=-50, ay=-20, xref="x",yref="y" )
# Indicador de numero total de confirmados
fig.add_indicator( title='Confirmados', value = world['Confirmados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Confirmados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.5], 'y': [0.25, .75]})
#Indicador numero total de muertos
fig.add_indicator(title='Muertos', value = world['Muertos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": world['Muertos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.5, 0.75], 'y': [0.25, .75]})  
fig.layout.update(showlegend = False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio
py.plot(fig, filename = 'total_casos_serie', auto_open=False)
#fig.show()


# ## Total Casos Confirmados de COVID 19 por Pais
# 

df1 = confirmed_group
# Cambiar el nombre de la columna
df1.rename(columns = {'date':'Fecha'}, inplace = True) 
df_melt = df1.melt(id_vars='Fecha', value_vars= list(df1.columns)[1:], var_name=None)
fig = px.line(df_melt, x='Fecha' , y='value', color='Country/Region',
              color_discrete_sequence=px.colors.qualitative.G10,
              title=f'Total Casos Confirmados de COVID 19 por Pais - {world.iloc[-1,0]}')
# 8 paises mas infectados
fecha = df1['Fecha'].iloc[-1] #obtener la fecha del ultimo dato
paises = df1.iloc[-1,1:] #obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
mas_infectados=[]
for n in range(8):
  fig.add_annotation(x=fecha, y=paises[n], text=paises.index[n],
                     showarrow=True, ax=+30, ay=0, xref="x",yref="y")
  mas_infectados.append(paises.index[n])
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
# grabar grafica en chart-studio
py.plot(fig, filename = 'total_casos_no_china', auto_open=False)
#fig.show()


# ## Total Casos Confirmados de COVID 19 por Pais (Excluyendo los 8 mas infectados)


df2 = confirmed_group.drop(columns=mas_infectados)
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
                     showarrow=True, ax=+30, ay=0, xref="x",yref="y")
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  )
py.plot(fig, filename = 'total_casos_no_8_infectados', auto_open=False)
#fig.show()


# # Animacion del Mapa de Evolucion Temporal del Codiv 19

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
py.plot(fig, filename = 'mapa_evolucion_temporal', auto_open=False)
#fig.show()


# ## Numero de Casos COVID 19 en Colombia

column_names = ["Fecha", "Confirmados", "Muertos"]
colombia = pd.DataFrame(columns = column_names)
colombia['Fecha'] = confirmed_group['Fecha']
colombia['Confirmados'] = confirmed_group['Colombia']

colombia['Muertos'] = death_group['Colombia']
df_melt3 = colombia.melt(id_vars='Fecha', value_vars= list(colombia.columns)[1:], var_name=None)
fig = px.line(df_melt3, x='Fecha' , y='value', color='variable',
              color_discrete_sequence=px.colors.qualitative.G10,
              title=f'Corona virus (COVID 19) en Colombia - {colombia.iloc[-1,0]}')
fig.add_indicator( title='Confirmados', value = colombia['Confirmados'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Confirmados'
                  ].iloc[-2], 'relative': True },domain = {'x': [0, 0.5], 'y': [0.25, .75]})

fig.add_indicator(title='Muertos', value = colombia['Muertos'].iloc[-1],
                  mode = "number+delta", delta = {"reference": colombia['Muertos'
                  ].iloc[-2], 'relative': True },domain = {'x': [0.5, 0.75], 'y': [0.25, .75]})
fig.layout.update(showlegend=False,
                  yaxis =  {"title": {"text": "Numero de Personas"}}, # Cambiar texto eje y
                  xaxis =  {"title": {"text": "Fecha"}})
py.plot(fig, filename = 'Colombia_general', auto_open=False)
#fig.show()

print("Graficas actualizadas \U0001f600")
print("https://joserzapata.github.io/")
