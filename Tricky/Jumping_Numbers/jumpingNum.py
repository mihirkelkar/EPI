def jumpingNums(number):
  que = list()
  que += [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  while que:
    num = que.pop(0)
    print num
    if num % 10 == 0:
      temp = num * 10 + 1
      if temp < number:
        que.append(temp)
    elif num % 10 == 9:
      temp = num * 10 + 8
      if temp < number:
        que.append(temp)
    else:
      temp = num * 10 + (num%10 - 1)
      if temp < number:
        que.append(num * 10 + (num%10 - 1))
        que.append(num * 10 + (num%10 + 1))
  print que

jumpingNums(91)
