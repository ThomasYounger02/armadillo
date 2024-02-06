def plot_hist(data):
	"""Function to output a histogram of the instance variable data using 
	matplotlib pyplot library.
	
	Args:
		None
		
	Returns:
		None
	"""
	plt.hist(data)
	plt.title('Histogram of Data')
	plt.xlabel('data')
	plt.ylabel('count')