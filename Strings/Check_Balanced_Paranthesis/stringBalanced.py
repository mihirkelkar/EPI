def stringBalanced(paranString):
  stack_list = list()
  param_dict = {'(' : ')', '[' : ']', '{' : '}'}
  for ii in paranString:
    if ii in [')', ']', '}']:
      stack_list.append(ii)
  for ii in paranString:
    if ii in ['(', '[', '{']:
      temp = stack_list.pop()
      if temp != param_dict[ii]:
        return False
  if len(stack_list) != 0:
    return False
  return True

print stringBalanced('({[}])')  
print stringBalanced('(([[{}]]))')
