# Sphere decoding algorithm functions
# Author: Edmund Dable-Heath
# Attempting to implement algorithm 1 from: http://users.ece.utexas.edu/~hvikalo/pubs/paper1r.pdf

import math


def adjustment(y, k, r, s, m):
    """
    Adjustment of vector
    :param y: y vector (1 dim array)
    :param k: base index to adjust (int)
    :param r: r matrix from QR decomp of basis (2 dim array)
    :param s: lattice vector values so far (dictionary?)
    :param m: dimension of lattice (int)
    :return: y_base|base+1, adjusted value (float)
    """
    l = k+1
    if l >= m+1:
        return y[k]
    else:
        adj = [r[l][j] * s[j] for j in range(l, m+1)]
        return y[k] - sum(adj)


def bound(adjy, k, squareddistance, r, type='U'):
    """
    Computing bounds on vectors
    :param adjy: adjusted y vector (1 dim array)
    :param k: which dimension being looked at (int)
    :param squareddistance: squared total distance (float)
    :param bound: upper or lower bound?
    :return: upper or lower bound?
    """
    if type == 'U':
        return math.floor((math.sqrt(squareddistance) + adjy)/r[k][k])
    if type == 'L':
        return math.ceil((-math.sqrt(squareddistance)+adjy)/r[k][k])