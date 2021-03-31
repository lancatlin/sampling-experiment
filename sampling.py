import numpy as np
import matplotlib.pyplot as plt

time_of_view = 0.5
analog_time = np.linspace(0, time_of_view, 10**6)

sampling_rate = 40
sampling_period = 1. / sampling_rate
sample_number = time_of_view / sampling_period
sampling_time = np.linspace(0, time_of_view, int(sample_number))

carrier_frequency = 20
amplitude = 1
phase = 0

quantizing_bits = 16
quantizing_levels = 2 ** quantizing_bits
quantizing_step = 2 * amplitude / quantizing_levels

def analog_signal(time_point):
    return amplitude * np.cos(2 * np.pi * carrier_frequency * time_point + phase)

sampling_signal = analog_signal(sampling_time)
quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step

plt.plot(analog_time, analog_signal(analog_time))
plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

plt.stem(sampling_time, sampling_signal - quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
plt.xlabel("Time")
plt.ylabel("Quantization error")
plt.show()