import java.util.Scanner;

public class MilesPerGallon {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        double totalMiles = 0;
        double totalGallons = 0;
        
        double sentinel = -1;
        
        while (true) {
            System.out.print("Enter miles driven (-1 to quit): ");
            double miles = input.nextDouble();
            if (miles == sentinel) {
                break;
            }
            
            System.out.print("Enter gallons used: ");
            double gallons = input.nextDouble();
            
            double mpg = miles / gallons;
            System.out.printf("Miles per gallon for this tankful: %.2f%n", mpg);
            
            totalMiles += miles;
            totalGallons += gallons;
        }
        
        if (totalGallons != 0) {
            double combinedMpg = totalMiles / totalGallons;
            System.out.printf("%nCombined miles per gallon for all tankfuls: %.2f%n", combinedMpg);

        } else {
            System.out.println("No data to calculate combined miles per gallon.");

        }
        
    }
}
