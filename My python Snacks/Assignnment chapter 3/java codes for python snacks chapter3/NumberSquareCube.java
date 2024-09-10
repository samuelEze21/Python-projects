public class NumberSquareCube {
    public static void main(String[] args) {

        System.out.println("Number\tSquare\tCube");

        for (int number = 0; number <= 5; number++) {

            int square = number * number;
            int cube = number * number * number;

            System.out.printf("%6d\t%6d\t%6d%n", number, square, cube);
        }
    }
}
