import java.util.Scanner;

public class IntegerRelationships {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Enter two integers, and I will tell you the relationships they satisfy.");

        System.out.print("Enter first integer: ");
        int number1 = input.nextInt();

        System.out.print("Enter second integer: ");
        int number2 = input.nextInt();

        if (number1 == number2) {
            System.out.println(number1 + " is equal to " + number2);
        } else {
            System.out.println(number1 + " is not equal to " + number2);
        }

        if (number1 < number2) {
            System.out.println(number1 + " is less than " + number2);
        } else {
            System.out.println(number1 + " is greater than " + number2);
        }

        if (number1 <= number2) {
            System.out.println(number1 + " is less than or equal to " + number2);
        }

        if (number1 >= number2) {
            System.out.println(number1 + " is greater than or equal to " + number2);
        }
    }
}
