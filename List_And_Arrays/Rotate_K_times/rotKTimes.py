def rotateKTimes(array, k):
  reverseArray(array, 0, len(array)-1)
  reverseArray(array, 0, len(array)-k-1)
  reverseArray(array, len(array)-k, len(array) - k - 1)
  print array

def reverseArray(arr, i, j):
  while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    j -= 1
    i += 1
    
rotateKTimes([1, 2, 3] ,1)
