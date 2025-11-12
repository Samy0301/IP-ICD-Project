import dic_work
import metodos_pruebas

salario_medio = 5922.60 

# promedio de toda la canasta en ambos canales 
promedio_canasta_off = metodos_pruebas.promedio(dic_work.lst_promedio_off)
promedio_canasta_on = metodos_pruebas.promedio(dic_work.lst_promedio_on)

# datos de consulta
    # promedio de gasto del salario por canasta en ambos canales
porciento_gasto_off_salario = metodos_pruebas.porciento_salario_gastado(promedio_canasta_off, salario_medio)
porciento_gasto_on_salario = metodos_pruebas.porciento_salario_gastado(promedio_canasta_on, salario_medio)
    # que porciento del salario se ahorra (restando el mas caro con el maas barato)
porciento_ahorro_salario = metodos_pruebas.porciento_positivo(porciento_gasto_off_salario, porciento_gasto_on_salario)
    # string para saber que canal es mas barato
canal_barato_precio = metodos_pruebas.canal_mas_barato(promedio_canasta_off, promedio_canasta_on)
    # producto que mas y menos rango de aumento de precio tienen
producto_mayor_rango, producto_menor_rango = metodos_pruebas.mayor_rango(dic_work.dic_productos_mas_saltan)

print(producto_mayor_rango)
print(producto_menor_rango)