import sys

nombre = sys.argv[1] if len(sys.argv) > 1 else "usuario"
print(f"Hola, {nombre}")