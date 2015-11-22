class Stack(object):
  def __init__(self):
    self.stack = list()

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def isEmpty:
    if len(self.stack) > 0:
      return False
    return True

def sortStack(stack):
  newStack = Stack()
  while not stack.isEmpty():
    temp = stack.pop()
    if newStack.isEmpty() or temp > stack.peek():
      newStack.push(temp)
    else:
      while newStack.peek() > temp:
        stack.push(newStack.pop())
        if newStack.isEmpty():
          break
      newStack.push(temp)
  return newStack
      
