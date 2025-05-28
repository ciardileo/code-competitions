/* 
 Para cada caso de teste, fazer um while enquanto anos < 100 ou população A < B
 a cada loop, realizar o crescimento de cada população (obs: o crescimento é inteiro)
 */

import java.util.Scanner;

public class Ex1160{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // número de casos de teste

        // declaração dos vetores
        int[] populacaoA = new int[N];
        int[] populacaoB = new int[N];
        double[] taxaA = new double[N];
        double[] taxaB = new double[N];

        // lendo cada caso
        for (int i = 0; i < N; i++){
            populacaoA[i] = in.nextInt();
            populacaoB[i] = in.nextInt();
            taxaA[i] = in.nextDouble() / 100;
            taxaB[i] = in.nextDouble() / 100;
        }

        int anos;
        for (int i = 0; i < N; i++){
            anos = 0;

            while (populacaoA[i] <= populacaoB[i]){
                if (anos >= 100){
                    System.out.println("Mais de 1 seculo.");
                    break;
                }

                populacaoA[i] *= 1 + taxaA[i];
                populacaoB[i] *= 1 + taxaB[i];
                anos += 1;
            }

            if (populacaoA[i] > populacaoB[i]){
                System.out.println(anos + " anos.");
            }
        }

        in.close();

    }
}