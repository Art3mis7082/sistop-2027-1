import java.util.Scanner; // 1. Importar la herramienta

public class hola {
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.print("Introduce tu nombre: ");
        
        String nombre = teclado.nextLine();
        System.out.println("Hola " + nombre);

        teclado.close();
    }
}