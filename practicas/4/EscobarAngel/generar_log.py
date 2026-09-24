from datetime import datetime

with open("salida.log", "a", encoding="utf-8") as archivo:
    archivo.write(f"Ejecucion: {datetime.now()}\n")

print("Archivo salida.log generado correctamente.")