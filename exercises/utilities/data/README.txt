iris.txt -- 4 dimensions + class labels


iris-slw.dat -- Iris 2D data: sepal length and sepal width


categorial-3way.dat -- discretized 3-way data for chap3
			sepal length, sepal width, class


iris-layout.txt -- Iris graph from chap4
	each edge is denoted as
		"e" xi xj w(xi, xj) 
	each vertex is denoted as
		"v" vi x-pos y-pos class


hprd.txt -- human protein interaction network for chap4, example 4.9
	each line has an edge 
		vi vj


iris-slwpl.dat -- Iris 3D data for chap7
		sepal length, sepal width, petal length


iris-2d-nonlinear.dat -- Non-linear 2D Iris data for chap7, example 7.7
	

iris-conv.txt -- discretized 4D + class Iris dataset for chap12,
	first used in example 12.9.


iris-PC.txt -- Iris 2D Principal Components dataset, 
		first used in chap13, example 13.2


kerneldata.txt -- dataset for kernel kmeans, chap12, example 13.3


t7-4k.txt -- density-based dataset for chap15, 
		first used in figure 15.1
		ignore the last dimension


iris-clusters-normalized.txt -- iris similarity graph for chap16.
     each vertex is denoted as
		"v" vi x-pos y-pos class class-val
	 each edge is denoted as
		"e" xi xj w(xi, xj) val


iris-slwc.txt -- Iris 2D, 2 class dataset for classification in chap18, 
		with Iris-setosa as c1 (-1) and others as c2 (+1)
                 chap19, chap20, chap21
		sepal length, sepal width, class (+1 or -1)


iris-PC-versicolor.txt -- Iris 2D Principal Components dataset, 
		with two classes (Iris versicolor:c1(-1) versus rest:c2(+1)).
		"non-linear" class boundary

		Used in chap20, example 20.4
		Used in chap21, example 21.8, 21.10
		Used in chap 22, example 22.3, 22.12, 22.13, 22.14


ldata.txt -- example dataset used in example 21.1 and 21.2
