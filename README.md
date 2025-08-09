
# Examen Corto No. 1

## Descripción

Este corto implementa la construcción de un Autómata Finito No Determinista (AFN) a partir de expresiones regulares. Permite generar la representación del autómata y visualizarlo.

---


## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Anaru03/Corto1_TDLC
```

### 2. Crear y activar entorno virtual

Para evitar conflictos con otras librerías, es recomendable usar un entorno virtual:

- En Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

- En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\activate
```


---

## Uso

Ejecuta el programa principal pasando la expresión regular como argumento:

```bash
python nombre_del_archivo.py
```

Esto generará un archivo `.dot` con el autómata. Para visualizarlo, puedes usar Graphviz (https://graphviz.org/download/):

```bash
dot -Tpng afn.dot -o afn.png
```

---

## Notas

- Asegúrate de tener instalado Graphviz para la visualización.
- Puedes modificar el script para cambiar la expresión regular o agregar nuevas funcionalidades.

---

