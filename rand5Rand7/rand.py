import random

def rand5():
  return random.randint(1, 5)

def rand7():
  vals = [
		[1, 2, 3, 4, 5], 
		[6, 7, 1, 2, 3],
		[4, 5, 6, 7, 1],
		[2, 3, 4, 5, 6],
		[7, 0, 0, 0, 0]
	]

  result = 0
  while result == 0:
    x = rand5()
    y = rand5()
    result = vals[x - 1][y - 1]
  return result

counter = 0
while counter < 10:
  print rand7() 
  counter += 1
