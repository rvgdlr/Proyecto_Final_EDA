# 📊 Proyecto Final EDA – Análisis Exploratorio y Dashboard

## 📌 Descripción del Proyecto

Este proyecto consiste en la realización de un **Análisis Exploratorio de Datos (EDA)** sobre un conjunto de datos financieros, con el objetivo de:

- Comprender la estructura del dataset
- Detectar problemas de calidad de datos
- Analizar variables categóricas y numéricas
- Gestionar valores nulos
- Optimizar tipos de datos
- Diseñar un dashboard orientado a negocio

El análisis se ha desarrollado utilizando **Python (Pandas, Seaborn, Matplotlib)** en entorno **Jupyter Notebook (VS Code)**.

---

## 🎯 Objetivos

- Limpieza y transformación de datos
- Análisis estadístico descriptivo
- Segmentación de variables
- Identificación de patrones
- Evaluación de calidad de datos
- Construcción de visualizaciones interpretables
- Generación de insights accionables

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Jupyter Notebook (VS Code)
- Git & GitHub

---
## EStructura de carpetas

Proyecto_Final_EDA/
│
├── Notebook/
│ ├── 01_Analisis_preliminar.ipynb
│ ├── 02_Limpieza.ipynb
│
├── src/
├── data/
└── README.md


---

## 🔎 Proceso de Análisis

### 1️⃣ Carga y exploración inicial
- Revisión de estructura (`df.info()`)
- Identificación de tipos de datos
- Análisis de dimensiones
- Detección de valores nulos

---

### 2️⃣ Limpieza y transformación

- Eliminación de columnas irrelevantes
- Conversión de IDs numéricos a tipo `category`
- Normalización de nombres de columnas
- Limpieza de variables de texto (lowercase y strip)
- Gestión estratégica de valores nulos

---

### 3️⃣ Gestión de Nulos

- Eliminación de registros con identificadores clave ausentes
- Creación de categoría explícita para valores faltantes en variables descriptivas
- Evaluación del impacto porcentual de los nulos

---

### 4️⃣ Análisis Descriptivo

#### Variables categóricas
- Distribución de frecuencias
- Detección de alta cardinalidad
- Identificación de categorías dominantes

#### Variables numéricas
- Media, mediana y desviación estándar
- Detección de asimetría
- Identificación de outliers

---

### 5️⃣ Visualización

- Countplots para variables categóricas
- Barplots para análisis de resultado por línea
- Ajuste dinámico según cardinalidad
- Optimización de tamaños y rotaciones

---

## 📊 Dashboard

El dashboard desarrollado permite:

- Visualizar distribución de resultados
- Analizar comportamiento por línea de venta
- Detectar concentración de ingresos
- Evaluar impacto por segmento

Se prioriza claridad visual y enfoque orientado a negocio.

---

## 📈 Principales Insights

- Existen variables identificadoras que debían tratarse como categóricas.
- Se detectaron valores nulos gestionables sin impacto crítico.
- Algunas categorías presentan alta concentración de resultados.
- Se observaron patrones que permiten segmentación estratégica.

---

## 🚀 Conclusiones

El análisis permitió transformar un dataset en bruto en una estructura optimizada y analíticamente consistente.

La correcta gestión de tipos de datos y nulos fue clave para evitar distorsiones estadísticas y garantizar interpretaciones fiables.

---

## 👤 Autor

Proyecto desarrollado como parte del análisis exploratorio final, enfocado en limpieza, comprensión y visualización de datos.

## 📂 Estructura del repositorio

