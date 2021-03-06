print("Please enter a number: ")
num = int(input())
i = 0
sum = 1

while(i<num):
  i = i + 1
  sum= sum * i
  if(i==num):
   print("{}".format(sum)) 