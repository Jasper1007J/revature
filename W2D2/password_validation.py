import re 
pattern = r"[A-Za-z0-9!@#$%^&+=]{8,}"
res = re.fullmatch(pattern, "Password1!")
if res:
    print("True")
else:
    print("False")
