import numpy as np
X=np.array([1,2,3,4,5,6,5]);
nums=np.zeros(X.size);
counts=np.zeros(X.size);
i=1;
elemOld=X[0];
nums[0]=elemOld;
counts[0]=1;
j=0;
while i<X.shape[0]:
    elem=X[i];
    if elem==elemOld:
        counts[j]=counts[j]+1;
    else:
        j=j+1;
        nums[j]=elem;
        counts[j]=counts[j]+1;
    elemOld=elem;
    i=i+1;
nums=nums[:j+1]
counts=counts[:j+1]
print(nums,counts)
