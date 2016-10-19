def parseInt(number):
  exp = len(number) - 1
  res = 0
  for ii in number:
    int_val = ord(ii) - ord('0')
    if int_val > 9 or int_val < 0:
      print "String might consist of non number chars"
      return 
    else:
      res += int_val * (10 ** exp)
      exp -= 1
  return res

print parseInt("550")	
print parseInt("554a")
