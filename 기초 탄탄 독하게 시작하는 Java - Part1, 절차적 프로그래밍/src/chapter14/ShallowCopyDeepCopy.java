package chapter14;

import java.util.Arrays;

public class ShallowCopyDeepCopy {
    public static void main(String[] args) {
        int num1[] = {10, 20, 30, 40, 50};
        int num2[] = num1;

        num2[2] = 100;
        for (int num : num1) {
            System.out.print(num + "\t");
        }

        int num3[] = new int[num1.length];
        for (int i = 0; i < num3.length; i++) {
            num3[i] = num1[i];
        }
        num3[0] = 200;

        System.out.println();
        for (int num : num1) {
            System.out.print(num + "\t");
        }

        int num4[] = num1.clone();
        num4[1] = 500;

        System.out.println();
        for (int num : num1) {
            System.out.print(num + "\t");
        }
    }
}
