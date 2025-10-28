def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0

def porciento_salario_gastado(parte, total):
    if parte==total: return 0
    elif parte>total: 
        return round((parte*100)/total), "no me da la vidaaaa"
    else:
        return round((parte*100)/total)
    