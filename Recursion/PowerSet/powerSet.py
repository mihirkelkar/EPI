def powerSet(array):
  length = len(array)
  for ii in range(0, 2**length):
    new_list = list()
    num = list(bin(ii)[2:].zfill(length))
    new_list = [array[ii] for ii in range(0, len(array)) if int(num[ii])]
    print new_list
powerSet([1, 2, 3, 4])
