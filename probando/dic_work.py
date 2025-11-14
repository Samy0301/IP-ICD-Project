import json 
import metodos_pruebas
from collections import defaultdict
import os


# json de las mypimes
ruta_json = os.path.join(os.path.dirname(__file__), "prueba.json")
with open(ruta_json, "r", encoding="utf-8") as f:
    jason = json.load(f)

dic_precio_productos_off = defaultdict(list) # dic de listas con los precios offline por producto
print(dic_precio_productos_off)
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




# que productos tienen un mayor aumento entre todas las tiendas
dic_productos_mas_saltan = defaultdict(float)

for key, value in dic_precio_productos_off.items():
    rango = metodos_pruebas.mas_alto(value) - metodos_pruebas.mas_bajo(value)
    dic_productos_mas_saltan[key] = rango

print(dic_productos_mas_saltan)
for key, value in dic_precio_productos_on.items():
    rango = metodos_pruebas.mas_alto(value) - metodos_pruebas.mas_bajo(value)
    if key in dic_productos_mas_saltan.keys():
        if dic_productos_mas_saltan[key] > rango:
            dic_productos_mas_saltan[key] = rango

print(dic_productos_mas_saltan)