import json 
import metodos_pruebas

salario_medio = 5922.60 
with open("C:\\Users\\pc\\Desktop\\CD\\repos\\IP-ICD-Project\\probando\\prueba.json", "r", encoding="utf-8") as f:
    jason=json.load(f)

lst_p1=[]
lst_p2=[]
lst_p3=[]
lst_p4=[]
lst_p5=[]
lst_p6=[]
lst_p7=[]
lst_p8=[]
lst_p9=[]
lst_p10=[]
for item in jason:
    lst_p1.append(item["products"]["1"])
    lst_p2.append(item["products"]["2"])
    lst_p3.append(item["products"]["3"])
    lst_p4.append(item["products"]["4"])
    lst_p5.append(item["products"]["5"])
    lst_p6.append(item["products"]["6"])
    lst_p7.append(item["products"]["7"])
    lst_p8.append(item["products"]["8"])
    lst_p9.append(item["products"]["9"])
    lst_p10.append(item["products"]["10"])

lst=[lst_p1, lst_p2, lst_p3, lst_p4, lst_p5, lst_p6, lst_p7, lst_p8, lst_p9, lst_p10]
print(lst)
lst_promedio_off=[]
for i in lst:
    lst_promedio_off.append(metodos_pruebas.promedio(i))


with open("C:\\Users\\pc\\Desktop\\CD\\repos\\IP-ICD-Project\\probando\\prueba_online.json", "r", encoding="utf-8") as f:
    jason1=json.load(f)

l_p1=[]
l_p2=[]
l_p3=[]
l_p4=[]
l_p5=[]
l_p6=[]
l_p7=[]
l_p8=[]
l_p9=[]
l_p10=[]
for item in jason1:
    l_p1.append(item["products"]["1"])
    l_p2.append(item["products"]["2"])
    l_p3.append(item["products"]["3"])
    l_p4.append(item["products"]["4"])
    l_p5.append(item["products"]["5"])
    l_p6.append(item["products"]["6"])
    l_p7.append(item["products"]["7"])
    l_p8.append(item["products"]["8"])
    l_p9.append(item["products"]["9"])
    l_p10.append(item["products"]["10"])

lst1=[l_p1, l_p2, l_p3, l_p4, l_p5, l_p6, l_p7, l_p8, l_p9, l_p10]
print(lst1)
lst_promedio_on=[]
for i in lst1:
    lst_promedio_on.append(metodos_pruebas.promedio(i))






