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
20 de agosto de 2026 y se encuentra en revisión y modernización progresiva. El
capítulo 1 incorpora grafos computacionales como representación visual de la
composición de funciones elementales y de la propagación de errores de entrada
y redondeo. El capítulo 2 contiene la formulación revisada de convergencia para
sucesiones escalares y vectoriales, convergencia lineal, superlineal y
cuadrática, y criterios de parada.

### Presentaciones

- [Unidad 1: Fundamentos del análisis numérico](presentaciones/Unidad_1_Fundamentos_Analisis_Numerico.pdf)
- [Unidad 2: Métodos iterativos y velocidad de convergencia](presentaciones/Unidad_2_Metodos_Iterativos_Convergencia.pdf)
- [Unidad 3A: Sistemas lineales, sustitución, Gauss y Gauss--Jordan](presentaciones/Unidad_3A_Sistemas_Gauss.pdf)
- [Unidad 3B: Factorización LU, estructuras especiales y condicionamiento](presentaciones/Unidad_3B_LU_Estructuras_Condicionamiento.pdf)
- [Unidad 3C: Factorización QR mediante Householder y Givens](presentaciones/Unidad_3C_QR_Householder_Givens.pdf)
- [Unidad 3D: Métodos iterativos matriciales](presentaciones/Unidad_3D_Metodos_Iterativos_Lineales.pdf)
- [Unidad 4A: Ecuaciones no lineales escalares](presentaciones/Unidad_4A_Ecuaciones_No_Lineales_Escalares.pdf)
- [Unidad 4B: Sistemas no lineales, Newton y Broyden](presentaciones/Unidad_4B_Sistemas_No_Lineales_Newton_Broyden.pdf)
- [Unidad 5A: Aproximación lineal y ecuaciones normales](presentaciones/Unidad_5A_Aproximacion_Lineal.pdf)
- [Unidad 5B: Mínimos cuadrados mediante QR y aplicaciones](presentaciones/Unidad_5B_Minimos_Cuadrados_QR.pdf)

La presentación de la Unidad 1 desarrolla representación en punto flotante,
errores, análisis diferencial, condicionamiento, estabilidad y costo
computacional.

La presentación de la Unidad 2 desarrolla el capítulo introductorio sobre
métodos iterativos mediante las tres nociones específicas de velocidad de
convergencia utilizadas en el curso, sin recurrir a una definición general de
orden.

La presentación de la Unidad 3A introduce los sistemas lineales, los sistemas
diagonales y triangulares, las sustituciones hacia adelante y hacia atrás, la
eliminación de Gauss con pivoteo parcial, Gauss--Jordan, el costo computacional
y la verificación mediante el residuo. Su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_3A_Sistemas_Gauss.tex)
se publica junto con el estilo y el logo necesarios para recompilarla.

La Unidad 3B desarrolla la factorización LU con pivoteo, Cholesky, sistemas
tridiagonales, normas, condicionamiento, perturbaciones y diagnóstico mediante
el residuo. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_3B_LU_Estructuras_Condicionamiento.tex).

La Unidad 3C presenta la factorización QR completa y reducida, su aplicación a
sistemas y mínimos cuadrados, y los algoritmos de Householder y Givens con un
ejemplo común. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_3C_QR_Householder_Givens.tex).

La Unidad 3D cierra el capítulo con iteraciones estacionarias, radio espectral,
Jacobi, Gauss--Seidel, relajación, SOR y criterios de convergencia y detención.
Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_3D_Metodos_Iterativos_Lineales.tex).

La Unidad 4A desarrolla bisección, punto fijo, Newton y secante para ecuaciones
escalares. Compara garantías, velocidad, costo y criterios de parada, e incluye
ejemplos numéricos y una estrategia híbrida. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_4A_Ecuaciones_No_Lineales_Escalares.tex).

La Unidad 4B extiende punto fijo y Newton a sistemas, presenta amortiguamiento,
aproximación del jacobiano y el método de Broyden, y cierra con una aplicación
al equilibrio de Cournot. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_4B_Sistemas_No_Lineales_Newton_Broyden.tex).

La Unidad 5A desarrolla el capítulo de aproximación lineal de las notas con
el teorema completo de mínimos cuadrados y las demostraciones de existencia,
unicidad, estructura afín del conjunto de soluciones y solución de norma mínima.
Incluye la formulación en otras normas y un ejemplo resuelto de ajuste de una
recta. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_5A_Aproximacion_Lineal.tex).

La Unidad 5B conserva el tratamiento numérico por QR y los cuatro ejercicios
originales del capítulo. Incluye la relación correcta
`cond₂(AᵀA) = cond₂(A)²` para rango columna completo y corrige la identidad del
ejercicio de regularización. Añade ejemplos y complementos sobre escala, SVD,
ponderación y ajuste en logaritmos. Está disponible su
[fuente LaTeX editable](presentaciones/fuentes/Unidad_5B_Minimos_Cuadrados_QR.tex).

### Repaso del examen parcial

- [Lista de repaso en PDF](repaso/Lista_Repaso_Parciales_2026-2.pdf)
- [Fuente LaTeX editable](repaso/fuentes/Lista_Repaso_Parciales_2026-2.tex)

Siete preguntas de material anterior sobre **sistemas lineales, sistemas no
lineales y propagación de error**. La lista reúne cinco preguntas de parciales
y dos ejercicios complementarios de un examen final y una práctica calificada
de 2025-2, con su procedencia y notas sobre erratas. No incluye soluciones ni
evaluaciones del ciclo 2026-2.

### Laboratorios

- [Laboratorio 1: punto flotante, error y estabilidad](laboratorios/Lab_Unidad_1_Punto_Flotante.ipynb)
- [Laboratorio del capítulo 3: sistemas lineales](laboratorios/Lab_Capitulo_3_Sistemas_Lineales.ipynb)
- [Laboratorio complementario: matrices dispersas y economía peruana](laboratorios/Lab_Matrices_Dispersas_Economia_Peruana.ipynb)

Los cuadernos están ejecutados y utilizan Python y las bibliotecas indicadas en
`requirements.txt`. El laboratorio 1 incluye experimentos sobre
representación, truncamiento, redondeo, cancelación, propagación de errores y
comparación de algoritmos.

El laboratorio del capítulo 3 desarrolla métodos directos e iterativos para
sistemas lineales, factorizaciones y aplicaciones. Su sección geométrica
interpreta las transformaciones ortogonales de QR como reflexiones de
Householder y rotaciones de Givens, y verifica la conservación de normas,
ángulos y productos internos.

El laboratorio complementario introduce los formatos COO, CSR y CSC, patrones
de dispersión, almacenamiento, solución directa e iterativa y redes. La
aplicación utiliza la matriz insumo-producto peruana de 2007, nivel 101
productos, publicada por el
[Instituto Nacional de Estadística e Informática (INEI)](https://www1.inei.gob.pe/estadisticas/indice-tematico/matriz-insumo-producto-13673/).
El archivo original se distribuye en
[`laboratorios/datos`](laboratorios/datos/inei_mip_2007_precios_basicos_total.xlsx)
para permitir la ejecución reproducible del cuaderno.

## Ejecución del laboratorio

Con Python 3.11 o posterior:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Luego abra el cuaderno elegido dentro de `laboratorios/` y ejecute las celdas
en orden. Los cuadernos publicados conservan también una ejecución completa de
referencia.

## Estado del material

Este repositorio contiene las versiones vigentes para el periodo 2026-2 y una
selección de preguntas de evaluaciones anteriores para el repaso del parcial.
Las evaluaciones del ciclo actual y los archivos internos de preparación no
forman parte de esta publicación.
