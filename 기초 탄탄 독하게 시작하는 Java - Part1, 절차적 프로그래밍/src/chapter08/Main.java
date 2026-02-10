package chapter08;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("나이를 입력하세요: ");
        int age = input.nextInt();
        input.nextLine();

        System.out.print("이름을 입력하세요: ");
        String name = input.nextLine();

        System.out.printf("당신의 나이는 %d살이고 이름은 \'%s\'입니다.", age, name);
    }
}