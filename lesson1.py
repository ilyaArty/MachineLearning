import numpy as np
X=np.array([[1,0,1],[2,0,2],[3,0,3],[4,4,4]]);
ans=1;
i=0;
while i<X.shape[0] and i<X.shape[1]:
    if X[i,i]>0:
        ans=X[i,i]*ans;
    i=i+1;
print(ans)


