import heapq
def sort_inc_dec(array):
  i = 0
  j = 0
  result = [[]]
  inc = True
  while i < len(array) - 1:
    if inc:
      if array[i] < array[i+1]:
        result[j].append(array[i])
      else:
        result[j].append(array[i])
        j+=1
        result.append([])
        inc=False
    elif not inc:
      if array[i] > array[i+1]:
        result[j] = [array[i]] + result[j]
      else:
        result[j] = [array[i]] + result[j]
        j += 1
        result.append([])
        inc = True
    i += 1
    if i == len(array) - 1:
      if inc:
        result[j].append(array[i])
      else:
        result[j] = [array[i]] + result[j]
  merge_sorted_arrays(result)
 

def merge_sorted_arrays(arrays):
  heap = []
  for ii in arrays:
    for jj in ii:
      heapq.heappush(heap, jj)
  temp = []
  while heap:
    temp.append(heapq.heappop(heap))
  print temp

sort_inc_dec([1, 5, 10, 15, 13, 11, 12, 14, 20, 18, 16, 17, 19, 30])
