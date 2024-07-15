p = 1000
r = 7
number_of_years = 30 
year_turnover = []

for year in range(1, number_of_years + 1):
    turnover = p * (1 + r / 100) ** year
    year_turnover.append(turnover)


yearturnover = p * (year + r) 
for year in range(1, number_of_years + 1):
    print(f"The return after year {year} = {year_turnover[year - 1]:.2f} USD")

