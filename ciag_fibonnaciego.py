def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    suma = 0
    for i in range(3, n+1):
        suma = elem_1 + elem_2
        elem_1, elem_2 = elem_2, suma
    return suma

fib(10)  #przykladowe sprawdzenie
