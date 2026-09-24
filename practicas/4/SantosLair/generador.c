#include <stdio.h>
#include <string.h>
#include <windows.h>

void verificar_memoria_carpeta(const char *ruta_base) {
    char search_path[MAX_PATH];
    snprintf(search_path, sizeof(search_path), "%s\\*.*", ruta_base);

    WIN32_FIND_DATA find_file_data;
    HANDLE hFind = FindFirstFile(search_path, &find_file_data);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error: No se pudo abrir la carpeta o la ruta no existe (%s).\n", ruta_base);
        return;
    }

    printf("Analizando archivos en: %s\n", ruta_base);
    printf("-------------------------------------------------------------------\n");
    printf("%-45s | %15s\n", "Nombre de Archivo", "Tamaño (Bytes)");
    printf("-------------------------------------------------------------------\n");

    unsigned long long total_bytes = 0;
    int count = 0;

    do {
        // Omitir los directorios especiales '.' y '..'
        if (strcmp(find_file_data.cFileName, ".") == 0 || strcmp(find_file_data.cFileName, "..") == 0) {
            continue;
        }

        // Verificar si es un archivo (ignorando subcarpetas para el cálculo simple)
        if (!(find_file_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
            unsigned long long file_size = ((unsigned long long)find_file_data.nFileSizeHigh << 32) + find_file_data.nFileSizeLow;

            // Ajustar formato si el nombre es muy largo
            printf("%-45s | %15llu\n", find_file_data.cFileName, file_size);

            total_bytes += file_size;
            count++;
        }
    } while (FindNextFile(hFind, &find_file_data) != 0);

    FindClose(hFind);

    printf("-------------------------------------------------------------------\n");
    printf("Total de archivos: %d\n", count);
    printf("Memoria total ocupada: %llu bytes (%.2f KB / %.2f MB)\n",
           total_bytes,
           (double)total_bytes / 1024.0,
           (double)total_bytes / (1024.0 * 1024.0));
}

int main() {
    const char *carpeta = "C:\\Users\\Predator\\Documents\\Tareas\\Sistemas_Operativos\\sistop-2027-1";
    verificar_memoria_carpeta(carpeta);
    return 0;
}
