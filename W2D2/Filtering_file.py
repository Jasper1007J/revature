import re

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
s = ["john@gmail.com","invalid-email","example@ex.org","example@com"]
res = []
for email in s:
    if re.search(email_pattern,email):
        res.append(email)
print(res)