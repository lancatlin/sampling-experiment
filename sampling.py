import numpy as np
import matplotlib.pyplot as plt

time_of_view = 0.5


class Sampler:
    def __init__(self, frequency=10, phase=0, sampling_rate=20, quantizing_bits=4):
        self.frequency = frequency
        self.phase = 0
        self.analog_time = np.linspace(0, time_of_view, 10**6)
        sample_number = time_of_view * sampling_rate
        self.sampling_time = np.linspace(0, time_of_view, int(sample_number))
        quantizing_levels = 1 << quantizing_bits
        self.quantizing_step = 2 / quantizing_levels

    def signal(self, t):
        return np.cos(2 * np.pi * self.frequency * t + self.phase)

    def analog_signal(self):
        return self.signal(self.analog_time)

    def sampling_signal(self):
        return self.signal(self.sampling_time)

    def quantizing_signal(self):
        return np.round(self.sampling_signal() / self.quantizing_step) * self.quantizing_step


if __name__ == '__main__':
    sampler = Sampler()
    plt.plot(sampler.analog_time, sampler.analog_signal())
    #plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
    plt.plot(sampler.sampling_time, sampler.quantizing_signal())
    plt.title("Analog to digital signal conversion")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

"""
plt.stem(sampling_time, sampling_signal - quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-')
plt.xlabel("Time")
plt.ylabel("Quantization error")
plt.show()
"""
