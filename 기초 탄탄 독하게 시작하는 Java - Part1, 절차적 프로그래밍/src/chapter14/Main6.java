package chapter14;

import java.util.Scanner;

public class Main6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("세 정수를 입력해주세요: ");
        int array[] = new int[3];
        for (int i = 0; i < array.length; i++) {
            array[i] = input.nextInt();
        }
        int result = getMax(array);
        System.out.println("최대값: " + result);
    }

    public static int getMax(int array[]) {
        int max = array[0];
        for (int i = 0; i < array.length; i++) {
            if (max < array[i]) {
                max = array[i];
            }
        }
        return max;
    }
}
