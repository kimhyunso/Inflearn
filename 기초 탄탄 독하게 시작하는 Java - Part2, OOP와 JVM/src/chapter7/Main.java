package chapter7;

public class Main {
    public static void main(String[] args) {
        // JVM GC 결과 설정: -verbose:gc
        // JVM GC 로그 설정: -Xlog:gc*
        {
            byte[] placeHolder = new byte[64 * 1024 * 1024];
        }
        int a = 0;
        System.gc();
    }
}
