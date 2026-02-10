package chapter11;

import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        final int pay = 1000;
        int result = pay;
        int age = input.nextInt();

        if (age >= 0 && age <= 3) {
            result = 0;
            System.out.println("영유아 요금: " + result);
        } else if (age <= 13) {
            result = (int) (result * 0.5);
            System.out.println("어린이 요금: " + result);
        } else if (age <= 19) {
            result = (int) (result * 0.75);
            System.out.println("청소년 요금: " + result);
        } else {
            System.out.println("성인 요금: " + result);
        }




        if (age > 14) {
            if (age <= 19) {
                result = (int) (result * 0.75);
                System.out.println("청소년 요금: " + result);
            } else {
                System.out.println("성인 요금: " + result);
            }
        } else {
            if (age >= 0 && age <= 3) {
                result = 0;
                System.out.println("영유아 요금: " + result);
            } else {
                result = (int) (result * 0.5);
                System.out.println("어린이 요금: " + result);
            }
        }

    }
}
