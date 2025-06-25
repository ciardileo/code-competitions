package exercises.neps;

import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Posição: ");
        int x = in.nextInt();
        int y = in.nextInt();

        int[][] combinacoes = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1},
            {1, 1},
            {-1, -1},
            {1, -1},
            {-1, 1}
        };

        for (int[] linha: combinacoes){
            System.out.println((x + linha[0]) + " " + (y + linha[0]));
        }

        in.close();
    }

}
