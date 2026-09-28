import java.util.ArrayList;
import java.util.Scanner;

public class zero{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        ArrayList<Integer> numeros = new ArrayList<Integer>();

        for (int i = 0; i < N; i++){
            int numero = in.nextInt();

            if (numero == 0){
                numeros.remove(numeros.size() - 1);
                continue;
            }

            numeros.add(numero);
        }

        int soma = 0;
        for (int x: numeros){
            soma += x;
        }

        System.out.println(soma);
        in.close();
    }
}