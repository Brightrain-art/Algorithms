package method;

public class MethodReturn2 {

    public static void main(String[] args) {

        check(14);
        check(20);
    }

    public static void check(int age) {
        if (age < 18) {
            System.out.println(age + "살, 미성년자는 출입이 불가합니다.");
            return;
        } else {
            System.out.println(age + "살, 입장하세요.");
            return;
        }
    }
}
