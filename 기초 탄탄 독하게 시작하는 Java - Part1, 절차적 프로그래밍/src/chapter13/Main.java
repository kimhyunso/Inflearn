package chapter13;

public class Main {

    public static void main(String[] args) {
        int numbers[] = {50, 40, 10, 30, 20};
        int max = 0;

        for (int i = 0; i < numbers.length; i++) {
            if (max < numbers[i]) {
                max = numbers[i];
            }
        }

        System.out.println(max);

        max = numbers[0];

        for (int i = 1; i < numbers.length; i++) {
            if (max < numbers[i]) {
                max = numbers[i];
            }
        }
        System.out.println(max);
    }
}
