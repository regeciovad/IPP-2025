# Matrix multiplication
# https://alysivji.github.io/python-matrix-multiplication-operator.html 
# On Merlin numpy package is not install for Python 3.10
# Use: python3 08_matrix.py

import numpy as np # nice pakcage for mathematical calculations and others

A = np.matrix('3 1; 8 2')
print(A)

B = np.matrix('6 1; 7 9')
print(B)

print(A @ B)
