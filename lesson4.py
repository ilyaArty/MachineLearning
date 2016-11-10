import numpy as np
X=np.array([6,2,0,3,0,0,5,7,0]);
i=1;
ans=0;
while i<X.shape[0]:
    if X[i-1]==0:
        if X[i]>ans:
            ans=X[i];
    i=i+1;
print(ans)            
        
