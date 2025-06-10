import java.util.Scanner;
public class Ex1020 {
 
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int dias = in.nextInt();
        
        int anos = dias / 365;
        int meses = (dias % 365) / 30;
        int restoDias = (dias % 365) % 30;

        System.out.println(anos + " ano(s)");
        System.out.println(meses + " mes(es)");     
        System.out.println(restoDias + " dia(s)");
        
        in.close();
    }
 
}