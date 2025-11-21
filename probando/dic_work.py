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

