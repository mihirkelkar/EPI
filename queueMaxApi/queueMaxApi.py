class Queue:
  def __init__(self):
    self.queue = list()
    self.max = -float("inf")  

  def enqueue(self, value):
    self.queue.append(value)
    if value > self.max:
      self.max = value
  
  def dequeue(self):
    return self.queue.pop(0)
    self.max = max(self.queue)
  #Stupid solution  
  def max(self):
    return self.max


