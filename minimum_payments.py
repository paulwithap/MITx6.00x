def paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate):
  totalPaid = 0
  finalBalance = 0
  for i in range(12):
    monthlyPayment = monthlyPaymentRate*balance
    totalPaid += monthlyPayment
    balance = balance-monthlyPayment
    balance = balance + (annualInterestRate/12.0)*balance
    finalBalance = balance
    print("Month: "+ str(i+1))
    print("Minimum monthly payment: "+str(round(monthlyPayment, 2)))
    print("Remaining balance: "+str(round(balance, 2)))
  print("Total paid: "+str(round(totalPaid, 2)))
  print("Remaining balance: "+str(round(finalBalance, 2)))