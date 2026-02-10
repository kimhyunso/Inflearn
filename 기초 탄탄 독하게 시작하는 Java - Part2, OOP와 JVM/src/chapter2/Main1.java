package chapter2;

class MyString1 {
    private byte[] string = null;

    public MyString1() { }
    public MyString1(String param) {
        this.string = param.getBytes();
    }
    public MyString1(int param) {
        this.string = String.valueOf(param).getBytes();
    }

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
        return param.compareTo(getString());
    }
}


public class Main1 {
    public static void main(String[] args) {
        MyString1 myString1 = new MyString1("Test");
        System.out.println(myString1.getString());
        MyString1 myString2 = new MyString1(512);
        System.out.println(myString2.getString());
    }
}