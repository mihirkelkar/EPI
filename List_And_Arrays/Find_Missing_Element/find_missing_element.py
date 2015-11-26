def findMissingNumber(array_one, array_two):
  #This has a O(nLogn) 
  array_one.sort()
  array_two.sort()
  print zip(array_one, array_two)
  for num_one, num_two in zip(array_one, array_two):
    if num_one != num_two:
      return num_one
  return array_one[-1]

def findMissing(array_one, array_two):
  #O(n) time and O(n) space
  temp_dict = {}
  for ii in array_two:
    if ii in temp_dict:
      temp_dict[ii] += 1
    else:
      temp_dict[ii] = 1

  for ii in array_one:
    if ii in temp_dict:
      if temp_dict[ii] == 0:
        return ii
      else:
        temp_dict[ii] -= 1
    else:
      return ii
    

"""
  There is however a constant time solution to the problem. Intitialiaze a variable to zero and xor every element in the first and second array. The value of the missing element is the value of the varble now. Since all duplicates will cancel out. 
"""

def missingXOR(array_one, array_two):
  result = 0
  for ii in array_one:
    result ^= ii
  for jj in array_two:
    result ^= jj
  return result


def main():
  print findMissingNumber([1, 2, 3, 4], [1, 2, 3])
  print findMissing([1, 2, 3, 4], [1, 2, 3])
  print missingXOR([1, 2, 3, 4], [1, 2, 3])

main()
