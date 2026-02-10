package chapter09;

import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int sum = 0;

        int num = input.nextInt();
        sum = sum(sum, num);

        num = input.nextInt();
        sum = sum(sum, num);

        num = input.nextInt();
        sum = sum(sum, num);

        System.out.println("total: " + sum);
    }

    public static int sum(int sum, int num) {
        return sum += num;
    }

}
