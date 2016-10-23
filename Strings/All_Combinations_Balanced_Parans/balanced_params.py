def balancedParams(number, open=0, closed=0, str=""):
  if closed == number:
    print str
  else:
    if open < number:
      balancedParams(number, open+1, closed, str + "{")

    if open > closed:
      balancedParams(number, open, closed+1, str + "}")

balancedParams(4)
