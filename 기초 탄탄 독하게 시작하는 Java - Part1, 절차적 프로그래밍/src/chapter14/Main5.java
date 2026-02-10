package chapter14;

import java.util.Scanner;

public class Main5 {
    public static void main(String[] args) {
        int score = getScore();
        if (score < 0)
            return;
        char grade = getGrade(score);
        System.out.println("학점: " + grade);
    }

    public static int getScore() {
        System.out.print("점수: ");
        Scanner input = new Scanner(System.in);
        int score = input.nextInt();
        if (score < 0 || score > 100) {
            System.out.println("ERROR: 점수범위가 부적절 합니다.");
            return -1;
        }
        return score;
    }

    public static char getGrade(int score) {
        if (score >= 90) return 'A';
        else if (score >= 80) return 'B';
        else if (score >= 70) return 'C';
        else if (score >= 60) return 'D';
        else return 'F';
    }
}
