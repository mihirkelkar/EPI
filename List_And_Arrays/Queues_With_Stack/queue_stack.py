class Stack(object):
  def __init__(self):
    self.stack = list()

  def push(self, value):
    self.stack.append(value)
  
  def pop(self):
    if self.stack:
      return self.stack.pop(-1)
    return None

  def empty(self):
    if self.stack:
      return False
    return True


#this queue is going to take penalties on 
class Queue(object):
  def __init__(self):
    self.one = Stack()
    self.two = Stack()
  
  def enqueue(self, value):
     if self.two.empty():
       self.one.push(value)
     else:
       while not self.two.empty():
         self.one.push(self.two.pop())
       self.one.push(value)

  def dequeue(self):
    if self.one.empty():
      return self.two.pop()
    else:
      while not self.one.empty():
        self.two.push(self.one.pop())
      return self.two.pop()

def main():
  one = Queue()
  one.enqueue(1)
  one.enqueue(2)
  print one.dequeue()
  print one.dequeue()
main()
