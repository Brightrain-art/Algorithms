package Ex;

import java.sql.SQLOutput;
import java.util.Scanner;

public class MethodEx4 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int balance = 0;

        while (true) {
            System.out.println("--------------------------------------");
            System.out.println("1. 입금 | 2. 출금 | 3. 잔액 확인 | 4. 종료");
            System.out.println("--------------------------------------");

            System.out.print("선택: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            if (choice == 1) {
                balance = deposit(balance);
            } else if (choice == 2) {
                balance = withdraw(balance);
            } else if (choice == 3) {
                check(balance);
            } else if (choice == 4) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else {
                System.out.println("잘못된 숫자를 입력하셨습니다.");
                continue;
            }
        }
    }

    public static int deposit(int balance) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("입금액을 입력하세요: ");
        int deposit = scanner.nextInt();
        scanner.nextLine();
        balance += deposit;
        System.out.println(deposit + "원을 입금하였습니다. 현재 잔액: " + balance +"원");
        return balance;
    }

    public static int withdraw(int balance) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("출금액을 입력하세요: ");
        int withdraw = scanner.nextInt();
        scanner.nextLine();

        if (withdraw > balance) {
            System.out.println(withdraw + "원을 출금하려 했으나 잔액이 부족합니다.");
            return balance;
        }
        balance -= withdraw;
        System.out.println(withdraw + "원을 출금하였습니다. 현재 잔액: " + balance + "원");
        return balance;
    }

    public static void check(int balance) {
        System.out.println("현재 잔액: " + balance);
    }
}