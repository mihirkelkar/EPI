def pondCells(array):
  sizeList = list()
  row = len(array)
  col = len(array[0])
  for ii in range(0, row):
    for jj in range(0, col):
      if array[ii][jj] == 0:
        sizeList.append(computeSize(array, ii, jj))
  print sizeList

def computeSize(array, ii, jj):
  if ii < 0 or jj < 0 or ii >= len(array) or jj >= len(array[0]):
    return 0
  if array[ii][jj] != 0:
    return 0
  size = 1
  print ii, jj
  array[ii][jj] = 1
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
       size += computeSize(array, ii+dx, jj+dy)
  return size

pondCells([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]])
