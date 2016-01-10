def sunset_view(array):
  if not array:
    return 0
  else:
    stack = list()
    ii = len(array) - 1
    while ii >= 0:
      insert(array[ii], stack)
      ii -= 1
    return stack

def insert(element, stack):
  if not stack or stack[-1] > element:
    stack.append(element)
  else:
    stack.pop()
    insert(element, stack)


print sunset_view([10, 20, 15, 40, 31, 55])
