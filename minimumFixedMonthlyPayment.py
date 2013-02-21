def minimumPayment(balance, annualInterestRate):
  payment = round(balance/12.0, -1)
  unpaidBalance = balance
  while True:
    unpaidBalance = balance
    for i in range(12):
      unpaidBalance = unpaidBalance - payment
      unpaidBalance = unpaidBalance + (annualInterestRate/12.0)*unpaidBalance
    if unpaidBalance > 0:
      payment += 10
    else:
      break
  print("Lowest Payment: "+str(int(payment)))