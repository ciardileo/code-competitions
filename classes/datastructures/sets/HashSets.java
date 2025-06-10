package datastructures.sets;
import java.util.HashSet;
import java.util.Scanner;

public class HashSets {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        Scanner in = new Scanner(System.in);

        int number = 0;

        while (number != -1) {
            System.out.print("Número: ");
            number = in.nextInt();
            set.add(number);
        }

        System.out.println("Total size: " + set.size());
        System.out.println(set);

        in.close();
    }
}
