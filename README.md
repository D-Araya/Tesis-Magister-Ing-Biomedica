# Evaluación del Leap Motion Controller en la adquisición de movimientos basados en el Test de Espiral de Arquímedes


### 📄 Información General

* **Autor:** Daniel Enrique Araya Rocha
* **Tesis:** Para la obtención del grado de Magíster en Ciencias de la Ingeniería, Mención Ingeniería Biomédica
* **Institución:** Universidad de Valparaíso, Chile
* **Profesor Guía:** Dra. Carolina Saavedra Ruiz
* **Profesor Co-Guía:** Dr. Rodrigo Salas Fuentes
* **Fecha:** Diciembre 2018

### Resumen

> El Leap Motion Controller (LMC) es un dispositivo de captura de movimiento de la mano, no profesional, que reúne una fuerte capacidad para evaluar varias tareas motoras en un ambiente clínico. En este estudio se verificó su exactitud, evaluando su desempeño en la adquisición de movimientos basados en la simulación del test de espiral de Arquímedes. Se presenta un método innovador para la obtención de información de las habilidades motoras finas durante la realización del test de dibujo en espiral mediante una plataforma de evaluación instrumentada usando el LMC. Primero se realizaron varias condiciones experimentales que permitieron desafiar el desempeño del LMC durante la simulación del test de espiral, luego se realizó un estudio de caso que permitió establecer la validez de su uso para evaluar el test de dibujo en espiral en humanos. Los resultados obtenidos en este estudio respecto a la condición de simulación del test de espiral indican que el valor de error máximo fue de 2.5 mm en el análisis 3D. Además, el error medio global para el análisis 3D fue de 0.7 mm, obteniendo una alta exactitud. Para el estudio de caso, las transformaciones afines utilizando los ángulos de orientación no contribuyen a la reducción del error. Debido a esta investigación es posible extrapolar el test de dibujo de espiral, desde un espacio bidimensional a un espacio tridimensional, sin restricciones, ni contacto con objetos y en un ambiente clínico controlado. Permitiendo a futuro, obtener variables de la cinemática de la mano durante una tarea de dibujo en espiral en un espacio tridimensional.

### 🗝️ Palabras Clave

* Leap Motion Controller
* Espiral de Arquímedes
* Exactitud
* Evaluación tridimensional

---

### 🎯 Hipótesis y Objetivos

#### Hipótesis
El dispositivo LMC permite adquirir movimientos controlados mediante simulación del test de espiral de Arquímedes con un **error medio inferior a 2.5 mm**, por lo que puede ser usado como un sistema válido para la cuantificación objetiva del movimiento natural de la mano en el espacio tridimensional.

#### Objetivo General
Evaluar el desempeño del Leap Motion Controller en la adquisición de movimientos basados en la simulación del test de espiral de Arquímedes, verificando su exactitud.

---

### 🛠️ Metodología

La evaluación se realizó comparando los datos del LMC contra una "verdad terrestre" (ground truth) generada por una máquina de alta precisión.

1.  **"Verdad Terrestre" (Ground Truth):**
    * Se utilizó una **mini-fresadora vertical CNC (Sherline CNC Mill 5400)** con una capacidad de exactitud de 0.01 mm.
    * Se programaron 3 tipos de espirales "ideales" (T1, T2, T3) que la CNC trazó usando un puntero de madera de 5 mm de diámetro.

2.  **Captura de Movimiento:**
    * El **Leap Motion Controller (LMC)** se posicionó para registrar la trayectoria del puntero de la CNC mientras ejecutaba las espirales.

3.  **Entorno Virtual y Software:**
    * Se desarrolló un ambiente virtual 3D usando **Python 2.7** y la librería **PyQtGraph** para visualizar y registrar los datos del LMC.
    * Los datos se registraron con una frecuencia de muestreo promedio de 44 cuadros por segundo.

4.  **Métrica de Evaluación:**
    * La exactitud se midió como la **Raíz del Error Cuadrático Medio (RMSE)**, comparando los puntos adquiridos por el LMC contra los 1000 puntos de la espiral ideal generada por la CNC.

#### Experimentos Realizados
* **Condición Experimental 1:** Adquisición de los 3 tipos de espiral con el LMC a 0 grados de rotación.
* **Condición Experimental 2:** Adquisición de la espiral tipo 2, rotando estáticamente el LMC a -10, 15, 20 y -30 grados.
* **Condición Experimental 3:** Adquisición de la espiral tipo 2 con -30 grados de rotación y 20 mm de traslación.
* **Estudio de Caso:** Un sujeto humano saludable (sin enfermedades diagnosticadas) realizó el test de espiral en el aire, sin contacto.

---

### 📊 Resultados Clave

* **Hipótesis Confirmada:** La investigación aceptó la hipótesis.
* **Alta Exactitud en Simulación (Condición 1):**
    * El **error medio global (RMSE)** para el análisis 3D fue de **0.7 mm**.
    * El **error máximo ($dist_{max}$)** en el análisis 3D fue de **2.5 mm**.
* **Transformaciones Afines (Simulación):** En las condiciones 2 y 3, el uso de transformaciones afines (rotación y traslación) fue efectivo para reducir el error y alinear la espiral capturada con la ideal.
* **Transformaciones Afines (Estudio de Caso):** En el estudio con el sujeto humano, un hallazgo clave fue que las transformaciones afines basadas en los ángulos de orientación del dedo (yaw, pitch, roll) **no contribuyeron** a reducir el error. Esto sugiere que el movimiento humano ya busca minimizar el error con la plantilla, independientemente de la orientación del dedo.

### 🏁 Conclusión

El LMC demostró ser un sistema válido y de alta exactitud (error medio de 0.7 mm) para la cuantificación objetiva del movimiento de la mano en el espacio tridimensional durante una tarea simulada del test de espiral de Arquímedes.

Esta investigación valida la extrapolación del test de dibujo en espiral de un entorno 2D (papel o tablet) a un **espacio 3D sin contacto ni restricciones**, abriendo la puerta a la obtención de nuevas variables cinemáticas de la mano en un ambiente clínico controlado.

---

### 📜 Citación

Si utilizas este trabajo, por favor cita la tesis:

> Araya Rocha, D. E. (2018). *Evaluación del Leap Motion Controller en la adquisición de movimientos basados en el Test de Espiral de Arquímedes* (Tesis de Magíster). Universidad de Valparaíso, Valparaíso, Chile.
