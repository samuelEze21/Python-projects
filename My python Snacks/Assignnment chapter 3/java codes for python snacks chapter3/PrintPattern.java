public class PrintPattern {
    public static void main(String[] args) {

        for (int row = 0; row < 10; row++) {
            for (int column = 0; column < 10; column++) {
                if (row % 2 == 1) {
                    System.out.print('<');
                } else {
                    System.out.print('>');
                }
            }
            System.out.println();
        }
    }
}
