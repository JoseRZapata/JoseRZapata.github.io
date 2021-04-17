---
# Title, summary, and page position.
linktitle: 5. Machine Learning
summary: Libreria de machine Learning que incluye varios algoritmos de clasificación, regresión y análisis de grupos, ademas de herramientas para seleccion, evaluacion de modelos.
weight: 50
icon: laptop-code
icon_pack: fas
authors: ["joserzapata"]

# Page metadata.
title: Machine Learning con Scikit Learn
date: "2021-04-17T00:00:00Z"
type: book  # Do not modify
---

Por [Jose R. Zapata](https://joserzapata.github.io/)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="joserzapata" data-color="#328cc1" data-emoji="" data-font="Cookie" data-text="Invítame a un Café" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script><br>


Scikit-learn es una biblioteca de código abierto de Python que
implementa una gran variedad de algoritmos de aprendizaje automático,
Preprocesamiento, validación cruzada y visualización.

## Proceso de un Proyecto de Machine Learning

En este link encuentran un listado de los pasos a realizar en un proyecto de machine Learning:

https://medium.com/@joserzapata/paso-a-paso-en-un-proyecto-machine-learning-bcdd0939d387

- [1. Definir el problema y mirar el panorama general.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#1-definir-el-problema-y-mirar-el-panorama-general)
- [2. Obténer los datos](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#2-obténer-los-datos)
- [3. Explorar los datos para obtener información.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#3-explorar-los-datos-para-obtener-información)
- [4. Preparación de los datos.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#4-preparación-de-los-datos)
- [5. Exploración y selección de modelos](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#5-exploración-y-selección-de-modelos)
-  [6. Afinar los modelos.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#6-afinar-los-modelos) 
- [7. Presentacion de la solución.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#7-presentacion-de-la-solución)
- [8. Desplegar, monitorear y mantener el sistema.](https://joserzapata.github.io/post/lista-proyecto-machine-learning/#8-desplegar-monitorear-y-mantener-el-sistema)

### Pasos para la construccion y seleccion de un Modelo de Machine Learning

![Construir Modelo](https://miro.medium.com/max/2805/0*IT9aLhgbOVDkMNKM)

1. Preparacion de los datos
2. Division de los datos entre datos de **Entrenamiento** (Para seleccionar el modelo, 80%) y datos de **Test** (para probar el modelo final, 20%)
3. Se selecciona la medida de Evaluacion segun la aplicacion
4. Usando solo los datos de **Entrenamiento** se selecciona los mejores modelos utilizando cross validation y comparando sus resultados 
5. Se toman los mejores modelos (1, 2 o 3 dependiendo de su rendimiento) y se ajustan los Hiper Parametros
6. Se toman los parametros del mejor modelo y se entrena con todos los datos de **Entrenamiento** y se evalua su rendimiento con los datos de **TEST**
7. Si hay un buen resultado se pasa a la etapa de Implementacion (Deployment), en caso contrario segun sea el problema, se prueba con otros modelos o se devuelve a la etapa de Feature Engineering.


## Ejemplo Basico con un solo modelo


```python
## Importar Librerias
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

##  Cargar Dataset
iris = datasets.load_iris()
## Definir cual es la columna de salida
X, y = iris.data[:, :2], iris.target

## Division del dataset en datos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

## Standarizacion de los valores
scaler = preprocessing.StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

## Seleccion del algoritmo de macchine learning
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

## Entrenamiento del Modelo
knn.fit(X_train, y_train)

## Prediccion
y_pred = knn.predict(X_test)

# Evaluacion
accuracy_score(y_test, y_pred)
```

## Preprocesamiento de Datos

### Standardizacion


```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)
```

### Normalizacion


```python
from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)
```

### Binarizacion


```python
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.0).fit(X)
binary_X = binarizer.transform(X)
```

### Encoding Categorical Features


```python
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
y = enc.fit_transform(y)
```

### Imputacion de valores Faltantes


```python
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit_transform(X_train)
```

### Generacion de Caracteristicas Polinomiales


```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(5)
oly.fit_transform(X)
```

### Division datos de Entrenamiento y Prueba


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)
```

## Creacion de Modelos
### Estimadores Aprendizaje Supervisado
#### Regresion
##### Regresion lineal


```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize=True) # los parametros son opcionales
```

##### Arboles de Regresion


```python
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(random_state = 0) # los parametros son opcionales
```

##### Regresion Random Forest


```python
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators = 10, random_state = 0) # los parametros son opcionales
```

#### Clasificacion

##### Regresion Logistica


```python
from sklearn.linear_model import LogisticRegression
lrc = LogisticRegression(random_state = 0) # los parametros son opcionales
```

##### Arboles de decision


```python
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)  # los parametros son opcionales
```

##### Clasificador Random Forest


```python
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0) # los parametros son opcionales
```

##### Support Vector Machines (SVM)


```python
from sklearn.svm import SVC
svc = SVC(kernel='linear') # los parametros son opcionales
```

##### Kernel Support Vector Machines (SVM)


```python
from sklearn.svm import SVC
svck = SVC(kernel = 'rbf', random_state = 0) # los parametros son opcionales
```

##### Naive Bayes


```python
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
```

##### KNN


```python
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5) # los parametros son opcionales
```

### Estimadores de Aprendizaje No supervizado
#### Principal Component Analysis (PCA)


```python
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
```

#### K Means


```python
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
```

#### Hierarchical


```python
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward') # los parametros son opcionales
```

## Entrenamiento de Modelos
### Aprendizaje Supervisado


```python
# Regresion
lr.fit(X_train, y_train)
dtr.fit(X_train, y_train)
rfr.fit(X_train, y_train)

#Clasificacion
lrc.fit(X_train, y_train)
dtc.fit(X_train, y_train)
rfc.fit(X_train, y_train)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
svck.fit(X_train, y_train)
gnb.fit(X_train, y_train)
```

### Aprendizaje No Supervisado


```python
k_means.fit(X_train)
pca_model = pca.fit_transform(X_train)
```

## Prediccion
### Estimacion Supervisada


```python
# Regresion
y_pred = lr.predict(X_test)
y_pred = dtr.predict(X_test)
y_pred = rfr.predict(X_test)

# Clasificacion
y_pred = svc.predict(X_test)
y_pred = svck.predict(X_test)
y_pred = lrc.predict(X_test)
y_pred = dtc.predict(X_test)
y_pred = rfc.predict(X_test)
y_pred = gnb.predict(X_test)
y_pred = knn.predict_proba(X_test))
```

### Estimacion No Supervisada


```python
y_pred = k_means.predict(X_test)
y_hc = hc.fit_predict(X_train)
```

## Evaluacion de los Modelos
### Metricas de Clasificacion
#### Accuracy Score


```python
knn.score(X_test, y_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```

#### Reporte de Clasificacion


```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred)))
```

#### Confusion Matrix


```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
```

### Metricas de Regresion
#### Error absoluto medio (Mean Absolute Error)


```python
from sklearn.metrics import mean_absolute_error
y_true = [3, -0.5, 2])
mean_absolute_error(y_true, y_pred))
```

#### Error Cuadratico Medio (Mean Squared Error)


```python
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred))
```

#### R2 Score


```python
from sklearn.metrics import r2_score
r2_score(y_true, y_pred))
```

### Metricas de Clustering

#### Adjusted Rand Index


```python
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(y_true, y_pred))
```

#### Homogeneidad


```python
from sklearn.metrics import homogeneity_score
homogeneity_score(y_true, y_pred))
```

#### V-measure


```python
from sklearn.metrics import v_measure_score
metrics.v_measure_score(y_true, y_pred))
```

## Cross-Validation


```python
print(cross_val_score(knn, X_train, y_train, cv=4))
print(cross_val_score(lr, X, y, cv=2))
```

## Sintonizacion del Modelo (Hyper - parametrizacion)
### Grid Search


```python
from sklearn.model_selection import GridSearchCV
params = {"n_neighbors": np.arange(1,3), "metric": ["euclidean", "cityblock"]}
grid = GridSearchCV(estimator=knn,param_grid=params)# 5 CV
grid.fit(X_train, y_train)
print(grid.best_score_)
print(grid.best_estimator_.n_neighbors)
```

### Optimizacion Aleatoria de Parametros


```python
# Ejemplo
from sklearn.model_selection import RandomizedSearchCV
params = {"n_neighbors": range(1,5), "weights": ["uniform", "distance"]}

rsearch = RandomizedSearchCV(estimator=knn,
           param_distributions=params,
           cv=4,
           n_iter=8,
           random_state=5)
rsearch.fit(X_train, y_train)
print(rsearch.best_score_)
print(rsearch.best_params_)
```


```python
knn = neighbors.KNeighborsClassifier(n_neighbors=2, weights = "uniform")
knn.fit(X_train, y_train)
```

## Referencias
Cheatsheet scikitlearn 
https://datacamp-community-prod.s3.amazonaws.com/5433fa18-9f43-44cc-b228-74672efcd116

**Phd. Jose R. Zapata**
- [https://joserzapata.github.io/](https://joserzapata.github.io/)
- joser.zapata@upb.edu.co
