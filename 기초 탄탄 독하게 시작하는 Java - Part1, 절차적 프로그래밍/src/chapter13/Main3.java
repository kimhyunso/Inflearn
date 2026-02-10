package chapter13;

public class Main3 {

    public static void main(String[] args) {
        int array[][] = {
            {10, 20, 30, 0},
            {40, 50, 60, 0},
            {0, 0, 0, 0}
        };
        int colSum, rowSum = 0;

        for (int i = 0; i < array.length; i++) {
            colSum = 0;
            for (int j = 0; j < array[i].length - 1; j++) {
                rowSum += array[i][j];
                colSum += array[j][i];
            }
            array[i][array[i].length - 1] = rowSum;
            array[array.length - 1][i] = colSum;
        }

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
