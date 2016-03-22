def makeIpAddress(string, stringSoFar, count = 0):
  if count < 3:
    makeIpAddress(string[1:], stringSoFar + [string[0]], count + 1)
    makeIpAddress(string[2:], stringSoFar + [string[:2]], count + 1)
    if int(string[:3]) < 256:
      makeIpAddress(string[3:], stringSoFar + [string[:3]], count + 1)   
  else:
    if len(string) > 3:
      return 
    else:
      print '.'.join(stringSoFar + [string])

#makeIpAddress('2552551990', [])
makeIpAddress('25525511135', [])
