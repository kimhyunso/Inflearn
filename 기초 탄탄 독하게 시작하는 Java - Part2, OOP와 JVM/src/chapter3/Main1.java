package chapter3;

class MyString1 {
    private static int count = 0;
    private byte[] string;
    private MyString1() {}

    private MyString1(int param) {
        string = getBytes(String.valueOf(param));
        incrementCount();
    }

    private MyString1(String param) {
        string = getBytes(param);
        incrementCount();
    }

    public static MyString1 newString(int count) {
        return new MyString1(count);
    }

    public static MyString1 newString(String param) {
        if (param == null || param.length() <= 0) {
            return new MyString1("(null)");
        }

        return new MyString1(param);
    }

    public String getString() {
        if (string == null || string.length == 0) {
            return "(null)";
        }
        return new String(string);
    }

    private byte[] getBytes(String param) {
        return param.getBytes();
    }

    private void incrementCount() {
        ++count;
    }

    public static int getCount() {
        return count;
    }
}


public class Main1 {
    public static void main(String[] args) {
        MyString1 s1 = MyString1.newString(10);
        MyString1 s2 = MyString1.newString("test");
        MyString1 s3 = MyString1.newString(null);

        System.out.println(s1.getString());
        System.out.println(s2.getString());
        System.out.println(MyString1.getCount());
    }
}
