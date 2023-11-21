import numpy as np
import matplotlib.pyplot as plt

signal1 = np.array([1, 2, 1])  # signal 1
signal2 = np.array([1, -1, 3])  # signal 2

# Perform convolution
result = np.convolve(signal1, signal2, mode='full')

plt.subplot(3, 1, 1)
plt.stem(signal1, use_line_collection=True)
plt.title('Signal 1')

plt.subplot(3, 1, 2)
plt.stem(signal2, use_line_collection=True)
plt.title('Signal 2')

plt.subplot(3, 1, 3)
plt.stem(result, use_line_collection=True)
plt.title('Convolution Result')

plt.tight_layout()
plt.show()
