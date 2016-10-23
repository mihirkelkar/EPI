class LRU(object):

  def __init__(self, cachesize):
    self.size = cachesize
    self.dict = dict()
    self.queue = list()

  def addCache(self, code, price):
    #if code in list
    if code in self.dict:
      self.queue.remove(code)
      self.queue.insert(0, code)
      self.dict[code] = price

    #if code is not in list
    else:
      if len(self.queue) < self.size:
        self.queue.insert(0, code)
        self.dict[code] = price
      else:
        code_old = self.queue.pop() 
        del self.dict[code_old]
        self.queue.insert(0, code)
        self.dict[code] = price

  def getCache(self, code):
    if code in self.dict:
      self.queue.remove(code)
      self.queue.insert(0, code)
      return self.dict[code]
    else:
      return "Not in dict"


temp = LRU(5)
for ii in range(0, 5):
  temp.addCache(ii, ii)
temp.addCache(6, 6)
temp.addCache(7, 7)
print temp.dict
