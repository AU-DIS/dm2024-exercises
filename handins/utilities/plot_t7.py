import numpy as np
import matplotlib.pyplot as plt
from argparse import Namespace
from tqdm import tqdm

from load_data import load_t7

X, y = load_t7()
n, d = X.shape
perm = np.random.permutation(n)
X = X[perm]
y = y[perm]

T = 1500
X = X[:T]
y = y[:T]

def norm2(x, y):
	diff = x.x - y.x 
	return np.sqrt(np.dot(diff, diff))

def searchNeighborhood(D, x, e, dist_fn):
	return [y.idx for y in D if dist_fn(x, y) < e] 

def densityConnected(x, k, core, D):
	x.visiting = True
	for y in x.neighborhood:
		y_ = D[y]
		if y_.visiting: continue
		y_.cluster = k
		if y_.idx in core: 
			densityConnected(y_, k, core, D)

def dbscan(X, e, m, dist_fn=norm2):
	D = []
	for i, x in enumerate(X):
		x_ = Namespace()
		x_.x = x
		x_.idx = i
		x_.visiting = False
		D.append(x_)
	
	core = []
	for x in tqdm(D):
		x.neighborhood = searchNeighborhood(D, x, e, dist_fn)
		x.cluster = None
		if len(x.neighborhood) > m: core.append(x.idx)

	k = 0
	for x in core:
		x_ = D[x]
		if x_.cluster is not None: continue
		x_.cluster = k
		densityConnected(x_, k, core, D)
		k += 1
	
	clusters = []
	for i in range(k):
		idxes = [x.idx for x in D if x.cluster == i]
		clusters.append(idxes)

	y = np.ones((len(D),)) * 25
	for i in range(k):
		y[clusters[i]] = i
	return y

y = dbscan(X, 15, 10)

fig, ax = plt.subplots(1, 1)
ax.scatter(*(X.T), c=y)
plt.show()
