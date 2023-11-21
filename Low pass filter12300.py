#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Low-pass filter parameters
order = 4  # Filter order
cutoff_frequency = 0.1  # Cutoff frequency in normalized units (0.0 to 1.0)

# Design low-pass Butterworth filter
b, a = butter(order, cutoff_frequency, 'low')

# Generate a sample signal (you can replace this with your own signal)
t = np.arange(0, 1, 0.01)  # Time vector
input_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.cos(2 * np.pi * 20 * t)  # Example input signal

# Apply the low-pass filter to the input signal
output_signal = lfilter(b, a, input_signal)

# Plot the original and filtered signals
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, input_signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plt.plot(t, output_signal)
plt.title('Low-pass Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


# In[ ]:




