def derangements(num):
  if num == 0:
    return 1
  elif num == 1:
    return 0
  elif num == 2:
    return 1
  return (num - 1) * (derangements(num - 1) + derangements(num - 2))

def main():
  num = 4
  print derangements(num)
  print "------"
if __name__ == "__main__":
  main()
