def calc_employee(prod, rate, prize):
    salary = (float(prod) * float(rate))
    result = salary + (salary * (float(prize) / 100)) #employee remuneration + (bonus)
    return round(result, 2)

def func_com(prev_el, el):
    return prev_el * el

def fact(n):
    result = 1
    for elem in range(2, n+1):
        result = result * elem
        yield result
