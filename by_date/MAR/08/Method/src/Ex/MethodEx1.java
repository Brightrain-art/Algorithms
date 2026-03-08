package Ex;

public class MethodEx1 {

    public static void main(String[] args) {

        int a = 1;
        int b = 2;
        int c = 3;
//        int a, int b, int c = 1, 2, 3;

        System.out.println("평균값: " + add(a, b, c));

        int x = 15;
        int y = 25;
        int z = 35;

        System.out.println("평균값: " + add(x, y, z));

    }

    public static double add(int a, int b, int c) {
        double result = (double) (a + b + c) / 3;
        return result;
    }
}
