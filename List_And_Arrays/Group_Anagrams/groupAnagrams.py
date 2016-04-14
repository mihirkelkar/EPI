import collections

def groupAnagrams(array):
  word_dict = collections.defaultdict(list)
  for ii in array:
    word_dict[''.join(sorted(ii))].append(ii)
  print word_dict.values()

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
