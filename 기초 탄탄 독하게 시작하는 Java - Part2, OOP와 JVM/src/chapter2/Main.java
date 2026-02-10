package chapter2;

import java.util.Arrays;
import java.util.Scanner;

class MyString {
    private byte[] string = null;

    public String getString() {
        // Short circuit
        if (string == null || string.length == 0) {
            return "(null)";
        }
        return new String(string);
    }

    public void setString(String string) {
        this.string = string.getBytes();
    }

    public int length() {
        if (string == null) {
            return 0;
        }
        return string.length;
    }

    public int compareTo(String param) {
//        if (param.equals(getString())) {
//            return 0;
//        }
//        return -1;
        return param.compareTo(getString());
    }
}


public class Main {
    public static void main(String[] args) {
        MyString string = new MyString();
        System.out.println(string.length());
        System.out.println(string.getString());

        string.setString("Hello Java");
        System.out.println(string.getString());
        System.out.println(string.length());
        System.out.println(string.compareTo("Hello Java"));
    }
}