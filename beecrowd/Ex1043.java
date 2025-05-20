package beecrowd;

import java.util.Scanner;

public class Ex1043 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		double a, b, c;
		a = in.nextDouble();
		b = in.nextDouble();
		c = in.nextDouble();
		
		if (((a + b) > c) && ((b + c) > a) && ((a + c) > b)) {
			System.out.println("Perimetro = " + (a + b + c));
		} else {
			System.out.println("Area = " + ((a + b) / 2 * c));
		}

	}

}
