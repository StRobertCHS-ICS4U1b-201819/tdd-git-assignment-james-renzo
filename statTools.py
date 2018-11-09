def mean(myList):
   if len(myList) == 0:
      return 0
   else:
      sum = 0
      for i in range(len(myList)):
         sum += myList[i]
      avg = sum / len(myList)
      return avg

def range(theList):
    if len(theList) == 0:
        return 0
    else:
        total = 0
        for t in range(len(theList)):
                total += theList[t]
        high = max(len(theList))
    return high

def deviant(myList):
   if len(myList) == 0:
      return 0
   else:
      sum = 0
      for i in range(len(myList)):
         sum += myList[i]
      men = sum / len(myList)
      sqrt = 2 ** (sum / len(myList))
      avg = sqrt
      return avg