import matplotlib.pyplot as plt
import numpy as np



def blackbody(T, nm):
    h = 6.626e-34
    c = 3.0e8
    k = 1.38e-23
    v = c / (nm * 1e-9)
    top = 8 * 3.1415 * h * v**3
    bottom = c**3 * (np.exp(h * v / (k * T)) - 1)
    return top / bottom

def blackbodyfreq(T, thz):
    h = 6.626e-34
    c = 3.0e8
    k = 1.38e-23
    v = thz * 1e12
    top = 8 * 3.1415 * h * v**3
    bottom = c**3 * (np.exp(h * v / (k * T)) - 1)
    return top / bottom

wavelengths = np.linspace(100, 10000, 1000)

frequencies = np.linspace(50, 1500, 1000)

plt.subplot(3, 1, 1)

plt.xlabel('Frequency (THz)')
plt.ylabel('Intensity')

plt.plot(frequencies, blackbodyfreq(2700, frequencies), label='2700 K')
plt.plot(frequencies, blackbodyfreq(4000, frequencies), label='4000 K')
plt.plot(frequencies, blackbodyfreq(5000, frequencies), label='5000 K')

plt.legend()

plt.subplot(3, 1, 2)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')

plt.plot(wavelengths, blackbody(2700, wavelengths), label='2700 K')
plt.plot(wavelengths, blackbody(4000, wavelengths), label='4000 K')
plt.plot(wavelengths, blackbody(5000, wavelengths), label='5000 K')

plt.legend()

plt.subplot(3, 1, 3)

wavelengths = np.linspace(400, 700, 1000)

plt.xlabel('Wavelength (nm)')

plt.plot(wavelengths, blackbody(2700, wavelengths), label='Warm White')
plt.plot(wavelengths, blackbody(4000, wavelengths), label='Neutral White')
plt.plot(wavelengths, blackbody(5000, wavelengths), label='Cool White')

plt.legend()

plt.show()