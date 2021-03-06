print("Calculate the sum of the first 100 numbers")
i = 0
sum = 0

while (i <100):
  sum =  sum + i
  i = i + 1
  if(i==100):
    print("... done. The answer is {}".format(sum))