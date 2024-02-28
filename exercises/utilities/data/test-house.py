import numpy as np

from numpy import genfromtxt

fn = 'house-votes-84.data'

l = [
'handicapped-infants',
'water-project-cost-sharing',
'adoption-of-the-budget-resolution',
'physician-fee-freeze',
'el-salvador-aid',
'religious-groups-in-schools',
'anti-satellite-test-ban',
'aid-to-nicaraguan-contras',
'mx-missile',
'immigration',
'synfuels-corporation-cutback',
'education-spending',
'superfund-right-to-sue',
'crime',
'duty-free-exports',
'export-administration-act-south-africa',
]

with open(fn, 'r') as f:
	X = np.array([[1. if x == 'y' else (0. if  x=='n' else -1.) for x in l.strip().split(',')[1:]] for l in f])
with open(fn, 'r') as f:
	y = np.array([1 if l.strip().split(',')[0] == 'republican' else 0 for l in f])

sel = np.where(X.min(axis=1) >= 0)

X = X[sel]
y = y[sel]

X += np.random.randn(*(X.shape))*0.03
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,6)
pairs = [ (2,3), (4,10), (5,11), (6,12), (7,13), (9,6) ]

for i, (p, q) in enumerate(pairs): 
	ax[i].scatter(X[:,p], X[:,q], c=y)
	ax[i].set_xlabel(l[p])
	ax[i].set_ylabel(l[q])

plt.show()
