import json
import os
#--------------------------------------------METHODS---------------------------------------------------
#--------Do The Percent Whit A List--------
def percent_lst(lst: list[float]) -> float:
    if len(lst) > 0:
        v_sum = 0
        for x in lst:
            v_sum += x
        return v_sum/(len(lst)-1)
    else: return 0

def media_lst(lst):
    lst.sort()
    return lst[len(lst)//2]
#--------------------------------------------SALARY----------------------------------------------------
route_salary = os.path.join(os.path.dirname(__file__), "salary.json")
with open(route_salary, "r", encoding = "utf-8") as f:
    js_salary = json.load(f)

#--------Salary List------------
lst_salary = []

for value in js_salary.values():
    lst_salary.append(value)

#--------Salary Percent Variable----------
v_salary_percent = percent_lst(lst_salary)
#-------------------------------------------MYPIMES---------------------------------------------------
route_mypime = os.path.join(os.path.dirname(__file__), "mypimes.json")
with open(route_mypime, "r", encoding = "utf-8") as f:
    js_mypimes = json.load(f)

#--------Products Price In Mypimes Percent-----------
dic_products_percent = {}
#--------Mypimes Cordenades---------------
dic_mypimes_cordenades = {}

for item in js_mypimes:
    if item["name"] not in dic_mypimes_cordenades:
        dic_mypimes_cordenades[item["name"]] = []
    dic_mypimes_cordenades[item["name"]].append(item["latitude"])
    dic_mypimes_cordenades[item["name"]].append(item["length"])
    for key, value in item["products"].items():
        if key not in dic_products_percent:
            dic_products_percent[key] = []
        dic_products_percent[key].append(value)

for key, value in dic_products_percent.items():
    dic_products_percent[key] = percent_lst(value)
#--------------------------------------------FOOD----------------------------------------------------
#--------Types Of Products--------
lst_solids = ["pizza", "galleta", "pan"]
lst_liquids = ["refresco limon", "energizante", "coca cola", "cerveza", "jugo"]

for x in range(len(lst_solids )):
    lst_solids [x] = dic_products_percent[lst_solids [x]]

for x in range(len(lst_liquids)):
    lst_liquids[x] = dic_products_percent[lst_liquids[x]]

#--------Price Of 1 Meal (1 Solid + 1 Liquid)---------------
v_meal = percent_lst(lst_solids ) + percent_lst(lst_liquids)
#--------Lifestyles If You Only Have A Snack---------
v_ls_minimalist = 22 * v_meal
#--------Lifestyle If You Have Snacks And Lunch 3 Times A Week------------
v_ls_comfortable = (22 * v_meal) + (12 * v_meal)
#--------Lifestyle If You Have Snacks And Lunch Everyday-----------
v_ls_luxurious = 22 * (2 * v_meal)
#------------------------------------------LIFESTYLES------------------------------------------------



