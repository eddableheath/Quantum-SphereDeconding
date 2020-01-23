# Testing sphere decoding algorithm
# Author: Edmund Dable-Heath
# Let's hope this works I guess?

import numpy as np
import SphereDecodingClassical as sd

# For first test use 2 dimensional integer lattice and target point [5/8, 5/8]

B = np.array([[1,0],[0,1]])
q, r = np.linalg.qr(B, mode='reduced')
x = np.array([5/8, 5/8])
dist = 1.

print(sd.SphereDecoding(q, r, x, dist, 2))