import json
import os
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from IPython.display import Markdown 
import textwrap
#--------------------------------------------METHODS---------------------------------------------------
#--------Do The Percent Whit A List--------
def open_json(js: str) -> list[dict]:
    route = os.path.join(os.path.dirname(__file__), js)
    with open(route, "r", encoding = "utf-8") as f:
        return json.load(f)

def percent_lst(lst: list[float]) -> float:
    if len(lst) > 0:
        v_sum = 0
        for x in lst:
            v_sum += x
        return v_sum/(len(lst)-1)
    else: return 0

def media_lst(lst: list[float]) -> float:
    lst.sort()
    return lst[len(lst)//2]
#--------------------------------------------SALARY----------------------------------------------------
js_salary = open_json("salary.json")

#-------------------------------------------MYPIMES---------------------------------------------------
js_mypimes = open_json("mypimes.json")

#--------Mypimes Cordenades---------------
dic_mypimes_cordenades = {}

for item in js_mypimes:
    if item["name"] not in dic_mypimes_cordenades:
        dic_mypimes_cordenades[item["name"]] = []
    dic_mypimes_cordenades[item["name"]].append(item["latitude"])
    dic_mypimes_cordenades[item["name"]].append(item["length"])

#--------------------------------------------FOOD----------------------------------------------------
js_productos = open_json("products.json")

#--------Products Price In Mypimes Percent-----------
dic_products_percent = {}
#-------list of solid products prices--------
lst_solids = []
#------list of liquids product prices--------
lst_liquids = []

for product in js_productos:
    if product["product"] not in dic_products_percent.keys():
        dic_products_percent[product["product"]] = []
    for x in product["price"].values():
        dic_products_percent[product["product"]].append(x)

for key, value in dic_products_percent.items():
    dic_products_percent[key] = percent_lst(value)

for dic in js_productos:
    if dic["clasification"] == "solido":
        lst_solids.append(dic_products_percent[dic["product"]])
    else:
        lst_liquids.append(dic_products_percent[dic["product"]]) 

#--------Price Of 1 Meal (1 Solid + 1 Liquid) Month---------------
v_meal = percent_lst(lst_liquids) + percent_lst(lst_solids)

#------------------------------------------TRANSPORT------------------------------------------------
js_transport = open_json("transport_routes.json")

dic_transport_routs = {}

for item in js_transport:
    dic_transport_routs[f"{item["via"]}/{item["name"]}/{item["vehiculo"]}"] = item["costo"]

v_transport = percent_lst(list(dic_transport_routs.values()))

#------------------------------------------GRAPHICS-------------------------------------------------
def localizacion():
    # ---------- 1. EXTRACCIÓN DE COORDENADAS ----------
    nombres, latitudes, longitudes = zip(*[(nombre, lat, lon)
                                        for nombre, (lat, lon) in dic_mypimes_cordenades.items()])
    latitudes  = np.array(latitudes)
    longitudes = np.array(longitudes)

    # ---------- 2. PUNTO DE REFERENCIA (UNIVERSIDAD) ----------
    lat_centro, lon_centro = 23.136326, -82.382190

    # ---------- 3. FUNCIÓN HAVERSINE EN METROS ----------
    def haversine_metros(lat1, lon1, lat2, lon2):
        R = 6371000
        phi1, phi2 = np.radians(lat1), np.radians(lat2)
        dphi   = np.radians(lat2 - lat1)
        dlambda= np.radians(lon2 - lon1)
        a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
        return 2 * R * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distancia_m = np.array([haversine_metros(lat_centro, lon_centro, lat, lon)
                            for lat, lon in zip(latitudes, longitudes)])

    # ---------- 4. DEFINICIÓN DE ZONAS CONCÉNTRICAS ----------
    zonas_m = [(0, 500), (500, 1000), (1000, 1500), (1500, 2000), (2000, 2500)]

    colores_zona = {
        500:  "rgba(54, 92, 160, 0.8)",
        1000: "rgba(125, 107, 182, 0.8)",
        1500: "rgba(195, 123, 157, 0.8)",
        2000: "rgba(220, 70, 90, 0.8)",
        2500: "rgba(240, 50, 50, 0.8)",
    }

    # ---------- 5. INICIALIZACIÓN DE LA FIGURA ----------
    fig = go.Figure()

    # ---------- 6. CÍRCULOS (SEMICÍRCULO ESTE) Y PUNTOS DE HOVER ----------
    angulos_circulo = np.linspace(-np.pi/2, np.pi/2, 200)   # solo derecha
    desplazamientos_x = [300, 900, 1500, 2100, 2700]        # 5 zonas

    for i, (radio_min, radio_max) in enumerate(reversed(zonas_m)):
        en_zona = np.where((distancia_m >= radio_min) & (distancia_m < radio_max))[0]
        en_zona_ordenado = sorted(en_zona, key=lambda idx: distancia_m[idx])

        texto_hover = "<br>".join(f"{nombres[idx]} — {distancia_m[idx]:.0f} m"
                            for idx in en_zona_ordenado)

        color_base = colores_zona[radio_max]

        # semicírculo Este
        fig.add_trace(go.Scatter(
            x=radio_max * np.cos(angulos_circulo),
            y=radio_max * np.sin(angulos_circulo),
            fill="toself",
            line=dict(color=color_base),
            showlegend=False
        ))

        # punto de referencia con hover
        fig.add_trace(go.Scatter(
            x=[desplazamientos_x[4 - i]],
            y=[2700],
            mode="markers+text",
            marker=dict(size=12, color=color_base),
            text=[f"{radio_min}-{radio_max} m"],
            textposition="bottom center",
            hovertemplate=f"<b>{radio_min}-{radio_max} m</b><br><br>{texto_hover}<extra></extra>",
            hoverlabel=dict(font=dict(color="white")),
            showlegend=False
        ))

    # ---------- 7. MARCADOR CENTRAL (UNIVERSIDAD) ----------
    fig.add_trace(go.Scatter(
        x=[0],
        y=[0],
        mode="markers+text",
        marker=dict(size=20, color="black"),
        text=["UH"],
        textposition="top right",
        textfont=dict(color="black"),
        showlegend=False
    ))

    # ---------- 8. CONFIGURACIÓN FINAL ----------
    fig.update_layout(
        title="Zonas de cercanía respecto a la UH (0–2500 m) – lado Este",
        xaxis=dict(title="Distancia Este (m)", range=[0, 2900]),
        yaxis=dict(title="Distancia Norte-Sur (m)", range=[0, 2900]),
        showlegend=False
    )

    fig.show()

def productos():
    categoria, valor = zip(*[(key, value) for key, value in dic_products_percent.items()])

    plt.figure(figsize=(8, 4))
    plt.plot(categoria, valor, color="#365C9C", marker='o', linestyle='-')

    plt.xlabel("productos")
    plt.ylabel("precio")
    plt.title("precios de productos")
    plt.ylim(150, 500)          # Y desde 50 hasta 500
    plt.tight_layout()
    plt.show()

def transporte():
    tabla = "| via | nombre | vehículo | costo (CUP) |\n"
    tabla += "|-----|--------|----------|------------|\n"

    for item in js_transport:
        tabla += f"| {item['via']} | {item.get('name', '')} | {item['vehiculo']} | {item['costo']:.2f} |\n"

    Markdown(tabla)

def gasto_mensual():
    meses_dias = {
        "Ene": 20, "Feb": 20, "Mar": 21, "Abr": 17,
        "May": 22, "Jun": 20, "Jul": 0,  "Ago": 0,
        "Sep": 17, "Oct": 21, "Nov": 20, "Dic": 15
    }

    v = v_meal + v_transport

    meses = list(meses_dias.keys())
    dias  = list(meses_dias.values())
    # gasto mensual = días * v
    gasto = [d * v for d in dias]

    # ---------- gráfico ----------
    plt.figure(figsize=(10, 5))
    barras = plt.bar(meses, dias, color="steelblue")

    # texto con gasto encima
    for barra, g in zip(barras, gasto):
        plt.text(barra.get_x() + barra.get_width()/2,
                barra.get_height() + 0.3,
                str(g),
                ha="center", va="bottom")

    plt.xlabel("Meses")
    plt.ylabel("Días lectivos")
    plt.title("Gasto universitario")
    plt.ylim(0, max(dias) + 5)
    plt.tight_layout()
    plt.show()

def trabajos():

    # ---------- nombres cortos (opcional) ----------
    sectores = [textwrap.fill(k, 30) for k in js_salary.keys()]
    salarios = list(js_salary.values())
    colores = ['crimson' if s < mi_valor else 'lightblue' for s in salarios]

    # ---------- figura más ALTA ----------
    plt.figure(figsize=(16, 14))          # 14 pulgadas de alto
    plt.barh(range(len(sectores)), salarios, color=colores)
    plt.axvline(mi_valor, color='black', linestyle='--', linewidth=2,
                label=f'Mi valor fijo: {mi_valor:,.0f}')

    plt.yticks(range(len(sectores)), sectores, fontsize=10)
    plt.xlabel('Salario medio (CUP)')
    plt.title('¿Dónde está mi valor?')
    plt.legend()
    plt.tight_layout()
    plt.show()
#---------------------------------------------------------------------------------------------------------------

def genera_catalogo_unificado():
    """
    Lee 'mypimes.json' (mismo directorio) y crea 'productos_unificados.json'
    con la estructura solicitada sin recibir ni devolver parámetros.
    """
    # 1. Cargar datos
    with open("mypimes.json", "r", encoding="utf-8") as f:
        js_mypimes = json.load(f)

    # 2. Construir índice
    product_index = {}
    for tienda in js_mypimes:
        nombre = tienda["name"]
        for prod, precio in tienda["products"].items():
            if prod not in product_index:
                product_index[prod] = {"clasificacion": "", "precio": {}}
            product_index[prod]["precio"][nombre] = precio

    # 3. Convertir a lista de diccionarios
    catalogo = [
        {"producto": k, "clasificacion": v["clasificacion"], "precio": v["precio"]}
        for k, v in product_index.items()
    ]

    # 4. Guardar resultado
    with open("productos_unificados.json", "w", encoding="utf-8") as f_out:
        json.dump(catalogo, f_out, ensure_ascii=False, indent=2)


