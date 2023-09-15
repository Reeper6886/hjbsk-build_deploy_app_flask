def summation(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Both inputs should be numerical."

def subtraction(a, b):
    try:
        result = a - b
        return result
    except TypeError:
        return "Error: Both inputs should be numerical."

def multiplication(a, b):
    try:
        result = a * b
        return result
    except TypeError:
        return "Error: Both inputs should be numerical."
