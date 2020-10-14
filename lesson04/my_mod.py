def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return  # =return None

def hello(name):
    print(f"Hello, {name}")