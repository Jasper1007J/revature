start = int(input())
end = int(input())
res = []
for i in range(start,end):
    if i > 1:
        for j in range(2, i//2):
            if (i % j) == 0:
                break
        else:
            res.append(i)
print(res)