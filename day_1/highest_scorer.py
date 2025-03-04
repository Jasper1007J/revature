# dictionary contains names as keys and scores as values.
# Return the name and score of the highest scorer.

dic = {
    "John": 100,
    "Alice": 85,
    "Bob": 92,
    "Charlie": 98
}

max_score = max(dic.values())
for k,v in dic.items():
    if v == max_score:
        print(k,v)
        break