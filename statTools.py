def mean(myList):
   if len(myList) == 0:
      return 0
   else:
      sum = 0
      for i in range(len(myList)):
         sum += myList[i]
      avg = sum / len(myList)
      return avg
