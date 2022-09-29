balance = 4773;
annualInterestRate = 0.2;
b = balance
p = 0
months = 0
while(b > 0):
    b = balance
    p += 10
    for months in range(1, 13):
        r = annualInterestRate / 12.0
        ub = b - p
        b = ub + r * ub
print("Lowest payment: " + str(p))