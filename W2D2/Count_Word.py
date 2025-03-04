import re
def rmv(text):
    return re.sub(r'[^a-zA-Z]', ' ', text)

text = input().lower()
res = tuple(map(str,rmv(text).split()))
print(res)

my_dict = {}
for word in res:
   my_dict[word] = res.count(word)
print(my_dict)