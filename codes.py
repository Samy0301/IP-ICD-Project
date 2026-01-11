import json
import os
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from IPython.display import Markdown 
import textwrap
#--------------------------------------------METHODS---------------------------------------------------
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

def sum_lst(lst: list[float]) -> float:
    v_sum = 0
    for x in lst:
        v_sum += x
    return v_sum

#-------------------------------------------MYPIMES---------------------------------------------------
js_mypimes = open_json("mypimes.json")

dic_mypimes_cordenades = {}

for item in js_mypimes:
    if item["name"] not in dic_mypimes_cordenades:
        dic_mypimes_cordenades[item["name"]] = []
    dic_mypimes_cordenades[item["name"]].append(item["latitude"])
    dic_mypimes_cordenades[item["name"]].append(item["length"])

#--------------------------------------------FOOD----------------------------------------------------
js_productos = open_json("products.json")

dic_products_percent = {}
lst_solids = []
lst_liquids = []
lst_solind_less = []
lst_liquids_less = []

for product in js_productos:
    if product["product"] not in dic_products_percent.keys():
        dic_products_percent[product["product"]] = []
    for x in product["price"].values():
        dic_products_percent[product["product"]].append(x)

for key, value in dic_products_percent.items():
    dic_products_percent[key] = percent_lst(value)

for dic in js_productos:
    if dic["clasification"] == "solido":
        if dic["prescindible"] == "no":
            lst_solind_less.append(dic_products_percent[dic["product"]])
        lst_solids.append(dic_products_percent[dic["product"]])
    else:
        if dic["prescindible"] == "no":
            lst_liquids_less.append(dic_products_percent[dic["product"]])
        lst_liquids.append(dic_products_percent[dic["product"]]) 

v_meal = percent_lst(lst_liquids) + percent_lst(lst_solids)
v_meal_less = percent_lst(lst_liquids_less) + percent_lst(lst_solind_less)
print(dic_products_percent.keys())
#------------------------------------------TRANSPORT------------------------------------------------
js_transport = open_json("transport_routes.json")

lst_transport_routs = []
lst_transport_routs_less = []

for item in js_transport:
    if item["vehiculo"] != "auto":
        lst_transport_routs_less.append(item["costo"])
    lst_transport_routs.append(item["costo"])


v_transport = percent_lst(lst_transport_routs)
v_transport_less = percent_lst(lst_transport_routs_less)

#------------------------------------------DATOS-------------------------------------------------------
dic_shool_days = {
    "Ene": 20, "Feb": 20, "Mar": 21, "Abr": 17,
    "May": 22, "Jun": 20, "Jul": 0,  "Ago": 0,
    "Sep": 17, "Oct": 21, "Nov": 20, "Dic": 15
}

lst_monthly_food = [d * v_meal for d in dic_shool_days.values()]
lst_monthly_transport = [d * v_transport for d in dic_shool_days.values()]
lst_monthly_total = [m + t for m, t in zip(lst_monthly_food, lst_monthly_transport)]
v_anual_total = sum_lst(lst_monthly_total)

lst_monthly_food_less = [d * v_meal_less for d in dic_shool_days.values()]
lst_monthly_transport_less = [d * v_transport_less for d in dic_shool_days.values()]
lst_monthly_total_less = [m + t for m, t in zip(lst_monthly_food_less, lst_monthly_transport_less)]
v_anual_total_less = sum_lst(lst_monthly_total_less)

v_anual_transport_less = sum_lst(lst_monthly_transport_less)
#--------------------------------------------SALARY----------------------------------------------------
js_salary = open_json("salary.json")

#------------------------------------------GRAPHICS-------------------------------------------------
def localization():
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


def products_percent():
    productos = list(dic_products_percent.keys())      # keys en orden
    precios   = list(dic_products_percent.values())    # values en orden

    # primeros 5 -> líquidos, resto -> sólidos
    n = len(productos)
    liquidos = precios[:5] + [0]*(n-5)   # mantener longitud
    solidos  = [0]*5 + precios[5:]       # 0 en líquidos, valor en sólidos

    # ---------- gráfico ----------
    plt.figure(figsize=(8, 4))
    plt.stackplot(productos, liquidos, solidos,
                labels=['Líquidos', 'Sólidos'],
                colors=['#f58518', '#4c78a8'],
                baseline='zero')

    plt.xlabel("Producto")
    plt.ylabel("Precio promedio (CUP)")
    plt.title("Precio promedio por categoría")
    plt.legend()
    plt.tight_layout()
    plt.show()


def transport_table():
    tabla = "| via | nombre | vehículo | costo (CUP) |\n"
    tabla += "|-----|--------|----------|------------|\n"

    for item in js_transport:
        tabla += f"| {item['via']} | {item.get('name', '')} | {item['vehiculo']} | {item['costo']:.2f} |\n"

    display(Markdown(tabla))


def monthly_expense():
    plt.figure(figsize=(16, 10))
    plt.bar(dic_shool_days.keys(), lst_monthly_food,      label='Meal',      color='steelblue')
    plt.bar(dic_shool_days.keys(), lst_monthly_transport, bottom=lst_monthly_food, label='Transport', color='orange')

    # etiqueta del total encima
    for i, t in enumerate(lst_monthly_total):
        plt.text(i, t + 0.3, f"{t:.1f}", ha='center', va='bottom')

    plt.xlabel("Meses")
    plt.ylabel("Importe (CUP)")
    plt.title("Gasto universitario mensual")
    plt.legend()
    plt.tight_layout()
    plt.show()


def works():
    sectores = [textwrap.fill(k, 25) for k in js_salary.keys()]
    salarios = [s * 12 for s in js_salary.values()]
    colores  = ['crimson' if s < v_anual_total else 'lightblue' for s in salarios]

    # ---------- figura MUY alargada ----------
    plt.figure(figsize=(16, 14))          # 20 pulgadas de alto
    plt.barh(range(len(sectores)), salarios, color=colores)
    plt.axvline(v_anual_total, color='k', ls='--', lw=2, label=f'Mi valor: {v_anual_total:,.0f}')

    plt.yticks(range(len(sectores)), sectores, fontsize=12)
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


