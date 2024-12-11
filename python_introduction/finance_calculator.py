Monthly_income = input("Enter your monthly income:")
Total_monthly_expenses = input("Enter your total monthly expenses:")

Monthly_savings = Monthly_income - Total_monthly_expenses
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

print(f"Your monthly savings are:{Monthly_Savings}$ \nProjected savings after one year, with interest, is:{Projected_Savings}$")
