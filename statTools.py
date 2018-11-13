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
        for i in range(len(myList)):
            diff = myList[i] - men
            vari = diff*2/len(myList)
      sqrt = 2 ** vari
      avg = sqrt
      return avg

def quartile(List):
    if len(List) == 0:
        return 0
    else:
        sum = 0
        for r in range(len(List)):
            sum += List[r]
            medi = sum / 2
            quar = medi / 2
