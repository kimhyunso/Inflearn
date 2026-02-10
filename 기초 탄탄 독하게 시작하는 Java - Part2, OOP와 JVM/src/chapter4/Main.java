package chapter4;

class MyString {
    protected byte[] string;

    public void setString(String string) {
//        if (onSetString(string))
//            this.string = string.getBytes();
//        else
//            this.string = new byte[]{'h', 'e', 'l', 'l', 'o'};

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

}

class MyStringEx extends MyString {
    @Override
    protected boolean onSetString(String string) {
        return !string.toLowerCase().contains("apple");
    }

    @Override
    protected String onSetStringReplace(String param) {
        if (param.compareTo("hello") == 0)
            return "world";
        return param;
    }
}

public class Main {
    public static void main(String[] args) {
        MyStringEx string = new MyStringEx();
        string.setString("apple");
        System.out.println(string.getString());

        string.setString("banana");
        System.out.println(string.getString());

        string.setString("hello");
        System.out.println(string.getString());
    }
}
