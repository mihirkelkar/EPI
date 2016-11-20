def group_anagrams(list_string):
  string_dict = {}
  for strng in list_string:
    key = ''.join(sorted(strng))
    print key
    try:
      string_dict[key] = string_dict[key] + [strng]
    except:
      string_dict[key] = [strng]
  for ii in string_dict.values():
    print ii
    
group_anagrams(["cat", "act", "dog",
                "door", "odor"])
