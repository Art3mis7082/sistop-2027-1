from datetime import datetime

with open("practicas/4/ArcosAyax/salida.log", "w") as archivo:
    archivo.write(f"Programa ejecutado: {datetime.now()}\n")

print("Se genero salida.log")
