
# DESCRIPTION
'''
In this example, we first generate a test signal that consists of two sine waves with frequencies of 10 Hz and 20 Hz.
We then plot the original signal to visualize it.

Next, we perform Principal Component Analysis (PCA) on the signal using the PCA class from the sklearn.decomposition module.
We set the number of principal components to 10, meaning that we want to keep only the 10 most important components.

We then reconstruct the signal using the compressed components by taking the dot product of the principal components with the transformed 
signal and flattening the result to obtain a 1D array.

Finally, we plot the reconstructed signal to visualize the effect of the compression.

This is just a simple example, and in practice, there are many ways to choose the number of principal 
components to keep and how to encode the compressed components for efficient storage or transmission.
'''






# CODE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generate a test signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

# Plot the original signal
plt.figure()
plt.plot(t, signal)
plt.title('Original Signal')

# Perform PCA on the signal
pca = PCA(n_components=10)
signal_pca = pca.fit_transform(signal.reshape(-1, 1))

# Reconstruct the signal using the compressed components
reconstructed_signal = np.dot(signal_pca, pca.components_).flatten()

# Plot the reconstructed signal
plt.figure()
plt.plot(t, reconstructed_signal)
plt.title('Reconstructed Signal')

plt.show()
