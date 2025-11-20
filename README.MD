# Clasificación de Vinos con Árboles de Decisión  

Esta practica implementa un **modelo de Árbol de Decisión** usando el dataset *Wine* de `sklearn`.  

---

## Objetivo de la practica
- Entrenar un árbol de decisión como clasificador.  
- Entender cómo genera reglas lógicas simbólicas.  
- Explorar el dataset de vinos y analizar sus características.  
- Comparar cómo cambia la precisión y la complejidad del árbol al modificar `max_depth`.

---

# Opiniones sobre los resultados

A continuacion una lista del comportamientos según la profundidad del árbol:

### max_depth bajo (1 o 2)
- Reglas muy simples y claras al igual que visualizar el arbol. 

### max_depth intermedio (3)
- Aumenta la precisión.  
- Las reglas siguen siendo legibles.

### max_depth=None (sin límite)
- El árbol crece de forma completa.  
- Las reglas se vuelven extensas y difíciles de interpretar.  

En general, no es necesario establecer una profundidad indefinida para poder interpretar o considerarlo correcto.

---

# ¿El dataset cumple los requisitos para un Árbol de Decisión?

### **Si cumple.**

### Razones:
1. **Todas las características son numéricas**, lo cual facilita la partición de nodos.  
2. **Las clases están claramente definidas** (0, 1 y 2).  
3. **Los datos no tienen valores faltantes**, sin valores faltantes.  
4. **Tamaño adecuado** para evitar sobreentrenamiento exagerado.  

---

# Características utilizadas

El dataset contiene las siguientes variables químicas:

1. color_intensity
2. proline
3. alcohol
4. ash

---

# Clases clasificadas por el modelo

- **Clase 0** – Vino tipo 1  
- **Clase 1** – Vino tipo 2  
- **Clase 2** – Vino tipo 3  

---

# ¿Qué pasaría si el dataset NO cumpliera los requisitos?

Si tuviera:

- Variables categóricas sin codificar  
- Datos incompletos  
- Pocos registros  
- Clases desbalanceadas  
- Mucho ruido (informacion que no es util)  

Entonces un árbol de decisión podría tener problemas.

### Cambios necesarios:
- Limpieza y preparación de datos  
- Codificación de categorías  
- Balanceo de clases  
- Eliminación de ruido

---

# ¿Se podría usar regresión en ese caso?

Siempre y cuando el objetivo sea **predecir un valor numérico** en lugar de una clase.  

---

## Módulos


### `main.py`
Ejecuta todos los modulos: Carga datos, entrena el modelo, muestra reglas y precisión.

### `colors.py`
Define códigos ANSI para imprimir texto con colores en la terminal.

### `progress.py`
Genera barras y animaciones de progreso.

### `dataset.py`
Carga y prepara el dataset del vino (X, y, train/test split).

### `model.py`
Crea, entrena y evalúa el árbol de decisión; exporta reglas del modelo.

