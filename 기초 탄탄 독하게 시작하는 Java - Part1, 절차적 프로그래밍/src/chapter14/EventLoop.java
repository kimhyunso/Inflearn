package chapter14;

import java.util.Scanner;

public class EventLoop {
    public static void main(String[] args) {
        int input = 0;

        for (printMenu(); (input = getCmdNumber()) != 0; printMenu()) {
            if (input == 1) {
                System.out.println("New Menu");
            } else if (input == 2) {
                System.out.println("Search Menu");
            }
        }
        System.out.println("Bye Bye");
    }

    public static void printMenu() {
        System.out.println("[1]New\t[2]Search\t[3]Print\t[0]Exit");
        System.out.print("Command(0-3): ");
    }

    public static int getCmdNumber() {
        Scanner input = new Scanner(System.in);
        return input.nextInt();
    }
}
