package chapter10;

import java.util.Scanner;

public class Main4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int z = input.nextInt();

        int result = Math.max(Math.max(x, y), z);
        int max = (x > y ? x : y) > z ? (x > y ? x : y) : z;

        System.out.println("Max: " + result);
        System.out.println(max);

    }
}
