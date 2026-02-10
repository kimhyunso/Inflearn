package chapter13;

public class Main1 {

    public static void main(String[] args) {
        int numbers[] = {50, 40, 60, 10, 30, 80, 20, 100};

        for (int i = 1; i <= numbers.length - 2; i++) {
            for (int j = 0; j < numbers.length - i; j++) {
                if (numbers[j] > numbers[j + 1]) {
                    int temp = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = temp;
                }
            }
        }

        for (int number : numbers) {
            System.out.print(number + "\t");
        }

    }
}
