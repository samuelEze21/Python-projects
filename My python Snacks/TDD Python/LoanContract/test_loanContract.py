import unittest

from SamuelPythonProjects.LoanContract.loan_contract import LoanContract


class TestLoanContract(unittest.TestCase):


    def setUp(self):
        self.borrower1 = LoanContract("Sapa boy", 55000,12.5, 3)
        self.borrower2 = LoanContract("trench kid", 96500,10.5, 1)

    def test_that_A_borrower_profile_identify_and_loan_contract_details_can_exist(self):
        user1_loan_details = self.borrower1.get_borrower_profile_and_loan_contract_details()
        self.assertEqual(user1_loan_details["Borrower Name"], "Sapa boy")
        self.assertEqual(user1_loan_details["Loan Amount"], 55000)
        self.assertEqual(user1_loan_details["Interest Rate"], 12.5)
        self.assertEqual(user1_loan_details["Loan Period"], 3)


    def test_that_multiple_borrower_profile_can_exist(self):
        user1_loan_details = self.borrower1.get_borrower_profile_and_loan_contract_details()
        self.assertEqual(user1_loan_details["Borrower Name"], "Sapa boy")
        self.assertEqual(user1_loan_details["Loan Amount"], 55000)
        self.assertEqual(user1_loan_details["Interest Rate"], 12.5)
        self.assertEqual(user1_loan_details["Loan Period"], 3)

        user2_loan_details = self.borrower2.get_borrower_profile_and_loan_contract_details()
        self.assertEqual(user2_loan_details["Borrower Name"], "trench kid")
        self.assertEqual(user2_loan_details["Loan Amount"], 96500)
        self.assertEqual(user2_loan_details["Interest Rate"], 10.5)
        self.assertEqual(user2_loan_details["Loan Period"], 1)


    def test_that_borrower_can_calculate_monthly_payment_required_to_Repay_Loan(self):
        monthly_payment_to_repay_loan = self.borrower1.get_monthly_repayment_plan(55000, 1.04, 36)
        self.assertEqual(monthly_payment_to_repay_loan, 57199.99999999999)


    def test_that_borrower_can_calculate_total_payment_made_over_the_loan_period(self):
        total_loan_amount_paid = self.borrower1.get_total_loan_payments_to_be_made(57199.99, 36)
        self.assertEqual(total_loan_amount_paid, 2059199.64)

















    #test_to_get_all_borrowers_profiles(add borrower objects to a list)

    # def test_invalid_channel_raises_error(self):
    #     # Test that invalid channel raises ValueError
    #     with self.assertRaises(ValueError):
    #         self.loan1.get_tv_channel(101)  # Invalid channel



    # def test_invalid_loan_values(self):
    #     # Test with invalid loan values (0 or negative amounts)
    #     with self.assertRaises(ValueError):
    #         self.loan.get_monthly_repayment_plan(0, 0.005, 12)  # Loan amount is 0
    #     with self.assertRaises(ValueError):
    #         self.loan.get_monthly_repayment_plan(10000, 0.005, 0)
    #





if __name__ == '__main__':
    unittest.main()
