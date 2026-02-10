package chapter7;

import java.util.Objects;

class Test {
    private int a;
    public Test(int a) {
        this.a = a;
    }

    public boolean equals(Test t) {
        return this.a == t.a;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Test test = (Test) o;
        return a == test.a;
    }

    @Override
    public int hashCode() {
        return Objects.hash(a);
    }
}

public class HashCodeTest {
    public static void main(String[] args) {
        Test t1 = new Test(1);
        Test t2 = new Test(1);

        if (t1 == t2) {
            System.out.println("== 같다.");
        }

        if (t1.equals(t2)) {
            System.out.println("equals 같다.");
        }

        System.out.printf("t1 hashcode: %s t2 hashcode: %s", t1.hashCode(), t2.hashCode());
    }
}

