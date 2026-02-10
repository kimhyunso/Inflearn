package chapter11;

import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int age = input.nextInt();
        final int pay = 1000;
        int result = pay;

        age = Math.min(20, age);
        age = Math.max(0, age);

        if (age < 20) {
            result = (int) (pay * 0.75);
        }

        System.out.println("나이: " + age + ", 최종요금: " + result);
    }
}
