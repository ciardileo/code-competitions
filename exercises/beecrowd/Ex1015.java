import java.io.IOException;
import java.util.Scanner;

public class Ex1015 {
        public static void main(String[] args) throws IOException {
            // Locale.setDefault(Locale.US);  // utiliza a formatação americana
            Scanner in = new Scanner(System.in);
            double x1, x2, y1, y2;

            x1 = in.nextDouble();
            y1 = in.nextDouble();
            x2 = in.nextDouble();
            y2 = in.nextDouble();

            double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

            System.out.printf("%.4f \n", distance);
            
            in.close();
        }
     
    }

