import dic_work
import metodos_pruebas

salario_medio = 5922.60 

# promedio de toda la canasta en ambos canales 
precio_canasta_off = metodos_pruebas.suma_canasta(dic_work.lst_promedio_off)
precio_canasta_on = metodos_pruebas.suma_canasta(dic_work.lst_promedio_on)

# datos de consulta
    # ahorro por semana
ahorro_semana = precio_canasta_off - precio_canasta_on
    # ahorro anual
ahorro_anual = ahorro_semana * 12
    # promedio de gasto del salario por canasta en ambos canales
porciento_gasto_off_salario = metodos_pruebas.porciento_salario_gastado(precio_canasta_off, salario_medio)
porciento_gasto_on_salario = metodos_pruebas.porciento_salario_gastado(precio_canasta_on, salario_medio)
    # que porciento del salario se ahorra (restando el mas caro con el maas barato)
porciento_ahorro_salario = metodos_pruebas.porciento_positivo(porciento_gasto_off_salario, porciento_gasto_on_salario)
    # string para saber que canal es mas barato
canal_barato_precio = metodos_pruebas.canal_mas_barato(precio_canasta_off, precio_canasta_on)

