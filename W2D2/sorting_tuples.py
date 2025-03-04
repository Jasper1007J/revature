data = [(3, 5), (1, 8), (4, 4), (2, 6)]

sum = []
for i,tup in enumerate(data):
    
    total = 0
    for item in tup:
        total += item
    sum.append(total)

for i in range(0, len(sum)):
    for j in range(i+1, len(sum)):
        if sum[i] < sum[j]:
            sum[i], sum[j] = sum[j], sum[i]
            data[i], data[j] = data[j], data[i]
        if sum[i] == sum[j]:
            if data[i][0] > data[j][0]:
                data[i], data[j] = data[j], data[i]
print(data)