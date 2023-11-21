import numpy as np
x = {1, 2, 3, 4}
# Define the signal
x = [1, 2, 3, 4]
# Compute the Discrete Fourier Transform (DFT)
X = np.fft.fft(x)
# Generate frequency axis for plotting
N = len(x)
frequencies = np.arange(0, N)*(1/N)
# Plot the magnitude and phase of the DFT
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 1)
axs[0].stem(frequencies, np.abs(X))
axs[0].set_title('Magnitude of DFT')
axs[0].set_xlabel('Frequency Index (k)')
axs[0].set_ylabel('|X(k)|')
axs[1].stem(frequencies, np.angle(X))
axs[1].set_title('Phase of DFT')
axs[1].set_xlabel('Frequency Index (k)')
axs[1].set_ylabel('Phase (radians)')
plt.show()


