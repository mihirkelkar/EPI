def merge(a, b, m, n):
  while (m > 0 and n > 0):
    if a[m - 1] > b[n - 1]:
      a[m+n-1] = a[m-1]
      m -= 1
    else:
      a[m+n-1] = b[n-1]
      n -= 1

  while n > 0:
    a[m + n - 1] = b[n - 1]
    n -= 1
  return a

print merge([1, 2, 3,"","",""], [4, 5, 6], 3, 3)
