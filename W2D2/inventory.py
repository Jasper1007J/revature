inventory = {
    'apple':(10,0.5),
    'banana':(20,0.3)
}
inventory.update({'apple':(15,0.5)})
inventory['orange'] = (15,0.4)
total_val = 0
for k,v in inventory.items():
    total_val += v[0]*v[1]
print(inventory)

print("Total Value:",total_val)