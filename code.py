# metodo de promedio
def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0
    
l=[1,2,3,4]
print(promedio(l))

# metodo del porciento % = (Parte*100)/Todo
def porciento():
    return