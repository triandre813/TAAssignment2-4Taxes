# input statements
salary = float(input("Enter the weekly salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate state withholding tax
state_tax_rate = 0.065
state_tax = salary * state_tax_rate

# calculate federal withholding tax
federal_tax_rate = 0.28
federal_tax = salary * federal_tax_rate

# calculate dependent deductions
dependent_deduction_rate = 0.025
dependent_deduction = salary * dependent_deduction_rate * numDependents

# calculate total withholding
total_withholding = state_tax + federal_tax + dependent_deduction

# calculate take-home pay
take_home_pay = salary - total_withholding

# output statements
print("Salary: $" + str(salary))
print("State Tax Withheld: $" + str(state_tax))
print("Federal Tax Withheld: $" + str(federal_tax))
print("Dependent Deductions: $" + str(dependent_deduction))
print("Take Home Pay: $" + str(take_home_pay))
