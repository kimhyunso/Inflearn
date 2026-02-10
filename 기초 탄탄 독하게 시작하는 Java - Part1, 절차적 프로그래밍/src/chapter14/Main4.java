package chapter14;

import java.util.Scanner;

public class Main4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("숫자(1-10)를 입력해주세요.");
        int number = Integer.parseInt(input.next());
        if (number < 0 || number > 10) {
            number = 1;
        }
        int result = factorial(number);

        System.out.print("결과물: " + result);
    }

    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
