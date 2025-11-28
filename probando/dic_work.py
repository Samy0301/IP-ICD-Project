import json 
import metodos_pruebas
from collections import defaultdict
import os


# json de las mypimes
ruta_json = os.path.join(os.path.dirname(__file__), "prueba.json")
with open(ruta_json, "r", encoding="utf-8") as f:
    jason = json.load(f)

dic_precio_productos_off = defaultdict(list) # dic de listas con los precios offline por producto
# desencapsular los precios offline por producto
for item in jason:
    for key, value in item["products"].items():
        dic_precio_productos_off[key].append(value)

lst_promedio_off = []   # lista con los promedios de precios de venta de las mypimes por producto
for value in dic_precio_productos_off.values():
    lst_promedio_off.append(metodos_pruebas.promedio(value))


# json de las tiendas virtuales
ruta_json = os.path.join(os.path.dirname(__file__), "prueba_online.json")
with open(ruta_json, "r", encoding="utf-8") as f:
    jason1=json.load(f)

dic_precio_productos_on = defaultdict(list) # dic de listas con los precios online de cada producto

# desencapsular los precios online
for item in jason1:
    for key, value in item["products"].items():
        dic_precio_productos_on[key].append(value)

lst_promedio_on=[] # lista de promedios de precios de venta en tiendas virtuales por productos 
for value in dic_precio_productos_on.values():
    lst_promedio_on.append(metodos_pruebas.promedio(value))

# lista de productos
lst_productos = metodos_pruebas.productos(jason[0]['products'])

# Diff que productos hacen que la mas barata sea la mas barata
lst_diff=[]
for i in range(10):
    lst_diff.append(metodos_pruebas.diff(lst_promedio_off[i], lst_promedio_on[i]))


# rango de los productos en cada canal 
lst_rango_off=[]  # lista con los ragos de diferencia de precio por productos en tiendas

for value in dic_precio_productos_off.values():
    lst_rango_off.append(metodos_pruebas.rango(value))

lst_rango_on=[]  # lista con los ragos de diferencia de precio por productos en linea

for value in dic_precio_productos_on.values():
    lst_rango_on.append(metodos_pruebas.rango(value))

# riesgo de comprar en la tienda equivocada
dic_off_canasta = defaultdict(list)  # cada tienda fisica el total de hacer la compra ahi
precio_por_tienda_off = 0

for item in jason:
    for value in item["products"].values():
        precio_por_tienda_off += value
    dic_off_canasta[item["name"]].append(precio_por_tienda_off)
    precio_por_tienda_off = 0

min_entre_off = metodos_pruebas.tienda_cheap(dic_off_canasta) # total de comprar en la tienda mas barata

for key, value in dic_off_canasta.items():
    dic_off_canasta[key].append(metodos_pruebas.porciento_riesgo(min_entre_off, value[0]))


dic_on_canasta = defaultdict(list)  # cada tienda online el total de hacer la compra ahi
precio_por_tienda_on = 0

for item in jason1:
    for value in item["products"].values():
        precio_por_tienda_on += value
    dic_on_canasta[item["name"]].append(precio_por_tienda_on) 
    precio_por_tienda_on = 0

min_entre_on = metodos_pruebas.tienda_cheap(dic_on_canasta)

for key, value in dic_on_canasta.items():
    dic_on_canasta[key].append(metodos_pruebas.porciento_riesgo(min_entre_on, value[0]))

