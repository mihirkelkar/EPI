def addNums(a, b):
  while b != 0:
    sum = a ^ b
    carry = (a&b) << 1
    a = sum
    b = carry
  return a


print addNums(22, 22) 
