import operator

def deliveryList(droneList):
  return reduce(operator.xor, droneList)  

print deliveryList([4, 2, 3, 2, 3, 4, 6])
