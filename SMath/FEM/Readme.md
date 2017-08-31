# Utilidades FEM
Implementación del método de elementos finitos en SMath.
Por el momento solo elementos 2D.
fem.sm es un snippet para [SMath](http://smath.info)

Funciones implementadas:
## k'(nodo1,nodo2)
calcula la matriz de rigidez de un elemento lineal a partir de las coordenadas de sus nodos

## k(nodo1,nodo2)
calcula la matriz de rigidez de un elemento 2D a partir de las coordenadas de sus nodos

## K(nodos,conectividad, A, E, free)
ensambla la matriz de rigidez global de un sistema definido por los nodos, la conectividad, el Area, el módulo de Elasticidad de sus elementos y los nodos libres (free) o no restringidos.
nodos es una matriz de n filas y 2 columnas. Cada fila representa las coordenadas de un nodo, la columna 1 representa las coordenadas x, la columna 2, las y.

## δ(K,Ffree,conectividad)
Devuelve el vector total deformaciones nodales

