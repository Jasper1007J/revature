import re

def is_valid_expression(expression:str):
    pattern = r'^[\d+\-*/().\s]+$'
    s =  bool(re.match(pattern,expression))
    return s
