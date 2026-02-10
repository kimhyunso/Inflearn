package chapter13;

public class Main7 {
    public static void main(String[] args) {
        int [][] numbers = new int[5][5];
//        int length = 9;
        int x = -1, y = 0, cnt = 0;
        int direction = 1;
//        boolean flag = true;

//        for (int length = 9; length > 0; length -= 2) {
//            if (flag) {
//                for (int i = 0; i < length; i++) {
//                    if (i < length / 2 + 1)
//                        ++x;
//                    else
//                        ++y;
//
//                    numbers[y][x] = ++cnt;
//                }
//            } else {
//                for (int i = 0; i < length; i++) {
//                    if (i < length / 2 + 1)
//                        --x;
//                    else
//                        --y;
//
//                    numbers[y][x] = ++cnt;
//                }
//            }
//            flag = !flag;
//        }

        for (int length = 9; length > 0; length -= 2) {
            for (int i = 0; i < length; i++) {
                if (i < length / 2 + 1)
                    x += direction;
                else
                    y += direction;

                numbers[y][x] = ++cnt;
            }
            direction = -direction;
        }

        for (int i = 0; i < numbers.length; i++) {
            for (int r = 0; r < numbers[0].length; r++) {
                System.out.print(numbers[i][r] + "\t");
            }
            System.out.println();
        }
    }
}
