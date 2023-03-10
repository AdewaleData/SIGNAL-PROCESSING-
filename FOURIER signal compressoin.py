'''
In this example, we first generate a test signal that consists of two sine waves with frequencies of 10 Hz and 20 Hz.
We then plot the original signal to visualize it.

Next, we compute the Fourier coefficients of the signal using the np.fft.fft function. 
These coefficients represent the amplitudes and phases of the sine waves that make up the signal.

We then remove the high-frequency coefficients by setting all coefficients outside of a certain range to zero. 
In this example, we keep only the first 20 coefficients and set the rest to zero.

Finally, we reconstruct the signal using only the low-frequency coefficients by applying the inverse Fourier transform using the np.fft.ifft function. 
We plot the reconstructed signal to visualize the effect of the compression.

This is just a simple example, and in practice, 
there are many ways to choose which Fourier coefficients to keep and how to encode them for compression.

'''


CODE

PYTHON

import numpy as np
import matplotlib.pyplot as plt

# Generate a test signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

# Plot the original signal
plt.figure()
plt.plot(t, signal)
plt.title('Original Signal')

# Compute the Fourier coefficients
coeffs = np.fft.fft(signal)

# Remove high-frequency coefficients
num_coeffs_to_keep = 20
coeffs[num_coeffs_to_keep:-num_coeffs_to_keep] = 0

# Reconstruct the signal using only the low-frequency coefficients
reconstructed_signal = np.fft.ifft(coeffs)

# Plot the reconstructed signal
plt.figure()
plt.plot(t, reconstructed_signal.real)
plt.title('Reconstructed Signal')

plt.show()
