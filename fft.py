from sampling import Sampler
import matplotlib.pyplot as plt
import numpy as np


def high_point(rate):
    sampler = Sampler(sampling_rate=rate)
    f = sampler.fft()
    largest = max(f)
    for i in range(len(f)-1, 0, -1):
        if f[i] >= largest * 0.9:
            print('{},{}'.format(rate, i))
            return i
    return 0


if __name__ == '__main__':
    high_points = [high_point(i) for i in range(10, 100)]
    #plt.plot(np.arange(10, 100), high_points)
    # plt.show()
