package chapter7;

class MyString {
    protected byte[] string;

    public void setString(String string) {
        this.string = onSetStringReplace(string).getBytes().clone();
    }
    protected boolean onSetString(String string) {
        return true;
    }

    protected String onSetStringReplace(String param) {
        return param;
    }

    public String getString() {
        if (string == null)
            return "(null)";
        return new String(string);
    }

    public boolean equals(MyString rhs) {
        String temp = new String(this.string);
        // return temp.equals(new String(rhs.string));
        return temp.compareTo(rhs.getString()) == 0;
    }
}
public class Main1 {
    public static void main(String[] args) {
        MyString s1 = new MyString();
        s1.setString("Hello");
        MyString s2 = new MyString();
        s2.setString("Hello");

        System.out.println(s1.equals(s2));
    }
}
