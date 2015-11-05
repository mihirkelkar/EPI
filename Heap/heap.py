class Heap(object):
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0 

  def reArrange(self, ii):
    while ii // 2 > 0:
      if self.heapList[ii] < self.heapList[ii//2]:
        temp = self.heapList[ii/2]
        self.heapList[ii/2] = self.heapList[ii]
        self.heapList[ii] = tmp
      ii = ii//2

  def insert(self,value):
    self.heapList.append(value)
    self.currentSize += 1
    self.reArrange(self.currentSize)

  
