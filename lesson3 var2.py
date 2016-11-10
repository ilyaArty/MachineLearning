import numpy as np
X=np.array([1,2,2,4,6,5,6,6,7,8,4,4]);
Y=np.array([4,2,1,2,4,4,5,7,6,8,6,6]);
X=np.sort(X);
Y=np.sort(Y);
if X.all()==Y.all():
    print("True");
else:        
    print("False");   
%timeit pass
