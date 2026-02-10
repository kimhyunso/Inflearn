package chapter14;

import java.util.Scanner;

public class LookupArray {
    public static void main(String[] args) {
        double[] rate = {
                0.9, 0.8, 0.75, 0.6, 0.5, 0.3, 0.1
        };

        Scanner input = new Scanner(System.in);
        int age = 1;
        int fee = 1000;
        try {
            age = Integer.parseInt(input.next());

            if (age < 0) {
                age = 1;
            } else if (age > 7) {
                age = 7;
            }

        } catch (Exception e) {
            System.out.println("잘 못된 입력입니다.");
        }


        System.out.printf("나이: %d, 할인전 금액: %d, 할인적용 금액: %d", age, fee, (int)(fee - rate[age - 1] * fee));
    }
}
