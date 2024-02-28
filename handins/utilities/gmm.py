"""
	Gaussian Mixture Model (EM-algorithm)

	This class implements the main functionality of a 
	Gaussian Mixture Model. There is some function
	implementations missing, which is up to the student
	to fill in.
"""
import numpy as np
from scipy.stats import multivariate_normal

class GMM: 
	def __init__(self, K=3):
		"""
			Constructor of the Gaussian Mixture Model.

			Args:
    			d (int): Data dimensionality
    			K (int): This is a second param.

			Returns:
    			This is a description of what is returned.
		"""
		self.K		= K
		self.mu		= None
		self.Sigma	= None
		self.pi		= np.ones((K,)) / K # Equal probability for simplicity.

	def prob(X, mu, sigma):
		mvn = multivariate_normal(mean=mu, cov=sigma)
		return mvn.pdf(X)

            
	def initialize_parameters(self, X):
		"""
			This function should utilize information from the data to initialize
			the parameters of the model.
			In particular, it should update self.mu and self.Sigma.

            This function corresponds to line 2-4 in Algorithm 13.3 in [Zaki, p. 349]
            
			Args:
    			X (matrix, [n, d]): Data to be used for initialization.

			Returns:
    			Tuple (mu, Sigma, pi), 
					mu has size		[K, d]
					Sigma has size	[K, d, d]
					pi has size		[K]
		"""
		raise NotImplementedError() 

        
	def posterior(self, X):
		"""
			The E-step of the EM algorithm. 
			Returns the posterior probability p(y|X)

            This function corresponds to line 8 in Algorithm 13.3 in [Zaki, p. 349]
            
			Args:
				X (matrix, [n,  d]): Data to compute posterior for.

			Returns:
				Matrix of size		[n, K]
		"""
		raise NotImplementedError()


	def m_step(self, X, P):
		"""
			Update the estimates of mu, Sigma, and pi, given the current
			posterior probabilities.

            This function corresponds to line 10-12 in Algorithm 13.3 and Eqn. (13.11-13) in [Zaki, p. 349].
            
			Args:
    			X (matrix, [n, d]): Data to be used for initialization.
    			P (matrix, [n, K]): The posterior probabilities for the n samples.

			Returns:
    			Tuple (mu, Sigma, pi), 
					mu has size		[K, d]
					Sigma has size	[K, d, d]
					pi has size		[K]
		"""
		raise NotImplementedError()
	
	
	def fit(self, X, max_iter=20, tol=1e-5):
		self.mu, self.Sigma, self.pi = self.initialize_parameters(X)

		for i in range(max_iter): # Loop max iter or break if changes are small
			# E-step
			P = self.posterior(X)

			# M-step
			mu, Sigma, pi = self.m_step(X, P)

			# Stopping criteria
			mu_close = np.allclose(mu,		self.mu,	atol=tol, rtol=tol)
			Si_close = np.allclose(Sigma,	self.Sigma, atol=tol, rtol=tol)
			pi_close = np.allclose(pi,		self.pi,	atol=tol, rtol=tol)

			if mu_close and Si_close and pi_close: break

			# Update parameters
			self.mu		= mu
			self.Sigma	= Sigma
			self.pi		= pi


	def predict(self, X):
		P = self.posterior(X)
		return np.argmax(P, axis=1)


