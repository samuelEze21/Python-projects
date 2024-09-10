import java.util.ArrayList;
import java.util.List;

public class InvestmentTurnover {
    public static void main(String[] args) {

        double p = 1000; 
        double r = 7;   
        int numberOfYears = 30; 

        List<Double> yearTurnover = new ArrayList<>();

        for (int year = 1; year <= numberOfYears; year++) {
            double turnover = p * Math.pow(1 + r / 100, year);
            yearTurnover.add(turnover);
        }

        for (int year = 1; year <= numberOfYears; year++) {
            System.out.printf("The return after year %d = %.2f USD%n", year, yearTurnover.get(year - 1));
        }
    }
}
