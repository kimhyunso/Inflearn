package chapter11;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int x = input.nextInt();
        int y = input.nextInt();
        int z = input.nextInt();

        if (x > y && x > z) {
            System.out.println("MAX: " + x);
        } else if (y > x && y > z) {
            System.out.println("MAX: " + y);
        } else {
            System.out.println("MAX: " + z);
        }
    }

}
