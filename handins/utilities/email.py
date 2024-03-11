import random
import scipy.io as sio
import time

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
### END IMPORTS

from utilities.load_data import load_mnist
import csv
from itertools import count

import os
print(os.getcwd())

data  = open('./utilities/data/email-Eu-core.txt', "r", encoding='utf8')
Graphtype = nx.Graph()

G = nx.parse_edgelist(data, delimiter=' ', create_using=Graphtype,
                      nodetype=int)

labels = {}
with open('./utilities/data/email-Eu-core-department-labels.txt', "r", encoding='utf8') as f: 
    cf = csv.reader(f, delimiter=' ')
    for row in cf:
        labels[int(row[0])] = int(row[1])

nx.set_node_attributes(G, labels, name="community")

G_copy = G.copy() 


## Select a subset of the communities to keep
com = set([1,2,7,15,32,3])

for i in range(G.number_of_nodes()):
    if G.nodes[i]['community'] not in com: 
        G_copy.remove_node(i)

for edge in G_copy.edges():
    if edge[0] == edge[1]:
        G_copy.remove_edge(edge[0], edge[1])

## Keep only largest connected component
remove = [node for node,degree in dict(G_copy.degree()).items() if degree <= 2]
G_copy.remove_nodes_from(remove)
largest_cc = max(nx.connected_components(G_copy), key=len)
S = G_copy.subgraph(largest_cc).copy() 

groups = set(nx.get_node_attributes(S,'community').values())
n_communities = len(groups)

mapping = dict(zip(sorted(groups), count()))
nodes = S.nodes()
colors = [mapping[S.nodes[n]['community']] for n in nodes]


G_final = nx.convert_node_labels_to_integers(G_copy)
G_final = G_final.to_directed()

S_dir = G_final
S_undir = S_dir.to_undirected()


communities = [S.nodes[n]['community'] for n in S.nodes()]
groups = set(nx.get_node_attributes(S,'community').values())
n_communities = len(groups)

mapping = dict(zip(sorted(groups), count()))
nodes = S_dir.nodes()
colors = [mapping[S_dir.nodes[n]['community']] for n in nodes]


# For plotting reasons
for v in S_dir.nodes():
    del S_dir.nodes[v]['community']
    
    
## drawing nodes and edges separately so we can capture collection for colobar
#plt.figure(1,figsize=(30,30))
#pos = nx.spring_layout(S)
#ec = nx.draw_networkx_edges(S, pos, alpha=0.2)
#nc = nx.draw_networkx_nodes(S, pos, nodelist=nodes, node_color=colors, node_size=100, cmap=plt.cm.jet)
#plt.colorbar(nc)

#plt.axis('off')
#plt.show()