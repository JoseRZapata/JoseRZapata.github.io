---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Paso a paso en un Proyecto Machine Learning"
subtitle: "Checklist y preguntas a realizar para su desarrollo"
summary: ""
authors: ["Jose R. Zapata"]
tags: ["Data-Science"]
categories: ["Data-Science"]
date: 2020-04-09T06:54:44-05:00
lastmod: 2020-04-09T06:54:44-05:00
featured: false
draft: true

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

Esta es una traduccion propia al español del Apendice B (Machine Learning Project Checklist) del libro
[Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems](https://www.amazon.com/-/es/gp/product/B07XGF2G87/) 2nd Edition de [Aurélien Géron](https://twitter.com/aureliengeron)
con algunos pasos propios agregados o que he encontrado en otros libros o cursos que he realizado.

Este Libro me ha gustado mucho, para mi es el libro practico mas completo sobre machine learning con python que he leido, tiene una excelente estructura, codigo en python muy bien explicado, ademas muchos tips y sugerencias para realizar un proyecto de machine learning.

El libro esta acompañado por un repositorio con Jupyter Notebooks: https://github.com/ageron/handson-ml2

{{% toc %}}

***

Esta lista de verificación puede ser una guia paso a paso para proyectos de Machine Learning.

# Definir el problema y mirar el panorama general.
1. Definir el objetivo en términos del negocio.
2. ¿Cómo se usará su solución?
3. ¿Cuáles son las soluciones actuales (si las hay)?
4. ¿Cómo se debe enmarcar este problema (supervisado / no supervisado, en línea / fuera de línea,
etc.)
5. ¿Cómo se debe medir el desempeño o el rendimiento de la solucion?
6. ¿La medida de desempeño está alineada con el objetivo del negocio?
7. ¿Cuál sería el desempeño o rendimiento mínimo necesario para alcanzar el objetivo del negocio?
8. ¿Cuáles son los problemas parecidos? ¿Se puede reutilizar experiencias o herramientas ya creadas?
9. ¿Hay experiencia del problema disponible?
10. ¿Cómo se puede resolver el problema manualmente?
11. Hacer un listado de los supuestos que hay hasta este momento.
12. Verificar los supuestos si es posible.

# Obténer los datos
{{% alert note %}}
**Nota:** automatizar tanto como sea posible este proceso para que pueda obtener fácilmente datos nuevos.
{{% /alert %}}

1. Enumere los datos que necesita y la cantidad que necesita.
2. Busque y documente dónde se pueden obtener los datos.
3. Compruebe cuánto espacio de almacenamiento ocuparán los datos.
4. Verifique las limitaciones legales y obtener autorización a los datos si es necesario.
5. Obtener autorizaciones de acceso a los datos.
6. Reservar suficiente espacio de almacenamiento para el proyecto.
7. Obtener los datos.
8. Convertir los datos a un formato que se pueda manipular fácilmente (sin cambiar los datos en sí).
9. Asegúrarse de que la información confidencial se elimine o se proteja (por ejemplo, anonimizar los datos).
10. Verificar el tamaño y el tipo de datos (series de tiempo, muestra de datos, geoposicionamiento, etc.).
11. **Separar un conjunto de datos prueba, dejarlos a un lado y nunca mirarlos.**

# Explorar los datos para obtener información.
{{% alert note %}}
**Nota:** intente obtener información de un experto en el tema para estos pasos.
{{% /alert %}}

1. Crear una copia de los datos para explorarlos (muestreándolos a un tamaño manejable
si necesario).
2. Crar un Jupyter Notebook para mantener un registro de la exploración de los datos.
3. Estudiar cada atributo y sus características **(Analisis Univariable)**:
  - Nombre
  - Tipo  de dato (categórico, int / float, acotado / no acotado, texto, estructurado, etc.)
  - porcentaje (%) de valores faltantes.
  - Ruido y tipo de ruido (estocástico, valores atípicos, errores de redondeo, etc.)
  - ¿Son posiblemente útiles para el proyecto?
  - Tipo de distribución (gaussiana, uniforme, logarítmica, etc.)
4. Para los proyectos de aprendizaje supervisado, identifique los atributos objetivo (target).
5. Visualizacion de los datos.
6. Estudiar las correlaciones entre atributos **(Analisis Bivariable)**.
7. Estudiar cómo resolver el problema manualmente.
8. Identificar las transformaciones que tal vez se puedan aplicar.
9. Identificar datos adicionales que pueden ser útiles.
10. Documentar lo que ha aprendido.

# Preparación de los datos.

Para exponer mejor los patrones de los datos y usarlos con los algoritmos de Machine Learning.

{{% alert note %}}

**Notas:**
- Trabaje en copias de los datos (mantenga intacto el conjunto de datos original).
- Escriba funciones para todas las transformaciones de datos que realice, por cinco razones:
  - Para que pueda preparar fácilmente los datos la próxima vez que obtenga un conjunto de datos nuevo
  - Para que pueda aplicar estas transformaciones en proyectos futuros
  - Para limpiar y preparar el set de datos de prueba
  - Para limpiar y preparar nuevas instancias de datos una vez que su solución esté activa (produccion)
  - Para que sea fácil probar diferentes formas de preparación de datos como hiperparámetros
  
{{% /alert %}} 

1. Limpieza de datos:
  - Eliminar registros datos duplicados (disminuir el numero de datos)
  - Corregir o eliminar valores atípicos (opcional). 
  - Los valores atípicos pueden separarse del dataset dependiendo del problema del proyecto (por ejemplo, deteccion de anomalias).
  - Completar los valores faltantes (por ejemplo, con cero, media, mediana ...) o eliminar las filas (o
columnas).
1. Selección de atributos (**Feature Selection**) (opcional):
- Descartar los atributos que no proporcionan información útil para el proyecto.
- Eliminar registros duplicados (al eliminar atributos pueden quedar registros iguales)
3. Ingeniería de atributos (**Feature Engineering**), cuando sea apropiado:
- Discretizar las atributos continuas.
- Descomponer en partes los atributos (p. Ej., Categóricas, fecha / hora, etc.).
- Agregar transformaciones prometedoras de las atributos (por ejemplo, log(x), sqrt(x), x^2, etc.).
- Aplicar funciones a los datos para agregar nuevos atributos.
4. Escalado de atributos (**Feature Scaling**).: 
- estandarizar o normalizar atributos.

# Exploracion y seleccion de modelos
{{% alert note %}}
**Notas:**
- Si se tiene una gran cantidad de datos, es posible que desee hacer un muestreo de los datos para tener conjuntos de entrenamiento más pequeños, de esta forma se pueden entrenar varios modelos diferentes en un tiempo razonable (se debe tener en cuenta que esto penaliza modelos complejos como redes neuronales grandes o Random Forest).
- Una vez más, intentar automatizar estos pasos tanto como sea posible.
{{% /alert %}}

1. Entrenar muchos modelos rápidos y utilizando parámetros estándar de diferentes categorías (p. Ej., Lineales, Naive Bayes, SVM, Random Forest, redes neuronales, etc.).
2. Medir y comparar su desempeño.
- Para cada modelo, utilice la validación cruzada (Cross validation) de N subconjuntos y calcule la media y la desviación estándar de la medida de rendimiento en las N evaluaciones.
3. Analice las variables más significativas para cada algoritmo.
4. Analice los tipos de errores que cometen los modelos.
- ¿Qué datos habría utilizado un humano para evitar estos errores?
5. Realizar rapidamente una selección de atributos e ingeniería de atributos (Feature selection, Feature Engineering).
6. Realice una o dos iteraciones rápidas más de los cinco pasos anteriores.
7. Hacer una lista corta de los tres a cinco modelos más prometedores, prefiriendo seleccionar modelos que cometan diferentes tipos de errores (diversidad de los errores).

# Afinar los modelos.
{{% alert note %}}
**Notas:**
- Se deberá utilizar la mayor cantidad de datos posible para este paso, especialmente a medida que avanza hacia el final del ajuste fino del modelo.
- Como siempre, automatizar lo que se pueda.
{{% /alert %}}

1. Ajuste los hiperparámetros ([hyperparameter tunning](https://en.wikipedia.org/wiki/Hyperparameter_optimization)) mediante validación cruzada (cross validation).
- Tratar las elecciones de transformación de datos como hiperparámetros, especialmente cuando no esta seguro de ellos (por ejemplo, ¿debería reemplazar los valores faltantes con cero o con el valor medio? ¿O simplemente dejar eliminar las filas?).
- A menos que haya muy pocos valores de hiperparámetros para explorar, prefiera la búsqueda aleatoria (random search)  a la búsqueda de cuadrícula (grid search). Si el entrenamiento es muy largo, es posible que prefiera un enfoque de optimización bayesiano (por ejemplo, utilizando procesos previos gaussianos, como lo describen [Jasper Snoek, Hugo Larochelle y Ryan Adams](https://goo.gl/PEFfGr)[^1].
2. Pruebe los métodos de Ensamble (ensemble methods). La combinación de sus mejores modelos a menudo tendrá un mejor rendimiento que se ejecutan individualmente (hay mejor desempeño si hay diversidad de errores entre los modelos).
3. Una vez que esté seguro de su modelo final, mida su rendimiento en el conjunto de prueba (test set, separado al inicio) para estimar el error de generalización.

{{% alert warning %}}
No modifique su modelo después de medir el error de generalización:
simplemente comenzaría a sobreajustar el conjunto de prueba.
{{% /alert %}}

# Presentacion de la solución. 
1. Documentar lo que ha hecho.
2. Crear una buena presentación.
- Asegúrese de resaltar el panorama general del proyecto o del problema primero.
3. Explicar por qué la solución encontrada logra el objetivo buscado.
4. No olvidar presentar puntos interesantes que se notaron en el camino.
- Describir qué funcionó y qué no.
- Enumerar los supuestos y las limitaciones del sistema.
5. Asegúrarse de que los hallazgos clave se comuniquen a través de hermosas visualizaciones o declaraciones fáciles de recordar (por ejemplo, "el ingreso medio es el predictor número uno de los precios de la vivienda").

# Desplegar, monitorear y mantener el sistema. 
1. Preparar la solución para producción (conectar las entradas de datos de producción, escribir pruebas unitarias (unit test), etc.).
2. Escribir código de monitoreo para verificar el rendimiento en tiempo real del sistema a intervalos regulares y activar alertas cuando se caiga o falle.
- Tener cuidado con la lenta degradación: los modelos tienden a "pudrirse" a medida que los datos evolucionan, el modelo va perdiendo validez en el tiempo.
- La medición del rendimiento puede requerir supervision humana (por ejemplo, a través de un servicio de crowdsourcing).
- Controlar la calidad de los datos de entrada (por ejemplo, Un sensor que funciona mal y que envía valores aleatorios, o la salida de datos de otro equipo se vuelve obsoleta). Esto es particularmente importante para los sistemas de aprendizaje en línea (online learning).
3. Vuelva a entrenar sus modelos de forma regular con datos nuevos (automatizar lo más posible).

# Referencias
- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems](https://www.amazon.com/-/es/gp/product/B07XGF2G87/)
- https://github.com/ageron/handson-ml2

[^1]: “Practical Bayesian Optimization of Machine Learning Algorithms,” J. Snoek, H. Larochelle, R. Adams (2012)