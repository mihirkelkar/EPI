def rotateCompare(number):
  start = 10
  while number > 0:
    newNum = number % start
    if newNum!=1 and newNum!=8 and newNum!=9 and newNum!=6 and newNum!=0:
      return False
    else:
      number = number // 10 
  return True

print rotateCompare(711)
print rotateCompare(161)
