def return_sum(array):
  carry = 1
  for ii in range(len(array)-1, -1, -1):
    if carry == 1:
      array[ii] += 1
      if array[ii] == 10:
        array[ii] = 0
      else:
        carry = 0
  print array

def main():
  return_sum([1, 3, 9])

if __name__ == "__main__":
  main()
 
