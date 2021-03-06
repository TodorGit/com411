print("How many live cables should i avoid ?")
live_cables = int(input())
i = 0

while (i < live_cables):
  print("Avoiding...",end="")
  i = i + 1 
  print("...Done! {} live cable avoided!".format(i))
  if(i==live_cables):
    print("All live cables have been avoided.")