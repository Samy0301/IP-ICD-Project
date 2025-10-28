import json 
import metodos_pruebas

salario_medio = 5922.60 
with open("C:\\Users\\pc\\Desktop\\CD\\repos\\IP-ICD-Project\\probando\\prueba.json", "r", encoding="utf-8") as f:
    jason=json.load(f)

lst_promedio_todas=[]
for item in jason:
    for i in item.keys():
        if i == "products":
            lst=[x for x in item[i].values()]
            lst_promedio_todas.append(metodos_pruebas.promedio(lst)) 

promedio_offline=metodos_pruebas.promedio(lst_promedio_todas)

num, text = metodos_pruebas.porciento_salario_gastado(promedio_offline, salario_medio)
print(f"{num}% {text}")




