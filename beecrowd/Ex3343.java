import java.util.Scanner;

// problema com erro

public class Ex3343 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numMuralhas = 1;
    
        // inputs
        int numTitas = in.nextInt();
        int tamMuralhas = in.nextInt();
        String tamTitas = in.next();
        int tamP = in.nextInt();
        int tamM = in.nextInt();
        int tamG = in.nextInt();
    
        // creating a titan vector
        int[] titas = new int[numTitas];
    
        for (int i = 0; i < numTitas; i++){
            if (tamTitas.charAt(i) == 'P'){
                titas[i] = tamP;
            } else if (tamTitas.charAt(i) == 'M'){
                titas[i] = tamM;
            } else{
                titas[i] = tamG;
            }
        }

        int restante = tamMuralhas;
        int i = 0;
        while (i < numTitas) {
            if (titas[i] <= restante) {
                restante -= titas[i];
                i++;
            } else {
                numMuralhas++;
                restante = tamMuralhas;
            }
        }

        System.out.println(numMuralhas);
        in.close();
    }
}