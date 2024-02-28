import numpy as np
from gmm import GMM
from load_data import load_iris
from matplotlib import pyplot as plt

class MyGMM(GMM):
	def initialize_parameters(self, X):
		"""
			This function should utilize information from the data to initialize
			the parameters of the model.
			In particular, it should update self.mu and self.Sigma.

			Args:
    			X (matrix, [n, d]): Data to be used for initialization.

			Returns:
    			Tuple (mu, Sigma, pi), 
					mu has size		[K, d]
					Sigma has size	[K, d, d]
					pi has size		[K]
		"""
		n, d	= X.shape
		K		= self.K

		X_		= X[np.random.permutation(n)] # Shuffle data

		mu		= np.zeros((self.K, d))
		size	= n // K

		for i in range(K):
			mu[i] = np.mean(X[i*size:(i+1)*size])

		Sigma	= np.tile(np.expand_dims(np.eye(d), 0), (K, 1, 1)) * 0.1 # (K, d, d)
		
		pi		= np.ones((self.K)) / self.K
		return mu, Sigma, pi


	def prior(self): 
		"""
			Returns the prior probabilities p(Y).

			Returns:
				Vector of size		[K]
		"""
		return self.pi


	def posterior(self, X):
		"""
			The E-step of the EM algorithm. 
			Returns the posterior probability p(y|X)

			Args:
				X (matrix, [n,  d]): Data to compute posterior for.

			Returns:
				Matrix of size		[n, K]
		"""
		P = np.zeros((X.shape[0], self.K))
		for i in range(self.K):
			P[:,i] = GMM.prob(X, self.mu[i], self.Sigma[i])

		return P / P.sum(axis=1, keepdims=True) # Normalize


	def m_step(self, X, P):
		"""
			Update the estimates of mu, Sigma, and pi, given the current
			posterior probabilities.

			Args:
    			X (matrix, [n, d]): Data to be used for initialization.
    			P (matrix, [n, K]): The posterior probabilities for the n samples.

			Returns:
    			Tuple (mu, Sigma, pi), 
					mu has size		[K, d]
					Sigma has size	[K, d, d]
					pi has size		[K]
		"""
		# Sizes
		n, d	= X.shape
		K		= self.K

		# Mu 
		Nks		= np.sum(P, axis=0, keepdims=True).T	# (K, 1)
		P_		= P.reshape((n, K, 1))					# (n, K, 1)
		X_		= X.reshape((n, 1, d))					# (n, 1, d)
		mu_hat	= (P_ * X_).sum(axis=0) / Nks			# (K, d)
		
		# Sigma
		Nks		= Nks.reshape((K, 1, 1))				# (K, 1, 1)
		P_		= P_.reshape((n, K, 1, 1))
	
		X_		= X_ - self.mu.reshape((1, K, d))		# (n, K, d)

		X_		= X_.reshape((n, K, d, 1)) * P_
		X__		= X_.reshape((n, K, 1, d))

		outer	= X_ @ X__								# (n, K, d, d)
		Si_hat	= outer.sum(axis=0) / Nks				# (K, d, d)

		# Pi
		pi_hat	= Nks.squeeze() / n
		return  mu_hat, Si_hat, pi_hat

if __name__ == "__main__":

	# Iris
	X, _	= load_iris()
	K		= 3
	gmm		= MyGMM(K)

	gmm.mu, gmm.Sigma, gmm.pi = gmm.initialize_parameters(X)
	
	y1 = gmm.predict(X) 
	gmm.fit(X, max_iter=100)
	y2 = gmm.predict(X) 

	fig, ax = plt.subplots(2, 2)

	ax[0, 0].scatter(X[:,0], X[:,1], c=y1)
	ax[0, 1].scatter(X[:,0], X[:,1], c=y2)


	# Simple dataset
	X	= np.zeros((300, 2))
	mus = [(0, 0), (1, 2), (3, 0)]
	for i, mu in enumerate(mus):
		X[i*100:(i+1)*100] = np.random.multivariate_normal(mu, np.eye(2) * 0.2, 100)
	
	K		= 3
	gmm		= MyGMM(K)

	gmm.mu, gmm.Sigma, gmm.pi = gmm.initialize_parameters(X)
	
	y1 = gmm.predict(X) 
	gmm.fit(X, max_iter=100)
	y2 = gmm.predict(X) 

	ax[1, 0].scatter(X[:,0], X[:,1], c=y1)
	ax[1, 1].scatter(X[:,0], X[:,1], c=y2)

	# Contours
	fig, ax = plt.subplots(1, 3)

	x, y = np.mgrid[-1:5:.1, -1:4:.1]
	pos = np.dstack((x, y))
	print(pos.shape)
	ps	= pos.shape
	pos = pos.reshape(-1, 2)
	P	= gmm.posterior(pos).T

	pos = P.reshape([3] + list(ps)[:-1])

	for i in range(3):
		ax[i].contourf(x, y, pos[i], levels=1)
		ax[i].scatter(*(X.T), c='red')


	plt.show()
