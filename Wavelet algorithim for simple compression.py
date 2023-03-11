# description
'''
In this example, we first generate a test signal that consists of two sine waves with frequencies of 10 Hz and 20 Hz. 
We then plot the original signal to visualize it.

Next, we perform the Wavelet transform on the signal using the pywt.wavedec function. This decomposes the signal into different frequency sub-bands,
with the lowest frequencies in the first element of the output tuple, and the highest frequencies in the last element.

We then set a compression threshold and set all coefficients with absolute values below this threshold to zero using the pywt.threshold function.
In this example, we set the threshold to 10% of the maximum coefficient in each sub-band.

Finally, we reconstruct the signal using the compressed coefficients using the pywt.waverec function.
We plot the reconstructed signal to visualize the effect of the compression.

This is just a simple example, and in practice, there are many ways to choose the compression threshold and how to encode the compressed coefficients for
efficient storage or transmission.


'''





# code

import pywt
import numpy as np
import matplotlib.pyplot as plt

# Generate a test signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

# Plot the original signal
plt.figure()
plt.plot(t, signal)
plt.title('Original Signal')

# Perform the wavelet transform
wavelet = 'db4'
coeffs = pywt.wavedec(signal, wavelet)

# Set a compression threshold
threshold = 0.1

# Set small coefficients to zero
for i in range(1, len(coeffs)):
    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))

# Reconstruct the signal using the compressed coefficients
reconstructed_signal = pywt.waverec(coeffs, wavelet)

# Plot the reconstructed signal
plt.figure()
plt.plot(t, reconstructed_signal)
plt.title('Reconstructed Signal')

plt.show()
