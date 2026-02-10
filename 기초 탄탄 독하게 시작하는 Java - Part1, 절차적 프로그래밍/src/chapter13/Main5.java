package chapter13;

public class Main5 {
    public static void main(String[] args) {
        int [][] numbers = new int[5][5];
        int count = 1;

        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers[0].length; j++) {
                numbers[i][j] = count;
                count++;
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
