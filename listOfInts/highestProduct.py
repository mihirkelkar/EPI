def highestProduct(array):
  min1, min2 = float("inf"), float("inf")
  max1, max2, max3 = -float("inf"), -float("inf"), -float("inf")
  for ii in array:
    if ii < min1:
      if ii < min2:
        min1 = min2
        min2 = ii
      else:
        min1 = ii
    if ii > max1:
      if ii > max2:
        if ii > max3:
          max1 = max2
          max2 = max3 
          max3 = ii
        else:
          max1 = max2
          max2 = ii
      else:
        max1 = ii
  return max([min1 * min2 * max3, max1 * max2 * max3])


print highestProduct([-1, 0, 1, 2, 3, 4])        
        
          
     
