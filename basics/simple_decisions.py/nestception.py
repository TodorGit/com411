print("where should i look? ")
u_input = input()

if(u_input == "in the bedroom"):
  print("Where in the bedroon? ")
  bedroom = input()
  if(bedroom == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")
elif (u_input=="in the bathroom"):
  print("Where in the bathroom should I look?")
  bathroom = input()
  if(bathroom == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but nobattery.")
elif (u_input=="in the lab"):
  print("Where in the lab should I look?")
  lab = input()
  if(lab == "on the table"):
    print("Yay i found my batter!")
  else:
    print("Found some tools but no battery.")
else:
  print("I donot know where that is but I will keep looking.")