# Lab-4-Fatiga
Este laboratorio tiene como objetivo analizar la fátiga del músculo aplicando un filtrado para las señales continuas que se obtendrán a través de un módulo de sensor EMG. El código esta implementado en Python y utiliza bibliotecas como `numpy`, `matplotlib`, `pandas`y `PyQt6`.

## Tabla de Contenido
1.[Introducción](#introducción)
2. [Marco Teórico](#Marco-Teórico)
3.[Requisitos](#requisitos)
4.[Materiales](#materiales)
5.[Resultados](#resultados).
6.[Test de Hipótesis](#Test-de-Hipótesis).
7.[Conclusión](#conclusión)

## Introducción
La electromiografia es crucial en la evaluacion de la actividad muscular y el diagnostico de enfermedades neuromusculares, el analisis de esta señal nos permite identificar condiciones clinicas  que pueda tener el paciente, en este laboratorio realizamos la adquisicion de datos con el (DAQ), el cual minimiza el ruido, garantizando presicion y resolucion al representar la actividad del musculo

## Marco Teórico
### Electromiografía
Técnica utilizada para registrar la actividad eléctrica de los musculos. Hay dos tipos principales de EMG, el invasivo y el no invasivo:

- El **no invasivo** es el cual usamos para este laboratorio, se obtiene mediante electrodos colocados sobre la piel.
- El **invasivo** utiliza agujas insertadas en el musculo para capturar señales mas profundas y especificas. 

La señal es generada por los potenciales de acción de las fibras musculares en respuesta a estimulos nerviosos, nuestro objetivo en este laboratorio es la señal EMG la cual se enfocara en la detección de fatiga muscular, en la que procesaremos la señal para evaluar parámetros estadísticos, los cambios que tiene reflejan la reducción en la eficiencia de la activación muscular conforme progresa la fatiga.

### Módulo de sensor EMG
Es un dispositivo electrónico diseñado para registrar la actividad eléctrica de los músculos. Cuenta con:

- **Electrodos de superficie:** Capturan las señales eléctricas de los músculos.
- **Amplificador:** Aumenta la señal para tener una mejor visualización y poder procesarla.
- **Filtro:** Incluye filtros que atenuan los ruidos no deseados, como el ruido del ambiente y tener la información lo más limpia posible.


### DAQ
La adquisición de datos (DAQ) es el proceso de medir fenómenos eléctricos o físicos como lo es el voltaje, la corriente, temperatura, entre otros. Los datos que arroje el fenómeno se convierten en formato digital para que se puedan analizar a través de una computadora. En este caso, se usa la DAQ para adquirir los datos que arroja el músculo, es decir la cantidad de contracciones que hace el mismo hasta llegar a la fatiga, con el fin de analizarlos en la computadora haciendo uso de un código en python.

## Requisitos
- **Phyton** Instalado en tu sistema.
- **Spyder** (Puedes instalarlo como parte de [Anaconda](https://www.anaconda.com/)).
- **Bibliotecas de Python:** `numpy`,`matplotlib`,`PyQt6`,`pandas`.

## Materiales
- **Módulo de sensor EMG** Para filtrado y amplificación de la señal.
- **Electrodos** Captura de la señal.
- **DAQ** Adqusición de datos.

## Test de Hipótesis
Es un procedimiento para juzgar si una propiedad que se supone en una población estadística es compatible con lo observado en una muestra de dicha población. En este caso vamos a analizar si realmente la primera muestra y la ultima muestra de la contraccion muscular, son diferentes y que exista fatiga en el músculo. Para eso seguimos los siguientes pasos:

1. Establecer la hipótesis:
- Ho: No hay diferencias (es conocida como hipótesis nula).
- Ha1: μ1-μ2 ≠ 0 (Ya sea un número mayor o menor que 0).
2. Escoger el estadistico de prueba (t):
  $$
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$
  


