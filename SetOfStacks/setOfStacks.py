class SetStack(object):
  def __init__(self, threshold):
    self.set = list()
    self.threshold = threshold
  def pushSet(self, value):
    if len(self.set) == 0:
      new_list = list()
      new_list.append(value)
      self.set.append(new_list)
    else:
      if len(self.set[-1]) < self.threshold:
        self.set[-1].append(value)
      else:
        new_list = list()
        new_list.append(value)
        self.set.append(new_list)
  
  def popSet(self):
    if len(self.set) == 0:
      return False
    else:
      if not self.set[-1]:
        self.set.pop()
      else:
        return self.set[-1].pop()


temp = SetStack(5)
for ii in range(0, 6):
  temp.pushSet(1) 

print temp.set 
temp.popSet()
temp.popSet()
print temp.set
temp.popSet()
print temp.set
