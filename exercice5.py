import numpy as np 
print ("original matrix :\n")
X=np.random.rand(5,10)
print(X)
print("\n subtract the mean of each row of the said matrix :\n")
Y=X-X.mean(axis=1 , keepdims=True)
print (Y)