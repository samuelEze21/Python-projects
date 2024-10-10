from sqlalchemy import Float


class LoanContract:

    def __init__(self, borrower_name: str, loan_amount: float, interest_rate: float, loan_period: float):
        self.borrower_name = borrower_name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_period = loan_period


    def get_borrower_profile_and_loan_contract_details(self):
        return {
            "Borrower Name": self.borrower_name,
            "Loan Amount": self.loan_amount,
            "Interest Rate": self.interest_rate,
            "Loan Period": self.loan_period
        }


    @staticmethod
    def get_monthly_repayment_plan(full_loan_amount, monthly_interest, loan_duration_by_months):
        if loan_duration_by_months <= 0 or full_loan_amount <= 0 or monthly_interest <= 0:
            raise ValueError("Loan amount and interest rate must be greater than zero")

        monthly_payment = full_loan_amount * monthly_interest / 1-(1/ (1+ monthly_interest) ** loan_duration_by_months)
        return monthly_payment



    def get_total_loan_payments_to_be_made(self, monthly_payment_amount, loan_duration_by_months):

        if loan_duration_by_months <= 0 or monthly_payment_amount <= 0:
            raise ValueError("Loan amount and interest rate must be greater than zero")

        total_loan_payment = monthly_payment_amount * loan_duration_by_months

        return total_loan_payment






















