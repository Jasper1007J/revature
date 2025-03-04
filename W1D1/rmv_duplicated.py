# remove the duplicated from the list
l = list(map(int,input().split()))

res = set()
duplicates = set()
for x in l:
    if x in res:
        duplicates.add(x)
    else:
        res.add(x)

print(res,duplicates)
