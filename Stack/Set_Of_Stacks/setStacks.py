class SetStacks(object):
  def __init__(self, threshold):
    self.set_stacks = list()
    self.threshold = threshold

  def push(self, value):
    if not self.set_stacks:
      self.set_stacks.append([])
    if len(self.set_stacks[-1]) < self.threshold:
      self.set_stacks[-1].append(value)
    else:
      self.set_stacks.append([])
      self.set_stacks[-1].append(value)

  def pop(self):
    if not self.set_stacks:
      print "Set Empty"
    else:
      if not self.set_stacks[-1]:
        self.set_stacks = self.set_stacks[:-1]
        return self.pop()
      else:
        return self.set_stacks[-1].pop()    

check = SetStacks(2)
for ii in range(0, 10):
  check.push(ii)
  print check.set_stacks

for ii in range(0, 10):
  print check.pop()
  print check.set_stacks
for ii in range(0, 10):
  check.push(ii)
  print check.set_stacks


