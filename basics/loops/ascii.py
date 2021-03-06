print("How many bars should be charged? ")
bars = int(input())
i = 0 

while(i<bars):
  print("Charging",  "█" * i)
  i = i + 1
  if(i == bars):
    print("The battery is charged")