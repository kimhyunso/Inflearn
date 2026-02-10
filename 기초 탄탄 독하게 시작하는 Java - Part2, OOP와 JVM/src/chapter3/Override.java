package chapter3;

class SuperClass {
    protected int number;
    public void setNumber(int number) {
        this.number = number;
        System.out.println("SuperClass.setNumber() " + number);
    }
}

class SubClass extends SuperClass {

    @java.lang.Override
    public void setNumber(int number) {
        // super.getNumber: 전위, 후위 가능
        // super.getNumber();
        // Override만 사용시, 함수 대체
        System.out.println("SubClass.setNumber() " + number);
        // 보정
        if (number < 0)
            number = 0;

        super.setNumber(number);
    }
}


public class Override {
    public static void main(String[] args) {
        SuperClass superClass = new SubClass();
        SubClass subClass = new SubClass();

        superClass.setNumber(-5);
        subClass.setNumber(30);
    }
}
