def sorter(array, index):
  #We basically split the whole zone into 3 parts. Less than the given pivot,
  #more than the given pivot and equal to the given pivot.
  pivot = array[index] 
  smaller = 0
  equal = 0
  larger=len(array)-1
  while equal <= larger:
    if array[equal] < pivot:
      array[smaller], array[equal] = array[equal], array[smaller]
      smaller += 1
      equal += 1
    elif array[equal] == pivot:
      equal += 1
    elif array[equal] > pivot:
      array[equal], array[larger] = array[larger], array[equal]
      larger -= 1

  print array


def main():
  sorter([3, 1, 6, 2, 8], 2)

if __name__ == "__main__":
  main()
