salario_medio = 5922.60 # salario medio en cuba 2025 => oficina nacional de estadistica e info de cuba (facebook)

# metodo de promedio
# para promediar cuanto cuesta en total comprar todos los productos
# se ingresa:
# 1er llamado:  lst(int) lst_int = precios de los productos en la mypime n = 0-n-1 y se van guardando en una lst "todas" se puede hacer con un while
# ultimo llamado:  con la lista "todas" este seria el costo de comprar offline, repetir con los precios de las tiendas online
def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0
    
l=[1,2,3,4]
#print(promedio(l))

# metodo del porciento % = (Parte*100)/Todo  
# para ver cuanto de tu salario inviertes mensualmente en comida
# se ingresa int parte = promedio de cuanto cuesta comprar todos los productos, int total = salario
def porciento_salario_gastado(parte, total):
    if parte==total: return 0
    elif parte>total: 
        return round((parte*100)/total), "no me da la vidaaaa"
    else:
        return round((parte*100)/total)
    
#print(porciento_salario_gastado(9000, salario_medio))

