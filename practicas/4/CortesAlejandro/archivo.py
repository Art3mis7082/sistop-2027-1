
nombre_archivo = "Hola.txt"
contenido = "Hola Mundo"

with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido)

print(f"El archivo '{nombre_archivo}' se ha creado con éxito.")