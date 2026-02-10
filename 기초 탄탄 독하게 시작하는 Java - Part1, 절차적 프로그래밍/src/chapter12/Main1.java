package chapter12;


public class Main1 {
    public static void main(String[] args) {
        for (int i = 5; i > 0; i--) {

            for (int j = 0; j <= i - 2; j++) {
                System.out.print("\t");
            }

            for (int j = i; j <= 5; j++) {
                System.out.print("*\t");
            }
            System.out.println();
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (j < 4 - i)
                    System.out.print("\t");
                else
                    System.out.print("*\t");
            }
            System.out.println();
        }
    }
}
