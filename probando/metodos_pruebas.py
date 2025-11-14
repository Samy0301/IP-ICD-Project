def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0

def suma_canasta(lst):
    suma=0
    for i in lst:
        suma+=i
    return suma

def porciento_salario_gastado(parte, total):
    if parte==total: return 0
    elif parte>total: 
        return (parte*100)/total, 
    else:
        return (parte*100)/total
    

def porciento_positivo(n, m):
    return n-m if n>=m else m-n

def canal_mas_barato(n, m):
    if n==m:
        return "la misma mierda"
    return "off es mas barato" if n<m else "on es mas barato"

def mas_alto(lst):
    n = 0
    for i in lst:
        if i>n:
            n=i
    return n 

def mas_bajo(lst):
    n=10**32
    for i in lst:
        if i<n:
            n=i
    return n

def mayor_rango(dic):
    mayor = 0
    menor = 10**32
    prod_mayor = ""
    prod_menor=""
    for key, value in dic.items():
        if value>mayor:
            mayor=value
            prod_mayor=key
        if value< menor:
            menor=value
            prod_menor=key

    return prod_mayor, prod_menor
