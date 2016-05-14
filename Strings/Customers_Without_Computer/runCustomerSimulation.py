import string
import collections

def runCustSimulation(number, string_one):
  string_one = string_one.lower()
  leters = string.letters[0:26]
  nums = [0] * 26
  temp = dict(zip(leters, nums))
  result = 0
  denied = collections.defaultdict(int)
  for ii in string_one:
    if sum(temp.values()) >= number:
      if temp[ii] == 1:
        temp[ii] -= 1
      else:
        if ii not in denied:
          denied[ii] = 1
          result += 1
        else:
          del denied[ii]
    else:
      if temp[ii] == 1:
        temp[ii] -= 1
      else:
        temp[ii] += 1
  print result
  
runCustSimulation(1, 'ABCBCADEED')
