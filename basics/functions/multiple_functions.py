def display_ladder(steps):
  for i in range(steps):
    print('''| |
***''')
  print("| |")

def create_ladder():
 steps = int(input("How many steps should the ladder have? "))
 display_ladder(steps)

create_ladder()