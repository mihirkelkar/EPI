import heapq

def almost_sorted(array, k):
  if k == 0:
    return arr
  sorted_array = list()
  heap = list()
  ii = 0
  while ii < k:
    heapq.heappush(heap, array[ii])
    ii += 1
  while ii < len(array):
    sorted_array.append(heapq.heappop(heap))
    heapq.heappush(heap, array[ii])
    ii += 1

  while heap:
    sorted_array.append(heapq.heappop(heap))  
    
  return sorted_array

print almost_sorted([3, -1, 2, 6, 4, 5, 8], 3)
