import json 
import metodos_pruebas

with open("prueba.json", "r") as f:
    jason=json.load(f)

for item in jason:
    for i in item.keys():
        if i == "products":
            metodos_pruebas.de_dic_a_lst(i) 