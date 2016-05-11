import math
def minReversals(string_one):
  stack = list()
  open_count = 0
  close_count = 0
  if len(string_one) % 2 != 0:
    return False
  for ii in string_one:
    if stack:
      if ii == ')' and stack[-1] == '(':
        stack.pop()
        close_count -= 1
        open_count -= 1
      else:
        stack.append(ii)
        close_count += 1
    else:
      stack.append(ii)
      open_count += 1
  print stack
  return 1+math.ceil(open_count / 2) + math.ceil(close_count / 2)



print minReversals('))((')

