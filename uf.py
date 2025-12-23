import os
import json

ruta_json_2 = os.path.join(os.path.dirname(__file__), "mypimes_selected.json")
with open(ruta_json_2, "r", encoding="utf-8") as f:
    mypimes_js = json.load(f)

lst=[]
for item in mypimes_js:
    lst.append(item["evidence"])

def crear_carpetas_desde_lista(lista_nombres, ruta_base):
    
    if not os.path.exists(ruta_base):
        print(f"La ruta base no existe: {ruta_base}")
        return

    for nombre in lista_nombres:
        ruta_carpeta = os.path.join(ruta_base, nombre)
        try:
            os.makedirs(ruta_carpeta, exist_ok=True)
            print(f"Carpeta creada o ya existente: {ruta_carpeta}")
        except Exception as e:
            print(f"Error al crear la carpeta '{nombre}': {e}")

# Ejemplo de uso
if __name__ == "__main__":
    nombres = lst
    ruta = "C:\\Users\\pc\\Desktop\\repos\\IP-ICD-Project\\New folder"  # Cambia esto por tu ruta real
    crear_carpetas_desde_lista(nombres, ruta)