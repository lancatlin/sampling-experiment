from matplotlib.animation import FuncAnimation
from sampling import Sampler
import matplotlib.pyplot as plt

fig = plt.figure()


def fft(rate):
    sampler = Sampler(sampling_rate=rate, quantizing_bits=16)
    fig.clear()
    plt.stem(sampler.fft())
    plt.xlabel('sampling rate {}'.format(rate))


ani = FuncAnimation(plt.gcf(), fft, interval=100, frames=range(10, 100, 2))

plt.show()
