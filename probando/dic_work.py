import json 
import metodos_pruebas
from collections import defaultdict
import os

#------------------------Json del Salario--------------------------------------------------------------------------------------
ruta_json_1 = os.path.join(os.path.dirname(__file__), "salario.json")
with open(ruta_json_1, "r", encoding="utf-8") as f:
    salario_js = json.load(f)

lst_salarios = [] # lista con los salarios por trabajo 
for value in salario_js["salario_por_empleo"].values():
    lst_salarios.append(value)

# ------------------------------------------json de las mypimes-----------------------------------------------------------------
ruta_json_2 = os.path.join(os.path.dirname(__file__), "prueba.json")
with open(ruta_json_2, "r", encoding="utf-8") as f:
    mypimes_js = json.load(f)

#cordenadas de la UH
uh_cor = [23.136326, -82.382190]
# dic de listas con los precios por producto
dic_precio_productos = defaultdict(list) 
#dic di listas de cordenadas pos mypime
dic_pimes_cor = defaultdict(list)

# desencapsular los precios por producto
for item in mypimes_js:
    dic_pimes_cor[item["name"]].append(float(item["latitude"]))
    dic_pimes_cor[item["name"]].append(float(item["length"]))
    for key, value in item["products"].items():
        dic_precio_productos[key].append(value)

print(dic_pimes_cor)

# lista con los promedios de precios de venta por producto
lst_promedio_venta = []  
for value in dic_precio_productos.values():
    lst_promedio_venta.append(metodos_pruebas.promedio(value))

# lista de productos
lst_productos = metodos_pruebas.productos(dic_precio_productos)








