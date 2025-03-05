

def calculate(expression:str) -> float:
    try:
        res = eval(expression)
        return res
    except ZeroDivisionError:
        return "Division by zero is not possible, please try again"
    except Exception as e:
        return f"Error encountered: {str(e)}"
    