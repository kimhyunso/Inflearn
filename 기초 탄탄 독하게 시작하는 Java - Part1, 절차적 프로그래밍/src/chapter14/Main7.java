package chapter14;

import java.util.Scanner;

public class Main7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.next();
        chatAt(str.length() - 1, str);
        System.out.println();
        chatAtVersion2(str.length() - 1, str);
    }

    public static void chatAtVersion2(int index, String str) {
        if (index < 0)
            return;
        System.out.print(str.charAt(index));
        chatAt(index - 1, str);
    }

    public static char chatAt(int index, String str) {
        if (index == 0) {
            print(str.charAt(index));
            return str.charAt(index);
        }
        print(str.charAt(index));
        return chatAt(index - 1, str);
    }

    public static void print(char ch) {
        System.out.print(ch);
    }
}
