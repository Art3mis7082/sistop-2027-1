import sys

def main():
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
    else:
        nombre = "invitado"
    print(f"¡Hola, {nombre}! Bienvenido.")

if __name__ == "__main__":
    main()