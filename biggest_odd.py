def biggest_odd(x, y, z):
  numbers = [x, y, z]
  odd_numbers = []

  for n in numbers:
    if n%2 != 0:
      odd_numbers.append(n)

  if len(odd_numbers) == 0:
    print "No odd numbers here. Sorry!"
  else:
    odd_numbers.sort()
    print odd_numbers[-1]