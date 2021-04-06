from sampling import Sampler
import matplotlib.pyplot as plt
import numpy as np


def high_point(rate):
    sampler = Sampler(sampling_rate=rate)
    f = sampler.fft()
    largest = max(f)
    result = []
    for i in range(len(f)):
        if f[i] >= largest * 0.9:
            print('{},{}'.format(rate, i))
            result.append(i)

    if len(result) < 2:
        return [-1, -1]
    return result


if __name__ == '__main__':
    high_points = [high_point(i) for i in range(10, 100)]
    plt.plot(np.arange(10, 100), [p[0]
             for p in high_points], label='First High Point')
    plt.plot(np.arange(10, 100), [p[1]
             for p in high_points], label='Second High Point')
    plt.legend()
    plt.title('Sampling Rate to FFT High Points Graph')
    plt.savefig('fft.png')
    plt.show()
