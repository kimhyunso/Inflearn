package chapter14;

public class Overload {
    public static void main(String[] args) {
        System.out.println(add(10, 30));
        System.out.println(add(15.6, 14.6));
        System.out.println(add("hello ", "world"));
    }


    public static int add(int a, int b) {
        return a + b;
    }

    public static double add(double a, double b) {
        return a + b;
    }

    public static String add(String a, String b) {
        return a + b;
    }
}
