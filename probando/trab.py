def promedio(lst_int):
    if len(lst_int) > 0:
        suma = 0
        for i in lst_int:
            suma += i
        return suma/(len(lst_int)-1)
    else:
        return 0
    

dic=[
    {"name":"si",
    "prod":{
        "1":7,
        "2":8
    }},

    {"name": "no", 
    "prod":{
        "1":4,
        "2":5
    }}]



lst1,lst2=[],[]
for item in dic:
        lst1.append(item["prod"]["1"])
        lst2.append(item["prod"]["2"])



print(lst1, lst2)

