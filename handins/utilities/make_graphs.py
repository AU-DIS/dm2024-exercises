filename = "./Graphs/"

def saveGraph(N, edges, filename):
    f = open(filename, 'w')
    for edge in edges:
        f.write(str(list(edge)[0])+" "+str(list(edge)[1]))
        f.write('\n')


def save_list_to_txt(list_of_elements, filename):
    for element in list_of_elements:
        writeNewLine(filename, str(element))
        
def writeNewLine(filename, newline):
    file_object = open(filename, 'a')
    file_object.write(newline+"\n")
    file_object.close()

def read_edge_list(filename):
    edge_list = []
    set_of_nodes = {''}
    with open(filename) as file:
        for line in file:
            u_to_v = line.split(' ')
            u = int(u_to_v[0])
            v = int(u_to_v[1])
            edge_list.append([u, v])
            if u not in set_of_nodes: set_of_nodes.add(u)
            if v not in set_of_nodes: set_of_nodes.add(v)
    return edge_list

def read_list(filename):
    import numpy as np
    element_list = []
    with open(filename) as file:
        for line in file:
            element_list.append(float(line[:-1]))
    return np.array(element_list)
  
def load_data():
    import numpy as np
    CysPoLV = read_list('./data/CysPoLV.txt')
    UPS = read_list('./data/UPS.txt')
    UPS = [int(el)+1 for el in UPS]
    pos_x = read_list('./data/pos_x.txt')
    pos_y = read_list('./data/pos_y.txt')
    data = [np.array([pos_x[i], pos_y[i]]) for i in range(len(CysPoLV))]
    return data, UPS


#function for making the InVS13 graph
def HVR1(filename):
    import graph_tool.all as gt
    import numpy as np
    print('Reading malaria_genes/HVR_1...')
    g = gt.collection.ns["malaria_genes/HVR_1"]
    g.set_directed(False)
    comp, hist = gt.label_components(g, attractors=True)
    sorted_keys = sorted(range(len(hist)), key=lambda k: hist[k]) 
    g = gt.Graph(gt.GraphView(g, vfilt=comp.a == sorted_keys[-1]), prune=True)
    N = g.num_vertices()
    CysPoLV = []
    UPS = []
    pos_x = []
    pos_y = []
    for i in range(g.num_vertices()):
        CysPoLV.append(g.vertex_properties['CysPoLV'][i])
        UPS.append(g.vertex_properties['UPS'][i])
        pos_x.append(g.vertex_properties['_pos'][i][0])
        pos_y.append(g.vertex_properties['_pos'][i][1])
    pos_x = np.array((pos_x-np.min(pos_x))/(np.max(pos_x)-np.min(pos_x)))
    pos_y = np.array((pos_y-np.min(pos_y))/(np.max(pos_y)-np.min(pos_y)))
    save_list_to_txt(CysPoLV,'./data/CysPoLV.txt')
    save_list_to_txt(UPS,'./data/UPS.txt')
    save_list_to_txt(pos_x,'./data/pos_x.txt')
    save_list_to_txt(pos_y,'./data/pos_y.txt')
    saveGraph(N, g.edges(), './data/edges.txt')
    return    


if __name__ == "__main__":
    HVR1(filename)  
    
    