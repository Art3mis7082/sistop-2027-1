#include <stdio.h>

int main() {
    FILE *archivo = fopen("resultado.txt", "w");

    if (archivo == NULL) {
        printf("Error al crear el archivo.\n");
        return 1;
    }

    fprintf(archivo, "Archivo generado automáticamente por el programa.\n");
    fclose(archivo);

    printf("Se generó correctamente resultado.txt\n");

    return 0;
}
