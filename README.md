# Lab-4-Fatiga
Este laboratorio tiene como objetivo analizar la fátiga del músculo aplicando un filtrado para las señales continuas que se obtendrán a través de un módulo de sensor EMG. El código esta implementado en Python y utiliza bibliotecas como `numpy`, `matplotlib`, `pandas`y `PyQT6`.

## Tabla de Contenido
1.[Introducción](#introducción)
2. [Marco Teórico](#Marco-Teórico)
3.[Requisitos](#requisitos)
4.[Resultados](#resultados).
5.[Test de Hipótesis](#Test-de-Hipótesis).
6.[Conclusión](#conclusión)

[Introducción]
La electromiografia es crucial en la evaluacion de la actividad muscular y el diagnostico de enfermedades neuromusculares, el analisis de esta señal nos permite identificar condiciones clinicas  que pueda tener el paciente, en este laboratorio realizamos la adquisicion de datos con el (DAQ), el cual minimiza el ruido, garantizando presicion y resolucion al representar la actividad del musculo

#Marco-Teórico
Electromiografia: Tecnica utilizada para registrar la actividad electrica de los musculos. Hay dos tipos principales de EMG: el invasivo y el no invasivo. El no invasivo que es el cual usamos para este laboratorio, se obtiene mediante electrodos colocados sobre la piel, por otro lado la electromiografia invasiva utiliza agujas insertadas en el musculo para capturar señales mas profundas y especificas. La señal es generada por los potenciales de acción de las fibras musculares en respuesta a estimulos nerviosos, nuestro objetivo en este laboratorio es la señal EMG la cual se enfocara en la deteccion de fatiga muscular, en la que procesaremos la señal para evaluar parametros estadisticos, los cambios que tiene reflejan la reduccion en la eficiencia de la activacion muscular conforme progresa la fatiga
