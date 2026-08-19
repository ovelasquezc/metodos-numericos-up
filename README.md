# Métodos Numéricos - 2026-2

<p align="center">
  <img src="assets/universidad-del-pacifico.png"
       alt="Universidad del Pacífico"
       width="540">
</p>

Repositorio docente del curso **Métodos Numéricos (130146-A)** de la
**Facultad de Economía de la Universidad del Pacífico**.

**Docente:** Oswaldo José Velásquez Castañón  
**Periodo académico:** 2026-2

## Material disponible

### Notas del curso

- [Métodos Numéricos - notas 2026-2](notas/Metodos_Numericos_2026-2.pdf)

Las notas reúnen el material central del curso. Esta edición fue recompilada el
19 de agosto de 2026 y se encuentra en revisión y modernización progresiva. El
capítulo 2 contiene la formulación revisada de convergencia para sucesiones
escalares y vectoriales, convergencia lineal, superlineal y cuadrática, y
criterios de parada.

### Presentaciones

- [Unidad 1: Fundamentos del análisis numérico](presentaciones/Unidad_1_Fundamentos_Analisis_Numerico.pdf)
- [Unidad 2: Métodos iterativos y velocidad de convergencia](presentaciones/Unidad_2_Metodos_Iterativos_Convergencia.pdf)

La presentación de la Unidad 1 desarrolla representación en punto flotante,
errores, análisis diferencial, condicionamiento, estabilidad y costo
computacional.

La presentación de la Unidad 2 desarrolla el capítulo introductorio sobre
métodos iterativos mediante las tres nociones específicas de velocidad de
convergencia utilizadas en el curso, sin recurrir a una definición general de
orden.

### Laboratorios

- [Laboratorio 1: punto flotante, error y estabilidad](laboratorios/Lab_Unidad_1_Punto_Flotante.ipynb)

El cuaderno está ejecutado y utiliza Python y NumPy. Incluye experimentos sobre
representación, truncamiento, redondeo, cancelación, propagación de errores y
comparación de algoritmos.

## Ejecución del laboratorio

Con Python 3.11 o posterior:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Luego abra `laboratorios/Lab_Unidad_1_Punto_Flotante.ipynb` y ejecute las
celdas en orden.

## Estado del material

Este repositorio contiene las versiones vigentes para el periodo 2026-2. Las
notas históricas, evaluaciones y archivos internos de preparación no forman
parte de esta publicación.
