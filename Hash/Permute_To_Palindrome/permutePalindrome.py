def permutePalindrome(string):
  string_dict = dict()
  even_string = 0
  if len(string) % 2 == 0:
    even_string = 1
  else:
    event_string = 0

  for char in string:
    try:
      string_dict[char] += 1
    except:
      string_dict[char] = 1

  even, odd = 0, 0

  for ii in string_dict.values():  
    if ii % 2 == 0:
      even += 1
    else:
      odd += 1 

  if even_string:
    if odd == 0:
      print "Yep Palindrome possible"
      return 
  else:
    if odd == 1:
      print "Yep Palindrome possible" 
      return 
  print "Palindrome not possible"


permutePalindrome("racecar")
permutePalindrome("nascar")
