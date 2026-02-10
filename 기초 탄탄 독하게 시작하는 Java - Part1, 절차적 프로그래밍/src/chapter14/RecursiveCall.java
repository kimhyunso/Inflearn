package chapter14;

public class RecursiveCall {
    public static void main(String[] args) {
        int result = getFactorialLoop(5);
        System.out.println(result);
    }

    public static int getFactorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    public static int getFactorialLoop(int n) {
        if (n <= 1)
            return 1;
        return n * getFactorialLoop(n - 1);
    }
}
