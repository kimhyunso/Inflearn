package chapter5;

public class Rectangle implements Shape {
    @Override
    public void render() {
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                System.out.print("*\t");
            }
            System.out.println();
        }
    }
}
