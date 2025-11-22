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
    
def productos(dic):
    lst=[]
    for i in dic.keys():
        lst.append(i)
    return lst

def diff(off, on):
    return (off-on)/off*100

def porciento_positivo(n, m):
    return n-m if n>=m else m-n

def canal_mas_barato(n, m):
    if n==m:
        return "la misma mierda"
    return "off es mas barato" if n<m else "on es mas barato"

def rango(lst):
    menor=10**32
    mayor=0
    for i in lst:
        if i<menor:
            menor=i
        if i > mayor:
            mayor=i
    
    return mayor-menor

def convertir_tabla(dic, lst1, lst2):
    tabla = ""
    for i in range(10):
        tabla += f"| {dic[i]} | {lst1[i]} | {lst2[i]} |\n"
    return tabla

