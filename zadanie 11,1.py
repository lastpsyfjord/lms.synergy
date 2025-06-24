def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial_sequence(n):
    fact_n = factorial(n)
    total = factorial(fact_n)
    res_list = [total]
    current = total
    for k in range(fact_n, 1, -1):
        current = current // k
        res_list.append(current)
    return res_list