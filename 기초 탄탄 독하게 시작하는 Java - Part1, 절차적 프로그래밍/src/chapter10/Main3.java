package chapter10;

import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        System.out.print("점수를 입력해주세요: ");
        Scanner input = new Scanner(System.in);

        int score = input.nextInt();
        score = Math.max(score, 0);
        score = Math.min(score, 100);

        String result = score >= 80 ? "합격" : "불합격";
        System.out.println(result);
    }
}
