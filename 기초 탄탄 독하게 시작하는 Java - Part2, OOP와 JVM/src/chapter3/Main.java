package chapter3;

class MyString {
    private byte[] string;
    public MyString() {

    }

    public MyString(String word) {
        this.string = word.getBytes();
    }

    public MyString(MyString rhs) {
        deepCopy(rhs);
    }

    public void deepCopy(MyString rhs) {
        this.string = rhs.string.clone();
    }

    public void setString(String string) {
        this.string = string.getBytes();
    }

    public String getString() {
        if (string == null || string.length == 0) {
            return "(null)";
        }
        return new String(string);
    }
}

public class Main {
    public static void main(String[] args) {
        MyString src = new MyString("Hello");
        MyString dst = new MyString(src);

        src.setString("World");
        System.out.println(dst.getString());
    }
}
