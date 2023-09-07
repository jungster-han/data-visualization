import matplotlib.pyplot as plt # import the library
plt.scatter(Xs, Ys) # Create the scatter plot, Xs and Ys are two numpy arrays of the same length
plt.show() # Display the plot you just created.

# When working with matrices, numpy provides some convenient facilities. For example, to find the inverse of a matrix, use
import numpy as np
np.linalg.inv(matrix_to_invert)

# The scipy package provides statistical distributions. For example, to calculate p-values for the t-distribution, you can use the survival function (sf):

import scipy.stats
scipy.stats.t.sf(T, num_degrees_of_freedom)

Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, \
0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, \
1.72, 2.03, 2.02, 2.02, 2.02])

Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, \
93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, \
840.0, 801.0, 519.0])

N = 24
