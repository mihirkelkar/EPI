def checkUnique(string):
  string = sorted(string.lower())
  for ii in range(1, len(string)):
    if string[ii] == string[ii - 1]:
      return False
  return True
print checkUnique("mihir")
