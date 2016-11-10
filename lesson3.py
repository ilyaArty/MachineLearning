import numpy as np
X=np.array([1,2,2,4]);
Y=np.array([4,2,1,2]);
X=np.sort(X);
Y=np.sort(Y);
i=0;
while i<X.size:
    if X[i]==Y[i]:
        if i==X.size-1:
            print("True");
    else:
        print("False");
        break
    i=i+1;

