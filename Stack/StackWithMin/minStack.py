class Node(object):
  def __init__(self, value):
    self.bottom = None
    self.value = value

class Stack(object):
  def __init__(self):
    self.top = None
    self.minList = list()
  def push(self, value):
    temp = Node(value)
    temp.bottom = self.top
    self.top = temp
    self.minAdd(self.top)

  def pop(self):
    if self.top != None:
      if self.top == self.minList[-1]:
        print "removed from minlist"
        self.minList.pop(-1)
      value = self.top.value
      self.top = self.top.bottom
      return value
    return None

  def minAdd(self, node):
    if self.minList and node.value <= self.minList[-1]:
      self.minList.append(node)
    else:
      self.minList.append(node)
  
  def min(self):
    if self.minList:
      return self.minList[-1].value
    else:
      print "Stack might be empty"


if __name__ == "__main__":
  main()  
