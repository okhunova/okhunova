son=[1 , 2,3,4,5,6,7,8,9]
n = len(son)
katta = son[0]
for k in range(1,n):
    if katta < son[k]:
        katta = son[k]
    else: 
        katta = katta
print('\nKatta=',katta)
