import collections

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def huffman(stringOne):
  temp_dict = collections.defaultdict(int)
  for ii in stringOne:
    temp_dict[ii] += 1
  dictone = {}
  temp_dict = temp_dict.items()
  while len(temp_dict) > 1:
    print temp_dict
    temp_dict = sorted(temp_dict, key = lambda x:x[1])
    one = temp_dict.pop(0)
    two = temp_dict.pop(0)
    temp_node = (one[0] + two[0], one[1] + two[1])
    temp_dict.append(temp_node)
    temp = Node(one[0]+two[0])
    try:
      temp.left = dictone[one[0]]
    except:
      dictone[one[0]] = Node(one[0])
      temp.left = dictone[one[0]]
    try:
      temp.right = dictone[two[0]]
    except:
      dictone[two[0]] = Node(two[0])
      temp.right = dictone[two[0]]
    dictone[temp_node[0]] = temp
  head = temp_dict[0]
  print head
  print dictone.keys()
  head_node = dictone[head[0]]
  make_code(head_node)  

def make_code(node, code=''):
  if node == None:
    return 
  if node.left == None and node.right == None:
    print node.value + " : " + code
  else:
    make_code(node.left, code+'0')
    make_code(node.right, code+'1')

string_one = 'hi there where are we'
huffman(string_one)
