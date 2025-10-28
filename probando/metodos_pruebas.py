def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0

def de_dic_a_lst(dicc):
    lst = [x for x in dicc.values()]
    return lst