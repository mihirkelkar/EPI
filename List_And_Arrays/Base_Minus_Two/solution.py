def solution(array):
  total = 0
  for index, value in enumerate(array):
    cur_total =  (value * ((-2) ** index))
    total += cur_total
  print array, total 
  print "---------"
  count = 1
  while True:
    for ii in range(0, (2**count)):
      fmt_string = '{0:0%sb}' % count
      bin_number = fmt_string.format(ii)
      bin_list = [int(jj) for jj in bin_number]
      bin_total = 0
      for index, value in enumerate(bin_list):
        bin_total += (value * ((-2) ** index))
      if bin_total == -1 * total:
        return bin_list, bin_total
    count += 1

print solution([1, 1, 1])
print solution([1, 0, 1])
print solution([1, 0, 1, 0, 1, 1])
