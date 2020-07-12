#!/usr/bin/env python
# coding: utf-8

"""[Actualizacion Bar Chart Race]

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
- 31/May/2020 bar chart race
"""

import pandas as pd
import numpy as np
import sys
import pandas_alive

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


# %% [markdown]
# ### Eliminar Ubicacion
#
# Se va realizar un analisis general de los datos y No se van a tomar los datos geograficos de *latitud*, *longitud* y los datos de *Province/State* estan incompletos.
#
# Solo se realizara un analisis por pais entonces se eliminaran las columnas mencionadas anteriormente
#

# %%
confirmed = confirmed.drop(columns=['Lat', 'Long','Province/State'])
death = death.drop(columns=['Lat', 'Long','Province/State'])
recovered  = recovered.drop(columns=['Lat', 'Long','Province/State'])
# %%
# ### Personas Activas
active =confirmed.copy()
# Calcular el numero de casos activos
active.iloc[:,1:] = active.iloc[:,1:] - death.iloc[:,1:] - recovered.iloc[:,1:]

# %% [markdown]
# ### Consolidar datos

# %%
active_group = active.groupby(by='Country/Region')
active_group = active_group.aggregate(np.sum)
active_group = active_group.T
active_group.index.name = 'date'
active_group =  active_group.reset_index()

# %% [markdown]
# ### Datos Mundiales

# #Evolucion Animada de casos activos por pais
active_evol = active_group.set_index('date')
active_evol.index = pd.to_datetime(active_evol.index)
active_evol.plot_animated(filename='evolucion_casos_activos.gif', n_bars=8,n_visible=8,
                          title='Evolución en el tiempo de Casos Activos COVID-19 por pais \n https://joserzapata.github.io/',
                          period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
                          dpi=100,
                          period_fmt='%B %d, %Y',
                          period_summary_func=lambda v: {'x': .99, 'y': .18,
                                      's': f'Total Activos: {v.nlargest(8).sum():,.0f}',
                                      'ha': 'right', 'size': 9, 'family': 'Courier New'});




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


print("Bar chart Race actualizada \U0001f600")
print("https://joserzapata.github.io/")
