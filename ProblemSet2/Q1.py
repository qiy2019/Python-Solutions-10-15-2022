balance = 42
b = balance
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 0
while (months < 12):
    p = monthlyPaymentRate * b
    ub = b - p
    r = annualInterestRate
    b = (ub + ((r/12.0) * float(ub)))
    months += 1
print("Remaining balance: " + str(round(b, 2)))
