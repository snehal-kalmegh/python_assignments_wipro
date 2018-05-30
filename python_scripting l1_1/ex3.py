import sys

def isListOfInts(lst):

    if not type(lst) == list:
        raise ValueError('{} --> arg not of <list> type'.format(lst))
        sys.exit(1)
    c=0
    for i in lst:
      if type(i) == int:
          c += 1
    return True if c == len(lst) else False

def testList(lst):
    out = isListOfInts(lst)
    print('{} --> '.format(lst), end='')
    print(out)

testList((1,2))

