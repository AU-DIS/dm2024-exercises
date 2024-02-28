import numpy as np

from numpy import genfromtxt

f = 'soybean-small.data'
with open(f, 'r') as f:
	X = np.array([[float(x) for x in l.strip().split(',')[:-1]] for l in f])
with open(f, 'r') as f:
	y = np.array([int(l.strip().split(',')[-1][1])-1 for l in f])

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)
ax.scatter(X[:,2], X[:,3], c=y)
plt.show()
