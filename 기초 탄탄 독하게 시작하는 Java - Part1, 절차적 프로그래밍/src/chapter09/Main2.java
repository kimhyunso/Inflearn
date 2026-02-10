package chapter09;

import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int temp;

        x = x + y;
        y = x - y;
        x = x - y;

        System.out.printf("a:%d, b:%d\n", x, y);


        temp = x;
        x = y;
        y = temp;

        System.out.printf("a:%d, b:%d", x, y);
    }

}
