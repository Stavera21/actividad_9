from escribir import DatosMeteorologicos

if __name__ == "__main__":
    datos_meteorologicos = DatosMeteorologicos("datos.txt")
    estadisticas = datos_meteorologicos.procesar_datos()

    print(f"Temperatura promedio: {estadisticas[0]}")
    print(f"Humedad promedio: {estadisticas[1]}")
    print(f"Presión promedio: {estadisticas[2]}")
    print(f"Velocidad del viento promedio: {estadisticas[3]}")
    print(f"Dirección predominante del viento: {estadisticas[4]}")