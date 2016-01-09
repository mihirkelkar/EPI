def highest_product(array):
  highest_num = max(array[0], array[1])
  lowest_num = min(array[0], array[1])
  highest_product_two = array[0] * array[1]
  lowest_product_two = array[0] * array[1]
  highest_product_three = array[0] * array[1] * array[2]
  for ii in range(2, len(array)):
    highest_product_three = max(
      highest_product_three, 
      highest_product_two * array[ii],
      lowest_product_two * array[ii]
    )
    highest_product_two = max(highest_product_two, highest_num * array[ii])
    lowest_product_two = min(lowest_product_two, lowest_num * array[ii])
    highest_num = max(highest_num, array[ii])
    lowest_num = min(lowest_num, array[ii])
    print highest_product_three
    print "---------------------"

def main():
  highest_product([-10, -4, 0, 1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
  main()
