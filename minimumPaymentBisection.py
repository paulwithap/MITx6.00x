def minPayBi(balance, annualInterestRate):
  monthlyInterestRate = annualInterestRate/12.0
  low = balance/12.0
  high = (balance *(1+monthlyInterestRate)**12)/12.0
  payment = (high+low)/2
  epsilon = 0.01

  def isPaidOff(balance, rate, payment):
    newBalance = balance
    for i in range(12):
      newBalance = newBalance - payment
      newBalance = newBalance + (rate/12.0)*newBalance
    return newBalance

  newBalance = isPaidOff(balance, annualInterestRate, payment)

  while abs(newBalance) > epsilon:
    if newBalance < 0:
      high = payment
      payment = (high+low)/2
    else:
      low = payment
      payment = (high+low)/2
    newBalance = isPaidOff(balance, annualInterestRate, payment)

  print("Lowest Payment: "+str(round(payment, 2)))