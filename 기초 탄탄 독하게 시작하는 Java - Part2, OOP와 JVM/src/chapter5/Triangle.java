package chapter5;

public class Triangle implements Shape {

    @Override
    public void render() {
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print("*\t");
            }
            System.out.println();
        }
    }
}
