# Algorithm for sphere decoding in a classical setting
# Author: Edmund Dable-Heath
# Attempting to implement algorithm 1 from: http://users.ece.utexas.edu/~hvikalo/pubs/paper1r.pdf

import numpy as np
import Functions as fn
import copy

# For full rank lattices Q is not decomposed into two separate matrices.


def SphereDecoding(Q, R, target, distance, dimension):
    """
    Classical Sphere Decoding
    :param Q: Q matrix from QR decomp of basis matrix
    :param R: R matrix from QR decomp of basis matrix
    :param target: Target point in R^m
    :param distance: Sphere decoding radius
    :param dimension: Dimension of target point space.
    :return: Library of points withing sphere; {point (vector) : distance from x (float)}. List of tuples of (k, s_k).
    """
    m = dimension - 1
    y = np.dot(Q, target)
    k = m
    d = distance
    s_current = {}
    dim_d = {k: d}
    s_results = {}
    tree_plotting = []
    while k <= m:
        print('current dimension: ', k)
        print('distances: ', dim_d)
        print('current s: ', s_current)
        # Adjust y
        y_adjk = fn.adjustment(y, k, R, s_current, m)
        print('current adjusted y: ', y_adjk)
        # Find upper bound
        UB = fn.bound(y_adjk, k, dim_d[k], R)
        print('Upper bound: ', UB)
        # Find first S_k
        print('sk val: ', fn.bound(y_adjk, k, dim_d[k], R, type='L') - 1)
        s_current[k] = fn.bound(y_adjk, k, dim_d[k], R, type='L') - 1
        print('init sk: ', s_current[k])
        while s_current[k] <= UB:
            s_current[k] = s_current[k] + 1
            print('what does s look like?: ', s_current[k])
            tree_plotting.append(copy.copy(s_current))
            print(k)
            if k == 0:
                # distance from target:
                final_dist = distance - dim_d[k] + (y[0] - R[0][0]*s_current[0])**2
                s_results[final_dist] = s_current
                continue
            else:
                # Decrease k
                print('DECREASE K HERE --------------')
                k -= 1
                dim_d[k] = dim_d[k+1] - (fn.adjustment(y, k+1, R, s_current, m) - R[k+1][k+1]*s_current[k+1])**2
                print('new distance: ', dim_d[k])
                break
        else:
            # Increase k
            print('INCREASE K HERE --------------------')
            k += 1
            if k == m+1:
                return s_results, tree_plotting
            else:
                continue
        continue

