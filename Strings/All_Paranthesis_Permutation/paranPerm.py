def paranPerm(open, closed = 0, string = ""):
  if open == 0 and closed == 0:
    print string
  else:
    if open > 0:
      paranPerm(open - 1, closed + 1, string + '<')
    if closed > 0:
      paranPerm(open, closed - 1, string + '>')

paranPerm(3)
