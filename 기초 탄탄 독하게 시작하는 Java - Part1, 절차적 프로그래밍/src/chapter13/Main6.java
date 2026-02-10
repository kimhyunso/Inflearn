package chapter13;

public class Main6 {
    public static void main(String[] args) {
        int [][] numbers = new int[5][5];
        int count = 0;

        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers[0].length; j++) {
                //if (i % 2 == 0) {
                if ((i & 0x000000001) == 0x000000000) {
                    numbers[i][j] = ++count;
                } else {
                    numbers[i][numbers[0].length - 1 - j] = ++count;
                }
            }
        }

        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers[0].length; j++) {
                System.out.print(numbers[i][j] + "\t");
            }
            System.out.println();
        }

    }
}
