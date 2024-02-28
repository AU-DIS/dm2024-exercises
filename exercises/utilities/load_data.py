import numpy as np
import os
import urllib.request
import gzip
import zipfile
import pickle

__all__ = [
        'load_iris',
        'load_iris_PC',
        'load_t7',
        'load_synthetic_data'
        'label_to_index',
        'index_to_label',
        'index_to_feature'
    ]

# Prepare label dictionaries to translate between strings in text files and ints in numpy.
label_to_index = { s: i for i, s in enumerate(["Iris-versicolor", "Iris-setosa", "Iris-virginica"]) }
index_to_label = { i: s for s, i in label_to_index.items() }
index_to_feature = ["Petal length", "Petal width", "Sepal length", "Sepal width"]

def _load_data(filename, onehot, lab_to_idx=label_to_index):
    data_path = os.path.dirname(os.path.realpath(__file__)) + '/data/' + filename
    print(data_path)
    
    X, y = [], []
    with open(data_path, 'r') as f:
        for l in f:
            if len(l) == 0: continue

            # Example line:
            # 6.6,2.9,4.6,1.3,"Iris-versicolor"
            l = l.replace('"', '') # Remove "

            x_ = [float(s) for s in l.split(',')[:-1]]
            y_ = lab_to_idx[l.split(',')[-1].strip()]

            X.append(x_)
            y.append(y_)

    n = len(y)
    d = len(lab_to_idx)

    y = np.array(y)
    if onehot:
        # Make (n, 3) array with one-hot encodings of the data.
        y_onehot = np.zeros( (n, d) )
        y_onehot[np.arange(n), y] = 1

    return np.array(X), y_onehot

def load_iris(onehot=True):
    """
        Loads full iris dataset
    """
    return _load_data('iris.txt', onehot)

def load_iris_PC(onehot=True):
    """
        Loads 2 principal components from iris dataset
    """
    return _load_data('iris-PC.txt', onehot)

def load_t7():
    """
        Loads dataset with non-convex clusters from [Zaki, p. 376].
    """
    return _load_data('t7-4k.txt', onehot=True, lab_to_idx={"0": 0})

def load_synthetic_data(index=0, dims=10):
    data_file = 'synth_multidim_%03i_%03i.arff' % (dims, index)
    pth = "%s/data/%s" % (os.path.dirname(os.path.abspath(__file__)), data_file)
    print(pth)

    with open(pth, 'r') as f:
        l = f.readline()
        # Skip header lines
        while not '@data' == l.strip(): 
            l = f.readline()

        data = []
        labels = []
        for l in f:
            splt = l.strip().split(',')
            d = [float(s) for s in splt[:-1]]
            l = int(splt[-1])
            data.append(d)
            labels.append(l)

    return np.array(data), np.array(labels)

def load_voting_data():

    data_path = os.path.dirname(os.path.realpath(__file__)) + '/data/' + 'house-votes-84.data'
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

    with open(data_path, 'r') as f:
        X = np.array([[1. if x == 'y' else (0. if  x=='n' else -1.) for x in l.strip().split(',')[1:]] for l in f])
    with open(data_path, 'r') as f:
        y = np.array([1 if l.strip().split(',')[0] == 'republican' else 0 for l in f])

    sel = np.where(X.min(axis=1) >= 0) # Remove rows containing '?'

    X = X[sel]
    y = y[sel]

    X += np.random.randn(*(X.shape))*0.03 # Add a little noise to the categorical data in order to better see plots.
    return X, y, l

def load_mnist():
    base_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../utilities/data/') + '/'
    X_train_file = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
    y_train_file = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
    X_test_file  = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
    y_test_file  = 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'

    names = ['X_train.gz', 'y_train.gz', 'X_test.gz', 'y_test.gz']
    files = [X_train_file, y_train_file, X_test_file, y_test_file]
    sizes = [60000,        60000,        10000,       10000]

    out = []
    for (url, fn, size) in zip(files, names, sizes):
        file_path = base_dir + fn

        if not os.path.exists(file_path):
            print("Downloading %s to %s" % (url, file_path))
            urllib.request.urlretrieve(url, file_path)

        is_img = 'X' in fn
        image_size = 28

        with gzip.open(file_path,'r') as f:
            f.read(16) if is_img else f.read(8)
            read_size = size * 28**2 if is_img else size

            buf = f.read(read_size)
            data = np.frombuffer(buf, dtype=np.uint8)
            if is_img: 
                data = data.astype(np.float32)
                data = data.reshape(size, image_size, image_size)
            out.append(data)
    
    return tuple(out)

def load_market_basket():
    url = "http://fimi.uantwerpen.be/data/retail.dat"
    name = "retail.dat"
    base_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../utilities/data/') + '/'
    
    file_path = base_dir + name
    if not os.path.exists(file_path):
        print("Downloading %s to %s" % (url, file_path))
        urllib.request.urlretrieve(url, file_path)
        
    with open(file_path, 'r') as f:
        lines = [[int(x) for x in l.strip().split(" ")] for l in f]    
    return lines

def load_dblp_citations():
    url = "http://nrvis.com/download/data/cit/cit-DBLP.zip"
    name = url.split('/')[-1]
    base_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../utilities/data/') + '/'
    
    file_path = base_dir + name
    edges_file = 'cit-DBLP.edges'
    
    if not os.path.exists(file_path):
        print("Downloading %s to %s" % (url, file_path))
        urllib.request.urlretrieve(url, file_path)
    
    if not os.path.exists(base_dir + edges_file):
        with zipfile.ZipFile(file_path, 'r') as z:
            print("Extracting citation file `%s` to %s" % (edges_file, base_dir))
            z.extract(edges_file, path=base_dir)
    
    edges = []
    with open(base_dir + edges_file, 'r') as f:
        f.readline()
        f.readline()
        
        edges = [tuple(map(int, s.strip().split(' '))) for s in f]
        
    # Load precomputed node locations for nodes
    with open(base_dir + 'cit-DBLP-pos.pkl', 'rb') as f:
        pos = pickle.load(f)
    return edges, pos
    
def load_city_tour():
    base_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../utilities/data/') + '/'
    file_name = base_dir + 'city_distances.txt'
    print(file_name)
    with open(file_name, 'r') as f:
        cities = [l.strip().split(',') for l in f if ('--' not in l) and ('#' not in l)]
    
    n = len(cities)
    distances = np.zeros((n, n), dtype=np.float)
    prev = 0.
    
    for i, (city, distance) in enumerate(cities):
        distance = int(distance)
        if i == 0: continue
        
        if distance < prev: prev = 0.
        
        dist = distance - prev
        distances[i-1, i] = dist
        
        prev = distance
     
    # Build rest of table
    for i in range(0, n):
        for j in range(i+2, n):
            distances[i, j] = distances[i, j-1] + distances[j-1, j]
    distances = distances + distances.T
    
    cities = list(map(lambda x: x[0], cities))
    return cities, distances
    

if __name__ == "__main__": 
    # Example usage. Just run
    # (dm20) > python load_data.py 
    # to see this execution. 
    c, d, fn = load_city_tour()
    print(c[:10])
    print(d[0,:10])
    print(fn(c[3], 0))
    print(fn(c[3], 300))
    exit()
    datasets = [
            ('iris.txt', load_iris), 
            ('iris-PC.txt', load_iris_PC),
            ('t7-4k.txt', load_t7),
            ('mnist', load_mnist),
        ]
    for n, fn in datasets:
        out = fn()
        print("%-15s shapes: " % n, [o.shape for o in out])

