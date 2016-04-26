def subarray(array):
  for ii in range(0, len(array)):
    for jj in range(ii + 1, len(array)):
      print array[ii:jj]

subarray([1, 2, 3, 4, 5, 6])


def subsequence(array):
  count = len(array)
  for ii in range(0, 2**len(array)):
    print [ii[1] for ii in zip(list(bin(ii)[2:].zfill(count)), array) if ii[0] == '1']
    
subsequence([1, 2, 3, 4, 5, 6])
