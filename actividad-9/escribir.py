class DatosMeteorologicos:

    def __init__(self, nombre_archivo:str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, "w") as archivo:
            for linea in archivo:
                campos = linea.split("-")

                nombre_estacion = campos[0]
                latitud = float(campos[1])
                longitud = float(campos[2])
                fecha = campos[3]
                hora = campos[4]
                temperatura = float(campos[5])
                humedad = float(campos[6])
                presion = float(campos[7])
                velocidad_viento = float(campos[8])
                direccion_viento = campos[9]

                self.temperatura_total += temperatura
                self.humedad_total += humedad
                self.presion_total += presion
                self.velocidad_del_viento_total += velocidad_viento
                self.direccion_del_viento.append(direccion_viento) 


        self.temperatura_promedio = self.temperatura_total / len(self.direccion_del_viento)
        self.humedad_promedio = self.humedad_total / len(self.direccion_del_viento)
        self.presion_promedio = self.presion_total / len(self.direccion_del_viento)
        self.velocidad_viento_promedio = self.velocidad_viento_total / len(self.direccion_del_viento)
        self.direccion_predominante_del_viento = self.calcular_direccion_predominante()

        return (
            self.temperatura_promedio,
            self.humedad_promedio,
            self.presion_promedio,
            self.velocidad_viento_promedio,
            self.direccion_predominante_del_viento,
        )
    
    
    def convertir_direccion_a_grados(self, direccion:str) -> float:
        diccinoario_direcciones = {
            "N": 0, 
            "NNE": 22.5, 
            "NE": 45, 
            "ENE":67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }
        
        grados = diccinoario_direcciones.get(direccion)
        
        if grados is None:
            return None
        else:
            return grados
        
    def convertir_grados_a_direccion(self, grados: float) -> str:
        diccionario_grados = {
            0: "N",
            22.5: "NNE",
            45: "NE",
            67.5: "ENE",
            90: "E",
            112.5: "ESE",
            135: "SE",
            157.5: "SSE",
            180: "S",
            202.5: "SSW",
            225: "SW",
            247.5: "WSW",
            270: "W",
            292.5: "WNW",
            315: "NW",
            337.5: "NNW",
        }

        direccion = diccionario_grados.get(grados)

        if direccion is None:
            return None
        else:
            return direccion


    def calcular_direccion_predominante(self) -> str:
        direccion_grados = [self.convertir_dirrecion_a_grados(direccion) for direccion in self.direccion_del_viento]

        promedio_grados = sum(direccion_grados) / len(direccion_grados)

        return self.convertir_grados_a_dirrecion(promedio_grados)
        