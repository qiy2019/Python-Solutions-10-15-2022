balance = 320000;
annualInterestRate = 0.2
prev = balance;
upper = balance
lower = 0;
monthlyInterestRate = annualInterestRate / 12

while (upper - lower > 0.01):
    mid = (upper + lower) / 2
    prev = balance;
    monthlyPayment = mid
    
    for i in range(12):
        unpaidBalance = prev - monthlyPayment
        updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
        prev = updatedBalance
        
    if (prev > 0): lower = mid
    elif (prev < 0): upper = mid
print("Lowest Payment: " + str(round((monthlyPayment * 100)/100, 2)))