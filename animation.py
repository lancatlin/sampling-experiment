from matplotlib.animation import FuncAnimation
from sampling import Sampler
import matplotlib.pyplot as plt

fig = plt.figure()


def fft(rate):
    sampler = Sampler(sampling_rate=rate)
    fig.clear()
    plt.stem(sampler.fft())
    plt.xlabel('sampling rate {}'.format(rate))


ani = FuncAnimation(plt.gcf(), fft, interval=200, frames=range(10, 100, 2))

ani.save('animation.mp4', fps=4, extra_args=['-vcodec', 'libx264'])

# plt.show()
