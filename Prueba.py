import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Cargar señal EMG
dataset_path = r"C:\Users\juand\Downloads\dataset_emg.txt"  # Reemplaza con la ruta de tu archivo
emg_signal = np.loadtxt(dataset_path)

# Asegurar que sea un array unidimensional
emg_signal = np.array(emg_signal).flatten()

# Verificar forma de la señal
print(f"Forma de emg_signal: {emg_signal.shape}")

# Frecuencia de muestreo
fs = 1000  

# Definir ventana
window_size = min(len(emg_signal) // 2, 256)  
window_size = max(10, window_size)  
window = "hann"  # Se usa string en lugar de array

# Verificar tamaños
noverlap = window_size // 2
print(f"🔹 Longitud de la señal: {len(emg_signal)}")
print(f"🔹 Tamaño de ventana: {window_size}")
print(f"🔹 Noverlap: {noverlap}")

# Calcular Welch
freqs, psd = welch(emg_signal, fs, window=window, noverlap=noverlap, nperseg=window_size)

# Calcular frecuencia mediana
cumulative_power = np.cumsum(psd)
median_freq = freqs[np.where(cumulative_power >= cumulative_power[-1] / 2)[0][0]]

# Graficar espectro
plt.figure(figsize=(8,5))
plt.semilogy(freqs, psd, label="Densidad espectral de potencia")
plt.axvline(median_freq, color='r', linestyle="--", label=f"FM = {median_freq:.2f} Hz")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad de potencia (dB/Hz)")
plt.title("Espectro de Potencia de la señal EMG")
plt.legend()
plt.grid()
plt.show()
