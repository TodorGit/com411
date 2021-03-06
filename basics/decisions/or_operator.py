print("What type of adventure should i havev ?")
adv_type = input()

if( adv_type == "scary") or (adv_type == "short"):
  print("Entering the dark forest")
elif (adv_type =="safe") or (adv_type == "long"):
  print("Taking the safe route")
else:
  print("Not sure which route to take.")