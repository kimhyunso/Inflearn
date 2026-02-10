package chapter3;

// 현재시점
class Test {
    protected int number;
    public void setNumber(int number) {
        System.out.println("Test.setNumber()");

        // 미래의 누군가를 위해 셋팅해놓음 -> 이 함수에서 범위가 필요할 것이라 판단
        if (onSetNumber(number))
            this.number = number;
        else
            this.number = 0;
    }

    protected boolean onSetNumber(int number) {
        System.out.println("Test.onSetNumber()");
        return true;
    }

    public int getNumber() {
        return number;
    }
}

// 미래시점
class TestEx extends Test {
    // 미래의 누군가가 override onSetNumber()를 함으로써, setNumber()의 결과가 달라짐
    @java.lang.Override
    protected boolean onSetNumber(int number) {
        System.out.println("TestEx.onSetNumber()");
        return number >= 0 && number <= 100;
    }
}



public class CalledByFramework {
    public static void main(String[] args) {
        Test test = new TestEx();
        test.setNumber(-1);
        System.out.println(test.getNumber());
        test.setNumber(50);
        System.out.println(test.getNumber());
        test.setNumber(101);
        System.out.println(test.getNumber());
    }
}
