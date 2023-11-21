import numpy as np
import matplotlib.pyplot as plt

def generate_signal(freq, duration, sample_rate):
    t = np.arange(0, duration, 1/sample_rate)
    return np.sin(2 * np.pi * freq * t)

def plot_spectrum(signal, sample_rate):
    n = len(signal)
    k = np.arange(n)
    T = n / sample_rate
    frq = k / T  # two sides frequency range
    frq = frq[:n // 2]  # one side frequency range
    Y = np.fft.fft(signal) / n  # fft computing and normalization
    Y = Y[:n // 2]
    plt.figure(figsize=(10, 6))
    plt.plot(frq, abs(Y))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum')
    plt.show()
    plt.savefig("fft.png")

def main():
    sample_rate = 1000  # Hz
    duration = 1  # seconds
    freq = 5  # Hz
    signal = generate_signal(freq, duration, sample_rate)
    plot_spectrum(signal, sample_rate)

if __name__ == "__main__":
    main()
