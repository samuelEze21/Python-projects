annual_interest_rate = 0.07

money = int(input("Enter your initial investment: "))

for year in range(1, 31):
    yearly_return = money * ((1 + annual_interest_rate) ** year)
    print(f"At the end of year {year}, you will have ${yearly_return:.2f}")

print(f"Final amount after 30 years: ${yearly_return:.2f}")
