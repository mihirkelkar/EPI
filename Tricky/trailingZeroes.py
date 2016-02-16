def trailingZeroes(number):
  count = 0
  for ii in range(1, number + 1):
    count += factorFive(ii)
  print count  


def factorFive(number):
  count = 0
  while number != 0:
    if number % 5 == 0:
      count += 1
    number = number / 5
  return count

trailingZeroes(3)
