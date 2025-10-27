# Examen Corto No. 1 — Teoría de la computación

Universidad del Valle de Guatemala  
Facultad de Ingeniería  
Ingeniería en Ciencia de la Computación y Tecnologías de la Información  

---

## 📘 Descripción

Este corto implementa la **construcción de Autómatas Finitos No Deterministas (AFN)** a partir de **expresiones regulares** mediante el **algoritmo de Thompson**.
Cada inciso del examen genera y visualiza distintos autómatas, además de incluir el cálculo de **ε-closures** y **transiciones δ**.

El proyecto permite:

* Construir AFN para distintas expresiones regulares.
* Visualizar gráficamente los autómatas.
* Calcular y mostrar las tablas de transiciones.
* Servir como base para la conversión a AFD mediante el método de subconjuntos.

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Anaru03/Corto1_TDLC
cd Corto1_TDLC
```

### 2. Crear y activar entorno virtual

Para evitar conflictos con otras librerías, se recomienda usar un entorno virtual.

#### En Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install networkx matplotlib
```

---

## ▶️ Uso

Cada archivo ejecuta una parte diferente del examen.
Corre el script correspondiente con:

```bash
python nombre_del_archivo.py
```

| Archivo            | Descripción                                                                                 | Instrucciones         |                |      |                      |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------------- | -------------- | ---- | -------------------- |
| **`thompson.py`**  | Construye el AFN básico de `letter` (`A                                                     | B                     | a              | b`). | `python thompson.py` |
| **`digit.py`**     | Construye los AFN de `letter`, `digit`, y `digits` (`digit+`).                              | `python digit.py`     |                |      |                      |
| **`id.py`**        | Construye los AFN de `letter`, `digit`, y `id = letter(letter                               | digit)*`.             | `python id.py` |      |                      |
| **`number.py`**    | Construye los AFN de `letter`, `digit`, `id`, y `number = digits(.digits)?(E[+-]?digits)?`. | `python number.py`    |                |      |                      |
| **`tabla_AFN.py`** | Calcula las **ε-closures** y **transiciones δ** del AFN de `id` (inciso 5 del examen).      | `python tabla_AFN.py` |                |      |                      |

---

## 📊 Relación con el examen

| Inciso | Descripción                                           | Archivo relacionado |
| ------ | ----------------------------------------------------- | ------------------- |
| 1      | AFN para `letter`                                     | `thompson.py`       |
| 2      | AFN para `digit` y `digits`                           | `digit.py`          |
| 3      | AFN para `id`                                         | `id.py`             |
| 4      | AFN para `number`                                     | `number.py`         |
| 5      | Tabla de transiciones (ε-closure y δ) del AFN de `id` | `tabla_AFN.py`      |
| 6      | Construcción de AFD (subconjuntos) — opcional         | *No implementado*   |
| 7      | AFD resultante — opcional                             | *No implementado*   |

---

## 🧩 Visualización opcional

Al ejecutar los archivos que dibujan autómatas (`thompson.py`, `digit.py`, `id.py`, `number.py`), se abre una ventana con la gráfica generada mediante **Matplotlib** y **NetworkX**.

También puedes generar archivos `.dot` y visualizarlos con [Graphviz](https://graphviz.org/download/):

```bash
dot -Tpng afn.dot -o afn.png
```

---

## 💡 Notas

* Todos los AFN se construyen con **Thompson**.
* Las funciones base (`new_state`, `add_transition`, `union`, `concat`, `star`, `plus`, etc.) están incluidas en cada archivo.
* `tabla_AFN.py` es el archivo **más completo**, ya que combina todas las construcciones y genera las tablas de análisis.
* El entorno virtual (`venv`) garantiza un ambiente limpio y reproducible.

---

## 🚀 Finalizar sesión

Cuando termines, desactiva el entorno virtual:

```bash
deactivate
```

---

**Autor:** Ruth de León  
**Curso:** CC3067 — Teoría de Lenguajes de Compiladores  
**Año:** 2025
