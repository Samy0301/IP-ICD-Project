import codes

def menor_alimento(lst: list[float]) -> float:
    x = 10**32
    for i in lst:
        if x>i: x=i
    return x

def mayor_alimento(lst: list[float]) -> float:
    x = 0
    for i in lst:
        if x<i: x=i
    return x

def transport(js):
    for dic in js:
        if dic["via"] == "estatal": transporte = dic["costo"]
    return transporte

def comida(js, dias):
    solido_less = []
    solido_more = []
    liquido_less = []
    liquido_more = []
    for dic in js:
        if dic["clasification"] == "solido":
            solido_less.append(menor_alimento(list(dic["price"].values())))
            solido_more.append(mayor_alimento(list(dic["price"].values())))
        else:
            liquido_less.append(menor_alimento(list(dic["price"].values())))
            liquido_more.append(mayor_alimento(list(dic["price"].values())))

    solido_less = menor_alimento(solido_less)
    liquido_less = menor_alimento(liquido_less)
    solido_more = mayor_alimento(solido_more)
    liquido_more = mayor_alimento(liquido_more)

    v_comida_less = solido_less+liquido_less
    v_comida_more = solido_more+liquido_more

    v_comida_less = v_comida_less * codes.sum_lst(dias.values())
    v_comida_more = v_comida_more * codes.sum_lst(dias.values())

    return (v_comida_less, v_comida_more)

comida_l, comida_m = comida(codes.js_productos, codes.dic_shool_days)

total_less = (comida_l + transport(codes.js_transport)) - (200 * 12)
total_more = (comida_m + transport(codes.js_transport)) - (200 * 12)

print(total_less, total_more)