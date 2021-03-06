print("How many numbers should i sum up? ")
num = int(input())
i = 0 
sum = 0

while(i< num):
  print("Please enter number {} of {}".format(i,num))
  j = int(input())
  sum = sum + j 
  i = i + 1
  if (i== num):
    print("The answer is {}".format(sum))

