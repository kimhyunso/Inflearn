package chapter12;


public class Main2 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 4 - i; j++) {
                System.out.print("\t");
            }

            for (int j = 0; j < (i * 2) + 1; j++) {
                System.out.print("*\t");
            }
            System.out.println();
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5 + i; j++) {
                if (j < 4 - i)
                    System.out.print("\t");
                else
                    System.out.print("*\t");
            }
            System.out.println();
        }
    }
}
