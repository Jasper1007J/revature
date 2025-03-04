# Finding the closest number to zero in the given list 
l = list(map(int,input().split()))
res = float('inf')
for i in l:
    if abs(i) < abs(res):
        res  = i
print(res)