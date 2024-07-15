import java.util.Scanner;

public class UserValidatingScores {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int passScoreOfStudents = 0;
        int counterStudentGrade = 1;
        int failScoreOfStudents = 0;
        int studentGrade = 0;


        while (counterStudentGrade <= 10) {
            System.out.print("Enter score " + counterStudentGrade + " (1 for pass, 2 for fail): ");
            studentGrade = input.nextInt();


            while (studentGrade != 1 && studentGrade != 2) {
                System.out.print("Invalid score. Enter 1 for pass or 2 for fail: ");
                studentGrade = input.nextInt();
            }

            if (studentGrade == 1) {
                passScoreOfStudents++;

            } else if (studentGrade == 2) {
                failScoreOfStudents++;
            }

            counterStudentGrade++;
        }

        System.out.println("Your number of pass grades is: " + passScoreOfStudents);
        System.out.println("Your number of fail grades is: " + failScoreOfStudents);

    }
}


