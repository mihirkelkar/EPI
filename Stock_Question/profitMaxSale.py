def maxProfit(array):
  max = -float("inf")
  min = float("inf")
  for ii in array[::-1]:
    if ii > max:
      max = ii
      min = ii
    else:
      if ii < min:
        min = ii
      else:
        continue
  return min, max

print maxProfit([1, 2, 100, 2, 3000, 2])
