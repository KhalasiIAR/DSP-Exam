from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def apply_lowpass_filter(data, cutoff_freq, sampling_freq, filter_order):
    b, a = butter_lowpass(cutoff_freq, sampling_freq, order=filter_order)
    filtered_data = lfilter(b, a, data)
    return filtered_data

# Generate sample data (sine wave)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second of data
data = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)  # 5 Hz and 50 Hz components

# Apply low-pass filter
cutoff_frequency = 15  # Cutoff frequency in Hz
filter_order = 4  # Filter order
filtered_signal = apply_lowpass_filter(data, cutoff_frequency, fs, filter_order)

# Plot the original and filtered signals and save as images
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, data, 'b-', label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig('original_signal.png')  # Save the plot as an image

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, 'r-', label='Filtered Signal')
plt.title('Filtered Signal (Low-pass at {} Hz)'.format(cutoff_frequency))
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig('filtered_signal.png')  # Save the plot as an image
