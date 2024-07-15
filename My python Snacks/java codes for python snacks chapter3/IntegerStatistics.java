import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class IntegerStatistics {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        List<Integer> integers = new ArrayList<>();
        int numOfIntegers = 4;

        for (int count = 0; count < numOfIntegers; count++) {
            System.out.print("Enter integer " + (count + 1) + ": ");
            int integer = input.nextInt();
            integers.add(integer);
        }

        int sumOfIntegers = 0;
        for (int integer : integers) {
            sumOfIntegers += integer;
        }

        double average = (double) sumOfIntegers / numOfIntegers;

        int product = 1;
        for (int integer : integers) {
            product *= integer;
        }

        int smallest = Collections.min(integers);
        int largest = Collections.max(integers);

        System.out.println("Sum = " + sumOfIntegers);
        System.out.println("Average = " + average);
        System.out.println("Product = " + product);
        System.out.println("Smallest = " + smallest);
        System.out.println("Largest = " + largest);
    }
}
