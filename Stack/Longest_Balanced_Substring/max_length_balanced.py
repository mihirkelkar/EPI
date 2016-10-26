def max_len_balanced(parans_str):
  stack = list()
  max_len = 0
  end = -1
  for index in range(0, len(parans_str)):
    if parans_str[index] == '(':
      stack.append(index)
    elif parans_str[index] == ')':
      if len(stack) == 0:
        end = index
      else:
        stack.pop()
        try:
          cur_len = index - stack[-1]
        except:
          cur_len = index - end
        if cur_len > max_len:
          max_len = cur_len
  return max_len  

print max_len_balanced("(())())()")
