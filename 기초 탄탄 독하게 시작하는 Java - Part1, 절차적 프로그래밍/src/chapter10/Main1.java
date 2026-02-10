package chapter10;

import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {

        int data = 0x11223344;
        System.out.printf("%d\n", data);
        System.out.printf("%08X\n", data & 0xFFFF0000);
        System.out.printf("%08X\n", data | 0xFFFF0000);
        System.out.printf("%08X\n", data ^ 0xFFFF0000);
        System.out.printf("%08X\n", data ^ 0xFFFF0000);
        System.out.printf("%08X\n", ~data);


        Scanner input = new Scanner(System.in);

        int x = input.nextInt(), y = input.nextInt();
        int result = x + (~y + 1);
        System.out.println(result);
    }
}
