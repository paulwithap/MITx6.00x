def biggest_odd_2():
  numbers = []
  odd_numbers = []

  for i in range(10):
    n = raw_input('Enter number {0}: \n'.format(i+1))
    numbers.append(n)

  for n in numbers:
    number = int(n)
    if number%2 != 0:
      odd_numbers.append(number)

  if len(odd_numbers) == 0:
    print "No odd numbers here, sorry!"
  else:
    odd_numbers.sort()
    print "The largest odd number is:", odd_numbers[-1]