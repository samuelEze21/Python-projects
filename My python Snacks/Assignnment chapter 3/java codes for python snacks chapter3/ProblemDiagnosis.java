import java.util.Scanner;

public class ProblemDiagnosis {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("What is your problem?: ");
        String problem = input.nextLine();

        System.out.print("Have you had this problem before (yes or no)?: ");
        String problemFollowUp = input.nextLine().trim().toLowerCase();

        if (problemFollowUp.equals("yes")) {
            System.out.println("Well, you have it again.");
        } else {

            System.out.println("Well, you have it now.");
        }
    }
}
