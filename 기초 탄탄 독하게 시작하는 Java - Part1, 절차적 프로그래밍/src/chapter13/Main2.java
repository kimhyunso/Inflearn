package chapter13;

public class Main2 {

    public static void main(String[] args) {
        int numbers[] = {50, 40, 60, 10, 30, 80, 20, 100};


        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[i] > numbers[j]) {
                    int temp = numbers[j];
                    numbers[j] = numbers[i];
                    numbers[i] = temp;
                }
            }
        }

        for (int num : numbers) {
            System.out.print(num + "\t");
        }

    }
}
