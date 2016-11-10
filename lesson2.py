import numpy as np
X=np.array(range(4*5)).reshape(4,5)+1;
print(X)
i_idx=np.array([1,3,0,2]);
j_idx=np.array([0,2,3,1]);
k=0;
ans=np.zeros(4,dtype=int);
m=i_idx.size
while k<m:
    ans[k]=X[i_idx[k],j_idx[k]];
    k=k+1;
print(ans)
