def atoi(string):
  exp = len(string)-1
  total = 0
  for ii in string:
    if ord(ii) < ord('0') or ord(ii) > ord('9'):
      return False
    else:
      num = ord(ii)-ord('0')
      total += num * (10**exp)
      exp -= 1
  return total

print atoi('321')
print atoi('2201')
