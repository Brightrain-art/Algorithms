package Ex;

public class MethodEx2 {

    public static void main(String[] args) {

        printSeveral("Hello, world", 10);
    }

    public static void printSeveral(String message, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(message);
        }
    }

}
