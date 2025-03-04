import re 

def getPattern(text):
    return re.sub(r"[a-zA-Z.]",' ', text)

text = "The event is scheduled for 2023-10-15 and 2023-11-20."
res = list(map(str,getPattern(text).split()))
print(res)