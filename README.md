# Lab-4-Fatiga
Este laboratorio tiene como objetivo analizar la fátiga del músculo aplicando un filtrado para las señales continuas que se obtendrán a través de un módulo de sensor EMG. El código esta implementado en Python y utiliza bibliotecas como `numpy`, `matplotlib`, `pandas`y `PyQt6`.

## Tabla de Contenido
1.[Introducción](#introducción)
2. [Marco Teórico](#Marco-Teórico)
3.[Requisitos](#requisitos)
4.[Materiales](#materiales)
5. [Test de Hipótesis](#Test-de-Hipótesis)
6.[Resultados](#resultados).
7.[Conclusión](#conclusión)

## Introducción
La electromiografia es crucial en la evaluacion de la actividad muscular y el diagnostico de enfermedades neuromusculares, el analisis de esta señal nos permite identificar condiciones clinicas  que pueda tener el paciente, en este laboratorio realizamos la adquisicion de datos con el (DAQ), el cual minimiza el ruido, garantizando presicion y resolucion al representar la actividad del musculo

 **Objetivo:**  
Desarrollar un sistema para adquirir, procesar y analizar señales EMG, proporcionando una guía clara y detallada que permita comprender **cómo se procesan estos datos y cómo detectar fatiga muscular**.  


## Marco Teórico
### Electromiografía
Técnica utilizada para registrar la actividad eléctrica de los musculos. Hay dos tipos principales de EMG, el invasivo y el no invasivo:

- El **no invasivo** es el cual usamos para este laboratorio, se obtiene mediante electrodos colocados sobre la piel.
- El **invasivo** utiliza agujas insertadas en el musculo para capturar señales mas profundas y especificas. 

La señal es generada por los potenciales de acción de las fibras musculares en respuesta a estimulos nerviosos, nuestro objetivo en este laboratorio es la señal EMG la cual se enfocara en la detección de fatiga muscular, en la que procesaremos la señal para evaluar parámetros estadísticos, los cambios que tiene reflejan la reducción en la eficiencia de la activación muscular conforme progresa la fatiga.

### ¿Qué es la fatiga muscular?  
La **fatiga muscular** ocurre cuando un músculo pierde su capacidad de generar fuerza tras un esfuerzo prolongado. Se manifiesta en la señal EMG con **una disminución en la frecuencia mediana** y **un aumento en la amplitud**. Analizar estos cambios nos ayuda a comprender el comportamiento del músculo durante la contracción sostenida. 

Este fenómeno es estudiado porque:

1. En rehabilitación : Ayuda a personalizar terapias en pacientes con lesiones neuromusculares.

2. En biomecánica : Optimiza prótesis y exoesqueletos para mejorar la movilidad.

3. En el deporte : Permite evitar sobrecargas musculares y mejorar el rendimiento de los atletas.

4 .En ergonomía : Ayuda a diseñar entornos de trabajo que minimicen la fatiga laboral.

##  ¿Cómo se mide la fatiga con señales EMG?

Durante el experimento, aplicamos **ventana Hamming** y **FFT** para analizar cómo cambia la frecuencia de la señal EMG con el tiempo. Hay dos indicadores principales:

---

###  1. Disminución de la Frecuencia Mediana  

La **frecuencia mediana (MF, Median Frequency)** es el valor en el cual la señal se divide en dos partes de igual energía.

 **¿Por qué es importante?**  
Cuando un músculo se fatiga:  
Las fibras musculares pierden conducción eléctrica.  
Se activan unidades motoras más grandes pero más lentas.  
**La frecuencia mediana se reduce** con el tiempo.  

**¿Cómo lo observamos?**  
 Si la **MF baja progresivamente**, indica que el músculo se está fatigando.  

### 2. Aumento de la Amplitud de la Señal EMG  

**¿Qué sucede en la fatiga muscular?**  
En **etapas iniciales de fatiga**, el músculo recluta más unidades motoras, **aumentando la amplitud** de la señal EMG.  
Con **fatiga extrema**, el sistema nervioso no logra activar nuevas unidades motoras, **reduciendo la amplitud**.  

**¿Cómo lo observamos?**  
 Un **aumento inicial** en la potencia de la señal, seguido de una **disminución brusca**, indica **fatiga avanzada**.  

 Para obtener todos estos datos y poder observar correctamente la señal necesitamos hacer uso de lo siguiente: 

### Módulo de sensor EMG
Es un dispositivo electrónico diseñado para registrar la actividad eléctrica de los músculos. Cuenta con:

- **Electrodos de superficie:** Capturan las señales eléctricas de los músculos.
- **Amplificador:** Aumenta la señal para tener una mejor visualización y poder procesarla.
- **Filtro:** Incluye filtros que atenuan los ruidos no deseados, como el ruido del ambiente y tener la información lo más limpia posible.

### DAQ
La adquisición de datos (DAQ) es el proceso de medir fenómenos eléctricos o físicos como lo es el voltaje, la corriente, temperatura, entre otros. Los datos que arroje el fenómeno se convierten en formato digital para que se puedan analizar a través de una computadora. En este caso, se usa la DAQ para adquirir los datos que arroja el músculo, es decir la cantidad de contracciones que hace el mismo hasta llegar a la fatiga, con el fin de analizarlos en la computadora haciendo uso de un código en python.

Esta es alguna de la teoria basica que se debe tener en cuenta antes de empezar con la progrmación de la adqusición de señal.

## Requisitos
- **Phyton** Instalado en tu sistema.
- **Spyder** (Puedes instalarlo como parte de [Anaconda](https://www.anaconda.com/)).
- **Bibliotecas de Python:** `numpy`,`matplotlib`,`PyQt6`,`pandas`.

## Materiales
- **Módulo de sensor EMG** Para filtrado y amplificación de la señal.
- **Electrodos** Captura de la señal.
- **DAQ** Adqusición de datos.

## Interpretación de las Gráficas  

Las siguientes gráficas permiten analizar la evolución de la señal EMG y detectar la fatiga muscular.  

### Espectrograma (Tiempo-Frecuencia)  
 **¿Qué muestra?**  
- Representa cómo cambian las frecuencias en el tiempo.  
- **Indicador de fatiga** → Si las **frecuencias altas desaparecen**, indica **fatiga progresiva**.  

###  Distribución de Amplitudes  
**¿Qué muestra?**  
- Representa la variabilidad de la señal en diferentes momentos.  
- **Indicador de fatiga** → Si la **amplitud disminuye**, el músculo **pierde actividad eléctrica**.  
## Test de Hipótesis en el Análisis de Fatiga Muscular  

### ¿Qué es un test de hipótesis y para qué se usa?  
Un **test de hipótesis** permite evaluar si un cambio en la señal EMG es **estadísticamente significativo** o si ocurrió por azar.  

En este experimento, lo usamos para comprobar si la **frecuencia mediana** realmente disminuye con la fatiga y si los cambios en la amplitud de la señal son relevantes.  

### Aplicaciones en el análisis de EMG  
Cuando un músculo se fatiga, se espera que:  
La **frecuencia mediana** de la señal EMG disminuya.  
La **amplitud** de la señal cambie debido al reclutamiento de nuevas unidades motoras.  

Para confirmar esto, aplicamos **tests de hipótesis**.  

### Tipos de tests de hipótesis utilizados  

####  **Test de una cola**  
**Objetivo**: Verificar si la **frecuencia mediana disminuye significativamente** con el tiempo.  
Hipótesis nula (\(H_0\)): No hay cambio en la frecuencia mediana.  
Hipótesis alternativa (\(H_1\)): La frecuencia mediana **disminuye** con la fatiga.  
**Interpretación**:  
- Si el valor \( p \) del test es menor que un umbral (\(\alpha = 0.05\)), la disminución es **estadísticamente significativa**.  


#### **Test de dos colas**  
**Objetivo**: Evaluar **cambios generales en la distribución** de la señal EMG.  
Hipótesis nula (\(H_0\)): No hay diferencia en la señal EMG entre el inicio y el final del experimento.  
Hipótesis alternativa (\(H_1\)): La distribución de la señal **cambia significativamente** con la fatiga.  
**Interpretación**:  
- Se usa cuando no se sabe si el cambio será un **aumento o disminución** en la señal.  

### Importancia del test de hipótesis en EMG  
Aplicar tests de hipótesis nos permite validar científicamente los cambios en la señal EMG y evitar interpretaciones erróneas. Esto es clave para aplicaciones como:  

**Rehabilitación** → Monitoreo de la fatiga muscular en terapias.  
**Deporte** → Optimización de entrenamientos para prevenir lesiones.  
**Neurociencia** → Estudio del control motor y enfermedades neuromusculares.  

### Procedimiento:

**1.** Establecer la hipótesis:
- Ho: No hay diferencias (es conocida como hipótesis nula).
- Ha1: μ₁-μ₂ ≠ 0 (Ya sea un número mayor o menor que 0).

**2.** Escoger el estadistico de prueba (t):
t = (μ₁ - μ₂) / sqrt((s₁² / n₁) + (s₂² / n₂))

**3.** Definir el valor crítico
Para esto se tiene en cuenta el valor de significancia ($\alpha$) que uno de los valores más comunes y que se usa en este laboratorio es de 0,05 (5%). También se determinan los grados de libertad que se calcula con la siguiente formula:

                                                               df = min(n1 - 1, n2 - 1)
Una vez que se tiene el nivel de significancia y los grados de libertad, se revisan estos valores en una tabla de valores criticos (dos colas o bilateral en este caso) para saber a cual pertenece. A continuación se observa un ejemplo de esta tabla de la cual se uso para saber el valor critico de este laboratorio:

![image](https://github.com/user-attachments/assets/175e8feb-3920-45a7-aa5c-2ff17e5295dd)
### *Figura 1: Tabla de Valores criticos de Student.*

## Resultados

![WhatsApp Image 2025-03-27 at 11 52 24 PM](https://github.com/user-attachments/assets/56925d31-2e65-43a2-b08d-04d9ff1bc925)
### *Figura 2: Grafica de la señal.*

### Test de Hipótesis:
- **Media primera contracción:** −1.63
- **Media última contracción:**-1.85  
- **Desviación estándar primera contracción:** 39.00
- **Desviación estándar última contracción:** 41.38
- **Tamaño de muestra:** n1=n2= 310
- **Grados de libertad:** 309
- **Estadistico de prueba (t):** 0.054
- **Valor crítico (para $\alpha$ = 0.05):** ±1.961

## Conclusión
Se aprende el uso del DAQ para pasar los datos de una señal EMG al computador para asi analizarlos, haciendo uso también de un filtro de ventana Hanning para las muestras. También se analiza la densidad espectral de la señal y la frecuencia mediana que es de 167.97 Hz, indicando una actividad muscular alta.

En el test de hipótesis se evidencia que las medias son muy cercanas, por lo tanto no se rechaza la hipótesis nula (Ho). Esto indica que no hay una diferencia significativa estadisticamente entre las dos partes de la señal, es decir, no hay suficiente evidencia que demuestre una fatiga entre la primera y ultima contracción del músculo.




