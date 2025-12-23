import json
import os
from collections import defaultdict
#--------------------------------------------METHODS---------------------------------------------------
#--------Do The Percent Whit A List--------
def percent_lst(lst: list[float]) -> float:
    if len(lst) > 0:
        v_sum = 0
        for x in lst:
            v_sum += x
        return v_sum/(len(lst)-1)
    else: return 0
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

#--------Product List-----------
lst_products = []
#--------Products Price Percent-----------
lst_products_percent = []
#--------Product Prices In Mypimes--------
dic_product_price = defaultdict(list)
#--------Mypimes Cordenades---------------
dic_mypimes_cordenades = defaultdict(list)

for item in js_mypimes:
    dic_mypimes_cordenades[item["name"]].append(item["latitude"])
    dic_mypimes_cordenades[item["name"]].append(item["length"])
    for key, value in item["products"].items():
        dic_product_price[key].append(value)
        if key not in lst_products:
            lst_products.append(key)

for value in dic_product_price.values():
    lst_products_percent.append(percent_lst(value))
#----------------------------------------DATA------------------------------------------------------
v_uh_cordenades = [23.136326, -82.382190]